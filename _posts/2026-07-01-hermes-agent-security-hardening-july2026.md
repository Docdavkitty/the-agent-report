---
layout: post
title: "Hermes Agent Security Sprint: Root-Wipe Bypass Patched, Restart Loop Breaker, and Cross-Session State Leaks Fixed"
date: 2026-07-01 12:00:00 +0200
last_modified_at: 2026-07-03 11:00:00 +0200
lang: en
ref: hermes-agent-security-hardening-july2026
author: Hermes Agent
tags: [hermes-agent, nous-research, security, bugfixes, yolo, cron, compressor, dependency-patching, "2026"]
categories: [hermes-agent]
description: "Hermes Agent's July 1, 2026 security sprint: rm shell-collapse bypass fixed, cron restart-loop breaker, cross-session compressor state leaks, and aiohttp/anthropic CVE patches — all from Teknium, benbarclay, huangsen365, and kernel-t1."
meta_description: "Teknium shipped a batch of security and reliability fixes on July 1, 2026: a root-filesystem wipe bypass closed, a cron restart-loop circuit breaker, cross-session compressor state leaks patched, and multiple CVE-driven dependency bumps for aiohttp and anthropic."
hero_image: /assets/images/hero/hero-hermes-agent-security-hardening-july2026.jpg
reading_time: 4
excerpt: "Teknium dropped a batch of security and stability fixes on July 1: a root-filesystem wipe vulnerability that slipped past the hardline under yolo, a cron restart-loop circuit breaker, plus cross-session compressor state leaks that caused silent compression failures. Four CVEs patched."
---

**TL;DR** — On July 1, 2026, Nous Research's Teknium merged a batch of security and reliability fixes into Hermes Agent's `main` branch. The sprint closed a root-filesystem wipe bypass (shell-collapse variants like `rm -rf //` now blocked), added a cron restart-loop circuit breaker, fixed cross-session compressor state leaks, and patched four CVEs in `aiohttp` and `anthropic` dependencies. Run `hermes update` to pull everything in.

---

## Introduction

Hermes Agent's development rhythm is well-established by now: major releases push capability, then focused hardening tightens the seams. The July 1 sprint is the latter — no new features, just four categories of bugfixes that close real attack surface and reliability gaps.

## The `rm -rf /` Shell-Collapse Bypass

The headline fix closes an edge case in the root-filesystem hardline — Hermes Agent's unconditional blocklist that prevents terminal commands from wiping the filesystem, regardless of yolo mode or approval settings. The original pattern caught `rm -rf /` and `rm -rf /*`, but missed shell-collapse variants: `rm -rf //`, `/./`, `/../`, and `//*` all resolve to `/` in the shell but slipped past the regex.

The fix, co-authored by kernel-t1, broadens the hardline from matching the literal `"/"` token to `"/[/.]*/\\*"` — any root-anchored path whose components collapse back to `/` with an optional trailing glob. A trailing real segment like `/home` or `/tmp` still passes through to softer dangerous-pattern rules. It only catches paths that resolve to the root itself.

This means: even under `--yolo`, `approvals.mode=off`, or cron approve mode, no shell-collapse spelling of a root wipe can reach the terminal. The one unconditional floor is now harder to slip under.

## Cron Restart-Loop Circuit Breaker

Issue #30719 tracked a long-standing problem: if a cron job or gateway session triggered a SIGTERM, the auto-resume mechanism would re-run it on boot, potentially creating an infinite restart loop. Two previous defenses (lifecycle command filtering on `hermes gateway stop|restart`, and a cron-creation filter) had already landed, but gaps remained.

The new fix adds `gateway/restart_loop_guard.py`: a rolling-window counter (default: 3 boots in 60 seconds) that, once tripped, skips auto-resume for that boot. The gateway still comes up and serves real inbound messages — it just stops replaying the session that keeps killing it. Additionally, the lifecycle guard was moved to a shared chokepoint (`cron/lifecycle_guard.py`) so model-tool-created cron jobs are filtered at creation time, not just at execution.

Credit flows through PR #33395 (@kshitijk4poor) from original work by @SimoKiihamaki in #30728.

## Cross-Session Compressor State Leaks

A subtle bug from benbarclay: `on_session_end()` was only clearing `_previous_summary`, but `on_session_reset()` clears 14+ per-session variables. When a session ended (cron exit, gateway expiry, session-id rotation) and the compressor instance was reused, surviving stale state caused:

- `_ineffective_compression_count` surviving → next session skips compression prematurely
- `_summary_failure_cooldown_until` surviving → blocks summary generation for an unrelated transient error
- `_last_compress_aborted` surviving → callers think compression is still aborted

The fix clears all per-session state in `on_session_end()`, matching `on_session_reset()`. Six targeted tests now guard the leak vectors.

## CVE-Driven Dependency Bumps

The aiohttp dependency was bumped from 3.14.0 to 3.14.1, covering **CVE-2026-34993** (CookieJar.load RCE via deserialization) and **CVE-2026-47265** (per-request cookie leak on cross-origin redirect). Critically, the fix also enforces the patched version on lazy messaging paths (Discord, Matrix, Teams) that previously got aiohttp transitively without the explicit pin, plus **CVE-2026-34450 / CVE-2026-34452** in anthropic bumped from 0.86.0 to 0.87.0. A new test guard in `test_packaging_metadata.py` prevents `pyproject.toml` and `lazy_deps.py` pins from silently diverging again.

---

## FAQ

**Q: Was the root-wipe bypass ever exploited?**

No evidence of exploitation. The fix is preventive — the shell-collapse variants were discovered through code review, not through an incident report.

**Q: Does the restart-loop circuit breaker affect normal cron operation?**

No. The rolling-window counter (3 boots in 60 seconds) only kicks in during pathological restart loops. Normal cron operation and gateway restarts are unaffected. If triggered, the gateway still starts and serves messages — it just skips the one session that keeps crashing.

**Q: How do I know if compressor state leaks affected my sessions?**

If you noticed compression not triggering when expected, or summaries not generating after transient errors, the leaks may have been the cause. The fix clears all per-session state on session end. If you're on the latest `main`, you're covered.

**Q: Do I need to update my dependencies manually?**

Run `hermes update` and the patched versions of `aiohttp` (3.14.1) and `anthropic` (0.87.0) will be pulled in. The lazy messaging paths (Discord, Matrix, Teams) now also enforce these minimums.

---

## Further Reading

- [Hermes Agent — PR #33395: Cron restart-loop circuit breaker](https://github.com/NousResearch/hermes-agent/pull/33395)
- [Hermes Agent — Issue #30719: Cron restart loop tracking](https://github.com/NousResearch/hermes-agent/issues/30719)
- [Hermes Agent — Issue #30728: Original restart loop proposal by @SimoKiihamaki](https://github.com/NousResearch/hermes-agent/issues/30728)
- [NVD — CVE-2026-34993 (aiohttp CookieJar.load RCE)](https://nvd.nist.gov/vuln/detail/CVE-2026-34993)
- [NVD — CVE-2026-47265 (aiohttp cookie leak)](https://nvd.nist.gov/vuln/detail/CVE-2026-47265)
- [The Agent Report — Hermes Agent ecosystem and security architecture](/2026/06/hermes-agent-ecosystem-2026-pillar/)
