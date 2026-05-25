---
layout: post
title: "Hermes Agent v0.14.0 'Foundation' Lands: Grok OAuth, OpenAI-Compatible Proxy, PyPI, Native Windows Beta, and 155K Stars"
date: 2026-05-18 10:00:00 +0200
last_modified_at: 2026-05-18 10:00:00 +0200
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, open-source, v0.14.0, foundation-release, grok-oauth, local-proxy, pypi, windows-beta, microsoft-teams]
reading_time: 8
hero_image: /assets/images/hero/hero-hermes-agent-v0140-foundation-release-may16.jpg
excerpt: "Hermes Agent v0.14.0 'Foundation' ships on May 16 with xAI Grok via SuperGrok OAuth (1M context window), an OpenAI-compatible local proxy for any OAuth provider, first-class X/Twitter search tool, end-to-end Microsoft Teams support, a debloating wave with PyPI packaging, native Windows beta, cross-session Claude prompt caching, LSP diagnostics, computer_use for non-Anthropic models, and 155K GitHub stars."
author: The Agent Report
---

Just 9 days after the massive Tenacity release, Nous Research has shipped **Hermes Agent v0.14.0 — the "Foundation Release"** — and the name is deserved. This isn't a single-feature release; it's a sweeping infrastructure reset that makes Hermes Agent ***installable, runnable, and connectable*** from almost anywhere.

The numbers alone are staggering: **808 commits, 633 merged PRs, 1,393 files changed, 165,061 insertions, 545 issues closed (12 P0, 50 P1), 215 community contributors** — all in 9 days since v0.13.0. The project now sits at **155,609 GitHub stars** (+17,000 since Tenacity), with **24,980 forks** and **11,989 open issues** reflecting a rapidly scaling community.

Here is the full breakdown of what the Foundation Release delivers.

---

## 🤖 xAI Grok via SuperGrok OAuth — With a 1M Context Window

The headliner. If you pay for SuperGrok, you can now use **xAI Grok inside Hermes Agent** by signing in with your xAI account — no API key, no separate billing. The integration goes through OAuth, so your subscription credentials are handled securely without exposing raw tokens.

But the real surprise: **Grok's context window jumps to 1M tokens** through this wire-through. That means you can drop entire codebases or research corpora into a single Grok prompt — a capability that puts Grok on par with Gemini 2.5 Pro for long-context use cases. ([#26534](https://github.com/NousResearch/hermes-agent/pull/26534), [#26664](https://github.com/NousResearch/hermes-agent/pull/26664), [#26644](https://github.com/NousResearch/hermes-agent/pull/26644))

> *"Proper handling for entitlement errors and an SSH-to-tunnel docs page for when you're SSH'd into a remote box and need to complete the OAuth flow."* — Release notes

For remote-server users, the OAuth flow also includes an **SSH tunneling guide** so you can authenticate from a headless machine through your local browser.

---

## 🏪 OpenAI-Compatible Local Proxy: One Subscription, Every Tool

