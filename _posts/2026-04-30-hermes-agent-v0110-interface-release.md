---
title: "Hermes Agent v0.11.0 'Interface' — Ink TUI, AWS Bedrock, GPT-5.5, and 17 Platforms"
date: 2026-04-30 12:56:00 +0200
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, release, v0.11, TUI, AWS Bedrock, GPT-5.5, QQBot]
reading_time: 4
excerpt: "Nous Research ships Hermes Agent v0.11.0 with a full React/Ink TUI rewrite, native AWS Bedrock support, GPT-5.5 via Codex OAuth, five new inference paths, the 17th messaging platform (QQBot), and a dramatically expanded plugin surface."
---

Hermes Agent, the open-source AI runtime from **Nous Research** that's taken GitHub by storm (126K+ stars), has just shipped **v0.11.0 "Interface"** — its largest release yet. With 1,556 commits, 761 merged PRs, and contributions from 29 community members across two weeks of intense development, this release redefines how developers interact with and extend the agent.

## ✨ A Brand-New Terminal Experience

The headline feature is a complete rewrite of the interactive CLI using **React/Ink**, accessible via `hermes --tui` or `HERMES_TUI=1`. The new TUI (~310 commits) ships with:

- A **sticky composer** that stays put while scrolling through conversation history
- **Live streaming** with OSC-52 clipboard support for copy-across-SSH
- **Stable picker keys**, a **per-turn stopwatch** in the status bar, and a **git branch indicator**
- A **subagent spawn observability overlay** for monitoring parallel workstreams
- A light-theme preset and `/clear` confirm to prevent accidental session resets

The Python JSON-RPC backend (`tui_gateway`) means the TUI is fully extensible — expect community themes and plugins soon.

## 🏗️ Pluggable Transport Layer & AWS Bedrock

The release introduces a formal **Transport ABC** that extracts format conversion and HTTP transport from the monolithic `run_agent.py` into dedicated modules:

- **AnthropicTransport** — Anthropic Messages API
- **ChatCompletionsTransport** — OpenAI-compatible providers
- **ResponsesApiTransport** — OpenAI Responses API + Codex
- **BedrockTransport** — Native AWS Bedrock via the Converse API

This architectural shift makes adding new provider backends dramatically simpler and opens the door for community-contributed transports.

## 🧠 Five New Inference Paths

Hermes now connects to more models than ever with native support for:

- **NVIDIA NIM** — Run Nemotron and other NVIDIA-hosted models
- **Arcee AI** — Specialized domain models
- **Step Plan** — Structured planning models
- **Google Gemini CLI OAuth** — Authenticate and use Gemini directly
- **Vercel ai-gateway** — With pricing, attribution, and dynamic model discovery

Plus **GPT-5.5** is available over Codex OAuth with live model discovery — new OpenAI releases show up in the model picker without any catalog updates.

## 📱 QQBot — Platform #17

Hermes now runs on **17 messaging platforms**. The newest addition is **QQBot**, built on the QQ Official API v2 with QR scan-to-configure setup, streaming cursor, emoji reactions, and DM/group policy gating matching WeCom and Weixin parity.

Other platform highlights include Telegram proxy support, Discord forum channels, Feishu document comment intelligence, and WhatsApp voice message delivery.

## 🔌 Plugin Surface: From Extensible to Fully Hackable

The plugin system received a massive expansion. Plugins can now:

- **Register slash commands** (`register_command`)
- **Dispatch tools directly** (`dispatch_tool`)
- **Veto tool execution** via `pre_tool_call` hooks
- **Rewrite tool results** with `transform_tool_result`
- **Transform terminal output** (`transform_terminal_output`)
- **Ship custom image generation backends**
- **Add custom dashboard tabs**
- **Wire shell scripts as lifecycle hooks** — no Python required

A bundled **disk-cleanup plugin** serves as a reference implementation, opt-in by default.

## 🎛️ Other Notable Improvements

- **`/steer <prompt>`** — Inject mid-run guidance that the agent sees after its next tool call, without breaking the prompt cache
- **Webhook direct-delivery mode** — Zero-LLM push notifications for alerting and event streams
- **Smarter delegation** — Subagents now have an explicit `orchestrator` role with configurable spawn depth and filesystem coordination
- **Dashboard plugin system** — Third-party tabs, widgets, and live-switching themes for the web dashboard
- **i18n** — The dashboard supports English and Chinese with a language switcher
- **Auto-prune old sessions** + VACUUM at startup to keep `state.db` healthy

## 📈 By the Numbers

- **126,132 GitHub stars** and **18,854 forks**
- **1,556 commits** since v0.9.0
- **29 community contributors** (290 including co-authors)
- **224,174 lines changed** across 1,314 files

## Getting Started

Hermes Agent runs on any Linux machine, a $5 VPS, or serverless infrastructure. Install with:

```bash
pip install hermes-agent
hermes setup
```

Then run `hermes --tui` to experience the new interface, or `hermes model` to pick from 200+ models across OpenRouter, Nous Portal, NVIDIA NIM, AWS Bedrock, and more.

Check the [documentation](https://hermes-agent.nousresearch.com) and [GitHub repo](https://github.com/NousResearch/hermes-agent) for full details. The project is MIT-licensed and community contributions are welcome.
