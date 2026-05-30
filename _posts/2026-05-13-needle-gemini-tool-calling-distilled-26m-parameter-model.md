---
layout: post
title: "Needle: Gemini Tool Calling Distilled Into a 26M Parameter Model — Tiny AI That Actually Calls Functions"
date: 2026-05-13 14:00:00 +0200
last_modified_at: 2026-05-13 14:00:00 +0200
meta_description: "Cactus Compute distills Gemini 3.1 tool-calling into a 26-million-parameter model running at 1200 tokens per second on phones, watches, and glasses with fully."
description: "Cactus Compute distills Gemini 3.1 tool-calling into a 26-million-parameter model running at 1200 tokens per second on phones, watches, and glasses with"
categories: [research]
tags: [needle, gemini, model-distillation, tool-calling, function-calling, on-device-ai, tiny-models]
hero_image: /assets/images/hero/hero-needle-gemini-tool-calling-distilled-26m-parameter-model.jpg
reading_time: 7
excerpt: "Cactus Compute distilled Gemini 3.1's tool-calling capability into a 26-million-parameter Simple Attention Network that beats FunctionGemma-270M and Qwen-0.6B on single-shot function calls. At 1200 tokens/sec on production hardware, it runs on phones, watches, and glasses — and the weights are fully open."
author: The Agent Report
---

**A 26-million-parameter model just humiliated models ten times its size at the one thing that matters most for AI agents: calling the right tool at the right time.**

Cactus Compute's [Needle](https://github.com/cactus-compute/needle) — which rocketed to **423 points on Hacker News** and **736 GitHub stars** in under 24 hours — is the first model to prove that function-calling intelligence doesn't need billions of parameters. By distilling Gemini 3.1's tool-calling capability into a radically minimalist 26M-parameter Simple Attention Network (SAN), Needle beats models like FunctionGemma-270M, Qwen-0.6B, Granite-350M, and LFM2.5-350M on single-shot function call benchmarks. And it can run on a smartwatch.

This isn't a toy. It changes the economics of on-device AI agents.

## What Needle Is — and Isn't

Let's be precise about what Needle does and doesn't do.

**What it does:** Given a user query and a set of tool definitions (JSON schema), Needle outputs the correct tool call with arguments. It's a single-turn function-calling engine — you get: `[{"name": "get_weather", "arguments": {"location": "San Francisco"}}]`.

**What it doesn't do:** Conversational chat, multi-turn reasoning, general knowledge QA, or anything that requires broad language understanding. That's not the point. Needle is a **specialized router** — the part of an agent pipeline that decides *which function to invoke* and *with what parameters* — a key concept in our [AI agent glossary]({% post_url 2026-05-27-ai-agent-glossary-55-terms %}) of 55 essential terms.

This specialization is exactly what makes it so powerful for agentic workloads, fitting into the [broader agent frameworks landscape]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).

## The Architecture: Simple Attention Networks

Needle is built on a **Simple Attention Network (SAN)** — an architecture designed by the Cactus team specifically for tiny, efficient models. The full stack:

| Component | Spec |
|-----------|------|
| **Parameters** | 26 million |
| **Embedding dim** | 512 |
| **Heads** | 8H / 4KV (GQA) |
| **Vocab size** | 8,192 (BPE) |
| **Encoder layers** | 12 (no FFN) |
| **Decoder layers** | 8 |
| **Pretraining** | 200B tokens on 16 TPU v6e (27 hours) |
| **Post-training** | 2B tokens of single-shot function calls (45 minutes) |

The encoder-decoder architecture is notable for what it *leaves out*: there are no feed-forward networks in the encoder. The team found that attention-only encoding with gated residual connections was sufficient for the function-calling task, dramatically reducing parameter count.

> "Needle is an experimental run for Simple Attention Networks, geared at redefining tiny AI for consumer devices — phones, watches, glasses," the team writes in the README.

## Benchmarks: What the Numbers Say

The comparison against established small models is striking:

| Model | Size | Single-shot Function Call Accuracy |
|-------|------|-----------------------------------|
| **Needle (SAN)** | **26M** | **Best** |
| FunctionGemma-270M | 270M | Beaten |
| Qwen-0.6B | 600M | Beaten |
| Granite-350M | 350M | Beaten |
| LFM2.5-350M | 350M | Beaten |

