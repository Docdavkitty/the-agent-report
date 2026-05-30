---
layout: post
title: "Ex-GitHub CEO Thomas Dohmke Launches Entire with $60M to Build the Next Developer Platform for AI Agents"
date: 2026-05-27 10:00:00 +0200
last_modified_at: 2026-05-27 10:00:00 +0200
meta_description: "Ex-GitHub CEO Thomas Dohmke launches Entire with 60 million dollars to rebuild the developer platform for an era where AI agents produce the majority of code,."
description: "Ex-GitHub CEO Thomas Dohmke launches Entire with 60 million dollars to rebuild the developer platform for an era where AI agents produce the majority of"
categories: [industry]
tags: [entire, thomas-dohmke, github, developer-platform, ai-coding-agents, git, seed-round]
reading_time: 8
hero_image: /assets/images/hero/hero-ex-github-ceo-entire-60m-developer-platform-ai-agents.jpg
excerpt: "Former GitHub CEO Thomas Dohmke announces Entire, a $60M seed-stage developer platform designed from the ground up for an era where AI agents — not humans — are the primary producers of code. The platform ships an open-source CLI that ties agent context into Git on every push."
author: The Agent Report
---

The game has changed. The system is cracking. And the former CEO of GitHub is betting $60 million that the entire software development lifecycle needs to be rebuilt from scratch.

**Thomas Dohmke**, who led GitHub through its exponential growth under Microsoft and oversaw the launch of GitHub Copilot — the product that arguably kicked off the AI coding revolution — has unveiled **Entire**, a new company building what he calls "the world's next developer platform." The company launches with a $60 million seed round co-led by Felicis, with participation from Madrona, M12 (Microsoft's venture arm), Basis Set, 20VC, Cherry Ventures, Picus Capital, and Global Founders Capital.

The announcement, published on [Entire's blog](https://entire.io/blog/hello-entire-world/), comes with an immediate open-source release: the **Entire CLI**, a tool that captures the reasoning, decisions, and constraints behind every line of AI-generated code and stores them as Git-compatible checkpoints.

## Why Entire Exists

Dohmke's thesis is stark: the software development lifecycle — issues, pull requests, code reviews, CI/CD — was designed for a world where humans wrote code and reviewed each other's work. That world is ending.

"In the last few months alone, the fundamental role of a developer has been refactored," Dohmke writes. "From Anthropic's Claude Code with Opus 4.6, to OpenAI's latest GPT-5.3-Codex agentic coding model, to Cursor's Composer 1.5 and more, advancements in agentic intelligence have turned the flow of coding on its head."

The core problem, as Dohmke frames it:

> **Issues** were designed for human planning and tracking, not as structured, machine-readable units of work. **Git repositories** were never extended to version everything developers build with in the AI era. **Pull requests** simply do not scale for large monorepos. Every day, agents are being choked and throttled by centralized API capacity and rate limits.

"The entire software ecosystem is being bottlenecked by a manual system of production that was never designed for the era of AI in the first place," he adds — invoking a historical parallel to the automotive assembly line that replaced craft-based production.

## The Three Pillars of Entire

Entire's architecture rests on three components:

1. **A Git-compatible database** — unifying code, intent, constraints, and reasoning in a single version-controlled system. Traditional Git preserves *what* changed. Entire's database also preserves *why*.
2. **A universal semantic reasoning layer** — enabling multi-agent coordination through a "context graph" that tracks dependencies, decisions, and exploration across parallel agent sessions.
3. **An AI-native software development lifecycle** — reinventing agent-to-human collaboration with primitives designed for machine-speed development rather than human-paced workflows.

## The Entire CLI: Checkpoints Over Commits

The first product shipping today is the Entire CLI, which introduces a new primitive called **Checkpoints**.

"Today, agent sessions are ephemeral. Prompts live in terminals and reasoning lives in context windows," Dohmke explains. "The decisions, constraints, and iteration that produce code disappear the moment you close the session."

The problem compounds at scale: "Without shared context, agents can't collaborate effectively. They retrace steps, duplicate reasoning, waste tokens, and lose the thread of decisions made hours or days earlier."

The Entire CLI solves this by capturing:

- The full prompt-reasoning-response chain for every code generation
- Decision points and alternatives considered (and rejected)
- Constraints and design goals that shaped the output
- Agent-to-agent coordination messages

All of this data is stored as Git-compatible checkpoints — not replacing Git, but extending it with what Dohmke calls "the missing half of version control."

## Who's Backing This

The investor lineup reads like a who's-who of the developer tools and AI ecosystem. Beyond the institutional investors, Dohmke's "slate of international investors" includes:

- **Gergely Orosz** (author of The Pragmatic Engineer)
- **Theo Browne** (t3.gg, developer educator)
- **Jerry Yang** (Yahoo co-founder)
- **Olivier Pomel** (Datadog CEO)
- **Garry Tan** (Y Combinator CEO)

The message is clear: the people who built the last generation of developer platforms believe the next one needs to be built from scratch.

## What This Means for the AI Agent Ecosystem

Entire's launch signals something profound about the maturity of the AI agent ecosystem. When a former GitHub CEO — who helped build the most ubiquitous developer platform in the world — says the current infrastructure is irreparably broken, it validates what many developers have been experiencing firsthand with tools like [Kiro's spec-driven IDE]({% post_url 2026-05-20-kiro-agentic-ide-may20 %}) and the rapidly maturing [open-source agent framework landscape]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).

The tooling problem is real. Current CI/CD pipelines stall on AI-generated PRs that can be thousands of lines long. Code review breaks down when reviewers can't understand the reasoning behind agent-written code. Git histories become useless when every commit message just says "agent-generated code."

Entire's approach — making agent reasoning a first-class citizen in version control — is one of the most promising solutions to emerge this year. The open-source CLI means the entire ecosystem can experiment with it immediately, and the $60M seed round gives the company runway to build the full platform vision. This fits into a broader pattern we're tracking: from [Block's Goose recipe runner]({% post_url 2026-05-27-block-goose-ai-agent-recipe-runner-scaled-60-percent %}) to purpose-built agentic IDEs, the developer tooling layer is being rebuilt from the ground up for the agent era.

The question now is whether Entire can win the network effects battle. Developer platforms are notoriously hard to displace — ask anyone who's tried to pry developers away from GitHub. But Dohmke knows this better than anyone. He spent years running GitHub, and his entire pitch is that the incumbents can't retrofit their way into the agent era.

"The truth is," he writes, "a system that cannot be retrofitted for what's ahead needs to be rebuilt. Just like when automotive companies replaced the traditional craft-based production system with the moving assembly line, we must now reimagine the entire software development lifecycle for a world where machines are the primary producers of code."

If he's right, Entire won't just be a new company. It will be the platform that the next decade of software — written primarily by AI agents — runs on.

---

*Sources: [Entire.io blog announcement](https://entire.io/blog/hello-entire-world/), [Hacker News discussion](https://news.ycombinator.com/item?id=41710227)*
