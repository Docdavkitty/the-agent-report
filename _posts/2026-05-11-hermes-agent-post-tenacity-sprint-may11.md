---
layout: post
title: "Hermes Agent's Post-Tenacity Sprint: 143K Stars, New Finance Skill, and 179 Merged PRs in 4 Days"
date: 2026-05-11 12:00:00 +0200
last_modified_at: 2026-05-11 12:00:00 +0200
meta_description: "Hermes Agent executes a post-Tenacity cleanup sprint with community-driven PRs addressing regression fixes, documentation updates, and platform stability."
categories: [hermes-agent]
tags: [Hermes Agent, Nous Research, open-source, post-tenacity, community-momentum, stocks-finance, kanban-diagnostics, platform-maturation]
reading_time: 6
hero_image: /assets/images/hero/hero-hermes-agent-post-tenacity-sprint-may11.jpg
excerpt: "Since the v0.13.0 'Tenacity' release on May 7, Hermes Agent has added 5,500 new GitHub stars (now 143.5K), merged 179 pull requests, and shipped a new Stocks & Finance skill, Telegram performance optimizations, Kanban diagnostics, provider 402 caching, and more. The project shows zero signs of slowing down."
author: The Agent Report
---

The **Hermes Agent v0.13.0 "Tenacity" release** dropped on May 7 with multi-agent Kanban boards, `/goal` persistence, Checkpoints v2, and 8 P0 security fixes. Four days later, the project hasn't just held its momentum — it's **accelerated**.

Since May 8, the GitHub repository has jumped from ~138,000 to **143,510 stars** (+5,500 in 96 hours), and **179 pull requests have been merged** from **13 unique contributors**. Here's what's landed in the immediate post-Tenacity window.

## 📈 Explosive Star Growth

At roughly **1,375 new stars per day**, Hermes Agent is [now the fastest-growing AI agent runtime on GitHub]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}) by a significant margin:

| Milestone | Stars | Date | Days |
|-----------|-------|------|------|
| v0.12.0 Curator | 127K | April 30 | — |
| Community wave | 131K | May 4 | +4 |
| i18n + Skill Lifecycle | 135K | May 6 | +2 |
| v0.13.0 Tenacity | 138K | May 7 | +1 |
| **Today** | **143.5K** | **May 11** | **+4** |

The project has added **~16,500 stars in 11 days** since v0.12.0 — a trajectory that shows no signs of slowing — and the project would go on to ship [v0.14.0 "Foundation" just 9 days later]({% post_url 2026-05-18-hermes-agent-v0140-foundation-release-may16 %}). Forks have reached **22,406**, and the repository now has **9,960 open issues** (a testament to the scale of community engagement).

## 🆕 New Skills and Features

### Stocks & Finance Skill

