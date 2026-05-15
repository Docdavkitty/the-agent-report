---
title: "Hermes Agent Crosses 150K Stars: SimpleX Chat, HuggingFace Skills Hub, Deep Crawl, and New Cron Features"
date: 2026-05-15 17:00:00 +0200
last_modified_at: 2026-05-15 17:00:00 +0200
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, open-source, 150k-stars, simple-x-chat, skills-hub, cron, deep-crawl, supply-chain-security, frontdesk]
reading_time: 7
hero_image: /assets/images/hero/hero-hermes-agent-150k-stars-feature-wave-may15.jpg
excerpt: "Hermes Agent has crossed 150,000 GitHub stars — up 3,410 in just two days to reach 151,192. Behind the milestone lies one of the busiest 48-hour feature sprints since the Tenacity release: a new SimpleX Chat gateway, HuggingFace Skills Hub integration, a local deep crawl tool, per-job cron reasoning, dependency supply-chain hardening, and much more."
---

The post-Tenacity momentum has accelerated into a new gear. Hermes Agent has vaulted past **150,000 GitHub stars** — reaching **151,192** as of this writing, up 3,410 in 48 hours from 147,782 on May 13. Forks have climbed to **23,955** (+733), and open issues have grown to **11,302** as the community engagement scales.

But the star count, impressive as it is, tells only half the story. The last 48 hours have delivered one of the **broadest feature sprints** since the v0.13.0 Tenacity release — spanning a new decentralized messaging gateway, a major Skills Hub expansion, an ambitious frontdesk runtime architecture, supply-chain security hardening, and a flurry of new tools and provider integrations.

Here's the full breakdown.

---

## 🌟 150,000 Stars: The Fastest-Growing Agent Runtime

Hermes Agent's growth trajectory continues to defy expectations:

| Metric | May 13 | May 15 | Change |
|--------|--------|--------|--------|
| **GitHub Stars** | 147,782 | **151,192** | **+3,410** |
| **Forks** | 23,222 | **23,955** | **+733** |
| **Open Issues** | 10,713 | **11,302** | +589 |
| **Active Contributors** | — | **15+ unique** in 48h | — |

At roughly **1,700 new stars per day**, Hermes Agent has added **~24,000 stars in 15 days** since v0.12.0. The project is now within striking distance of overtaking major frameworks like LangChain (161K) and is on track to cross **155K by the weekend**.

---

## 🆕 SimpleX Chat: A Private, Decentralized Gateway