A **10x parameter disadvantage** — yet Needle wins on the narrow task it was designed for. This is the power of extreme distillation combined with architectural minimalism.

On production hardware (Cactus's own inference stack), Needle achieves:
- **6,000 tokens/sec** prefill
- **1,200 tokens/sec** decode

These numbers make it viable for real-time agentic applications where every millisecond counts.

## Why This Matters for AI Agents

Tool calling is the fundamental primitive of the agentic stack. Every time an agent needs to query a database, send an email, edit a file, or call an API, it goes through a function-calling layer. Getting this *right* — and getting it *fast* — has been a bottleneck for on-device agents.

**The on-device implication:** Until now, reliable function calling required either a cloud round-trip (latency, privacy, cost) or a model large enough to be impractical on consumer hardware. Needle changes that. A 26M model:

- Fits in **~50MB of RAM** (FP32) or ~13MB (quantized)
- Runs on a **phone CPU** without a GPU
- Can be **fine-tuned on a laptop** in minutes
- Works on **wearables** — watches, glasses, earbuds

## The Distillation Pipeline

The team used Gemini 3.1 as the teacher model, generating 2 billion tokens of single-shot function-call training data. The dataset covers a wide range of tool schemas — simple single-parameter functions through complex nested-object schemas with optional fields, enums, and arrays.

The post-training step took only 45 minutes on TPU hardware, meaning the distillation pipeline is reproducible enough that others could adapt it to their own tool domains.

## Comparison with Other Tiny Models

Needle isn't the only small model targeting function calling. The landscape includes:

- **[FunctionGemma-270M](https://ai.google.dev/gemma)** — Google's fine-tuned Gemma variant for function calling
- **[Qwen-0.6B](https://github.com/QwenLM/Qwen)** — Alibaba's tiny general-purpose model with tool-calling fine-tunes
- **[Granite-350M](https://www.ibm.com/granite)** — IBM's enterprise-focused small model
- **[LFM2.5-350M](https://www.ibm.com/granite)** — Linux Foundation's AI model

All of these use conventional transformer architectures. Needle's SAN approach is architecturally distinct — and the results suggest that for highly specialized tasks, simpler architectures with better training data can outperform bigger models with generic designs.

## How to Use It

Getting started is straightforward:

```bash
git clone https://github.com/cactus-compute/needle.git
cd needle && source ./setup
needle playground
```

This opens a web UI at `http://127.0.0.1:7860` where you can test and fine-tune on your own tools. Weights are auto-downloaded.

For programmatic use:

```python
from needle import SimpleAttentionNetwork, load_checkpoint, generate, get_tokenizer

params, config = load_checkpoint("checkpoints/needle.pkl")
model = SimpleAttentionNetwork(config)
tokenizer = get_tokenizer()

result = generate(
    model, params, tokenizer,
    query="What's the weather in San Francisco?",
    tools='[{"name":"get_weather","parameters":{"location":"string"}}]',
    stream=False,
)
print(result)
# [{"name":"get_weather","arguments":{"location":"San Francisco"}}]
```

The weights are fully open on [Hugging Face](https://huggingface.co/Cactus-Compute/needle), and the training data generation pipeline is also open-sourced.

## What's Next

The Needle team — Henry Ndubuaku, Jakub Mroz, Karen Mosoyan, Roman Shemet, Parkirat Sandhu, Satyajit Kumar, Noah Cylich, and Justin H. Lee — positions this as an experimental run for Simple Attention Networks. But the results are already production-viable for single-shot function calling.

The implications for the agent ecosystem are clear:

- **Privacy-preserving agents** that do tool routing entirely on-device
- **Ultra-low-latency agent loops** where tool selection happens in microseconds
- **Wearable AI** — the first generation of agentic smart glasses and watches that don't need cloud connectivity for basic function calls
- **Specialized agent chips** — if a 26M model can handle tool routing, it can be embedded in silicon

Needle proves something the AI agent community has suspected for months: **the reasoning doesn't have to be big. It just has to be focused.**

---

*Sources: [Needle on GitHub](https://github.com/cactus-compute/needle), [Hacker News Discussion (423 pts)](https://news.ycombinator.com/item?id=48102954), [Hugging Face Weights](https://huggingface.co/Cactus-Compute/needle), [Cactus Compute](https://github.com/cactus-compute/cactus)*
