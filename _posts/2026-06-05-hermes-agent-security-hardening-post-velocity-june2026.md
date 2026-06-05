---
layout: post
title: "Hermes Agent Post-Velocity Security Sprint — Google OAuth Redaction, Cron Leak Fix, and the Hardening Wave"
date: 2026-06-05 14:00:00 +0200
last_modified_at: 2026-06-05 14:00:00 +0200
meta_description: "Hermes Agent's v0.15 Velocity release introduced promptware defense — and the week after, a coordinated wave of security patches landed: Google OAuth token redaction, cron error-path sanitization, model default hardening, and more."
description: "Hermes Agent's v0.15 Velocity release introduced promptware defense — and the week after, a coordinated wave of security patches landed: Google OAuth token redaction, cron error-path sanitization, model default hardening, and more."
categories: [hermes-agent]
tags: [hermes-agent, nous-research, open-source, security, promptware-defense, oauth-redaction, agent-security, hardening]
reading_time: 7
hero_image: /assets/images/hero/hero-hermes-agent-security-hardening-post-velocity-june2026.jpg
excerpt: "One week after Hermes Agent's v0.15 Velocity release shipped promptware defense at three chokepoints, a fresh wave of security patches tightens credential redaction, cron error paths, model defaults, and more. We break down each fix — Google OAuth token scrubbing, LLM error sanitization, and the quiet hardening that's making Hermes the most security-conscious open-source agent framework."
author: The Agent Report
---

One week ago, Hermes Agent v0.15.0 — the Velocity Release — landed with **1,302 commits, 747 merged PRs, and 321 community contributors**. The headline features were the 76% `run_agent.py` refactor, the Kanban multi-agent platform, the cold-start speedups, and the rebuilt `session_search`. But buried in the changelog was a feature that might matter most for production users: the **promptware defense system** — three layers of protection against brainworm-class attacks.

This week, that security foundation got thicker.

On June 5 alone, a coordinated wave of patches hit the `main` branch: Google OAuth token redaction, cron error-path credential sanitization, model default hardening to prevent accidental $50/hour bills, and several other surgical fixes. Here's what changed, why it matters, and what it signals about Hermes Agent's evolving security posture.

> **Note:** These fixes are being merged to `main` but haven't been tagged as a release yet. You can track them in the [open PRs](https://github.com/NousResearch/hermes-agent/pulls) and update via `hermes update` once they're in a release branch.

## The Promptware Defense That Started It All

