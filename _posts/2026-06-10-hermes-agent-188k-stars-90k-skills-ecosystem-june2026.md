---
layout: post
title: "Hermes Agent Crosses 188K GitHub Stars as Skills Hub Explodes Past 90,000 Skills"
date: 2026-06-10 10:00:00 +0200
last_modified_at: 2026-06-10 10:00:00 +0200
meta_description: "Hermes Agent has crossed 188,000 GitHub stars and the Skills Hub has exploded from 310+ to 90,881 skills across 12 registries — making it the fastest-growing open-source agent framework of 2026 according to Dealroom. Here's what the ecosystem looks like now."
description: "Hermes Agent crosses 188,000 GitHub stars while the Skills Hub explodes past 90,000 skills across 12 registries. A look at the community ecosystem that's making it the fastest-growing open-source agent framework of 2026."
categories: [hermes-agent]
tags: [hermes-agent, nous-research, open-source, ecosystem, skills-hub, community, github-stars, plugins]
reading_time: 6
hero_image: /assets/images/hero/hero-hermes-agent-188k-stars-90k-skills-ecosystem-june2026.jpg
excerpt: "In the two weeks since we last mapped the ecosystem at 165K stars and 310+ community skills, Hermes Agent has added 23,000 stars and the Skills Hub has exploded from hundreds to 90,881 skills across 12 registries — with Dealroom naming it the fastest-growing open-source agent framework of 2026. Here's what changed."
author: The Agent Report
---

When we last [surveyed the Hermes Agent ecosystem]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}) on May 25, the numbers were already staggering: **165,000 GitHub stars, 27,300 forks, and 310+ community skills**. Two weeks later, those numbers look quaint.

