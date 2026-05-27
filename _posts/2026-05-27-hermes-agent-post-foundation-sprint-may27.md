---
layout: post
title: "Hermes Agent Post-Foundation Sprint: Dashboard OAuth, Kynver Memory, Qwen 3.7-Max, and 30+ Merged PRs"
date: 2026-05-27 14:00:00 +0200
last_modified_at: 2026-05-27 14:00:00 +0200
meta_description: "In the 11 days since v0.14.0 Foundation, the Hermes Agent team has merged over 30 PRs — shipping Dashboard OAuth login, a Kynver memory provider bridge, Qwen 3.7-Max support, API server session controls, security plugins with pattern-matched code warnings, and major Codex reliability fixes."
categories: [hermes-agent]
tags: [hermes-agent, nous-research, open-source, dashboard-oauth, kynver-memory, qwen-37-max, api-server, security-plugins, codex-reliability]
reading_time: 6
hero_image: /assets/images/hero/hero-hermes-agent-post-foundation-sprint-may27.jpg
excerpt: "Eleven days after v0.14.0 'Foundation', Hermes Agent's development hasn't slowed down: Dashboard OAuth login shipped, a Kynver memory provider brings AgentOS bridge, Qwen 3.7-Max lands in model catalogs, the API server gets session controls, and a new security-plugins system delivers pattern-matched code warnings. Plus a cluster of Codex reliability fixes and Telegram UX improvements — all merged on May 27."
author: The Agent Report
---