**[PR #26208](https://github.com/NousResearch/hermes-agent/pull/26208)** by community contributor **Mibayy** adds **SimpleX Chat** as a Hermes gateway platform — bringing Hermes Agent to one of the most privacy-forward messaging networks available.

SimpleX ([simplex.chat](https://simplex.chat)) is unique among messaging platforms: there are **no persistent user IDs**. Every contact is identified by an opaque internal ID generated at connection time. There are no servers to compromise, no directory to leak.

The adapter connects to a local `simplex-chat` daemon via WebSocket, listens for inbound messages, and sends replies. It was originally proposed in PR #2558 as a core-modifying integration but was reshaped into the plugin architecture, making it easy to install and maintain independently.

> *"SimpleX has no user IDs, no email, no phone numbers — the best candidates for Hermes agent traffic"* — PR description

This is a significant addition for developers building privacy-sensitive agent applications — medical, legal, or journalistic use cases where message metadata cannot be exposed.

---

## 🧠 Skills Hub: HuggingFace/skills Becomes a Trusted Default Tap

**[PR #2549](https://github.com/NousResearch/hermes-agent/pull/2549)**, merged by **kshitijk4poor**, adds **HuggingFace's official skill catalog** to Hermes Agent's default GitHub taps and classifies it as a **trusted source** — alongside the existing `openai/skills` and `anthropics/skills` taps.

This means users now have access to HuggingFace's growing library of **huggingface/skills** out of the box, with no additional configuration. The integration spans:

- `tools/skills_guard.py` — `huggingface/skills` added to `TRUSTED_REPOS`
- `tools/skills_hub.py` — `GitHubSource.DEFAULT_TAPS` includes the new tap
- Documentation — listed under default taps and trusted-source examples

HuggingFace's skill catalog has been expanding rapidly, covering everything from multimodal inference to dataset processing — making this a natural addition to Hermes Agent's skill ecosystem.

---

## 🕸️ Crawl4AI Deep Crawl: Local, Recursive Web Scraping

**[PR #26213](https://github.com/NousResearch/hermes-agent/pull/26213)** by **breakneo** adds a new built-in `crawl4ai_deep_crawl` tool to the web toolset — a **local, recursive, multi-page web crawler** powered by Crawl4AI with **zero external API cost**.

Key features:

- **Recursive crawling** — follows links, extracts Markdown, with configurable depth control
- **Local execution** — runs entirely on the user's machine, no third-party API calls
- **Smart fallback** — auto-detects `crawl4ai` in the Hermes venv, falls back to `~/tasklines/browser/.venv/bin/python`
- **Security-aware** — respects Hermes' existing SSRF and website policy checks
- **Progress feedback** — sentinel-based stdout parsing handles Crawl4AI's progress logs

For users who need to analyze websites or scrape documentation (the canonical use case for agent tool use), this tool eliminates the need for paid web scraping APIs.

---

## ⏰ Cron Evolves: Per-Job Reasoning + Name-Based Lookup

Two major cron improvements landed on May 15:

### Per-Job Reasoning Effort

**[PR #26214](https://github.com/NousResearch/hermes-agent/pull/26214)** by **evaclawdbot** adds a `reasoning_effort` override for individual cron jobs. Scheduled tasks can now opt into deeper or lighter model reasoning independently from the global interactive-agent setting.

```yaml
# A low-effort daily check-in
- name: daily_summary
  schedule: "0 9 * * *"
  reasoning_effort: low

# A deep-analysis weekly report
- name: weekly_research
  schedule: "0 8 * * 1"
  reasoning_effort: high
```

This completes the pattern started by per-job model/provider/base URL overrides — giving cron users full flexibility without sacrificing the global defaults.

### Name-Based Job Lookup

**[PR #26226](https://github.com/NousResearch/hermes-agent/pull/26226)** by **buntingszn** adds **name-based lookup** for cron mutation operations. `hermes cron run my_job_name` now works directly, instead of requiring the hex ID. The system handles ambiguity with clear error messages when two jobs share a name.

### WakeAgent Pre-Run Gate Recipes

**Teknium** also landed **[PR #26229](https://github.com/NousResearch/hermes-agent/pull/26229)** — documentation for three pre-run gate recipes using the existing `script` + `wakeAgent` mechanism:

- **File-change gate** — only run if a file's mtime has changed
- **External-flag gate** — run only when a flag file exists
- **SQL-count gate** — run only if a database condition is met

These patterns give users conditional cron execution at **zero additional code cost**.

---

## 🏗️ Frontdesk: Always-Available Live Worker Runtime

**[PR #26261](https://github.com/NousResearch/hermes-agent/pull/26261)** by **wkimdevai-legend** introduces the **frontdesk** runtime — an ambitious new architectural layer for always-available foreground routing and background worker lanes.

This is still in its early stages (open PR), but the scope is substantial:

- Always-available foreground routing and background worker lanes
- Task registry metadata for durable orchestration
- Worker/reviewer lane scaffolding with review-import surfaces
- Cancellation semantics and TUI/gateway/CLI alignment
- Full product/PRD documentation included in the PR

The frontdesk system points toward a future where Hermes Agent runs as a persistent background service with proper process lifecycle management — a major step toward enterprise-grade agent infrastructure.

---

## 🔒 Supply Chain Security: Dependency Upper Bounds Codified

**[PR #24226](https://github.com/NousResearch/hermes-agent/pull/24226)** by **Siddharth Balyan** adds tight upper bounds to **5 loose dependencies** and formally documents the project's **supply chain pinning policy**.

This is a direct response to two recent industry incidents:

- **Mini Shai-Hulud supply chain campaign** (May 2026)
- **litellm compromise** (March 2026)

The PR adds upper bounds to `hindsight-client`, `pyyaml`, `httpx`, `pydantic`, and `requests`, and writes the policy into contributor documentation so future PRs don't reintroduce loose pins.

> *"Codify the dependency pinning policy that was established in PRs #2810 and #9801 but never written down for contributors."* — PR #24226 description

---

## 🎤 New TTS Provider: SenseAudio

**[PR #26262](https://github.com/NousResearch/hermes-agent/pull/26262)** by **QWERTY0205** registers **SenseAudio** as a new TTS provider, following the same dispatch pattern as MiniMax.

SenseAudio exposes a MiniMax-style `t2a_v2` endpoint that returns hex-encoded MP3 audio. Configuration:

- Auth via `SENSEAUDIO_API_KEY` environment variable
- Default model: `senseaudio-tts-1.5-260319`
- Default voice: `female_0033_b`
- Default base URL: `https://api.senseaudio.cn`

---

## 🔧 Highlights from the Fixes & Hardening

Beyond the feature work, the last 48 hours saw an impressive volume of quality-of-life fixes:

| Area | Change | PR/Commit |
|------|--------|-----------|
| **YOLO Mode** | Red warning in banner + status bar when `--yolo` active | [#26239](https://github.com/NousResearch/hermes-agent/pull/26239) by **Mibayy** |
| **Image Gen** | Actionable setup message with FAL signup link + gateway status | [#26222](https://github.com/NousResearch/hermes-agent/pull/26222) by **Teknium** |
| **ACP** | `hermes acp --setup-browser` bootstraps browser tools for registry installs | [#26211](https://github.com/NousResearch/hermes-agent/pull/26211) by **Teknium** |
| **WhatsApp** | Fail-fast timeout on Baileys `sendMessage` hangs (60s default) | [#26215](https://github.com/NousResearch/hermes-agent/pull/26215) by **Wysie** |
| **Web Tools** | `asyncio.gather` bug fixed — single failing URL no longer discards all results | by **Nidhi Singh** |
| **Slack** | Whitespace-only command text no longer causes IndexError | by **nidhi-singh02** |
| **Provider UA** | User-Agent set on provider profile model fetches to avoid WAF 403s | by **teknium1** |
| **Telegram** | Tool progress bubbles roll over before hitting platform message limits | [#26208](https://github.com/NousResearch/hermes-agent/pull/26208) by **Qwinty** |
| **Codex Runtime** | Three config-corruption bugs fixed in the Hermes↔Codex migration path | Multiple PRs from **kshitijk4poor**, **Steve Kelly**, **zccyman** |
| **Env Flags** | Require explicit truthy values for session env vars across all consumers | [#26254](https://github.com/NousResearch/hermes-agent/pull/26254) by **teknium1** |
| **CTRL+J** | Newline input now works on macOS CLI | by **flowioo** |

---

## 📊 By the Numbers: The Post-Tenacity Sprint in Context

| Period | Stars Added | Key Features |
|--------|------------|--------------|
| May 7–11 (post-Tenacity) | +5,500 | Finance skill, Kanban diagnostics, Nix fixes |
| May 11–13 | +4,272 | Cache overhaul, Portal tagging, Qwen Cloud |
| **May 13–15** | **+3,410** | **SimpleX, HF Skills Hub, deep crawl, cron reasoning, supply chain policy** |
| **Total since v0.12.0 (Apr 30)** | **+24,192** | — |

The pace is remarkable: **~1,600 new stars per day on average** across the entire post-Tenacity period, with **no signs of deceleration**.

---

## 🔭 What's Next

Based on the open PR pipeline and the density of commits, several themes are emerging for v0.14.0:

1. **Frontdesk runtime** — if merged, this would be one of the most significant architectural changes since Tenacity, enabling persistent background agent operation
2. **Cron maturity** — per-job reasoning, name-based lookup, and pre-run gates are rounding out the cron subsystem into a first-class scheduling platform
3. **Messaging breadth** — SimpleX brings the platform count even higher, with WhatsApp reliability fixes ensuring existing gateways are production-ready
4. **Codex interop** — the flurry of Codex migration fixes suggests Hermes Agent is becoming the default runtime for Codex users, which would add significant user growth
5. **Supply chain hardening** — the dependency policy PR signals that Nous Research is taking post-compromise supply chain defense seriously

At this cadence, **v0.14.0** could land within a week — and 160K stars may not be far behind.

---

*Coverage based on GitHub activity between May 13–15, 2026. Star counts as of 2026-05-15 16:00 UTC. Full commit log: [`main...main`](https://github.com/NousResearch/hermes-agent/compare/v2026.5.7...main)*
