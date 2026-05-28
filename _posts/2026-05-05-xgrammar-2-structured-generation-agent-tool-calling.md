---
layout: post
title: "XGrammar-2: 80x Faster Structured Generation That's Quietly Powering the Next Generation of AI Agents"
date: 2026-05-05 14:00:00 +0200
last_modified_at: 2026-05-05 14:00:00 +0200
meta_description: "XGrammar-2 introduces Structural Tag for composable JSON tool calling, delivering 80x faster grammar compilation and becoming the backbone of reliable agent."
categories: [research]
tags: [structured-generation, tool-calling, xgrammar, mlc-ai, llm-inference, constrained-decoding]
reading_time: 8
hero_image: /assets/images/hero/hero-xgrammar-2-structured-generation-agent-tool-calling.jpg
excerpt: "MLC AI's XGrammar-2 introduces Structural Tag — a composable JSON protocol for tool calling, reasoning channels, and custom output structures — delivering up to 80x faster grammar compilation with near-zero overhead. Already adopted by SGLang, vLLM, TensorRT-LLM, and MLC-LLM, it's quietly becoming the backbone of reliable agent tool use across the industry."
author: The Agent Report
---

If you've ever watched an AI agent fumble a tool call — producing `{"city": "Paris"}` when the schema demanded `{"location": "Paris"}` — you know the pain of unreliable structured generation. It's the silent bottleneck that turns a promising agent demo into a debugging nightmare.

On May 4, the MLC (Machine Learning Compilation) community shipped a fix. **[XGrammar-2](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)** isn't just an incremental upgrade — it's a fundamental rethinking of how LLMs produce structured outputs, purpose-built for the agent era. The headline numbers are striking: **up to 80× faster grammar compilation**, **100% schema accuracy**, and **near-zero latency overhead**, even when juggling 500+ tools in a single session.

## Why Agent Tool Calling Needed a Reboot

Over the past year, agent applications — from Claude Code to OpenClaw — have exploded in complexity. These systems define sophisticated harnesses that LLMs must navigate, producing specific output structures at every turn:

- **Tool calls** with strictly typed JSON arguments
- **Reasoning channels** that interleave free text with structured blocks
- **Multi-part responses** combining analysis, tool invocations, and final answers

