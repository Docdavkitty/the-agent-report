---
title: "Openclaw v2026.5.4: Google Meet Voice Integration, File Transfer Plugin, and 368K GitHub Stars"
date: 2026-05-05 14:30:00 +0200
last_modified_at: 2026-05-05 14:30:00 +0200
categories: [openclaw]
tags: [openclaw, claw-controller, agent-autonomy, google-meet, voice-agents]
reading_time: 7
hero_image: /assets/images/hero/hero-openclaw-v2026-5-4-google-meet-file-transfer.jpg
excerpt: "Openclaw hits v2026.5.4 with Google Meet voice call integration, a bundled file-transfer plugin, OpenRouter caching, WhatsApp Newsletter support, and over 120 fixes. The project now sits at an astonishing 368,455 GitHub stars — cementing its place as the fastest-growing open-source AI project."
---

**Openclaw** — the open-source personal AI assistant that has taken the developer world by storm — shipped **v2026.5.4** today, a blockbuster release packing a Google Meet voice bridge, a built-in file-transfer plugin, OpenRouter caching support, WhatsApp Newsletter messaging, and over 120 bug fixes and performance improvements.

The release arrives as Openclaw's GitHub repository crosses **368,455 stars** with **75,895 forks**, making it one of the most-starred open-source projects on the planet. The project, built by Peter Steinberger (now at OpenAI) and a massive community of contributors, has evolved from a simple Claude Code harness into a full-blown personal AI operating system.

## What's New in v2026.5.4

### Google Meet Voice Call Integration

The headline feature is the **Google Meet voice bridge**. Openclaw can now join Google Meet calls as an agent, using Twilio dial-in through a realtime Gemini voice bridge. The implementation features:

- **Paced audio streaming** with backpressure-aware buffering — prevents audio pile-up on slow connections
- **Barge-in queue clearing** — the agent can interrupt itself when the user speaks over it
- **No TwiML fallback** during realtime speech — snappier voice responses without XML redirect delays
- **Agent-mode talk-back** by default, with `mode: "bidi"` for direct realtime voice and `mode: "agent"` for STT → Openclaw agent → TTS pipeline
- **`realtime.introMessage: ""`** support for silent joins — the agent can enter a meeting without speaking

The Meet integration also includes automatic `BlackHole 2ch` audio routing for local Chrome realtime joins, coalescing of nearby speech transcript fragments, and echo suppression to prevent the agent from hearing its own output.

### Bundled File-Transfer Plugin

A new **file-transfer plugin** ships bundled with v2026.5.4, providing five agent-accessible tools:

- `file_fetch` — read binary files from paired nodes
- `dir_list` — list directory contents
- `dir_fetch` — fetch entire directory trees
- `file_write` — write binary files to paired nodes
- Default-deny per-node path policies requiring operator approval
- Symlink traversal refused by default (opt-in via `followSymlinks`)
- **16 MB byte ceiling** per round-trip — prevents runaway transfers

This is a significant expansion of Openclaw's agent capabilities, enabling file operations across machines in a multi-agent setup.

### OpenRouter Caching and Provider Updates

Openclaw now supports **OpenRouter's response caching** with opt-in headers for `X-OpenRouter-Cache`, `X-OpenRouter-Cache-TTL`, and cache-clear directives (only sent on verified OpenRouter routes). The provider also expands app-attribution categories to include coding, programming, writing, chat, and personal-agent usage.

**DeepSeek V4** users get support for `xhigh` and `max` thinking levels through the lightweight provider-policy surface, giving Control UI `/think` pickers access to the highest reasoning options.

### WhatsApp Newsletter Support

Openclaw now supports explicit WhatsApp **Channel/Newsletter** `@newsletter` outbound message targets with channel session metadata instead of DM routing. This opens up broadcast-style messaging for agent communications.

### Security Hardening

The release includes numerous security improvements:

