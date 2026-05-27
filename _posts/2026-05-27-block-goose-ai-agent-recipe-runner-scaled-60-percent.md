---
layout: post
title: "Block Open-Sourced Goose: How a YAML Recipe File Scaled an AI Agent to 60% of the Company"
date: 2026-05-27 14:00:00 +0200
last_modified_at: 2026-05-27 14:00:00 +0200
categories: [tools-frameworks]
tags: [goose, block, square, open-source, mcp, enterprise-adoption, agent-framework]
reading_time: 6
hero_image: /assets/images/hero/hero-block-goose-ai-agent-recipe-runner-scaled-60-percent.jpg
excerpt: "Block open-sourced Goose, an AI agent that scaled to 60% of its 12,000 employees. The key innovation isn't the model or the prompt — it's a YAML recipe format that any team member can author."
author: The Agent Report
---

Block — the parent company of Square, Cash App, and Afterpay — released **Goose** as an open-source AI agent in early 2025. A year later, the tool has **44,000+ GitHub stars, 368+ contributors, and 2,600+ forks**. But the headline number isn't open-source adoption. It's internal adoption: **roughly 60% of Block's ~12,000 employees use Goose weekly**, spanning 15 different job profiles — engineering, sales, design, product, and customer success.

The question that follows is obvious: how does a single CLI tool serve both an engineer debugging a flaky test and a product manager triaging a Jira ticket?

The answer is a **30-line YAML file**.

## The Architecture: Local Agent, MCP Tools, Recipe Workflow

Goose is a Rust binary that runs entirely on the user's machine. It connects to any major LLM provider — Anthropic, OpenAI, Gemini, Mistral, xAI, or a local model via Ollama — and uses **MCP (Model Context Protocol)** servers as its tool surface. The architecture has three layers that each evolve independently:

1. **The agent runtime** — a core loop (plan → call tools → evaluate → repeat) that stays generic.
2. **The extension system** — every tool is an MCP server. Adding GitHub access, Jira integration, or an internal API is a config entry, not a code change.
3. **The recipe** — a YAML document bundling instructions, required extensions, parameters, and the prompt into a single shareable file.

The separation is deliberate. The agent doesn't decide which tools to load — the recipe does. The agent doesn't free-form its way through the task — the recipe provides a numbered sequence with checkpoints.

## What a Recipe Looks Like

A recipe is a YAML file that any team member can author. Here's an abridged example for reviewing a GitHub pull request:

```yaml
name: review-pr
description: Review a GitHub PR for risk areas
params:
  pr_url:
    type: string
    description: The GitHub PR URL to review.
extensions:
  - name: developer
  - name: github
    args: ["-y", "@modelcontextprotocol/server-github"]
prompt: |
  1. Fetch the PR diff and the list of changed files.
  2. For each file, identify: behavior changes, new dependencies,
     missing tests, anything that looks rushed.
  3. Group findings by severity: must-fix, should-fix, nit.
  4. Post a single review comment with the grouped findings.
```

The recipe is run with a single command:

```bash
goose recipe run review-pr --params pr_url=https://github.com/org/repo/pull/42
```

The `params` block makes the recipe a function — you call it with different inputs instead of writing one per task. The `extensions` block loads MCP servers dynamically for the duration of the run and discards them afterward. The numbered prompt steps act as a planning skeleton — the agent doesn't reinvent the workflow each time.

## Why This Pattern Scaled

The recipe format is the architectural breakthrough that explains the adoption number. A **YAML file is a thing a product manager can author**. They can copy a recipe a teammate wrote, change the prompt, run it, and see what happened — no deploy, no code review, no engineering handoff.

For engineers, the value is different: a recipe is a **committable artifact** that lives in the same repo as the code it operates on. A team's review workflow sits at `recipes/review-pr.yaml` next to the service code. New hires read the recipe to understand the workflow. Changes get reviewed like any other artifact.

The MCP extension layer is the multiplier. Every new internal capability is a one-time MCP server build, and then it's available to every recipe. Block doesn't write a separate "PR review agent" and "ticket triage agent." They write **one Goose binary**, then ship a directory of recipes and a directory of MCP servers. **Composition does the rest.**

## Goose Is Now a Foundation Project

In a move that changes the risk calculus for enterprise adoption, Goose has moved from Block's governance to the **Agentic AI Foundation under the Linux Foundation**. The tool is now a community-governed project — no single company controls its roadmap.

The implications are significant. The governance risk that held back enterprise teams ("what if Block stops investing?") is gone. Recent community activity points toward a public recipe registry, tighter MCP server interoperability, and richer parameter types including file uploads and structured objects.

## What This Means for the Industry

Goose's recipe pattern is the strongest signal yet that the future of enterprise AI agents is not about better models — it's about **workflow abstractions that non-engineers can author**. The recipe is an architectural pattern, not a Goose-specific feature. The same shape works on top of Claude Code skills, Cursor agents, or any runtime that supports YAML-defined workflows and MCP tools.

The takeaway for any team building internal agent platforms: if your system doesn't have an analog for the recipe, you're going to end up with bespoke agent builds per team. The recipe is what lets one tool serve a 12,000-person company without forking.

The boring abstraction — a YAML file with a name, a prompt, and an extension list — is how you reach 60% of the company.
