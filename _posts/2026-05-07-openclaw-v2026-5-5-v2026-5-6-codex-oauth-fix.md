---
layout: post
title: "Openclaw Ships Two Releases in a Day: v2026.5.5 and v2026.5.6 Fix Codex OAuth Routing, Plugin Fetch Stability"
date: 2026-05-07 10:00:00 +0200
last_modified_at: 2026-05-07 10:00:00 +0200
meta_description: "Openclaw ships two releases in one day: v2026.5.5 with Discord and Telegram fixes, then v2026.5.6 hotfixing a critical Codex OAuth routing regression from doctor --fix."
categories: [openclaw]
tags: [openclaw, claw-controller, agent-autonomy, codex-oauth, rapid-iteration]
reading_time: 5
hero_image: /assets/images/hero/hero-openclaw-v2026-5-5-v2026-5-6-codex-oauth-fix.jpg
excerpt: "Openclaw shipped two back-to-back releases on May 6 — v2026.5.5 with extensive platform fixes across Discord, Telegram, and provider integrations, followed hours later by v2026.5.6 to hotfix a critical doctor --fix regression that could rewrite OpenAI Codex OAuth routes. The rapid turnaround highlights the project's operational maturity at 369K+ stars."
author: The Agent Report
---

**Openclaw** — the open-source personal AI assistant now sitting at **369,246 GitHub stars** and **76,186 forks** — demonstrated its operational cadence on May 6 with two releases in a single day. For ecosystem context, see our [ultimate guide to agent frameworks]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}). **v2026.5.5** shipped in the morning with a broad set of fixes across messaging platforms, provider integrations, and the control UI. Hours later, **v2026.5.6** followed to hotfix a regression introduced by v2026.5.5's `doctor --fix` repair logic that could accidentally break OpenAI Codex OAuth setups.

The double-release is a glimpse into what operating at this scale looks like: even well-intentioned automated repair tools need careful guardrails, and the project's ability to detect, roll back, and communicate fixes within hours is a sign of growing engineering maturity.

## v2026.5.5 — A Platform-Wide Cleanup

Released on the morning of May 6, **v2026.5.5** brought fixes across seven different areas of the codebase, reflecting the breadth of platforms Openclaw now supports:

### Messaging Platform Fixes

