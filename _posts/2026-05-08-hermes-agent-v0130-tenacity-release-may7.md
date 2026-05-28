---
layout: post
title: "Hermes Agent v0.13.0 \"Tenacity\" Lands — Multi-Agent Kanban, /goal Persistence, Checkpoints v2, and Major Security Hardening"
date: 2026-05-08 16:00:00 +0200
last_modified_at: 2026-05-08 16:00:00 +0200
meta_description: "Hermes Agent v0.13.0 Tenacity ships multi-agent Kanban boards, goal persistence, Checkpoints v2, 8 P0 security fixes, Google Chat as the 20th platform,."
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, open-source, v0.13.0, tenacity, multi-agent-kanban, durable-goals, security-hardening, checkpoints, i18n]
reading_time: 7
hero_image: /assets/images/hero/hero-hermes-agent-v0130-tenacity-release-may7.jpg
excerpt: "Hermes Agent ships v0.13.0 'The Tenacity Release' — the biggest update yet. Multi-agent Kanban boards, /goal persistence, Checkpoints v2 with real pruning, 8 P0 security fixes with redaction ON by default, Google Chat as the 20th platform, pluggable providers, and seven i18n locales. Now at 138K GitHub stars."
author: The Agent Report
---

Hermes Agent, the open-source AI runtime from **Nous Research**, has released **v0.13.0 (v2026.5.7) — "The Tenacity Release"** — its most ambitious update to date. The release ships just one week after v0.12.0 "Curator" — and it arrives in the midst of a rapidly maturing open-source agent ecosystem and represents **864 commits, 588 merged PRs, 829 files changed, 128,366 insertions, and 282 issues closed** (13 of them P0 severity). The project has also crossed **138,390 GitHub stars**, up from 135K just two days ago.

> *"The Tenacity Release — Hermes Agent now finishes what it starts."* — Teknium1, release notes

## 🧩 Multi-Agent Kanban: Delegate to an AI Team That Actually Finishes

Hermes Agent sits among the [top open-source AI agent frameworks]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}), and this release cements that position.

The headline feature of v0.13.0 is the **durable multi-agent Kanban board system** — a complete reimplementation that lets you spin up a board, drop tasks on it, and have multiple Hermes worker agents pick them up, hand off, and close them out with real reliability guarantees.

### Worker Lifecycle That Doesn't Forget

The Kanban system solves the hardest problem in multi-agent orchestration: **making sure tasks actually complete**. Key durability mechanisms include:

