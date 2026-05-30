---
layout: post
title: "Hermes Agent v0.15.0 'Velocity' + v0.15.1 Hotfix: run_agent.py -76%, Kanban as a Platform, and 172K Stars"
date: 2026-05-29 18:00:00 +0200
last_modified_at: 2026-05-29 18:00:00 +0200
meta_description: "Hermes Agent v0.15.0 'Velocity Release' ships the biggest refactor ever (run_agent.py 16K→3.8K lines), Kanban as a multi-agent platform, 4,500× faster session_search, promptware defense, Bitwarden Secrets Manager, and a same-day v0.15.1 hotfix."
description: "Hermes Agent v0.15.0 'Velocity Release' ships the biggest refactor ever (run_agent.py 16K→3.8K lines), Kanban as a multi-agent platform, 4,500× faster"
categories: [hermes-agent]
tags: [hermes-agent, nous-research, open-source, v0.15.0, velocity-release, run-agent-refactor, kanban-platform, session-search, promptware-defense, bitwarden-secrets]
reading_time: 8
hero_image: /assets/images/hero/hero-hermes-agent-v0150-velocity-release-may28.jpg
excerpt: "Hermes Agent v0.15.0 'The Velocity Release' arrives on May 28 with the biggest internal refactor in project history — run_agent.py collapses from 16,083 to 3,821 lines (-76%) across 14 cohesive modules. Kanban graduates to a full multi-agent platform spanning 104 PRs. session_search becomes 4,500× faster and free. Promptware defense lands against Brainworm-class attacks, Bitwarden Secrets Manager replaces N per-provider API keys with one bootstrap token, and the Ink TUI gains a multi-session orchestrator. A same-day v0.15.1 hotfix on May 29 patches the dashboard infinite-reload loop. The project crosses 172K GitHub stars."
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

Just **11 days** after the [Foundation Release]({% post_url 2026-05-18-hermes-agent-v0140-foundation-release-may16 %}), Nous Research has shipped **Hermes Agent v0.15.0 — "The Velocity Release"** — and followed it with a same-day **v0.15.1 hotfix** on May 29. If Foundation was about breadth (install anywhere, connect to anything), Velocity is about depth — making everything dramatically faster, smaller, and smarter.

The stats are staggering:

<div class="stat-grid">
<div class="stat-card"><div class="stat-value">1,302</div><div class="stat-label">Commits</div></div>
<div class="stat-card"><div class="stat-value">747</div><div class="stat-label">Merged PRs</div></div>
<div class="stat-card"><div class="stat-value">321</div><div class="stat-label">Contributors</div></div>
<div class="stat-card"><div class="stat-value">560+</div><div class="stat-label">Issues Closed</div></div>
<div class="stat-card"><div class="stat-value">172K</div><div class="stat-label">GitHub Stars</div></div>
<div class="stat-card"><div class="stat-value">28.9K</div><div class="stat-label">Forks</div></div>
</div>

> *"The Velocity Release — Hermes gets dramatically faster — to start, to run, to ship work, and to grow."* — Teknium1, release notes

Here is the full breakdown of what lands in v0.15.0 and v0.15.1.

---

## 🔧 The Big Refactor: `run_agent.py` Goes from 16K to 3.8K Lines

The headline engineering story of v0.15.0 is the surgical dismantling of the monolithic `run_agent.py` — the file at the heart of Hermes' agent conversation loop. It has been reduced from **16,083 lines to 3,821 lines (-76%)**, with the extracted logic redistributed across **14 cohesive modules** under `agent/`.

Every extraction keeps a thin forwarder for backward compatibility, so behavior is unchanged — but the codebase is now dramatically easier to navigate, test, and contribute to. This is the kind of infrastructure debt payment that pays compounding interest for every future release.

> *A 16,000-line file is a research prototype. A 3,800-line module tree is a production platform.*

## 🧩 Kanban: From Feature to Multi-Agent Platform

The Kanban system — first introduced in v0.13.0 "Tenacity" — has matured from a task board into a full **multi-agent orchestration platform** across **104 merged pull requests**. New capabilities include:

- **Orchestrator auto-decomposition** — the Kanban master breaks complex goals into sub-tasks automatically
- **Swarm topology** — workers self-organize into dependency-aware execution graphs
- **Scheduled tasks** — cron-integrated board slots that fire on a timer
- **Worktree-per-task** — each task gets an isolated working directory to prevent cross-contamination
- **Per-task model overrides** — assign different LLMs to different board slots

This positions Kanban as a genuine rival to dedicated multi-agent frameworks like AutoGen and CrewAI — but running inside a single `hermes` install with zero extra infrastructure.

## ⚡ Cold-Start Performance: Another Second Shaved Off

The cold-start performance wave that began in Foundation continues. v0.15.0 delivers:

- **~1 more second off `hermes` launch** — boot-to-prompt is now dramatically faster
- **47% fewer per-conversation function calls** — the agent spends less time on boilerplate, more time doing work
- **`hermes --version` benchmark win** — Hermes Agent now beats Codex CLI head-to-head in cold-start benchmarks

For an agent runtime that users invoke dozens of times per day, every second compounds into real productivity.

## 🔍 `session_search`: 4,500× Faster and Free

The `session_search` skill — which lets Hermes search across all your past conversations — has been rebuilt. The result: **4,500× faster lookups** at zero additional cost. No vector database, no external API, no embedding service required. This is pure algorithmic optimization on the local conversation store.

