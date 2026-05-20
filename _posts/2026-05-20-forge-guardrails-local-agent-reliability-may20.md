---
title: "Forge: How Guardrails Lift an 8B Local Model to 86% on Agentic Tool-Calling Tasks"
date: 2026-05-20 10:00:00 +0200
last_modified_at: 2026-05-20 10:00:00 +0200
categories: [tools-frameworks]
tags: [guardrails, local-models, tool-calling, open-source, agent-reliability, self-hosted]
reading_time: 6
hero_image: /assets/images/hero/hero-forge-guardrails-local-agent-reliability-may20.jpg
excerpt: "Forge, a new open-source Python framework from Texas Instruments engineer Antoine Zambelli, uses guardrails to lift a local 8B model (Ministral-3) from 53% to 86.5% on multi-step agentic tool-calling tasks — rivaling frontier models on structured workflows. With 440 points on Hacker News and 726 GitHub stars on day one, it addresses the most pressing problem for developers running agents on local hardware: reliability."
---

The dream of running capable AI agents entirely on local hardware has always collided with an uncomfortable reality: small models make mistakes. They call the wrong tools, format arguments incorrectly, skip required steps, and get confused in multi-turn workflows. An 8B parameter model running on a consumer GPU can generate code and answer questions — but trusting it to autonomously execute a multi-step tool-calling sequence has been a gamble.

**Forge**, a new open-source Python framework released yesterday by Antoine Zambelli (a software engineer at Texas Instruments), aims to close that gap entirely. Its headline result: applying Forge's guardrails to a Ministral-3 8B Instruct Q8 model running on llama-server lifts its agentic task completion rate from a baseline of **53% to 86.5%** across a 26-scenario evaluation suite — and **76% on the hardest scenarios**.

The project shot to the top of Hacker News with **440 points** and has already accumulated **726 GitHub stars**, as the developer community recognizes a framework that addresses the single biggest blocker to local agent adoption.

## The Problem: Small Models Can't Handle Multi-Step Tool Calling

The gap between frontier models (Claude Opus, GPT-5) and open-source local models is not just about knowledge or reasoning. On agentic tool-calling tasks — where a model must decide which tool to call, format parameters correctly, process the result, and decide the next step — small models fail in predictable ways:

- **Malformed tool calls** — The model generates JSON arguments with incorrect syntax, wrong parameter names, or missing required fields
- **Step skipping** — The model jumps to a conclusion before calling all required tools
- **Self-correction failure** — When a tool returns an error, the model doesn't know how to retry or adjust
- **Context drift** — Over a multi-turn sequence, the model loses track of what it was doing

"Small local models (~8B) cannot be trusted to choose correctly between text and tool calls," Zambelli writes in the Forge documentation. "Guiding them to a tool is a must."

## How Forge Fixes This

Forge is not a model. It's a **reliability layer** that wraps around local LLM backends (llama-server, Ollama, Llamafile) and applies three categories of guardrails:

### 1. Response Validation & Rescue Parsing

Before Forge passes a model's output to any tool, it runs the response through a validation pipeline. If the tool call is malformed — bad JSON, wrong parameter types, missing fields — Forge doesn't crash. It catches the error, generates a targeted "nudge" prompt that describes exactly what went wrong, and sends the model back through inference with the corrected context.

This rescue loop is the single biggest driver of the reliability improvement. A model that would have failed on a malformed tool call gets a second (or third) chance with precise feedback.

### 2. Step Enforcement

Multi-step workflows require the model to execute steps in order. Forge tracks which steps have been completed and which are still pending. If the model tries to skip ahead or produce a final answer before all required tools have been called, the step enforcer intervenes with a nudge that steers it back on track.

### 3. Context Management with Tiered Compaction

Local models have limited context windows — and agentic workflows eat context fast. Each tool call adds the result to the conversation, and before long, the model is trying to reason with 16K+ tokens of accumulated history.

Forge's context manager uses a **tiered compaction strategy**: it preserves the most recent turns and the most important structural elements (system prompt, tool definitions), while compressing or dropping intermediate tool results. This keeps the model operating within its optimal context budget without losing the thread of the conversation.

The system is also VRAM-aware — it detects available hardware and sets context budgets accordingly, preventing the silent OOM crashes that plague local agent setups.

## Three Ways to Use It

Forge ships with three deployment modes, reflecting different use cases:

| Mode | Best for | How it works |
|------|----------|-------------|
| **WorkflowRunner** | Building agent loops from scratch | Define tools, pick a backend, run structured loops with full guardrail stack |
| **Guardrails Middleware** | Adding reliability to existing orchestration | Import forge's response validator and step enforcer into your own loop |
| **Proxy Server** | Drop-in upgrade for any OpenAI-compatible client | Sits between client and model server, applies guardrails transparently |

The proxy mode is particularly clever. You point any agent framework — OpenCode, Continue, aider, Claude Code — at `http://localhost:8081/v1` instead of directly at llama-server, and Forge handles validation, rescue, and step enforcement transparently. The client thinks it's talking to a smarter model.

## The Evaluation Results

Forge's evaluation suite includes 26 scenarios across two tiers:

- **OG-18** (18 scenarios): baseline multi-step tool-calling tasks
- **Advanced Reasoning** (8 scenarios): harder scenarios requiring planning, branching, and error recovery

The best configuration — Ministral-3 8B Instruct Q8 on llama-server with Forge's full guardrail stack — scores:

| Metric | Score |
|--------|-------|
| OG-18 (baseline) | **91.7%** |
| Advanced Reasoning | **76.0%** |
| **Overall** | **86.5%** |
| Baseline (no guardrails) | ~53% |

The guardrails are not free — they add latency from retry loops and validation passes — but for autonomous agent workflows where reliability matters more than raw speed, the tradeoff is transformative.

## Backend Variance: A Surprising Finding

One of the more interesting findings in Forge's documentation is how much **the serving layer matters**. The same model running on different backends produces meaningfully different results:

| Backend | OG-18 | Advanced | Overall |
|---------|-------|----------|---------|
| llama-server (with `--jinja`) | 91.7% | 76.0% | **86.5%** |
| Ollama (native FC) | 86.1% | 62.5% | **78.9%** |
| Llamafile (prompt-injected) | 58.3% | 25.0% | **48.1%** |

The gap between llama-server and Ollama (7.6 percentage points) is significant and suggests that the inference engine's tool-calling implementation has a material impact on reliability — separate from the model itself. For developers trying to get the most out of local models, this is a valuable calibration point.

## Why This Matters

Forge arrives at a moment when the agent ecosystem is bifurcating. On one side, frontier API providers (Anthropic, OpenAI) offer increasingly capable agents that are expensive and centralized. On the other, the open-source community is building local agent infrastructure — but reliability has been the critical gap.

Forge doesn't claim to solve alignment or make small models as smart as Claude Opus. What it does is **extract maximum reliability from the models we already have** — through engineering rather than scale.

For anyone running agents on a local GPU with an 8B model, Forge is the most practical reliability upgrade available today. And with the HN community's enthusiastic reception, it's clear that the pain point it addresses is widely shared.

---

*Sources: [Forge GitHub repository](https://github.com/antoinezambelli/forge), [Hacker News discussion](https://news.ycombinator.com/item?id=48192383), [Forge evaluation results](https://github.com/antoinezambelli/forge/tree/main/docs/results), [Ministral-3 model](https://huggingface.co/mistralai/Ministral-3B-Instruct-2512)*