- **Heartbeat tracking** — workers pulse their status; silent workers get reclaimed
- **Zombie detection** — processes that crash without cleanup are detected and their tasks re-assigned ([#21183](https://github.com/NousResearch/hermes-agent/pull/21183))
- **Per-task max_retries** — override retry budgets at the individual task level ([#21330](https://github.com/NousResearch/hermes-agent/pull/21330))
- **Hallucination gate + recovery** — detects when a worker fabricates card completions and triggers recovery UX ([#20232](https://github.com/NousResearch/hermes-agent/pull/20232))
- **Auto-block on incomplete exit** — workers that exit without completing their task automatically self-block ([#21214](https://github.com/NousResearch/hermes-agent/pull/21214))
- **Diagnostics engine** — a generic distress-signal engine for task health monitoring ([#20332](https://github.com/NousResearch/hermes-agent/pull/20332))

> One install, many kanbans. Your AI team now holds itself accountable.

The dashboard also gained per-platform home-channel notification toggles ([#19864](https://github.com/NousResearch/hermes-agent/pull/19864)), multi-project board support ([#19653](https://github.com/NousResearch/hermes-agent/pull/19653)), and workspace-aware inline creation forms ([#19679](https://github.com/NousResearch/hermes-agent/pull/19679)).

## 🎯 `/goal` — The Agent Doesn't Forget What You Asked

The new **`/goal` slash command** introduces the "Ralph loop" as a first-class primitive: lock the agent onto a target and it stays on task across turns, even when you switch context or the session bounces ([#18262](https://github.com/NousResearch/hermes-agent/pull/18262)). This is a fundamental shift from stateless turn-by-turn interaction to **persistent objective-oriented execution**.

## 💾 Checkpoints v2 — State Persistence Rewritten

Checkpoints received a ground-up rewrite with **real pruning**, disk guardrails, and no more orphan shadow repos ([#20709](https://github.com/NousResearch/hermes-agent/pull/20709)). Combined with **auto-resume after gateway restart** ([#21192](https://github.com/NousResearch/hermes-agent/pull/21192)), sessions now survive `/update` restarts, source-file reloads, and gateway bounces seamlessly.

## 🛡️ Security Wave — 8 P0 Closures

v0.13.0 delivers the most aggressive security hardening pass in Hermes Agent's history. (For context on the broader [state of AI agent development as of May 2026]({% post_url 2026-05-29-state-of-ai-agents-may-2026 %}), see our comprehensive overview.) Eight Priority-0 issues were closed:

| Security Fix | Impact |
|-------------|--------|
| **Redaction ON by default** | Secrets are now auto-redacted in all output ([#21193](https://github.com/NousResearch/hermes-agent/pull/21193)) |
| **Discord role-allowlists guild-scoped** | Closes CVSS 8.1 cross-guild DM bypass ([#21241](https://github.com/NousResearch/hermes-agent/pull/21241)) |
| **WhatsApp rejects strangers by default** | No more responding to unknown numbers ([#21291](https://github.com/NousResearch/hermes-agent/pull/21291)) |
| **MCP OAuth TOCTOU fix** | Time-of-check/time-of-use window closed ([#21176](https://github.com/NousResearch/hermes-agent/pull/21176)) |
| **auth.json TOCTOU fix** | Credential writers now atomic ([#21194](https://github.com/NousResearch/hermes-agent/pull/21194)) |
| **Browser SSRF floor** | Cloud-metadata endpoints blocked in hybrid routing ([#21228](https://github.com/NousResearch/hermes-agent/pull/21228)) |
| **`hermes debug share` redaction** | Logs redacted before upload ([#19318](https://github.com/NousResearch/hermes-agent/pull/19318)) |
| **Cron prompt-injection scanning** | Skill content scanned before execution ([#21350](https://github.com/NousResearch/hermes-agent/pull/21350)) |

Additional security improvements include **SRI integrity for dashboard plugin scripts**, **0600 permissions on all credential files**, and **platform allowlists** (`allowed_channels` / `allowed_chats` / `allowed_rooms`) across Slack, Telegram, Mattermost, Matrix, and DingTalk ([#21251](https://github.com/NousResearch/hermes-agent/pull/21251)).

## 🌐 Language, Platforms & Providers

### Seven i18n Locales
The static gateway and CLI messages now translate to **Chinese, Japanese, German, Spanish, French, Ukrainian, and Turkish**. The docs site also gained a **zh-Hans (Chinese) locale** ([#20231](https://github.com/NousResearch/hermes-agent/pull/20231), [#20329](https://github.com/NousResearch/hermes-agent/pull/20329), [#20467](https://github.com/NousResearch/hermes-agent/pull/20467), [#20474](https://github.com/NousResearch/hermes-agent/pull/20474)).

### Google Chat — Platform #20
**Google Chat** joins the supported platform roster — the 20th messaging platform. It ships alongside a **generic platform-plugin hooks surface** so third-party adapters can drop in without touching core code ([#21306](https://github.com/NousResearch/hermes-agent/pull/21306), [#21331](https://github.com/NousResearch/hermes-agent/pull/21331)).

### Pluggable Providers
The `ProviderProfile` ABC and `plugins/model-providers/` directory make inference providers a **pluggable surface** — third-party providers can now be dropped in without modifying the runtime ([#20324](https://github.com/NousResearch/hermes-agent/pull/20324)).

## 🎬 New Capabilities

- **`video_analyze` tool** — native video understanding on Gemini and compatible multimodal models ([#19301](https://github.com/NousResearch/hermes-agent/pull/19301))
- **xAI Custom Voices** — voice cloning as a TTS provider ([#18776](https://github.com/NousResearch/hermes-agent/pull/18776))
- **Post-write delta lint** — the agent now lints its own `write_file` and `patch` calls for Python, JSON, YAML, and TOML syntax errors ([#20191](https://github.com/NousResearch/hermes-agent/pull/20191))
- **`no_agent` cron mode** — script-only watchdog pattern for cron jobs ([#19709](https://github.com/NousResearch/hermes-agent/pull/19709))
- **`transform_llm_output` plugin hook** — reshape or filter LLM output before it hits the conversation ([#21235](https://github.com/NousResearch/hermes-agent/pull/21235))
- **ACP `/steer` and `/queue`** — direct in-flight agents or queue follow-ups from Zed, VS Code, or JetBrains ([#18114](https://github.com/NousResearch/hermes-agent/pull/18114))
- **API server `X-Hermes-Session-Key`** — long-term memory scoping per session ([#20199](https://github.com/NousResearch/hermes-agent/pull/20199))

## 🔌 New Models & Skills

**New models** include `deepseek/deepseek-v4-pro`, `x-ai/grok-4.3`, `openrouter/owl-alpha` (free tier), `tencent/hy3-preview`, and Arcee Trinity Large with temperature + compression overrides.

**6 new optional skills** landed: Shopify (Admin + Storefront GraphQL), here.now location awareness, shop-app personal shopping assistant, an Anthropic financial-services bundle, kanban-video-orchestrator, and searxng-search.

## 📊 By the Numbers

| Metric | Value |
|--------|-------|
| GitHub Stars | **138,390** |
| Forks | **21,332** |
| Open Issues | 8,904 |
| Commits since v0.12.0 | 864 |
| Merged PRs | 588 |
| Community contributors | 295 |
| P0 issues closed | 13 |

## The Takeaway

v0.13.0 "Tenacity" marks a decisive inflection point for Hermes Agent. The multi-agent Kanban system transforms it from a single-agent CLI tool into a **durable multi-agent orchestration platform**. The `/goal` persistence, Checkpoints v2, and gateway auto-resume together create a system that genuinely **remembers and finishes what it starts**. And the 8-P0 security wave — combined with platform allowlists, i18n, and pluggable providers — signals that Nous Research is investing heavily in making Hermes Agent enterprise-ready.

With 138K stars and nearly 300 community contributors in a single weekly cycle, the project's trajectory shows no signs of slowing down. If you haven't tried Hermes Agent since the early days, **v0.13.0 is the release to come back for**.

---

*Full changelog: [v2026.4.30...v2026.5.7](https://github.com/NousResearch/hermes-agent/compare/v2026.4.30...v2026.5.7)*
