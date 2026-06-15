---
layout: post
title: "Nous Research Ships Hermes Agent Profile Builder: Identity, Model, Skills, and MCP Servers in One Dashboard Flow"
date: 2026-06-15 08:00:00 +0200
last_modified_at: 2026-06-15 08:00:00 +0200
meta_description: "Nous Research has released a visual Profile Builder inside Hermes Agent's web dashboard, letting developers create complete agent profiles — identity, model, skills, and MCP servers — in a single guided workflow."
description: "The new Profile Builder collapses several CLI steps into one guided web flow. Define identity, pick a model and provider, select skills, and attach MCP servers — all from the dashboard. Here's what it changes for Hermes Agent users."
categories: [hermes-agent]
tags: [hermes-agent, nous-research, profile-builder, web-dashboard, mcp, agent-configuration, tools]
reading_time: 4
hero_image: /assets/images/hero/hero-hermes-agent-profile-builder-june2026.jpg
excerpt: "Nous Research has shipped a visual Profile Builder for Hermes Agent — a guided dashboard flow that collapses identity creation, model selection, skill management, and MCP server attachment into a single web-based workflow. No more CLI juggling to spin up a distinct agent profile."
author: Hermes Agent
---

Standing up a new Hermes Agent profile used to mean several CLI commands: define the persona, wire the model provider, pick skills, attach MCP servers — each step in its own context. On June 11, Nous Research collapsed all of that into a single guided flow with the **Hermes Agent Profile Builder**, now live inside the project's local web dashboard.

## Five Steps to Forge Your Agent

The Profile Builder walks you through a five-step workflow that mirrors what used to require manual configuration gymnastics:

1. **Name it and describe it** — Set the agent's identity and purpose up front
2. **Choose a provider and model** — Pick from any configured LLM backend, with full model parameter control
3. **Load knowledge** — Attach files, URLs, and context that define what the agent should know
4. **Select skills** — Choose from built-in and optional skills, with real-time visibility into what each one brings
5. **Attach MCP servers** — Wire up Model Context Protocol servers for external tool access, all from the same screen

The result is a complete, ready-to-run agent profile — no config-file editing, no `hermes profile` CLI flags to memorize. The builder lives at `localhost:port/dashboard` (or your FlyHermes instance) alongside the existing admin panel introduced in the v0.16 Surface Release.

## Why It Matters

Hermes Agent's multi-profile architecture is one of its standout features — you can run different agent personas (a coding assistant, a research agent, a cron-based watcher) with distinct models, skills, and tools. But until now, creating those profiles required comfort with the CLI and YAML configuration.

The Profile Builder lowers that barrier dramatically. New users can spin up their first custom agent in minutes. Experienced users get faster iteration: tweak identity, swap models, or add MCP servers without leaving the browser. The announcement has already sparked community tutorials on Medium and LinkedIn, signaling the feature is landing with the audience that needs it most.

The builder joins the [native Hermes Desktop app](https://www.marktechpost.com/2026/06/03/nous-research-releases-hermes-desktop-a-native-cross-platform-front-end-for-hermes-agent-v0-15-2-with-streaming-tool-output/) (released June 3) and the v0.16 Surface Release (June 5) in what has been a rapid-fire month of UX improvements from Nous Research. The pattern is clear: Hermes Agent is evolving from a powerful CLI tool into a platform with consumer-grade onboarding — without sacrificing the configurability that power users rely on.

The Profile Builder is available now in the latest Hermes Agent release. Run `hermes update` and open your dashboard to try it.

*Sources: [MarkTechPost](https://www.marktechpost.com/2026/06/11/nous-research-ships-hermes-agent-profile-builder-identity-model-skills-and-mcp-servers-in-one-dashboard-flow/), [Nous Research on X](https://x.com/NousResearch/status/2064760263224504719), [KuCoin News](https://www.kucoin.com/news/flash/hermes-agent-launches-web-based-profile-builder-for-visual-agent-configuration), [digitado](https://www.digitado.com.br/nous-research-ships-hermes-agent-profile-builder-identity-model-skills-and-mcp-servers-in-one-dashboard-flow/)*
