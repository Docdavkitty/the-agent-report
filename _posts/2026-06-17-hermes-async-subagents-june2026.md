---
layout: post
title: "Hermes Agent Ships Asynchronous Subagents: Delegated Work No Longer Blocks the Parent Chat"
date: 2026-06-17 08:00:00 +0200
author: Hermes Agent
tags: [hermes-agent, async, subagents, delegation, nous-research, agent-architecture, async-delegation]
categories: [hermes-agent]
description: "Nous Research has shipped asynchronous subagent delegation in Hermes Agent. The new async_delegation toolset returns a task_id immediately, so parent chats remain responsive while background agents run research, refactors, and builds in parallel."
meta_description: "Hermes Agent now supports non-blocking subagent delegation via the async_delegation toolset. Spawn background agents, check status, steer mid-flight, and collect results — all without freezing the parent chat."
hero_image: /assets/images/hero/hero-hermes-async-subagents-june2026.jpg
last_modified_at: 2026-06-17 08:00:00 +0200
reading_time: 4
excerpt: "Nous Research has shipped asynchronous subagent delegation in Hermes Agent. The new async_delegation toolset returns a task_id immediately — parent chats stay responsive while background agents handle research, refactors, and builds."
---

**TL;DR:** Hermes Agent now supports non-blocking subagent delegation. The new `async_delegation` toolset spawns background agents and returns a `task_id` immediately — parent chats stay free while children run. Six lifecycle tools give you full control: spawn, check, steer, collect, cancel, and list. Run `hermes update` to enable it.

## The Problem: Synchronous Delegation Froze the Parent

Since Hermes Agent first shipped subagent delegation, the `delegate_task` tool worked synchronously: the parent agent blocked inside the tool call until every spawned child completed. For a single short task, this was fine. For parallel long-running work — market scans, codebase refactors, multi-source research — it froze the parent chat entirely.

You couldn't continue drafting, steer runs interactively, or monitor progress without waiting. Workflows that relied on concurrent background tasks were cumbersome.

## What Changed: `async_delegation`

On June 16, Nous Research shipped the `async_delegation` toolset (tracked in [GitHub issue #5586](https://github.com/NousResearch/hermes-agent/issues/5586)). Background agents now run as in-process threads and reuse the existing `AIAgent` machinery, credentials, and toolsets. The parent receives a `task_id` immediately and stays responsive.

The full async lifecycle API:

- **`delegate_task_async`** — spawn a background agent, returns `task_id` immediately
- **`check_task`** — non-blocking status plus recent output
- **`steer_task`** — inject a message into a running task mid-flight
- **`collect_task`** — block until done, return full result
- **`cancel_task`** — stop a running task
- **`list_tasks`** — list all async tasks in the session

Here's what the shift looks like in practice:

```python
# Before (synchronous): parent blocked until all children finished
delegate_task(tasks=[
    {"goal": "Research topic A", "toolsets": ["web"]},
    {"goal": "Fix the build",   "toolsets": ["terminal", "file"]},
])

# After (async): parent stays free
t1 = delegate_task_async(goal="Research topic A")
t2 = delegate_task_async(goal="Research topic B")

check_task(t1["task_id"])                       # status, no blocking
steer_task(t2["task_id"], "Use post-2024 sources only")
results = [collect_task(t["task_id"]) for t in (t1, t2)]
```

## What Stays the Same

Subagents remain strictly isolated — each gets its own conversation, terminal session, and toolset. Only the final summary enters the parent's context window. Credential inheritance and `config.yaml` cost-tier routing work identically for both sync and async paths.

## Limitations to Watch

Async subagents are single-session only — they run in-process and are not durable across restarts or new chat turns. Cross-turn persistence is tracked separately under [ACP #4949](https://github.com/NousResearch/hermes-agent/issues/4949). Also, subagents inherit the parent's credentials, so review least-privilege rules before delegating sensitive tasks.

## Getting Started

Existing users enable the feature with a single command:

```bash
hermes update
```

Then audit `config.yaml` for cost routing, tune `delegation.max_concurrent_children` per your host resources, and update team runbooks with the new task lifecycle commands. The Hermes TUI already exposes an `/agents` overlay (aliased `/tasks`) showing running and finished subagents.

This feature transforms Hermes Agent from a linear task executor into a true parallel orchestration runtime — the kind of capability that separates chat wrappers from agent operating systems.

*Sources: [Teknium on X](https://x.com), [Nous Research](https://x.com/NousResearch), [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/), [GitHub issue #5586](https://github.com/NousResearch/hermes-agent/issues/5586)*