- **Feishu** (Chinese enterprise messaging): Fixed missing native topic starter thread IDs before session routing, ensuring first turns and follow-ups stay in the same topic session. (#78262) — Thanks @joeyzenghuan.
- **LINE**: Added validation to reject `dmPolicy: "open"` configurations without a wildcard `allowFrom`, preventing webhook DMs from being silently acknowledged and then blocked. (#78316)
- **Telegram/Codex**: Kept message-tool-only progress drafts visible and fixed duplicate item/tool draft line rendering in Codex environments. (#75641)

### Provider Integration Fixes

- **xAI/Grok**: Two fixes for the Grok 4.3 integration — stopped sending OpenAI-style reasoning effort controls to native Grok Responses models (which caused `Invalid reasoning effort` errors on live Gateway runs), and clamped the bundled xAI thinking profile to `off` to prevent unsupported reasoning levels from being sent to native Grok models.
- **Matrix/approvals**: Added retry logic for approval delivery (up to 3 times with short backoff) so transient Matrix send failures don't strand pending approval prompts. (#78179) — Thanks @Patrick-Erichsen.

### Discord and Control UI

- **Discord/gateway**: Fixed a heartbeat ACK timing issue — the timeout is now measured from the actual heartbeat send rather than a potentially stale reference point, preventing false reconnect loops while the channel is still awaiting readiness. (#77668) — Thanks @bryce-d-greybeard and @NikolaFC.
- **Discord/guilds**: Plain text control commands like `/steer` are now routed through the normal authorization and mention gate, instead of being silently dropped before an agent session can see them. (#78080) — Thanks @ramitrkar-hash.
- **Control UI/Sessions**: The compaction count is now a compact `N Checkpoint(s)` disclosure, with expanded session-level details using modern checkpoint history cards across responsive table layouts. — Thanks @BunsDev.
- **Control UI/performance**: Chat and channel tabs remain responsive while history payloads and channel probes are slow, with partial channel loading indicators.

## v2026.5.6 — The Critical Hotfix

Barely eight hours after v2026.5.5 shipped, **v2026.5.6** landed as a targeted hotfix release. The urgency was clear: v2026.5.5's `doctor --fix` repair logic had a bug that could rewrite valid `openai-codex/*` ChatGPT/Codex OAuth routes to `openai/*`, potentially breaking OAuth-only GPT-5.5 setups or accidentally moving users onto the OpenAI API-key route.

The fix was a clean **revert** of that specific repair path in the `doctor` tool. For users who had already run v2026.5.5's `doctor --fix` and found their default model changed, the release notes included a straightforward recovery command:

```
openclaw models set openai-codex/gpt-5.5 && openclaw config validate
```

Beyond the revert, v2026.5.6 included three additional fixes:

1. **Plugin/runtime fetch stability**: Third-party symbol metadata was being passed through plain request header dictionaries into native `fetch` or `Headers` objects, causing SDK and guarded/proxy fetch paths to reject otherwise valid plugin requests. (#77846) — Thanks @shakkernerd.

2. **Debug proxy normalization**: Captured fetch header dictionaries from caller-owned header objects could contain symbol metadata that made debug-proxy replays fail. The fix normalizes these dictionaries before replaying requests.

3. **Web fetch timeout handling**: Guarded dispatcher cleanup is now properly bounded after request timeouts, meaning timed-out fetches return tool errors instead of leaving Gateway tool lanes active. (#78439) — Thanks @obviyus.

## What This Says About Openclaw's Operational Maturity

Shipping two releases in one day — and hotfixing a regression within hours — is the kind of operational tempo that distinguishes mature platforms from weekend projects. For more on the agent framework ecosystem, see our [ultimate guide to agent frameworks]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).

| Metric | v2026.5.5 → v2026.5.6 |
|--------|----------------------|
| Time between releases | ~8 hours |
| Regression detected | Community-reported (#78407) |
| Fix type | Clean revert of affected path |
| Recovery guidance | Provided in release notes |
| Additional fixes shipped with hotfix | 3 (fetch, proxy, timeout) |

The project's rapid response to the Codex OAuth regression demonstrates several things:

- **Active monitoring**: The community and maintainers detected the issue quickly.
- **Surgical fixes**: Rather than reverting the entire v2026.5.5 release, the team identified the specific `doctor --fix` path that caused the problem and reverted only that change.
- **Clear communication**: The release notes included exact recovery commands and links to documentation.
- **Continuous improvement**: The hotfix also shipped three unrelated fixes that had been queued, maximizing the value of the rapid patch cycle.

## The Bigger Picture

Openclaw's growth shows no signs of slowing. At **369,246 stars** (up roughly 800 stars since yesterday's coverage at 368,455), the project continues to absorb new contributors and users. The **76,186 forks** indicate a massive ecosystem of custom agents, plugins, and deployments.

The v2026.5.5 / v2026.5.6 cycle also highlights a tension inherent in open-source AI infrastructure: **automated repair tools** like `doctor --fix` are powerful but must be carefully scoped. The regression affected the Codex OAuth path — a critical authentication route for users who rely on OpenAI's free-tier ChatGPT/Codex OAuth tokens rather than paid API keys. Any tool that touches authentication routes needs extra safeguards, and Openclaw's team clearly agrees.

For organizations running Openclaw in production, the takeaway is straightforward:

1. **Pin your Openclaw version** if you rely on Codex OAuth authentication.
2. **Test `doctor --fix` in a staging environment** before running it on production gateways.
3. **Monitor the release feed** — Openclaw's rapid patch cycle means fixes arrive quickly, but so do new changes.

## Quick Reference

| Release | Date | Key Changes |
|---------|------|-------------|
| v2026.5.5 | May 6, 2026 | Feishu, LINE, Telegram, xAI/Grok, Discord, Control UI fixes |
| v2026.5.6 | May 6, 2026 | Reverted Codex OAuth route rewrite in `doctor --fix`, fetch stability, debug proxy, timeout handling |

Both releases are available now via `npm install -g openclaw`. Full release notes on [GitHub](https://github.com/openclaw/openclaw/releases).

---

*Openclaw continues to define what it means to operate an open-source AI agent controller at planetary scale. Two releases, one day, zero drama — just software engineering.*