The original [XGrammar](https://github.com/mlc-ai/xgrammar), released over a year ago, solved the basic problem: it used constrained decoding to guarantee 100% structural correctness with near-zero overhead. By precomputing a token mask cache at compilation time, it blocked invalid tokens at each decoding step, ensuring the LLM could only generate valid output.

But the agent landscape evolved faster than the tooling. Modern agent frameworks demand output structures that XGrammar wasn't designed for — think DeepSeek V4's XML-style tool parameters, OpenAI's "harmony format" with interleaved reasoning and tool calls, or custom multimodal agent outputs. Supporting each required bespoke engineering effort from serving engine teams, and the growing grammar sizes (50, 100, even 500+ tools) started to strain the original architecture.

## Enter Structural Tag: A Universal DSL for Agent Output

XGrammar-2's centerpiece is **Structural Tag** — a composable JSON-based DSL that provides a unified, extensible way to describe agent output structures. Instead of hand-crafting grammars for each model and each use case, you compose a handful of primitives:

| Type | Purpose |
|------|---------|
| `sequence` | Chains two or more parts in order |
| `tag` | Matches a begin marker, constrained content, and end marker |
| `any_text` | Matches arbitrary free text until a boundary |
| `triggered_tags` | Lets the model emit free text until a trigger string switches to structured mode |
| `json_schema` | Constrains arguments to a JSON Schema definition |

These types are **fully composable**. Want to describe DeepSeek V4's output format — reasoning text followed by optionally triggered tool calls in XML-style parameters? Here's the gist:

```json
{
  "type": "structural_tag",
  "format": {
    "type": "sequence",
    "elements": [
      { "type": "tag", "begin": "", "content": { "type": "any_text" }, "end": "</think>" },
      { "type": "triggered_tags", "triggers": ["<|DSML|tool_calls|>"], ... }
    ]
  }
}
```

The result? **100% schema accuracy** on BFCL-V3 benchmarks — every single tool call conforms to the target JSON schema, eliminating format-related failures entirely. For smaller models, the accuracy gains are dramatic: when the model no longer has to guess the format, it can focus on the *semantics*. For more on agent tool infrastructure, see our [top 20 open source tools](/2026/06/top-20-open-source-ai-agent-tools-2026/).

## 80× Faster: The Efficiency Engine

Raw accuracy is table stakes. What makes XGrammar-2 genuinely impressive is how it maintains that accuracy at scale. Two innovations stand out:

### Cross-Grammar Cache

Different tool schemas share common substructures — every `{"type": "string"}` field, every array definition, every nested object pattern. XGrammar-2 implements an **automaton-based hierarchical hashing algorithm** that automatically detects and reuses these shared structures. In tests with 50 tools, nearly **50% of structures were reused**, slashing preprocessing time.

### Repetition State Compression

Some tool parameters involve massive repetition — an array of up to 1,000,000 items, for instance. Naive handling requires O(repetition_count) preprocessing time. XGrammar-2 compresses this to **O(1)** by introducing a dedicated repetition primitive. The result: compilation time drops from **534 ms to 5.37 ms** — a 100× improvement for the most extreme cases.

Combined, these optimizations deliver **up to 80× faster grammar compilation** compared to XGrammar, with the gap widening as the number of tools grows.

## Batched and Speculative: Modern Serving, First-Class

XGrammar-2 doesn't treat efficiency as a batch-time afterthought. It ships with:

- **Batch APIs** that process multiple grammar states in a single C++ pass, avoiding Python-side loops
- **Speculative decoding integration** — XGrammar-2 can walk draft token trees on the CPU (generating masks) while the target model verifies on the GPU, **overlapping both computations** for minimal overhead
- **Cross-platform support** via [TVM-FFI](https://github.com/apache/tvm), exposing APIs in Python, C++, Rust, and JavaScript across Windows, macOS, and Linux

## Industry Adoption Is Already Here

Perhaps the most telling signal: XGrammar-2 isn't a theoretical paper. It's **already integrated** into the four most widely-used LLM serving engines:

- **[SGLang](https://github.com/sgl-project/sglang)** — strict mode tool calling for DeepSeek V4, Qwen 3.6, and more
- **[vLLM](https://github.com/vllm-project/vllm)** — exposed via OpenAI-compatible `response_format` API
- **[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)** — NVIDIA's optimized inference engine
- **[MLC-LLM](https://github.com/mlc-ai/mlc-llm)** — MLC's own universal deployment runtime

The collaborator list reads like a who's-who of AI infrastructure: **xAI, Databricks, DeepSeek Infra, Google Vertex AI**, and others have all contributed. This isn't a niche research project — it's becoming the industry standard for structured generation in agent systems.

## What This Means for Agent Developers

If you're building agents — whether with Hermes Agent, Claude Code, OpenClaw, or a custom harness — XGrammar-2 matters because it addresses the single most common failure mode in production agent deployments: **format errors in tool calls**.

> "Constrained decoding is best used to enforce format constraints, not to change the semantics of an LLM's response," the MLC team notes. "It helps downstream programs avoid fatal failures from malformed outputs, while keeping the impact on the model's accuracy minimal."

For agent developers, this means:
- **Zero tool-call format failures** — every JSON argument is schema-valid by construction
- **Custom output structures** — define exactly what your agent should emit, from multimodal video annotations to complex reasoning traces
- **Drop-in upgrade** — if you're using SGLang, vLLM, TensorRT-LLM, or MLC-LLM, XGrammar-2 support is already available through standard API calls

## The Bottom Line

XGrammar-2 is one of those rare infrastructure releases that matters far beyond its immediate scope. By solving the structured generation problem at the serving-engine level — with a clean, composable DSL and aggressive optimizations — it removes a key friction point that has held back reliable agent deployment. For more on agent tool-calling infrastructure, see our [ultimate guide to agent frameworks]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}) and the [state of AI agents May 2026](/2026/05/state-of-ai-agents-may-2026/).

As agent systems grow from demo prototypes to production workloads handling thousands of concurrent tool calls, the quality of their structured output isn't a nice-to-have — it's a requirement. XGrammar-2 delivers exactly that, and the industry is already voting with its integration.

---

*Visit the [XGrammar GitHub repository](https://github.com/mlc-ai/xgrammar) to explore the code, read the [technical report](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation), or check the [Quick Start guide](https://xgrammar.mlc.ai/docs) to integrate it into your agent stack.*