<style>
.highlight-box { background: #1a1a2e; border-left: 4px solid #6c5ce7; padding: 1.2rem 1.5rem; margin: 1.5rem 0; border-radius: 0 8px 8px 0; }
.highlight-box p { margin: 0; }
.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.stat-card { background: #1a1a2e; border-radius: 8px; padding: 1rem; text-align: center; border: 1px solid #2a2a3e; }
.stat-card .stat-value { font-size: 1.8rem; font-weight: bold; color: #6c5ce7; }
.stat-card .stat-label { font-size: 0.85rem; color: #888; margin-top: 0.3rem; }
</style>

Just 11 days after the massive [v0.14.0 "Foundation" release]({% post_url 2026-05-18-hermes-agent-v0140-foundation-release-may16 %}), the Hermes Agent team is showing no signs of slowing down. Today, May 27, saw a coordinated batch of **30+ merged pull requests** ship across the entire stack — from infrastructure and auth to new model support and security tooling.

The numbers tell the story: the repo has climbed from **155K to 169.5K stars** (+14,500 in 11 days), while **forks have surged from 24,980 to 28,216**, and **open issues have grown to 14,219** — reflecting a community that's not just watching but building.

<div class="stat-grid">
<div class="stat-card"><div class="stat-value">169.5K</div><div class="stat-label">GitHub Stars</div></div>
<div class="stat-card"><div class="stat-value">28.2K</div><div class="stat-label">Forks</div></div>
<div class="stat-card"><div class="stat-value">14.2K</div><div class="stat-label">Open Issues</div></div>
<div class="stat-card"><div class="stat-value">30+</div><div class="stat-label">PRs Merged Today</div></div>
</div>

Here's what landed in today's sprint.

---

## 🏠 Dashboard OAuth Login (#30156)

The most user-facing change in today's batch is the **Dashboard OAuth login flow**. Previously, dashboard users had to configure their provider credentials manually through config files. Now the dashboard supports a full OAuth login flow — operators can log in through their identity provider directly from the dashboard UI.

The implementation is backed by the new `dashboard.public_url` config option ([commit by @benbarclay](https://github.com/NousResearch/hermes-agent/commit/a890389b69575916dfaf3980556f31f7f25c9871)), which allows operators behind reverse proxies to set the absolute base URL for OAuth callbacks. This fixes a common pain point for self-hosted deployments behind nginx, on-prem ingress controllers, and custom-domain Fly.io setups where `X-Forwarded-Host` headers aren't reliably forwarded.

> "When set, it is the complete authority — scheme + host + optional path prefix — and becomes the base for the OAuth `redirect_uri`."
> — Commit message on `HERMES_DASHBOARD_PUBLIC_URL`

The config follows a clean precedence chain: **env var > `config.yaml` > auto-detected from request headers**, matching the existing `dashboard.oauth.client_id` pattern.

---

## 🧠 Kynver Memory Provider + AgentOS Bridge (#33158)

Memory is one of the most critical subsystems in any self-improving agent, and today Hermes gained a new backend. PR [#33158](https://github.com/NousResearch/hermes-agent/pull/33158) adds the **Kynver memory provider** alongside an **AgentOS bridge**.

Kynver is a specialized memory substrate for AI agents, offering persistent, queryable storage optimized for agentic workloads. The AgentOS bridge means Hermes can now leverage AgentOS-compatible memory tools and infrastructure. This is a significant expansion of Hermes' already rich memory ecosystem, which previously depended on filesystem-based, vector-store, and other backends.

---

## 🤖 Qwen 3.7-Max Joins the Model Catalog (#32806, #33129)

Two PRs today add **Qwen 3.7-Max** — Alibaba's latest frontier model — to Hermes' model catalogs. PR [#32806](https://github.com/NousResearch/hermes-agent/pull/32806) adds it to the Alibaba provider list, while [#33129](https://github.com/NousResearch/hermes-agent/pull/33129) adds it to the `alibaba-coding-plan` catalog.

Qwen 3.7-Max has been making waves in the open-source AI community for its strong reasoning capabilities and competitive benchmark scores. Hermes users on the Alibaba provider can now select it via `hermes model` and start building agents with it immediately.

---

## 🔌 API Server Session Controls (#33134, #29302)

The API server — Hermes' HTTP interface for programmatic access — gets a major upgrade with **session control APIs**. PR [#33134](https://github.com/NousResearch/hermes-agent/pull/33134) (salvaging [#29302](https://github.com/NousResearch/hermes-agent/pull/29302)) introduces endpoints for:
- **Session management** — create, list, and manage active sessions
- **Chat endpoints** — send messages, retrieve conversation history
- **Fork support** — branch a session into a new independent context
- **SSE streaming** — real-time event streaming for live agent responses

This transforms the API server from a basic HTTP interface into a full-featured agent interaction platform — enabling custom UIs, CI/CD integrations, and programmatic agent orchestration.

---

## 🛡️ Security Plugins: Pattern-Matched Code Warnings (#33131)

A new plugin category lands today: **security-guidance plugins**. PR [#33131](https://github.com/NousResearch/hermes-agent/pull/33131) introduces a system that pattern-matches against dangerous code patterns in agent-written code and surfaces warnings _before_ the code is executed.

This is especially important for self-improving agents that write and execute their own code — Hermes' core value proposition. The security-guidance plugin catches common dangerous patterns (unsafe `eval()`, file-system traversal, shell injection vectors) and flags them with actionable remediation hints.

---

## 🛠️ Codex Reliability Cluster

A significant portion of today's merged PRs focus on **Codex (GitHub Copilot) provider reliability** — the workhorse backend for many Hermes users:

- **Credential pool sync on re-auth** ([#33074](https://github.com/NousResearch/hermes-agent/pull/33074)) — fixes a bug where Codex re-authentication via `hermes setup` / `hermes model` would write fresh OAuth tokens but leave the credential pool holding stale entries, causing 401 errors on every subsequent request
- **Foreign-issuer reasoning on replay** ([#33156](https://github.com/NousResearch/hermes-agent/pull/33156), salvaging [#31629](https://github.com/NousResearch/hermes-agent/pull/31629)) — prevents `HTTP 400 invalid_encrypted_content` errors when switching between model providers mid-conversation (e.g., from Grok to GPT-5.5)
- **Transient rs_tmp reasoning state** ([#33146](https://github.com/NousResearch/hermes-agent/pull/33146)) — drops stale temporary reasoning items that could accumulate and cause failures
- **Null output stream handling** ([#33008](https://github.com/NousResearch/hermes-agent/pull/33008), [#33050](https://github.com/NousResearch/hermes-agent/pull/33050)) — normalizes `response.output=None` to empty lists, preventing iteration crashes
- **Silent-hang workaround hints** ([#33133](https://github.com/NousResearch/hermes-agent/pull/33133), [#33034](https://github.com/NousResearch/hermes-agent/pull/33034)) — improved user-facing hints when ChatGPT silent-hang scenarios are detected
- **Homebrew CI poller nudges** ([#33142](https://github.com/NousResearch/hermes-agent/pull/33142)) — the terminal tool now detects anti-pattern CI polling scripts and nudges users toward canonical green-CI snippets

---

## 💬 Telegram UX Cleanup

A cluster of three PRs addresses Telegram operational noise:
- [#31034](https://github.com/NousResearch/hermes-agent/pull/31034) — quiets operational chatter in Telegram gateway
- [#31098](https://github.com/NousResearch/hermes-agent/pull/31098) — ignores `/start` platform pings on Telegram
- [#31941](https://github.com/NousResearch/hermes-agent/pull/31941) — hides compaction status noise

These are small but important UX improvements — reducing noise in Telegram channels where Hermes operates as a bot makes the conversation feel more natural and less "robotic."

---

## 📊 What This Sprint Means

Eleven days after the Foundation release, Hermes Agent's development velocity is accelerating:

1. **The dashboard is becoming a real product** — OAuth login and session control APIs point to Hermes evolving beyond a CLI-only tool into a platform with proper web UI and API access layers
2. **Memory diversity is growing** — the Kynver + AgentOS bridge means Hermes can plug into more enterprise and research-grade memory substrates
3. **Security is front-and-center** — pattern-matched security plugins for code writing is a direct response to the unique risks of self-improving agents
4. **Daily reliability compounding** — the Codex cluster alone fixes 7+ distinct failure modes that real users were hitting

The pace is remarkable: 30+ PRs merged in a single day, spanning infrastructure (auth, config, API), models (Qwen 3.7-Max), memory systems, security, and reliability. If the Foundation release was about _surface area_, this sprint is about _depth_ — making every subsystem more reliable, more secure, and more capable.

With **169.5K stars and counting**, Hermes Agent continues to be the fastest-growing open-source agent framework — and if today's sprint is any indication, the next release (v0.15.0?) will be worth the wait.
