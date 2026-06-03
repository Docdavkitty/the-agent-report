---
layout: post
title: "Hermes Desktop Launches in Public Preview — Native Cross-Platform App Arrives Alongside NVIDIA + Microsoft Computex Partnership"
date: 2026-06-03 10:00:00 +0200
last_modified_at: 2026-06-03 10:00:00 +0200
meta_description: "Hermes Desktop, the native macOS/Windows/Linux app for Hermes Agent, launches in public preview — days after Nous Research announced NVIDIA RTX Spark, OpenShell runtime, and Microsoft security primitives integration at Computex 2026."
description: "Hermes Desktop, the native macOS/Windows/Linux app for Hermes Agent, launches in public preview — days after Nous Research announced NVIDIA RTX Spark, OpenShell runtime, and Microsoft security primitives integration at Computex 2026."
categories: [hermes-agent]
tags: [hermes-agent, nous-research, open-source, hermes-desktop, desktop-app, computex-2026, nvidia-rtx-spark, openshell, microsoft-security]
reading_time: 7
hero_image: /assets/images/hero/hero-hermes-desktop-native-app-computex-2026.jpg
excerpt: "Hermes Desktop — the native GUI app for macOS, Windows, and Linux — is now in public preview. Announced alongside NVIDIA's Computex 2026 keynote, the app wraps the v0.15.2 Hermes Agent runtime in an Electron shell with chat UI, file browser, voice mode, and full settings management. First demoed in Jensen Huang's GTC keynote, it's now available via `hermes desktop` or a one-line `--include-desktop` installer."
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

The pace of Hermes Agent development has reached a new inflection point. On **June 2, 2026**, Nous Research announced **Hermes Desktop** — the open-source agent's first **native GUI application** — now in public preview for macOS 12+, Windows 10/11, and Linux. The launch comes just **one day** after the company revealed its deepening partnership with **NVIDIA and Microsoft** at Computex 2026, positioning Hermes Agent as a first-class citizen on the new **NVIDIA RTX Spark superchip** with **OpenShell runtime** and **Windows security primitives**.

> *"The next evolution of Hermes Agent is here! Introducing Hermes Desktop: everything you love about Hermes, now native on your machine. First demoed in Jensen's GTC keynote, it's now in public preview."* — Nous Research, June 2, 2026

Here's everything you need to know.

---

## 🖥️ What Is Hermes Desktop?

Hermes Desktop is not a separate product — it's a **native Electron wrapper** around the same Hermes Agent runtime you get from the CLI and gateway. As the [official documentation](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) states:

> *"It is not a separate product or a lightweight clone; it installs the standard Hermes Agent runtime into the standard `~/.hermes` layout and drives it through a real UI."*

This means your config, API keys, sessions, skills, and memory are **fully shared** across CLI, TUI, web dashboard, and the new Desktop app. Start a conversation in one, resume it in another.

### Key Features

| Feature | Description |
|---------|-------------|
| **Chat Interface** | Full text-based conversation with the agent, with message history and streaming |
| **File Browser** | Explore and preview the working directory without leaving the app |
| **Voice Mode** | Talk to Hermes and hear responses (macOS microphone integration) |
| **Settings & Onboarding** | Manage providers, models, tools, and credentials via UI — no YAML editing |
| **Management Panes** | Mirror `hermes` subcommands: providers, model selection, MCP servers, gateway config, session management |
| **Auto-Updates** | One-click updates when a new version is available |

### Supported Platforms

- **macOS:** 12+ (signed + notarized `.dmg`)
- **Windows:** 10/11 (`.exe` NSIS installer or `.msi`)
- **Linux:** `.AppImage`, `.deb`, `.rpm`

The Windows installer is particularly notable — it bundles Python via `uv`, a portable Git, and ripgrep in a single `.exe` that requires **no admin rights or system-wide changes**. First launch calls `install.ps1` under the hood, provisioning everything into `%LOCALAPPDATA%\hermes`.

---

## 🚀 Installation: Two Ways

