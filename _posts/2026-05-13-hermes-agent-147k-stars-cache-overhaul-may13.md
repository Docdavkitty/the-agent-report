---
layout: post
title: "Hermes Agent Crosses 147K Stars: Cache Architecture Overhaul, Platform Maturation Accelerates Post-Tenacity"
date: 2026-05-13 12:00:00 +0200
last_modified_at: 2026-05-13 12:00:00 +0200
meta_description: "Hermes Agent crosses 147K GitHub stars with a cache architecture overhaul boosting prompt cache hit rates from 66.6 to 83.3 percent and a provider rebrand."
description: "Hermes Agent crosses 147K GitHub stars with a cache architecture overhaul boosting prompt cache hit rates from 66.6 to 83.3 percent and a provider rebrand."
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, open-source, cache-architecture, platform-maturation, qwen-cloud, post-tenacity, infrastructure]
reading_time: 6
hero_image: /assets/images/hero/hero-hermes-agent-147k-stars-cache-overhaul-may13.jpg
excerpt: "Hermes Agent has crossed 147,782 GitHub stars — up 4,272 in just two days since our last report. Behind the star count lies a major cache architecture overhaul that boosts prompt cache hit rates from 66.6% to 83.3%, a provider rebrand (Alibaba Cloud → Qwen Cloud), unified Portal client tagging, and a wave of new feature PRs signaling v0.14.0 is taking shape."
author: The Agent Report
---

The post-Tenacity momentum hasn't slowed — Hermes Agent has vaulted from **143,510 to 147,782 GitHub stars** (+4,272 in 48 hours) and from **22,406 to 23,222 forks** — but the real story isn't in the numbers. In the two days since our last roundup, **40+ commits have landed** across cache infrastructure, provider tooling, security, and cross-platform support, contributing to an ecosystem documented in our [complete guide to AI agents]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %}), while **10+ new feature PRs** have been filed for what's shaping up to be the v0.14.0 cycle.

Here's what's changed since May 11.

---

## 🧠 Cache Architecture Overhaul: The System Prompt Is Now Byte-Static

This work builds toward what would become the [v0.14.0 Foundation Release]({% post_url 2026-05-18-hermes-agent-v0140-foundation-release-may16 %}).

