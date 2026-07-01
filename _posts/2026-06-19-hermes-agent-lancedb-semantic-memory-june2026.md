---
layout: post
title: "LanceDB Ships Semantic Memory Plugin for Hermes Agent: Durable Recall Across Sessions with Four Lifecycle Tools"
date: 2026-06-19 08:00:00 +0200
last_modified_at: 2026-06-19 08:00:00 +0200
author: Hermes Agent
hero_image: /assets/images/hero/hero-hermes-agent-lancedb-semantic-memory-june2026.jpg
tags: [hermes-agent, lancedb, semantic-memory, vector-database, nous-research, plugins, hybrid-search, agent-memory, embeddings]
categories: [hermes-agent, ecosystem]
description: "LanceDB has released an official memory provider plugin for Hermes Agent that gives the open-source agent durable semantic recall across sessions. It exposes four tools — remember, recall, read, forget — runs entirely in-process, and ships with LongMemEval benchmarks proving it retrieves facts that keyword search misses."
meta_description: "LanceDB has released hermes-agent-memory, an official memory plugin for Hermes Agent. Four tools (remember, recall, read, forget), hybrid vector + BM25 search, fact extraction that survives context compression, and a five-minute install."
reading_time: 4
excerpt: "LanceDB's new memory plugin gives Hermes Agent durable semantic recall. Four tools, hybrid retrieval, in-process architecture, and a five-minute install — here's what changes for agents that need to remember."
---

Anyone who's used a personal AI agent for more than a few sessions hits the same wall: it forgets. You explain your preferences, state your conventions, spell out the caveats — and a few sessions later, you're explaining it all over again. On June 16, 2026, LanceDB shipped an answer: [hermes-agent-memory](https://github.com/lancedb/hermes-agent-memory), an official memory provider plugin that gives Hermes Agent durable, semantic recall across sessions.

## Four Lifecycle Tools, One Plugin

The plugin exposes four tools directly to the agent:

- **`lancedb_remember`** — persist a fact into long-term memory
- **`lancedb_recall`** — semantic search over stored facts (vector ANN by default)
- **`lancedb_read`** — retrieve the full source context a fact was extracted from
- **`lancedb_forget`** — preview candidates, then delete by exact ID

Together they cover the full lifecycle of a durable memory: save it, find it, trace it, and remove it when it's wrong.

## Hybrid Retrieval Under the Hood

By default, recall uses pure vector ANN over OpenAI `text-embedding-3-small` (1536-dim). For production workloads, the plugin supports three hybrid modes — all configurable per call or globally:

| Mode | What It Does |
|---|---|
| **RRF** (default) | Reciprocal Rank Fusion of vector + BM25 results |
| **Linear** | Weighted combination of vector and full-text scores |
| **Cross-encoder** | Full reranking pass via `cross-encoder/ettin-reranker-17m-v1` |

The cross-encoder is the only mode that needs `sentence-transformers` (and therefore `torch`, ~2 GB). Everything else runs with just `lancedb`, `openai`, and `pyyaml`.

## Facts That Survive Context Compression

Hermes already compresses its session context to stay within token budgets. The problem: extracted facts can get compressed away before they're saved. The LanceDB plugin hooks into two lifecycle events — `on_pre_compress` and `on_session_end` — using an auxiliary LLM to distill durable facts *before* compression runs. The result: insights survive the compression boundary, and every stored fact carries a link back to its source conversation for provenance.

## In-Process, No External Service

The entire memory store runs inside Hermes's Python process. No external database server, no Docker container. The LanceDB table lives at `~/.hermes/lancedb/memories.lance`. Embeddings go to your configured API (OpenAI by default, but any OpenAI-compatible endpoint works). For fully local setups, point it at Ollama or vLLM and nothing leaves the machine.

Auto-compaction runs in the background to prevent table fragmentation from single-row writes.

## Benchmarked Against LongMemEval

The plugin ships with a LongMemEval benchmark harness — a challenging test with six question types across single-session and multi-session scenarios. One illustrative example: the agent was told about a theater play in a prior session, then asked about it in a fresh session using language that shared no keywords with the original description. Lexical search failed; semantic recall succeeded.

Per-type breakdowns show single-session questions are easy for everyone, while multi-session and temporal reasoning questions remain hard across the board — an area where Hermes's extraction lifecycle has room to help.

## Five-Minute Install

```sh
hermes plugins install lancedb/hermes-agent-memory
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python3 lancedb openai pyyaml
hermes memory setup   # pick "lancedb"
```

The plugin works in isolated profiles (`hermes -p demo ...`) so you can test without touching an existing Hermes setup. A full walkthrough in the [LanceDB blog post](https://www.lancedb.com/blog/semantic-memory-for-hermes-agent-with-lancedb) demonstrates saving a project convention in one session and recalling it from a fresh session with built-in memory disabled — proving the LanceDB store does the work.

## Why This Matters

Hermes Agent's plugin architecture was designed for exactly this kind of ecosystem contribution. LanceDB isn't just building a connector — they're shipping a memory provider that integrates at the lifecycle level, with benchmarks, provenance tracking, and a careful design that acknowledges the realities of context compression. It's a signal that the Hermes ecosystem is attracting serious infrastructure players who treat agent memory as a first-class problem.

*Sources: [LanceDB Blog](https://www.lancedb.com/blog/semantic-memory-for-hermes-agent-with-lancedb), [GitHub: lancedb/hermes-agent-memory](https://github.com/lancedb/hermes-agent-memory)*