Before we dive into this week's patches, it's worth understanding what v0.15.0 already shipped. The Velocity release introduced a **three-chokepoint promptware defense** ([#27248](https://github.com/NousResearch/hermes-agent/pull/27248)):

1. **`tools/threat_patterns.py`** — ~15 new prompt injection patterns detected at tool-call time, covering brainworm-class attacks that try to exfiltrate context or override agent behavior.
2. **Recalled memory scanning** — every piece of persistent memory is scanned for injection patterns *at load time*, before it reaches the agent's context window.
3. **Tool result delimiter markers** — injected delimiters around every tool output to prevent successful delimiter-based prompt injection from poisoning subsequent tool results.

Together, these defenses turned Hermes Agent into one of the few open-source frameworks with **runtime injection detection** — not just static filtering, but behavioral monitoring across memory, tools, and output. The framework earned a mention in several security roundups for this architecture.

## June 5 Patch Wave: Four Security Fixes in One Day

The Velocity release may have shipped the foundation, but security is never done. Yesterday saw four significant security-focused PRs merged or opened:

### 1. Google OAuth Token Redaction ([#39697](https://github.com/NousResearch/hermes-agent/pull/39697))

**Author:** [@briandevans](https://github.com/briandevans) | **Status:** Merged

The existing secret scrubber (`agent/redact.py`) had a prefix-based denylist for catching API keys in tool output and logs — OpenAI, Anthropic, xAI tokens were all covered. But **bare Google OAuth 2.0 tokens** — which start with `ya29.` — and **refresh tokens** — which start with `1//` — had no prefix entry. They were only redacted when adjacent to a JSON key name.

This PR closed **Gap #2** of issue [#39654](https://github.com/NousResearch/hermes-agent/issues/39654) by adding two new regex patterns:

```python
r"ya29\.[A-Za-z0-9_-]{20,}",   # Google OAuth access token
r"1//[A-Za-z0-9_-]{20,}",      # Google OAuth refresh token
```

The minimum 20-character suffix prevents short non-token strings (like `1//foo`) from being falsely redacted — confirmed by a dedicated test case.

This matters because Hermes Agent interacts with Google services through tools (browser automation, Google Drive, Gmail via MCP) and through the Gateway's authentication flows. An unredacted `ya29.` token in a tool output or error log could grant access to a user's entire Google Workspace.

> **Related:** This follows the same pattern as the xAI key redaction patch (`xai-` prefix, commit `5613dfe`), also from last cycle. The pattern is becoming a template for provider-specific credential coverage.

### 2. Cron LLM Error Path Redaction ([#39702](https://github.com/NousResearch/hermes-agent/pull/39702))

**Author:** [@shivros](https://github.com/shivros) | **Status:** Open (Draft → Ready)

When an LLM-backed cron job fails — say, a scheduled report generation or a nightly briefing — the raw exception message was delivered **verbatim** to the user's chat (Telegram, Discord, etc.) and persisted in **plaintext inside `jobs.json`**.

The problem: provider error messages can contain **API key fragments, bearer tokens, or endpoint URLs with embedded credentials**. A truncated error message like `Authentication failed: sk-proj-...` would leak the first ~40 characters of a session key.

The fix is a single line: calling `redact_sensitive_text()` on `error_msg` immediately after construction in `cron/scheduler.py` (line ~1900), matching the same defensive pattern already used in the `no_agent` script path (lines 1019–1024). The import follows the established in-function convention, and a `try/except Exception: pass` wrapper ensures graceful degradation if redaction itself fails.

Both automated reviews (GPT-5.5 and Gemini 3 Flash) approved the change as "correct and achieves the stated goal."

### 3. Model Default Hardening ([#39708](https://github.com/NousResearch/hermes-agent/pull/39708))

**Author:** [@teknium1](https://github.com/teknium1) | **Status:** Merged

Before this fix, if Hermes Agent couldn't determine which model to use (e.g., because of an incomplete setup or a misconfigured provider), it would **silently default to the most expensive Nous flagship model**. For users running on API billing, this meant potential surprise costs of $40–50/hour.

The fix ensures that when the model resolution logic can't find a match, it doesn't silently escalate to the most expensive option. Instead, it falls back to a reasonable default — or surfaces an error clearly so the user can configure it properly. This is both a **cost-security and an availability-security** fix: nobody wants their cron budget blown by a silent model upgrade.

### 4. Desktop Bootstrap & Misc Fixes ([#39707](https://github.com/NousResearch/hermes-agent/pull/39707))

**Author:** [@teknium1](https://github.com/teknium1) | **Status:** Merged

A smaller but telling fix: the Desktop bootstrap marker was getting autostashed by `hermes update` because it wasn't in `.gitignore`. This meant that every time users ran `hermes update`, they'd lose their Desktop installation marker and have to re-run the bootstrap. The `.gitignore` entry now prevents this.

While not a security fix in the traditional sense, it prevents an **availability issue**: users running `hermes update` shouldn't lose their Desktop setup.

## The Broader Security Picture

This patch wave is significant for what it says about **Hermes Agent's security maturation**:

| Area | What Changed | Risk Reduced |
|------|-------------|-------------|
| **Credential leak prevention** | Google OAuth redaction added to prefix denylist | Token theft via tool output / logs |
| **Cron error handling** | Error messages redacted before delivery/ persistence | Credential leakage through scheduled job failures |
| **Model selection** | No silent fallback to priciest model | Cost surprises / billing shock |
| **Update infrastructure** | Desktop marker excluded from git stash | Desktop availability after updates |

The Velocity release's promptware defense addressed **active injection attacks** — brainworm-class exploits and ad-hoc prompt injection. This week's patches address **passive leak vectors** — credentials ending up in places they shouldn't through normal operation. Together, they form defense-in-depth.

## What's Still In Progress

Not everything is resolved. Issue [#39654](https://github.com/NousResearch/hermes-agent/issues/39654) — which prompted the Google OAuth redaction — identified **two gaps**:

- **Gap #1 (deferred):** Persistence-layer redaction in `state.db` — credentials that leak into the session database aren't yet scrubbed on write.
- **Gap #2 (fixed):** Log/tool-output redaction — handled by PR #39697.

The persistence gap is a harder problem — it requires either on-write redaction (which could destroy data needed for debugging) or a separate encrypted credential store. Expect more discussion on this front in the coming weeks.

Additionally, the `_process_job` except block at `cron/scheduler.py:2087–2089` passes `str(e)` to `mark_job_run()` without redaction. This path only triggers for infrastructure exceptions, not LLM provider errors, so the risk is lower — but a complete audit would eventually address it.

## Community Security Contributions Are Rising

A notable trend: security-focused PRs are increasingly coming from **community contributors**, not just core maintainers. PR #39697 came from [@briandevans](https://github.com/briandevans), PR #39702 from [@shivros](https://github.com/shivros). This matches a broader pattern:

- 19 security-tagged issues were closed in v0.15.0 alone
- The promptware defense system was a community-collaborative design ([#27248](https://github.com/NousResearch/hermes-agent/pull/27248))
- The `hermes-agent` skill includes security hardening patterns submitted by community members

For organizations evaluating Hermes Agent for production use, this is a positive signal: the security surface is being actively audited by a broad community, not just a small internal team.

## The Takeaway

The v0.15 Velocity release was about **speed and scale** — faster cold starts, faster search, faster iteration. The week since has been about **security and stability** — closing credential leak paths, hardening error handling, and preventing cost surprises.

This is the rhythm of a maturing open-source project: big feature releases followed by targeted hardening sprints. For production users, the message is clear: Hermes Agent is being built with operational security as a first-class concern, not an afterthought.

If you're running Hermes Agent in production — or evaluating it for deployment — these patches are worth tracking. The credential redaction and model default fixes alone address two of the most common pain points for self-hosted agent deployments: **credential leakage** and **unexpected API costs**.

Stay tuned. The post-v0.15 hardening sprint is still in progress, and more patches are likely before the next tagged release.