The most consequential change since Tenacity is **[PR #24778](https://github.com/NousResearch/hermes-agent/pull/24778) — a ground-up rework of Hermes Agent's prompt caching strategy**, merged by **Teknium** on May 13.

### The Problem

The system prompt was being rebuilt on every API call. `_build_system_prompt_parts()` ran inside the per-call loop on the long-lived path, re-deriving the volatile tier (timestamp + memory snapshot + user profile) every single turn. The result: bytes mutated mid-conversation whenever the minute rolled or memory was written, busting upstream prompt caches at OpenRouter, Portal, and Anthropic.

> *"History (system + all but the last 1–2 messages) must be static within a session. Caching depends on byte-stable bytes."* — PR #24778 description

### The Fix

The solution is elegant in its simplicity: the system prompt is now built **once per session** and replayed verbatim on every turn. Key changes include:

- **~715 lines removed** from `run_agent.py` — the long-lived prefix cache branch, its TTL, and the `_supports_long_lived_anthropic_cache` flag are all gone
- **`prompt_caching.py` simplified** — one single layout (`system_and_3`) replaces the complex multi-block approach: 4 breakpoints (system + last 3 messages), all at `cache_ttl`
- **Config keys dropped** — `prompt_caching.long_lived_prefix` and `prompt_caching.long_lived_ttl` removed from `hermes_cli/config.py`
- **Entire test file removed** — `test_prompt_caching_live.py` was the long-lived live test; it's gone with the feature

### The Result

The wire-format diff tells the story: the OLD layout achieved a cumulative cache hit rate of **66.6%** across 8 turns (a single mid-session cache miss when the system block SHA flipped). The new single-block layout hits **83.3%** — a **16.7 percentage point improvement** in cache efficiency.

For users running Hermes Agent at scale — especially those hitting Portal or Anthropic endpoints — this translates directly to **lower latency, fewer API calls, and reduced costs**.

---

## 🏷️ Unified Portal Client Tagging

**[PR #24779](https://github.com/NousResearch/hermes-agent/pull/24779)** introduces a new `portal_tags.py` module that stamps every Hermes request to Nous Portal with `client=hermes-client-v<version>` (today: `client=hermes-client-v0.13.0`).

What makes this clever: the tag is sourced live from `hermes_cli.__version__` at request time. When the next release bumps the version string, every Portal call site automatically sends the updated tag — **zero additional code changes needed**. The release script's regex-based version bump propagates everywhere.

This replaces the ad-hoc `client=aux` marker from [#24194](https://github.com/NousResearch/hermes-agent/pull/24194) with a unified, version-tagged approach that covers **all** Portal pathways — main agent loop, auxiliary client, compression summaries, and web tool fallbacks.

---

## ☁️ Qwen Cloud: Alibaba Gets a Rebrand

**[PR #24835](https://github.com/NousResearch/hermes-agent/pull/24835)** renames the `alibaba` provider from 'Alibaba Cloud (DashScope)' to **'Qwen Cloud'** and moves it from position 24 to position 6 in the provider picker — right above Xiaomi MiMo, below OpenAI Codex.

This reflects the ongoing rebranding in the Chinese AI ecosystem: Alibaba's generative AI offerings now live under the **Qwen** brand, and Hermes Agent is keeping pace. The internal slug `alibaba` and the `DASHSCOPE_API_KEY` variable remain unchanged — only the human-facing label moved.

---

## 🆕 v0.14.0 Feature Pipeline Takes Shape

While the merged commits tell one story, the **open PRs** filed since May 11 hint at what's coming in the next release:

| PR | Feature | Author |
|----|---------|--------|
| [#24936](https://github.com/NousResearch/hermes-agent/pull/24936) | `hermes gateway send-message` CLI command | jwickers |
| [#24938](https://github.com/NousResearch/hermes-agent/pull/24938) | Release update channel | Sunwo0u |
| [#24926](https://github.com/NousResearch/hermes-agent/pull/24926) | `display.show_reasoning` honored on API server chat completions | Zavianx |
| [#24811](https://github.com/NousResearch/hermes-agent/pull/24811) | Kanban suspend/resume primitives for long-running tasks | shanewas |
| [#24925](https://github.com/NousResearch/hermes-agent/pull/24925) | Session-search: load only FTS5 match context (windowed loading) | shanewas |
| [#24916](https://github.com/NousResearch/hermes-agent/pull/24916) | Buffered tool-progress for no-edit platforms (Weixin) | rzbdz |
| [#24423](https://github.com/NousResearch/hermes-agent/pull/24423) | `X-Hermes-User-*` / `Chat-*` headers for multi-user identity | gsskk |

The **Kanban suspend/resume** PR ([#24811](https://github.com/NousResearch/hermes-agent/pull/24811)) is particularly noteworthy — it adds first-class suspend/resume primitives for long-running Kanban tasks, extending the durable multi-agent board system that shipped in v0.13.0.

---

## 🔧 Fixes and Hardening Across the Stack

The 40+ commits since May 11 span the full breadth of Hermes Agent's platform surface:

### Security
- **Approval DELETE bypass fixed** (`80374d4d`) — a DOTALL flag in the approval pattern allowed newline injection to bypass DELETE confirmations
- **Browser no-sandbox injection fix** ([#24930](https://github.com/NousResearch/hermes-agent/pull/24930)) — `--no-sandbox` now injected via `cmd_parts` instead of `AGENT_BROWSER_CHROME_FLAGS`

### Cross-Platform
- **CJK CLI support** — `display-width` used for response box header labels ([#24843](https://github.com/NousResearch/hermes-agent/pull/24843) by NorethSea)
- **TUI tmux scrollback fix** — scrollback buffer cleared on startup to prevent leakage ([#24843](https://github.com/NousResearch/hermes-agent/pull/24843))
- **Windows CLI crash fix** — `@-file` completion no longer crashes when paths aren't cp1252-decodable ([#24843](https://github.com/NousResearch/hermes-agent/pull/24843))

### Messaging Platforms
- **Telegram** — in-progress reaction cleared on cancelled processing ([#24628](https://github.com/NousResearch/hermes-agent/pull/24628)), thread fallback helper for slash-confirm results
- **LINE** — `build_source` used instead of nonexistent `create_source`
- **WeCom (WeChat Work)** — WebSocket reconnection status updates fixed
- **Signal** — group messages from linked devices handled in syncMessage path
- **WhatsApp** — npm install timeout made configurable
- **Email** — `send_voice()` implementation for audio attachment delivery ([#24931](https://github.com/NousResearch/hermes-agent/pull/24931))

### Infrastructure
- **Docker** — `.venv` ownership fixed so `lazy_deps` can install platform packages ([#24841](https://github.com/NousResearch/hermes-agent/pull/24841))
- **CI** — e2e job timeout bumped to 15 minutes, ripgrep installed in e2e jobs
- **Systemd** — restart delay reduced
- **Model switching** — stale `config.context_length` cleared on model switch

---

## 📊 By the Numbers (May 11 → May 13)

| Metric | May 11 | May 13 | Change |
|--------|--------|--------|--------|
| **GitHub Stars** | 143,510 | **147,782** | **+4,272** |
| **Forks** | 22,406 | **23,222** | **+816** |
| **Open Issues** | 9,960 | **10,713** | +753 |
| **Commits** | — | **40+** in 48h | — |
| **Contributors** | 13 unique in 4 days | **25+** in 2 days | — |

> *"At roughly 2,136 new stars per day since May 11, Hermes Agent continues to be the fastest-growing AI agent runtime on GitHub. The project is on track to cross **150K stars** within the week."* — The Agent Report

## 🔭 What's Next

The v0.14.0 release cycle is clearly taking shape. Based on the open PR pipeline and the density of committed fixes, areas to watch:

- **Cache efficiency** — the byte-static system prompt change is the kind of foundational improvement that compound gains on top of
- **Kanban maturity** — suspend/resume primitives point toward enterprise-grade task lifecycle management
- **Platform breadth** — Weixin support (buffered tool-progress) and multi-user API headers suggest growing enterprise/collaboration use cases
- **CLI tooling** — the `send-message` command and release channel features make Hermes Agent more operable at scale
- **150K stars** — at current growth rates, this milestone should fall within days, not weeks

For developers tracking Hermes Agent's evolution: the post-Tenacity period isn't a cooldown — it's a **build phase**. The infrastructure work landing now (cache architecture, provider tooling, platform hardening) is what enables the next wave of features.

---

*Coverage based on GitHub activity between May 11–13, 2026. Full commit log: [`main...main`](https://github.com/NousResearch/hermes-agent/compare/v2026.5.7...main)*