**[PR #25969](https://github.com/NousResearch/hermes-agent/pull/25969)** introduces `hermes proxy` — a local HTTP server that speaks the OpenAI API format but is backed by whichever OAuth provider you're signed into. This is deceptively powerful:

| Subscription | Becomes available to | Without |
|-------------|---------------------|---------|
| Claude Pro | Codex CLI, Aider, Cline, Continue | An Anthropic API key |
| ChatGPT Pro | Any OpenAI-compatible tool | An OpenAI API key |
| SuperGrok | Any OpenAI-compatible tool | An xAI API key |

Run `hermes proxy`, get a `http://localhost:port` endpoint, and point any tool that expects an OpenAI-compatible API at it. **One subscription, every tool** — no additional API keys required. This effectively turns your Hermes Agent subscription into a universal API gateway for the entire agent tool ecosystem.

---

## 🐦 x_search: First-Class X (Twitter) Search

The agent can now search X/Twitter directly — no skill installation, no custom integration wiring. **[PR #26763](https://github.com/NousResearch/hermes-agent/pull/26763)** adds `x_search` as a built-in gated tool with two auth modes:

- **X OAuth login** — use your existing Twitter session
- **API key** — traditional bearer token auth

Search the timeline, find threads, surface specific posts — all from the chat interface. For journalists, researchers, and social media analysts running Hermes Agent as their primary interface, this eliminates an entire category of manual workflow.

---

## 🏢 Microsoft Teams: End-to-End

Hermes Agent now speaks **Microsoft Teams** natively. This isn't a partial integration — the full stack lands together:

1. **Microsoft Graph auth + client foundation** ([#21922](https://github.com/NousResearch/hermes-agent/pull/21922))
2. **Webhook listener** that receives Teams events ([#21969](https://github.com/NousResearch/hermes-agent/pull/21969))
3. **Pipeline plugin runtime** for processing Teams messages ([#22007](https://github.com/NousResearch/hermes-agent/pull/22007))
4. **Outbound delivery** to post back ([#22024](https://github.com/NousResearch/hermes-agent/pull/22024))

Wire up the bot once, then chat to your agent from any Teams channel, DM, or group. This is a massive step for enterprise adoption — Microsoft Teams is the corporate standard, and now Hermes Agent sits inside it as a first-class citizen.

---

## 📦 PyPI Packaging: `pip install hermes-agent && hermes`

One of the most requested features has landed: **Hermes Agent is now a real PyPI package**. No more cloning the repo or running shell installers. One `pip install hermes-agent` command and you're running. The wheel ships with the Ink TUI bundle and shell launcher, so the full interactive experience comes out of the box. ([#26593](https://github.com/NousResearch/hermes-agent/pull/26593))

This is paired with a comprehensive **debloating wave** ([#24220](https://github.com/NousResearch/hermes-agent/pull/24220), [#24515](https://github.com/NousResearch/hermes-agent/pull/24515)):

- Heavy backends (Slack/Matrix/Feishu SDKs, image-gen, voice/TTS providers) now **lazy-install on first use**
- The `[all]` extras drop everything covered by lazy-deps
- **Tiered install fallback** when a wheel doesn't fit your platform
- **Supply-chain advisory checker** scans every install for unsafe versions

The net effect: faster installs, a smaller disk footprint, fewer transitive vulnerabilities, and a dramatically lower barrier to entry.

---

## ⚡ Performance: Cache, Cold Start, and Browser

### Cross-Session 1-Hour Claude Prompt Cache

**[PR #23828](https://github.com/NousResearch/hermes-agent/pull/23828)** brings cross-session prompt caching to Claude (via Anthropic, OpenRouter, or Nous Portal). The prompt prefix (system prompt, skills, memory) now caches for **one full hour across sessions**. Start a `/new` session and the first response comes back faster and cheaper because the cache is still warm. Background memory review hits the cache too — no full-price turns. ([#25434](https://github.com/NousResearch/hermes-agent/pull/25434))

### Cold-Start Wave: ~19 Seconds Off `hermes` Launch

A coordinated performance pass across the launch path:

| Optimization | Improvement |
|-------------|-------------|
| Heavy adapters deferred to first use | Major import-time reduction |
| Model catalogs from disk cache first | Eliminates network wait |
| Doctor checks run in parallel | Concurrent connectivity probes |
| `chat -q` skips welcome banner | Instant prompt |
| `hermes tools` All-Platforms screen | **14s → under 1.5s** |

### 180× Faster Browser Console Evaluations

**[PR #23226](https://github.com/NousResearch/hermes-agent/pull/23226)** routes browser console evaluations through the supervisor's persistent CDP WebSocket instead of spinning up a new DevTools session per call. Things that used to take seconds now return in milliseconds — real-world page interactions feel instantaneous.

---

## 💬 Two New Platforms: LINE + SimpleX Chat

Hermes Agent adds **two more messaging platforms**, bringing the total to **22**:

- **LINE** ([#23197](https://github.com/NousResearch/hermes-agent/pull/23197)) — huge in Japan, Korea, and Taiwan. Native integration with the LINE Messaging API.
- **SimpleX Chat** ([#26232](https://github.com/NousResearch/hermes-agent/pull/26232)) — the privacy-focused decentralized messenger with no user IDs, no servers, no directory.

Both are full first-class platforms with inbound + outbound messaging.

---

## 🪟 Native Windows Beta

**[PR #21561](https://github.com/NousResearch/hermes-agent/pull/21561)** brings Hermes Agent to **native Windows** — running on `cmd.exe` and PowerShell **without WSL**. A full PowerShell installer handles MinGit auto-install, Microsoft Store Python stub detection, and Ctrl+C handling. There are still rough edges (this is early beta), but the basic loop works end-to-end on a clean Windows box.

---

## 🧠 Smarter Agent: LSP Diagnostics, Handoff, and File Verification

Three improvements that make the agent dramatically more reliable:

| Feature | What it does | PR |
|---------|-------------|-----|
| **LSP Semantic Diagnostics** | After every `write_file`/`patch`, runs a real language server against the file and surfaces errors (type errors, undefined symbols, missing imports) | [#24168](https://github.com/NousResearch/hermes-agent/pull/24168) |
| **`/handoff` Live Session Transfer** | Moves the active session — every message, tool call, and context — to a different model/persona/profile mid-conversation | [#23395](https://github.com/NousResearch/hermes-agent/pull/23395) |
| **Per-Turn File-Mutation Verifier** | After every turn that wrote/edited files, a footer summarizes exactly what changed on disk — paths, line counts, deltas | [#24498](https://github.com/NousResearch/hermes-agent/pull/24498) |

The LSP diagnostics are a particularly consequential improvement. v0.13.0 had basic Python/JSON/YAML/TOML linting; v0.14.0 upgrades to **actual semantic analysis** — the same kind of error detection your IDE gives you, now inside the agent's loop.

---

## 🖥️ Computer Use for Non-Anthropic Models

The `computer_use` tool (agent-controlled mouse + keyboard for GUI apps) used to be locked to Anthropic's SDK. The new **cua-driver backend** ([#21967](https://github.com/NousResearch/hermes-agent/pull/21967)) works with non-Anthropic providers too, with proper focus-safe operations and auto-refresh on `hermes update`. Now any vision-capable model can drive your desktop.

---

## 🎥 New Capabilities: Video Generation, Vision Pixels, and Web Search

A trio of new capabilities rounds out the Foundation Release:

- **`video_generate` with pluggable backends** ([#25126](https://github.com/NousResearch/hermes-agent/pull/25126)) — one tool, any video model, with plugin architecture for future providers
- **`vision_analyze` returns raw pixels** ([#22955](https://github.com/NousResearch/hermes-agent/pull/22955)) — vision-capable models (GPT-5, Claude, Gemini, Grok-vision) now get actual pixels instead of text-summary round-trips
- **Brave Search (free tier) + DuckDuckGo** ([#21337](https://github.com/NousResearch/hermes-agent/pull/21337)) — two new free web-search backends join Tavily, SearXNG, and Exa

---

## 🔒 Security: Sudo Brute-Force Block, Tool Error Sanitization, and More

Three significant security improvements:

1. **Sudo brute-force block** — the approval gate now blocks `sudo -S` brute-force attempts and classifies stdin-fed/askpass-stripped sudo invocations as DANGEROUS ([#23736](https://github.com/NousResearch/hermes-agent/pull/23736))
2. **Three dangerous-command bypasses closed** — inspired by Claude Code's command-detection work ([#26829](https://github.com/NousResearch/hermes-agent/pull/26829))
3. **Tool error sanitization** — error strings are sanitized before being re-injected into the model context, preventing malicious files or remote services from passing instructions through error output ([#26823](https://github.com/NousResearch/hermes-agent/pull/26823))

---

## 📊 Growth Summary (May 7 → May 18)

| Metric | May 7 (v0.13.0) | May 18 (v0.14.0) | Change |
|--------|-----------------|------------------|--------|
| **GitHub Stars** | ~138,000 | **155,609** | **+17,609** |
| **Forks** | ~22,000 | **24,980** | **+2,980** |
| **Issues Closed** | — | **545** (12 P0, 50 P1) | — |
| **Merged PRs** | — | **633** | — |
| **Contributors** | — | **215** | — |
| **Messaging Platforms** | 19 | **22** | +3 |
| **Inference Providers** | ~20 | **~25** | +NovitaAI, Grok OAuth |

---

## 🔭 What's Next

The Foundation Release name is apt: v0.14.0 builds the infrastructure that the next wave of features will sit on top of. With PyPI packaging, a local OpenAI-compatible proxy, native Windows support, and 22 messaging platforms, Hermes Agent has **the broadest surface area of any open-source agent runtime**.

Areas to watch for v0.15.0:

1. **Frontdesk runtime** — the always-available background worker architecture (still in PR)
2. **Kanban maturity** — suspend/resume primitives for long-running task lifecycle
3. **Cron expansion** — per-job reasoning, name-based lookup, conditional gates
4. **More providers** — the NovitaAI addition suggests growing the long-tail of provider support
5. **160K stars** — at current growth (~1,700/day), this milestone falls within days

For developers building agentic systems: the Foundation Release is the release you've been waiting for to integrate Hermes Agent into your stack — it installs cleanly, connects everywhere, and runs on every major operating system.

---

*Coverage based on the Hermes Agent v0.14.0 (v2026.5.16) release. Star counts as of 2026-05-18 09:00 UTC. Full changelog: [v2026.5.7...v2026.5.16](https://github.com/NousResearch/hermes-agent/compare/v2026.5.7...v2026.5.16)*
