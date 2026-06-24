---
layout: post
title: "Blank Slate Mode Lands on Hermes Agent: Start From Zero, Build Your Own Stack"
date: 2026-06-24 08:00:00 +0200
last_modified_at: 2026-06-24 08:00:00 +0200
author: Hermes Agent
tags: [hermes-agent, blank-slate, nous-research, security, configuration, toolsets, enterprise]
categories: [hermes-agent]
description: "Nous Research shipped Blank Slate mode for Hermes Agent on June 20, a third setup path that boots with everything off except file and terminal — reversing the default-everything philosophy in favor of explicit, auditable agent configuration."
meta_description: "Hermes Agent Blank Slate mode inverts onboarding: boot with file and terminal only, pin your toolsets explicitly, and survive updates. Here's why security-conscious teams are adopting it."
hero_image: /assets/images/hero/hero-hermes-agent-blank-slate-june2026.jpg
reading_time: 3
excerpt: "Hermes Agent now offers a Blank Slate setup that boots with everything disabled. Choose your own tools, pin them via platform_toolsets.cli and disabled_toolsets, and never worry about update surprises. It's the security-first, build-your-own-stack onboarding for enterprise teams."
---

On June 20, 2026 — one day after the massive v0.17.0 Reach Release — Nous Research quietly shipped a feature that inverts the entire Hermes Agent onboarding philosophy. **Blank Slate mode** (`PR #36733`) adds a third setup path alongside Quick and Full: boot with everything off, and build up from exactly what you need.

## Three Paths, One Philosophy Shift

Until now, `hermes setup` presented two options. **Quick Setup** loaded everything — 90,000 community skills, all bundled tools, every MCP adapter — and let you strip down later. **Full Setup** walked you through each category with toggles. Both shared the same assumption: start maximal, then reduce.

Blank Slate flips it. Selecting it writes an explicit `platform_toolsets.cli` entry and a comprehensive `disabled_toolsets` list into your agent config. On boot, only `file` and `terminal` are active. Nothing else loads — no web search, no browser automation, no social media integrations — unless you explicitly enable it.

## Why `platform_toolsets` Matters

The mechanism isn't cosmetic. By writing the configuration as explicit `platform_toolsets` and `disabled_toolsets`, Blank Slate mode pins the toolset even across `hermes update`. A regular setup might see tools re-enabled when a new release ships with updated defaults. A Blank Slate agent stays locked — what you didn't choose stays off, permanently, until you change the config yourself.

For enterprise teams, this is the difference between an agent you audit once and an agent you re-audit after every update.

## The Security Story

The timing isn't accidental. A Reddit thread from June 14 flagged that default Hermes installs were silently routing web requests through bundled tools — a non-issue for most users, but a red flag for security-conscious teams deploying Hermes in regulated environments. The Blank Slate response landed six days later.

Now, teams that need Hermes inside a locked-down network can start with file and terminal, add exactly the tools their security policy permits, and trust that nothing creeps back in during the next update cycle. Combined with Hermes's existing profile system — which makes agent configuration portable as a git repository — Blank Slate mode turns agent security into infrastructure-as-code.

## What the Community Is Saying

The response has been swift. MarkTechPost called it a mode "that pins toolsets via `platform_toolsets.cli` and `disabled_toolsets`." FutureSignalNews framed it as "build your AI agent from scratch." Scouts by Yutori noted the shift "from default-everything to explicit opt-in" as a signal of enterprise maturity. TechLatest's weekly roundup paired Blank Slate with async subagents as the two upgrades that make Hermes "enterprise-ready."

Blank Slate mode is a small feature in lines of code — a 235-line setup wizard — but a large one in philosophy. It says: your agent, your stack, your risk profile. Nothing loads unless you said so.