- **Tree-sitter-backed shell command explainer** for future approval and command-review surfaces (#75004)
- **Windows security hardening**: `reg.exe`, `cmd.exe`, and `SystemRoot`/`WINDIR` resolution now goes through the canonical Windows install-root validator, preventing workspace `.env` overrides from redirecting system binaries to attacker-controlled locations (#74454, #74458, #77470, #77472)
- **Browser SSRF prevention**: tab-scoped debug routes (console, page errors, network requests, screenshots, storage) now enforce the current-tab URL navigation policy *before* collecting data, blocking exfiltration from unapproved tabs (#75731)
- **Managed proxy enforcement**: debug proxy direct upstream forwarding is disabled during managed proxy mode unless explicitly opted in (#74905)

### Performance at Scale

Several performance improvements target large multi-agent deployments:

- **Gateway startup optimization**: non-readiness sidecars are deferred until after the ready signal; hot-path channel plugin barrel imports are avoided; bundled plugin metadata uses a fast path
- **Session list pagination**: `sessions.list` RPC responses are bounded with truncation metadata, preventing Slack-heavy long-lived stores from forcing unbounded Gateway row construction
- **Plugin metadata snapshots**: unscoped model catalog and plugin metadata readers reuse the current workspace-compatible snapshot, avoiding repeated cold scans on hot control-plane paths
- **Tool-call loop detection**: a post-compaction guard aborts runs after detecting the same `(tool, args, result)` triple repeated within a configurable window (#77474)

## By the Numbers

Openclaw's growth metrics tell a story of explosive adoption:

| Metric | Value |
|--------|-------|
| GitHub Stars | **368,455** |
| Forks | 75,895 |
| Open Issues | 6,897 |
| Core Language | TypeScript |
| License | MIT |
| Repository | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) |

Since our last coverage on May 1 — when Openclaw had approximately 35,000 stars according to that article — the project has grown by **an order of magnitude** in roughly four days. The "awesome-openclaw-skills" collection has surpassed **47,949 stars** with over 5,400+ skills cataloged.

## The Ecosystem Expands

The Openclaw ecosystem now includes:

- **CC-Switch** (59,427 stars) — a cross-platform desktop all-in-one assistant tool for Claude Code, Codex, OpenCode, Openclaw, and Gemini CLI
- **Awesome Openclaw Skills** (47,949 stars) — 5,400+ curated skills from the official Openclaw Skills Registry
- **ClawHub** — the skills marketplace at clawhub.ai
- **50+ integrations** including Discord, Slack, Telegram, WhatsApp, Signal, iMessage, Gmail, GitHub, Spotify, Obsidian, Philips Hue, and Google Meet

## Community Sentiment

The reception on X and social media has been remarkable:

> *"Setup @openclaw yesterday. All I have to say is, wow. The fact that claw can just keep building upon itself just by talking to it in discord is crazy. The future is already here."* — @jonahships_

> *"After a few weeks in with it, this is the first time I have felt like I am living in the future since the launch of ChatGPT."* — @davemorin

> *"OpenClaw is the first 'software' in ages for which I constantly check for new releases on GitHub."* — @cnakazawa

> *"It's running my company."* — @therno

## The Bigger Picture

Openclaw v2026.5.4 arrives amid an intensifying landscape for AI agent tooling. The project's meteoric rise — from zero to 368K stars in roughly five months — signals a genuine shift in how developers and power users want to interact with AI. Rather than being locked into walled-garden subscriptions, the community is rallying around open-source, self-hostable, multi-provider agent infrastructure.

The Google Meet voice integration is particularly significant: it transforms Openclaw from a text-based assistant into a **voice-native agent** that can participate in meetings, take calls, and act on spoken instructions. Combined with the file-transfer plugin, cron job scheduling, multi-agent orchestration, and 50+ channel integrations, Openclaw is rapidly approaching the vision of a **true digital employee** — one that works 24/7 across every communication platform you use.

---

*Openclaw v2026.5.4 is available now via `npm install -g openclaw`. Full release notes on [GitHub](https://github.com/openclaw/openclaw/releases/tag/v2026.5.4).*