## 🛡️ Promptware Defense: Protection Against Brainworm-Class Attacks

v0.15.0 ships **promptware defense** — a security layer specifically designed to detect and neutralize **Brainworm-class prompt injection attacks**. In an era where agents reading untrusted web content is table stakes, this is a critical addition. The defense layer:

- Scans incoming content for known injection patterns
- Sandboxes suspicious content before it reaches the agent loop
- Reports attempted attacks without disrupting legitimate work

## 🔐 Bitwarden Secrets Manager: One Token to Rule Them All

One of the most practical quality-of-life improvements: **Bitwarden Secrets Manager** integration. Instead of managing N different API keys for N different providers (Claude, Grok, OpenAI, etc.), you now configure a **single Bitwarden bootstrap token**, and Hermes retrieves the rest automatically at runtime. This is a massive win for:

- **Security** — fewer tokens in plaintext config files
- **Portability** — move your Hermes install without migrating keys
- **Team deployments** — share secrets via Bitwarden without sharing files

## 🎨 Ink TUI: Multi-Session Orchestrator

The terminal user interface gets its own **multi-session orchestrator**, letting you manage multiple Hermes sessions from a single TUI dashboard. Switch between conversations, inspect Kanban boards, and monitor background tasks — all without leaving the terminal.

## 📦 Skill Bundles: One Slash Command, One Workflow

A new **skill bundle** system lets you group multiple skills behind a single slash command. Instead of loading skills one at a time, you define a bundle — `@deploy` could load `k8s-skills`, `docker-skills`, `monitoring-skills`, and `rollback-skills` in one shot.

## 🌐 Platform Expansion

v0.15.0 extends Hermes' already impressive platform reach:

- **ntfy** becomes the **23rd messaging platform** — push notifications to any device via ntfy.sh
- **Two new `image_gen` providers**: Krea 2 (Medium + Large) and a FAL plugin port
- **Nous-approved MCP catalog** with an interactive picker — discover and install MCP servers from within Hermes
- **OpenHands orchestration skill** — run OpenHands workflows as Hermes skills
- **Deep xAI integration round** — Web Search plugin via Grok, `xai-oauth` proxy upstream, retired-May-15 model detection with `hermes migrate xai`, natural TTS speech-tag pauses, `base_url` leak guard, and OpenAI-style execution guidance for Grok

## 🪲 v0.15.1 Hotfix (May 29) — The Dashboard Infinite-Reload Fix

Released just hours after v0.15.0, **v0.15.1** is a same-day **hotfix release** with **28 commits, 21 merged PRs, and 9 contributors**. The headline fix:

- **Dashboard 401 reload loop fixed** — In loopback mode (Docker, hosted Hermes, fresh installs), the dashboard's identity probe (`/api/auth/me`) returns 401 by design, but v0.15.0's stale-token reload guard treated every 401 as a rotated session and full-page-reloaded. This caused an infinite loop — captured in issues [#34206](https://github.com/NousResearch/hermes-agent/issues/34206) and [#34202](https://github.com/NousResearch/hermes-agent/issues/34202), fixed in PR [#30698](https://github.com/NousResearch/hermes-agent/pull/30698) by @austinpickett.

Additional fixes in v0.15.1:

- **Docker `--insecure` as explicit env opt-in** — no longer derived from bind host
- Kanban worker SIGTERM handling improved
- `/model` picker unification across UI and CLI
- `/yolo` session bypass for power users
- Full **19,932-entry skills.sh catalog** now loads correctly
- `.md` media delivery restoration in conversations
- Gateway **probe-stepdown safety** — graceful degradation on upstream failure
- **Web-URL redaction passthrough** fixed for private browsing mode
- Kanban worker **vision on referenced images** — workers can now see attached images
- Hindsight observation set as default behavioral mode
- MCP server **bare-command PATH resolution** on systems with custom PATHs
- **arm64 PR-build cache fixes** for Apple Silicon and ARM Linux contributors

## 📊 The Growth Trajectory

<div class="highlight-box">
<p><strong>172,224 GitHub Stars · 28,932 Forks · 14,855 Open Issues</strong></p>
<p>Since the Foundation release (May 16): +17K stars (+11%) in 13 days. The project is now the #1 most-starred AI agent runtime on GitHub by a wide margin, and the velocity of contributions shows no signs of slowing.</p>
</div>

## The Bottom Line

Hermes Agent v0.15.0 "Velocity" is not a feature release — it's a **foundational investment in speed and maintainability**. The `run_agent.py` refactor alone will pay dividends for every release that follows. The Kanban platform maturation, session_search rewrite, promptware defense layer, and Bitwarden integration together create a runtime that's faster, safer, and more practical for daily production use.

The same-day v0.15.1 hotfix demonstrates the project's operational maturity — shipping a critical bug fix within hours of a major release, with clear communication and detailed changelogs. That's the hallmark of a project that treats its users seriously.

With **172K stars**, **28.9K forks**, and a **321-contributor release cycle**, Hermes Agent is not just the fastest-growing open-source agent runtime — it's becoming the default choice for developers who want an agent that ships real work, at real speed.

*Stay tuned for our next deep dive — the Velocity release has already generated over 200 new open issues, and the community sprint shows no signs of stopping.*
