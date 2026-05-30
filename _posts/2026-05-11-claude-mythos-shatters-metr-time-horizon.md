---
layout: post
title: "Claude Mythos Shatters METR's Time Horizon Graph — First Model to Crack Multi-Hour Autonomous Tasks"
date: 2026-05-11 14:00:00 +0200
last_modified_at: 2026-05-11 14:00:00 +0200
meta_description: "Claude Mythos Preview hits a 6.25-hour 50% time horizon on METR's benchmark, nearly doubling the next-best model. METR warns measurements above 16 hours are now unreliable."
description: "Claude Mythos Preview hits a 6.25-hour 50% time horizon on METR's benchmark, nearly doubling the next-best model. METR warns measurements above 16 hours"
categories: [research]
tags: [anthropic, claude, claude-mythos, metr, ai-agents, time-horizon, model-benchmarks]
reading_time: 7
excerpt: "Anthropic's Claude Mythos Preview achieves a 6.25-hour 50% time horizon on METR's benchmark — nearly double the next-best model and so capable that METR had to add a warning: measurements above 16 hours are unreliable with their current task suite."
hero_image: /assets/images/hero/hero-claude-mythos-shatters-metr-time-horizon.jpg
author: The Agent Report
---

# Claude Mythos Shatters METR's Time Horizon Graph — First Model to Crack Multi-Hour Autonomous Tasks

**Anthropic's Claude Mythos Preview achieved a staggering 6.25-hour 50% time horizon on the METR benchmark — more than double any other publicly evaluated model — a milestone that comes as Anthropic also announced [Claude Managed Agents]({% post_url 2026-05-07-anthropic-managed-agents-dreaming-outcomes %}) entering a new era of orchestration that its measurement suite cannot reliably assess tasks beyond 16 hours.**

On May 8, 2026, METR (Model Evaluation and Threat Research) updated its [Task-Completion Time Horizons](https://metr.org/time-horizons/) page with a new entry: "Claude Mythos Preview (early)." The release date is listed as April 7, 2026, but the evaluation results were only published this week — and they immediately broke the chart.

## What Is the METR Time Horizon?

The **time horizon** measures the task duration (estimated by human expert completion time) at which an AI agent is predicted to succeed with a given reliability. A 50% time horizon of 6.25 hours means Claude Mythos has a 50% chance of successfully completing tasks that take a skilled human expert over six hours to finish.

This is not about how long the AI itself takes — AI agents are typically several times faster than humans. It's a measure of **task difficulty** an AI agent can handle autonomously.

| Metric | Claude Mythos | Claude Opus 4.6 (next best) |
|---|---|---|
| **50% Time Horizon** | **6.25 hours** | 3.69 hours |
| **80% Time Horizon** | **31.1 minutes** | 7.7 minutes |
| Release Date | April 7, 2026 | February 5, 2026 |

## Breaking the Benchmark

The most notable detail in METR's update is a new notice: *"Measurements above 16 hrs are unreliable with our current task suite."* This was added alongside the Mythos entry — a direct acknowledgement that the model's capabilities are straining against the limits of METR's evaluation methodology.

On Reddit's r/ClaudeAI, a post titled **"Claude Mythos literally broke the METR graph"** surged to 214 points, while a companion meme post **"What's up, Claude?"** accumulated **3,313 upvotes** — signaling the community's excitement about the new model's capabilities.

## The Leap: From Hours to a Full Workday

The progression of Claude's time horizons tells a dramatic story:

- **Claude 3.7 Sonnet** (Feb 2025): 6.2 minutes (0.10 hours)
- **Claude Opus 4.5** (Nov 2025): 60.3 minutes (1.01 hours)
- **Claude Opus 4.6** (Feb 2026): 221.6 minutes (3.69 hours)
- **Claude Mythos Preview** (Apr 2026): **375.1 minutes (6.25 hours)**

In just over one year, Claude's autonomous task-completion capability has grown **60x** — from 6 minutes to over 6 hours. The gap between Mythos and the next-best model (Opus 4.6) is larger than the gap between Opus 4.6 and any other publicly evaluated model.

For context, here's how Mythos compares to the broader landscape:

- **Claude Mythos**: 6.25 hrs — nearly 2× the next competitor
- **Claude Opus 4.6**: 3.69 hrs
- **Gemini 3.1 Pro**: 1.49 hrs
- **GPT-5.4**: 1.26 hrs
- **GPT-5.2**: 1.31 hrs

## What This Means for AI Agents — contextualized in our [complete guide to AI agents]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %})

A 6.25-hour time horizon is a milestone. It means Claude Mythos can reliably handle tasks that would take a human professional most of a workday — debugging complex systems, building substantial features from scratch, or performing multi-step research.

For the agent ecosystem, this unlocks **agentic workflows that span hours without human intervention**. Agents built on Claude Mythos could:

- **End-to-end feature development**: Design, implement, test, and deploy code changes across an entire codebase
- **Multi-stage security audits**: Scan, analyze, and patch vulnerabilities with minimal oversight
- **Long-horizon research**: Execute extended research pipelines involving literature review, experimentation, and report generation
- **Complex data migrations**: Plan and execute multi-phase data transformations

## The "Glasswing" Connection

Anthropic's navigation links "Mythos preview" to a new initiative called **[Project Glasswing](https://www.anthropic.com/glasswing)** — described as "a new initiative to secure the world's most critical software and give defenders a durable advantage in the coming AI-driven era of cybersecurity." This suggests Claude Mythos may debut with a cybersecurity focus, though the model's capabilities extend far beyond security tasks.

## Caveats and Context

Some important qualifications:

1. **"Preview (early)"** — This is an early preview, not a final release. The final shipping model may differ.
2. **Measurement ceiling** — METR's 16-hour unreliability warning means Mythos' true ceiling may be even higher than measured.
3. **Context matters** — Time horizon measures one specific type of capability (self-contained software/ML/security tasks). Real-world performance depends on context, tooling, and integration.
4. **Scaffolding matters** — Results depend on the agent scaffold used. METR's results use their own scaffold and elicitation pipeline.

## The Bottom Line

Claude Mythos represents a step-change in AI agent capabilities. Where previous models plateaued in the 1-4 hour range, Mythos crosses into multi-hour autonomous task execution. If this trajectory continues, the next generation of Claude models may push beyond the 16-hour mark — into territory where AI agents can handle a full workday's worth of complex, autonomous work.

The community is watching closely. For agent builders, Mythos isn't just another model update — it's the first signal that AI agents may soon operate at timescales that fundamentally change how we build software, conduct research, and automate knowledge work.