As of June 10, 2026, the [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) repository has crossed **188,781 GitHub stars** — a gain of over 23,000 stars in roughly two weeks. The Skills Hub now lists **90,881 skills across 12 registries**, up from a few hundred. And [Dealroom](https://dealroom.co) has officially designated Hermes Agent as **the fastest-growing open-source agent framework of 2026**.

> "The open-source self-improving AI agent from Nous Research has now accumulated over 180,000 GitHub stars in under four months since its February 25 launch." — [Ewan Mak, Medium](https://medium.com/@tentenco/hermes-agent-desktop-app-everything-you-need-to-know-about-nous-researchs-self-improving-ai-agent-3cb59bd31e5f)

The surface-level story is growth. The deeper story is *structural* — the ecosystem is reorganizing itself around discoverability, curation, and plugin infrastructure that didn't exist two weeks ago.

## The Skills Hub: From Hundreds to 90,881

The single most dramatic change is the Skills Hub. In late May, the community was sharing skills ad-hoc — GitHub gists, Reddit threads, Discord pins. The [official Skills Hub](https://hermes-agent.nousresearch.com/docs/skills/) changed that.

Now cataloguing **90,881 skills across 12 registries**, the Hub auto-refreshes twice daily and includes contributions from NVIDIA/skills (added to trusted taps in [v0.16.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5)), alongside community registries. A skill installed through the Hub isn't just a file download — it's a versioned, auditable artifact that Hermes's built-in **Curator** can grade, prune, and consolidate automatically.

The Skill ecosystem has also spawned its own meta-layer: [lobehub.com](https://lobehub.com/skills/aradotso-trending-skills-awesome-hermes-agent) now features a trending skills marketplace for Hermes Agent, updated daily, complete with trigger phrases and usage examples for each skill.

## The Curation Layer: Awesome Lists and Atlas

Two weeks ago, finding community tools meant scrolling through Reddit or searching GitHub. Now there are three major discovery surfaces:

| Resource | Stars | Description |
|---|---|---|
| [SamurAIGPT/awesome-hermes-agent](https://github.com/SamurAIGPT/awesome-hermes-agent) | New | Comprehensive curated list — skills, plugins, tools, integrations, deployment templates. Updated 2 days ago. |
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | Growing | Curated ecosystem guide with safety flows and evolution loops. Updated 1 week ago. |
| [Hermes Atlas](https://hermesatlas.com/) (ksimback/hermes-ecosystem) | Community map | 100+ tools mapped with live GitHub data and AI-powered search. Published "The State of Hermes — May 2026" report. |

This is the classic sign of a maturing open-source ecosystem: the project no longer needs to tell you what's available — the community builds the map.

## New Plugin Infrastructure: Hermes LCM

The v0.16.0 Surface Release formally introduced the [context engine plugin slot](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin), and the community responded immediately. **[stephenschoettler/hermes-lcm](https://github.com/stephenschoettler/hermes-lcm)** — published just two days ago — is a Lossless Context Management plugin that replaces the default lossy summarization with a **DAG-based context engine**.

Instead of the agent periodically summarizing and discarding old messages (the standard approach that inevitably loses nuance), LCM builds a directed acyclic graph of conversation context. Every message, tool call, and result is preserved — the engine just prunes the graph traversal, not the data. For long-running agents that operate across days or weeks (cron jobs, infrastructure operators, research assistants), this is transformative.

The plugin architecture itself is significant: it means the community can now extend Hermes's internals at well-defined extension points rather than forking the core.

## Mainstream Signals: "STARTUP EDITION" and Media Attention

The ecosystem growth is being noticed outside developer circles. A [June 2026 "STARTUP EDITION"](https://blog.mean.ceo/hermes-agent-news-june-2026/) roundup on blog.mean.ceo frames Hermes Agent explicitly for founders and investors, highlighting the self-hosted, always-on architecture as a differentiator from SaaS agents. Multiple Medium publications have published deep-dive guides ([Ewan Mak](https://medium.com/@tentenco/hermes-agent-desktop-app-everything-you-need-to-know-about-nous-researchs-self-improving-ai-agent-3cb59bd31e5f), [ThePlanetTools](https://theplanettools.ai/blog/hermes-desktop-nous-research-open-source-gui-app-june-2026)), and a [Substack guide](https://nervegna.substack.com/p/hermes-agent-desktop-the-full-guide) now walks product designers, PMs, and CMOs through real-world use cases.

The [Hermes Agent Challenge on DEV](https://dev.to/challenges/hermes-agent-2026-05-15) — covered [in our last report]({% post_url 2026-06-01-hermes-agent-challenge-results-may-2026 %}) — produced 14 community projects, but the ripple effects continue: several challenge participants have since published their projects as standalone open-source repos, feeding back into the ecosystem.

## What's Powering This Growth?

Three structural factors are driving the acceleration:

1. **The Surface Release (v0.16.0)** landed June 5 with 874 commits, 542 merged PRs, and Hermes Desktop — a native app for macOS, Windows, and Linux. Desktop access lowered the barrier from "configure a CLI tool" to "download and start chatting."

2. **The self-evolution loop** — [hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) with DSPy + GEPA, [covered June 8]({% post_url 2026-06-08-hermes-agent-self-evolution-dspy-gepa-june2026 %}) — means Hermes can now *improve its own skills*, creating a feedback loop where more usage produces better skills, which attracts more users.

3. **Plugin architecture maturity** — the context engine plugin slot, MCP integration, and profile system mean the community can build at the edges without waiting for the core team. The hermes-lcm plugin went from concept to published repo in under a week.

## What to Watch

The 188K star milestone will likely be 200K+ within weeks. But the more interesting trajectory is the Skills Hub: if it maintains even a fraction of its current growth rate, Hermes Agent will have the largest skill library of any open-source agent framework — by a wide margin.

The plugin ecosystem is still in its infancy. The context engine slot is the first of what will likely become a broader plugin API. Community projects like SkillClaw (a post-task evolution loop on top of Hermes's built-in skill creation) and the emerging fleet management tools suggest the next wave will be about *coordinating multiple Hermes instances* — not just running one.

For now, the numbers tell a clear story: Hermes Agent isn't just growing. It's developing the institutional infrastructure — skill registries, curated lists, plugin APIs, community maps — that transforms a popular project into a platform.