Community contributor **Mibayy** shipped a new **[stocks & finance optional skill](https://github.com/NousResearch/hermes-agent/pull/23587)** that integrates Yahoo Finance data with zero API key required. The skill provides:

- Real-time stock quotes and historical data
- Portfolio tracking
- Market summary and sector performance
- No external API registration needed — it uses Yahoo Finance's public endpoints

This is a significant addition for developers building financial assistant agents or market-monitoring cron jobs.

### Kanban Diagnostics: `stranded_in_ready`

Project lead **Teknium** added a **[stranded_in_ready diagnostic](https://github.com/NousResearch/hermes-agent/pull/23578)** for the Kanban system — a new check that surfaces tasks sitting in the "Ready" column without a worker assigned. This makes it easier to identify stalled boards and unblock workflows.

### API Testing / REST-GraphQL Debug Skill

The `api-testing` skill has been **[renamed and relocated](https://github.com/NousResearch/hermes-agent/pull/23589)** to `rest-graphql-debug`, providing a structured skill for API endpoint testing, response validation, and debugging REST and GraphQL services directly from the agent.

## ⚡ Performance and Reliability

### Telegram Adaptive Cadence

**wilsen0** contributed a **[Telegram gateway performance optimization](https://github.com/NousResearch/hermes-agent/pull/23588)** that tunes message cadence dynamically and adds an adaptive fast-path for short replies. The result: snappier responses on Telegram without hitting API rate limits.

### Provider 402 Caching

**Teknium** landed a **[fix for provider retry storms](https://github.com/NousResearch/hermes-agent/pull/23597)** — when an LLM provider returns a 402 (Payment Required) error, the agent now caches the provider as "unhealthy" with a TTL rather than retrying on every single call. This prevents cascading billing failures and reduces API overhead.

### Docker Extra Args + Timestamps

**Mibayy** contributed **[docker_extra_args and display.timestamps](https://github.com/NousResearch/hermes-agent/pull/23599)** features to the terminal and CLI tooling, giving users finer control over Docker container execution and timestamp visibility in agent output.

## 🔧 Nix and Infrastructure

### Nix Container Entrypoint Fix

**Siddharth Balyan** fixed a **[critical Nix container entrypoint issue](https://github.com/NousResearch/hermes-agent/pull/23633)** where `chown -R` was stripping the `setgid` bit, breaking hostUsers group access in Nix environments. This improves Hermes Agent's compatibility with Nix-based deployments — an increasingly important use case as the project expands beyond traditional Docker setups.

### Nix extraDependencyGroups

The same contributor added **[extraDependencyGroups for sealed venv extras](https://github.com/NousResearch/hermes-agent/pull/21817)**, making it easier to manage Hermes Agent's dependency tree in NixFlake environments.

## 🔒 Security

### Env Sanitization in Quick Commands

**0xbyt4** shipped a **[security fix](https://github.com/NousResearch/hermes-agent/pull/23595)** that sanitizes environment variables and redacts output in quick commands, closing a potential information-leak vector. The fix also removes write-only `_pending_messages` state, reducing the overall attack surface.

### YAML Parse Failure Warnings

A new **[config safety improvement](https://github.com/NousResearch/hermes-agent/pull/23585)** from **Teknium** makes Hermes Agent warn loudly on YAML parse failures instead of silently falling back to defaults. This prevents subtle misconfiguration bugs where a broken `config.yaml` would go unnoticed until runtime.

## 🧠 Community Pulse

The post-Tenacity window has seen contributions from a diverse set of community members:

| Contributor | Notable PR |
|-------------|-----------|
| **Mibayy** | Stocks & Finance skill, Docker extra args |
| **wilsen0** | Telegram adaptive cadence optimization |
| **Siddharth Balyan** | Nix container entrypoint, dependency groups |
| **0xbyt4** | Discord typing indicator cleanup, env sanitization |
| **kjames2001** | Telegram edit overflow split-and-deliver |
| **eloklam** | Kanban search test cleanup |
| **Gutslabs** | Three defensive fixes from PR #1974 |

> "This is what open-source at scale looks like — 179 PRs in 4 days across security, performance, infrastructure, and new skills. The Tenacity release was the headline, but the community sprint is the real story." — The Agent Report

## 🔭 Looking Ahead

At the current cadence of **~45 merged PRs per day**, the next release (v0.14.0) could arrive within a week. Areas to watch:

- **Kanban maturity**: The `stranded_in_ready` diagnostic suggests deeper Kanban reliability features are coming
- **Nix ecosystem**: Multiple Nix-related PRs signal growing enterprise deployment demand
- **New skills pipeline**: The finance and API testing skills point to a broadening of Hermes Agent's domain coverage
- **143K+ and climbing**: At this growth rate, 150K stars is likely within the next week

For developers who haven't tried Hermes Agent since the v0.12.0 "Curator" release — or those who joined during the Tenacity wave — now is the perfect time to explore the post-release improvements. The project is available at [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) and documented at [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com).
