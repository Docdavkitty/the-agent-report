---
layout: post
title: "Statewright: Visual State Machines That Make AI Coding Agents Reliable — From 20% to 100% Pass Rate on SWE-bench"
date: 2026-05-19 14:00:00 +0200
last_modified_at: 2026-05-19 14:00:00 +0200
meta_description: "Statewright introduces visual state machines enforcing per-phase tool access for AI coding agents, lifting local models from 20 to 100 percent pass rates."
categories: [tools-frameworks]
tags: [statewright, ai-agents, state-machines, agent-reliability, swi-bench, claude-code, codex, mcp, open-source, developer-tools]
reading_time: 6
hero_image: /assets/images/hero/hero-statewright-visual-state-machines-ai-agents.jpg
excerpt: "Statewright introduces state machine guardrails for AI coding agents — enforcing tool access per phase of a workflow. In benchmarks, local models went from 2/10 to 10/10 pass rates on SWE-bench tasks. The Rust-powered, MCP-integrated engine is open-source."
author: The Agent Report
---

**A new open-source project called Statewright is tackling the #1 pain point of AI coding agents — reliability — by constraining not *what* the model thinks, but *what tools it can reach at each phase of a workflow.** The approach is strikingly simple: replace the open-ended tool free-for-all with a state machine that dictates exactly which tools the agent can see and use at each step.

The results speak for themselves. In a 5-task SWE-bench subset, two local models went from **2 of 10 attempts passing to 10 of 10** — a fivefold improvement — with zero changes to the models themselves.

## The Problem: 40 Tools, One Agent, Zero Structure

Anyone who has watched an AI coding agent at work has seen the failure pattern. Give Claude Code or Codex a bug report and 40+ tools, and the agent often:

- Re-reads the same file five times
- Calls edit tools during its analysis phase
- Deploys code before tests pass
- Gets stuck in "read-loop death spirals"
- Calls destructive shell operations without guardrails

The conventional response is to use a bigger model or write a longer system prompt. This helps at the margins but doesn't fix the root cause: **the model is being asked to self-regulate its own tool use — a problem that the [Forge guardrails framework]({% post_url 2026-05-20-forge-guardrails-local-agent-reliability-may20 %}) also addresses from a different angle, and it's not good at it.**

Observability tools tell you what went wrong after the fact. They don't prevent it.

## The State Machine Approach: Structure Beats Reasoning

Statewright's insight is elegant: instead of making the model bigger, make the *problem space* smaller.

> *"Agents are suggestions, states are laws."* — Statewright README

The system defines a workflow as a state machine. Each state has:

- **Allowed tools** — the model can only see and call tools permitted in the current phase
- **Tool restrictions** — fine-grained limits on edits, command execution, and file access
- **Transitions** — conditions that move the workflow to the next state
- **Guards** — programmatic checks (e.g., "test_result eq pass") that gate transitions

A typical bugfix workflow looks like this:

| Phase | Allowed Tools | What Happens |
|-------|--------------|--------------|
| Planning | Read, Grep, Glob | Agent analyzes code, identifies the bug |
| Implementing | Read, Edit, Write | Agent fixes the code with edit guards |
| Testing | Read, Bash (pytest only) | Agent runs tests; passes → completed, fails → back to implementing |
| Completed | — | Workflow ends |

Call a tool that's not in the current phase and the agent gets rejected with a message explaining what IS available and how to transition. This is **hard enforcement** — the tool call is intercepted at the hook layer before execution.

## Under the Hood: A Rust Engine with MCP Integration

The core of Statewright is a **deterministic Rust engine** that evaluates state machine definitions, part of a growing ecosystem of [agent reliability tooling](/2026/06/top-20-open-source-ai-agent-tools-2026/). No LLM in the loop — it's pure rules.

On top of this sits a plugin layer that integrates with coding agents via **MCP (Model Context Protocol)**. When a workflow is activated, hooks enforce tool restrictions per state. The model goes from seeing 40 tools to seeing 5 — and gets clear instructions about its current phase and how to progress.

The supported agents and their enforcement levels:

| Agent | Enforcement |
|-------|-------------|
| Claude Code | Hard (hooks + MCP) |
| Codex | Hard (hooks + MCP) |
| Pi | Hard (with tool recovery for local models) |
| opencode | Hard (alpha) |
| Cursor | Advisory (MCP + rules) |

The **guardrails** go beyond simple tool allow/block. Among the most notable:

- **Bash discernment** — blocks `echo > file`, `rm -rf`, `sed -i`, and scripting interpreters even when Bash itself is permitted
- **Edit guards** — rejects diffs exceeding configurable line limits, caps files edited per state
- **Conditional transitions** — programmatic guards on context data like `test_result eq pass`, `coverage gt 80`
- **Approval gates** — pauses for human review at critical decision points
- **Interrupts** — editing a file matching a glob pattern triggers auto-transition to a validation state
- **Fork/join** — run branches sequentially or in parallel

## The Research Results: 20% → 100% on SWE-bench

Statewright's team ran a 5-task SWE-bench subset against several local models:

| Model | Size | Without Statewright | With Statewright |
|-------|------|-------------------|-----------------|
| gpt-oss:20b | 13.8GB | 2/10 | 10/10 |
| gemma4:31b | 19.9GB | 2/10 | 10/10 |
| llama3.3 | 42.5GB | 2/2 | 2/2 |

The 2-of-10 baseline on the unconstrained runs is not unusual — local models frequently get stuck in loops, call the wrong tools, or lose context after too many failed edits. With Statewright's constraints, the same models on the same hardware achieved perfect scores.

The team also identified a **floor around 13GB model size**: below that, models can identify bugs correctly but can't serialize surgical edits (they rewrite entire files). That's a model limitation, not a guardrail limitation.

## How to Use It

Getting started takes two commands in Claude Code:

```
/plugin marketplace add statewright/statewright
/plugin install statewright
```

This opens the visual workflow editor at statewright.ai, where users can drag states, draw transitions, and assign tools per phase — no JSON editing required unless desired.

The managed cloud at statewright.ai handles workflow storage, run history, and the MCP gateway. Pricing starts at **free (3 workflows, 200 transitions/month)**, with Pro at $29/month and Team at $99/month. The Rust engine is **Apache 2.0** and embeddable with no runtime dependencies.

## Why This Matters: The Agent Reliability Crisis

Statewright arrives at a moment when the industry is grappling with a fundamental question: **how do you make AI agents trustworthy enough to run autonomously?**

The current answers fall into three camps:
1. **Better models** — always works, but expensive and not available on local hardware
2. **Better prompts** — fragile, model-specific, easy to jailbreak
3. **Observability** — tells you what broke, doesn't prevent it

Statewright proposes a **fourth path**: structural constraints enforced at the tool-call level, independent of the model's reasoning ability. It's closer to how real engineering works — you don't trust the developer to remember not to `rm -rf /`; you configure the permissions system.

For teams running AI coding agents in production — especially with local models where reliability gaps are widest — this is a genuinely new category of solution. Not a prompt hack. Not a bigger model. A **guardrail system** that makes the agent follow the process, whether it wants to or not.

---

*Sources: [Statewright GitHub](https://github.com/statewright/statewright), [statewright.ai](https://statewright.ai), [Hacker News discussion](https://news.ycombinator.com/item?id=48143961)*