### Way 1: Fresh Install with Desktop Support

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --include-desktop
```

This provisions the agent runtime and builds the desktop app in a single pass.

### Way 2: Add Desktop to an Existing Hermes Install

If you already have Hermes Agent installed, just run:

```bash
hermes desktop
```

The command installs workspace Node dependencies, builds the unpacked Electron app, and launches it — all using your existing config, keys, sessions, and skills.

---

## 🔬 Under the Hood: How It Works

The packaged desktop app ships only the **Electron shell**. On first launch, it installs the Hermes Agent runtime into `HERMES_HOME` (`~/.hermes` on macOS/Linux, `%LOCALAPPDATA%\hermes` on Windows) — **the exact same layout a CLI install uses**.

The React renderer communicates with a `hermes dashboard --tui` backend over standard gateway APIs. This means the app is essentially a polished front-end to the same battle-tested agent loop that powers the CLI, web dashboard, and gateway.

For developers who want to build from source:

```bash
cd apps/desktop
npm run dev          # Vite renderer + Electron, boots Python backend
```

Additional flags include `--skip-build` (launch existing build), `--cwd PATH` (set initial project directory), and `--fake-boot` (test startup UI with deterministic delays).

---

## 🏢 The Computex 2026 Announcement: NVIDIA RTX Spark + OpenShell + Microsoft

Just one day before the Desktop launch, Nous Research made waves at **Computex 2026** in Taipei. On June 1, the team tweeted:

> *"We have been working closely with @nvidia to ensure Hermes Agent works smoothly on their new @NVIDIARTXSpark superchip and integrates with the new OpenShell runtime, which connects Hermes to @Microsoft's security primitives."*

This is a **triple-layered partnership**:

### 1. NVIDIA RTX Spark Superchip

NVIDIA's new **RTX Spark** — an ARM-based system-on-chip combining a Blackwell RTX GPU with a 20-core Grace CPU — was officially unveiled at Computex. Built in collaboration with MediaTek, the Spark is designed for AI workloads on compact PCs and laptops. Partners including ASUS, Dell, HP, Lenovo, and MSI plan to ship Spark-powered devices in fall 2026.

NVIDIA's blog post explicitly calls out Hermes Agent:

> *"RTX Spark and NVIDIA OpenShell give Hermes users a powerful and secure environment for agents to run and work alongside you."*

### 2. OpenShell Runtime

**OpenShell** is NVIDIA's new runtime environment for local AI agents, developed in partnership with Microsoft. It allows users to define what agents can and cannot access, route queries to local models based on privacy preferences, and obscure personal data in any queries sent to cloud services. This is a critical piece of infrastructure for making local agent runtimes production-ready.

### 3. Microsoft Windows Security Primitives

The OpenShell runtime connects Hermes Agent to **Microsoft's new Windows security primitives** — operating system-level controls governing identity verification, process containment, and policy enforcement for agent applications. This brings hardware-backed security guarantees to autonomous agent execution, addressing one of the most common enterprise deployment blockers.

---

## 📊 The Trajectory

Hermes Agent's growth continues to accelerate. The project has climbed to well over **172,000 GitHub stars** — the #1 most-starred AI agent runtime — with more than **1,000 merged pull requests** in just the past two weeks alone across the v0.15.0/0.15.1/0.15.2 release cycle.

The Desktop launch fills a clear gap: while Hermes Agent was already powerful as a CLI tool, messaging gateway, and web dashboard, it lacked a **polished native desktop experience** for everyday users. The public preview changes that — and with prebuilt installers for all three major platforms plus a zero-admin Windows path, the barrier to entry has never been lower.

> *"An open-source, MIT-licensed agent that persists skills and memory across Telegram, Discord, Slack, WhatsApp, Signal, email, and CLI changes the economics of deploying AI assistants for small teams: no vendor lock-in, no per-session context loss."* — AI Weekly

---

## 🔮 What This Means for the Agent Ecosystem

The combination of Hermes Desktop + NVIDIA RTX Spark + Microsoft security primitives is more than a series of launches — it's a signal that **open-source agent runtimes are moving from developer tools to consumer infrastructure**.

1. **Desktop-first UX** — Hermes Desktop brings the same persistent memory, skill auto-generation, and multi-channel gateway to a native GUI that anyone can install and use
2. **Hardware partnership** — The NVIDIA Computex integration means Hermes Agent will run natively on the next generation of AI PCs hitting the market this fall
3. **Enterprise security** — Microsoft's security primitives address the compliance and governance concerns that have kept many enterprises from deploying autonomous agents

For developers already running Hermes Agent, the transition is seamless: `hermes desktop` launches the app using your existing config. For newcomers, the `--include-desktop` installer provides a single-command path from zero to a fully functional, self-improving agent with a native app interface.

---

## 📦 Summary of What's Shipping

| Item | Status | Date |
|------|--------|------|
| **Hermes Desktop (public preview)** | ✅ Live | June 2, 2026 |
| **Hermes Agent v0.15.2** | ✅ Bundled | May 29, 2026 |
| **NVIDIA RTX Spark integration** | ✅ Announced at Computex | June 1, 2026 |
| **OpenShell runtime** | ✅ Preview | June 1, 2026 |
| **Microsoft security primitives** | ✅ Preview | June 1, 2026 |
| **RTX Spark hardware shipping** | 📅 Fall 2026 | Partners listed |

Try Hermes Desktop today:

```bash
# New install with desktop app
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --include-desktop

# Existing install
hermes desktop
```

*Stay tuned — this week's Velocity Release deep dive and Computex coverage are just the beginning. The Hermes ecosystem is moving faster than ever.*
