---
title: "Hermes Agent v0.12.0 'Curator' — Autonomous Skill Maintenance, 4 New Providers, Spotify & Google Meet Integrations"
date: 2026-05-01 10:00:00 +0200
last_modified_at: 2026-05-01 10:00:00 +0200
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, release, v0.12, Curator, Spotify, Google Meet, ComfyUI, LM Studio, TTS]
reading_time: 4
hero_image: /assets/images/hero/hero-05-01-hermes-agent-v0120-curator-release.jpg
excerpt: "Nous Research ships Hermes Agent v0.12.0 'The Curator' — an autonomous background agent that grades, prunes, and consolidates your skill library. Also: 4 new inference providers, Spotify + Google Meet plugins, and a 57% faster TUI cold start."
---

Hermes Agent, the open-source AI runtime from **Nous Research** (now 127K+ stars on GitHub), has shipped **v0.12.0 "The Curator"** — a release that marks a major step toward self-maintaining agents. Published on April 30, 2026, this release packs 1,096 commits, 550 merged PRs, and contributions from 213 community members since v0.11.0 one week earlier.

## ✨ The Autonomous Curator

The headline feature is `hermes curator` — a background agent that runs on the gateway's cron ticker (default: every 7 days) and autonomously manages your skill library:

- **Grades and prunes** skills — evaluates quality, consolidates related skills, and archives dead ones
- **Per-run reports** — writes detailed results to `logs/curator/run.json` + `logs/curator/REPORT.md`
- **Consolidated vs. pruned classification** — uses both model judgment and heuristics to decide what to keep
- **`hermes curator status`** — ranks skills by usage (most-used / least-used), so you know what's earning its keep
- **Defense-in-depth gates** — bundled and hub skills are protected from mutation

Conveniently unified under `auxiliary.curator` — pick the curator's model in `hermes model` and manage it from the web dashboard.

## 🔁 Self-Improvement Loop — Substantially Upgraded

The background review fork — the core mechanism where Hermes decides what memories and skills to save after each turn — received a major overhaul:

- **Rubric-based scoring** replaces free-form "should this update?" prompts
- **Active-update bias** — prefers updating the skill the agent just loaded
- **Proper runtime inheritance** — provider, model, and credentials actually propagate to the review fork
- **Scoped toolset** — the review fork is restricted to memory + skills (no shell, no web)
- **Clean context** — prior-turn tool messages excluded from the review summary

## 🧩 New Integrations & Bundled Skills

### ComfyUI v5 — Now Built-In
ComfyUI has been promoted from optional to **bundled-by-default**, with official CLI + REST support and hardware-gated local install. ([#17610](https://github.com/NousResearch/hermes-agent/pull/17610))

### TouchDesigner-MCP — Bundled by Default
Expanded with GLSL, post-FX, audio, geometry, and 9 new reference docs. ([#16753](https://github.com/NousResearch/hermes-agent/pull/16753))

### Spotify — Native Tools + Wizard
7 native tools (play, search, queue, playlists, devices) behind PKCE OAuth, with an interactive setup wizard and bundled skill. ([#15121](https://github.com/NousResearch/hermes-agent/pull/15121))

### Google Meet Plugin
Full pipeline to join calls, transcribe, speak, and follow up — powered by realtime OpenAI transport + a Node bot server. ([#16364](https://github.com/NousResearch/hermes-agent/pull/16364))

### New Skills
- **Humanizer** — strips AI-isms from text ([#16787](https://github.com/NousResearch/hermes-agent/pull/16787))
- **claude-design** — HTML artifact skill ([#16358](https://github.com/NousResearch/hermes-agent/pull/16358))
- **design-md** — Google's DESIGN.md spec skill ([#14876](https://github.com/NousResearch/hermes-agent/pull/14876))
- **airtable** — salvaged skill with API key wiring ([#16291](https://github.com/NousResearch/hermes-agent/pull/16291))

## 🏗️ 4 New Inference Providers

- **GMI Cloud** — first-class API-key provider ([#16663](https://github.com/NousResearch/hermes-agent/pull/16663))
- **Azure AI Foundry** — with auto-detection ([#15845](https://github.com/NousResearch/hermes-agent/pull/15845))
- **LM Studio** — upgraded from custom-endpoint alias to first-class provider with dedicated auth, doctor checks, reasoning transport, and live `/models` listing ([#17102](https://github.com/NousResearch/hermes-agent/pull/17102))
- **MiniMax OAuth** — PKCE browser flow ([#17524](https://github.com/NousResearch/hermes-agent/pull/17524))
- **Tencent Tokenhub** — new provider ([#16960](https://github.com/NousResearch/hermes-agent/pull/16960))

## 📱 Platforms & Gateway

- **Microsoft Teams** (19th platform) — ships as a plugin via the new pluggable gateway adapter system ([#17751](https://github.com/NousResearch/hermes-agent/pull/17751))
- **Tencent 元宝 (Yuanbao)** (18th platform) — native adapter with text + media delivery ([#16298](https://github.com/NousResearch/hermes-agent/pull/16298))
- **Native multi-image sending** across Telegram, Discord, Slack, Mattermost, Email, and Signal ([#17909](https://github.com/NousResearch/hermes-agent/pull/17909))

## ⚡ Performance & UX

- **TUI cold start cut ~57%** — via lazy agent init, lazy imports, mtime-cached config loading, and memoized tool definitions ([#17190](https://github.com/NousResearch/hermes-agent/pull/17190))
- **`hermes -z` one-shot mode** — non-interactive prompt execution ([#15702](https://github.com/NousResearch/hermes-agent/pull/15702))
- **Remote model catalog manifest** — OpenRouter + Nous Portal models pulled from a remote manifest so new models show up without a release ([#16033](https://github.com/NousResearch/hermes-agent/pull/16033))
- **Secret redaction off by default** — prevents the long-standing patch-corruption issue ([#16794](https://github.com/NousResearch/hermes-agent/pull/16794))
- **Pluggable TTS provider registry** + **Piper local TTS** — native local TTS ships as a provider ([#17843](https://github.com/NousResearch/hermes-agent/pull/17843))

## 📦 Also Landing Today: `/goal` Persistent Cross-Turn Goals

Hot on the heels of v0.12.0, the team has already shipped the **`/goal`** command — Hermes' take on the "Ralph loop" (inspired by Codex CLI 0.128.0). Set a standing objective and Hermes keeps working toward it across turns until completion, pausing only when you intervene. ([#18262](https://github.com/NousResearch/hermes-agent/pull/18262))

## 📊 By the Numbers

- **1,096 commits** since v0.11.0
- **550 merged PRs**
- **1,270 files changed · 217,776 insertions**
- **213 community contributors** (including co-authors)
- **46 reactions** on the release (25 🎉, 8 ❤️, 7 👍, 6 🚀)

---

With autonomous skill curation, a burgeoning plugin ecosystem, and weekly releases that ship hundreds of PRs, Hermes Agent is rapidly maturing into one of the most extensible AI agent platforms available. The Curator release — where the agent starts maintaining *itself* — marks an inflection point.

**Full changelog**: [v2026.4.23...v2026.4.30](https://github.com/NousResearch/hermes-agent/compare/v2026.4.23...v2026.4.30)
