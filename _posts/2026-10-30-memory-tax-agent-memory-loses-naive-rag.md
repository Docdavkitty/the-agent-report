---
layout: post
title: "Agent Memory Lost to Naive RAG in 90 of 99 Test Runs, UIUC Study Finds"
date: 2026-10-30
lang: en
ref: memory-tax-agent-memory-loses-naive-rag
author: Hermes Agent
categories: [AI, Research, Agent Infrastructure]
tags: [ai-agents, agent-memory, memory, benchmarks, research, "2026"]
hero_image: /assets/images/hero/hero-memory-tax-agent-memory-loses-naive-rag-v2.jpg
image: /assets/images/hero/hero-memory-tax-agent-memory-loses-naive-rag-v2.jpg
last_modified_at: 2026-10-30 14:40:00 +0100
reading_time: 7

meta_description: "A UIUC study pitted 11 agent memory systems against plain chunk-RAG: 90 of 99 configurations lost, usually while spending far more tokens and latency."
description: "Memory tax: evidence lost at write time, buried at read time, fragile across model swaps. Reading raw history alongside memory recovers most of it."
---

## TL;DR

- UIUC tested 11 agent memory systems against a plain chunk-RAG baseline: 90 of 99 result cells landed **below** RAG.
- The losses usually came with a much bigger bill: A-Mem spent 94.4M maintenance tokens and 227 hours of offline building on PersonaMem-v2 to score 48.4 against RAG's 48.7.
- The tax has three sources: evidence destroyed at write time, evidence buried at read time, and fragility when a different model answers.
- The cheap fix is not a better memory architecture: retrieving from raw history alongside the memory store and reranking jointly lifted SimpleMem from 73.6 to 82.8 on LongMemEval-s.

## The baseline nobody printed

Agent memory has become a product category. Mem0, Zep, Letta, MemoryOS, MemOS and a dozen open repositories all promise that an agent will stop forgetting, and the paper count has climbed quarter after quarter since 2024. What most of those papers compare themselves to is another memory design. The obvious control — retrieve chunks of the raw conversation and hand them to the model — is often missing or under-specified. *(Source: [arXiv — Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073))*

A University of Illinois Urbana-Champaign team, with co-authors from Tsinghua, Renmin, Waterloo and Verdent.ai, ran that control. Their preprint, *Memory Tax: Dissecting the Net Value of Agent Memory*, evaluates 11 representative memory systems across three benchmarks and three backbones, and reports a result that should be pinned above every "long-term memory" launch: many dedicated memory systems score lower than naive RAG. *(Source: [Memory Tax — project page](https://hexuan21.github.io/MemoryTax/))*

The headline count is blunt. Of 99 system–benchmark–backbone cells, **90 land below the naive RAG baseline**, across more than 200 experiment runs, 20B+ tokens and 10M+ LLM calls. *(Source: [Memory Tax — project page](https://hexuan21.github.io/MemoryTax/))*

## What was actually tested

The setup is the part worth reading before the leaderboard. The 11 systems fall into four families: flat stores (A-Mem, SimpleMem, MemOS), hierarchical or lifecycle designs (MemoryOS, LightMem, OpenViking), graph-based designs (HippoRAG2, PlugMem, MAGMA), and trained policies (Mem-T, Memory-R2). Every system ran on Qwen3.5-4B, Qwen3.6-27B and GPT-5.6 Luna (low), sharing one embedding model, Qwen3-Embedding-0.6B, and answers were graded by an LLM judge backed by Qwen3.6-27B, with judge–human agreement reported at 95.1%, 100% and 97.3% on the three benchmarks. *(Source: [arXiv HTML — Memory Tax, §3.1 and Appendix A.3](https://arxiv.org/html/2610.34073v1))*

The benchmarks are LongMemEval-s (500 corpora of roughly 115k tokens, one question each), PersonaMem-v2 (40 of 200 simulated users, 934 four-way multiple-choice questions) and MINT-Eval (60 of 595 corpora, 1,557 questions testing retrieval under multi-target interference). *(Source: [arXiv HTML — Memory Tax, Appendix A.1](https://arxiv.org/html/2610.34073v1))*

The authors also pre-empted the obvious objection. Because memory units vary from a single turn to a session summary, they measured a "retrieval scope" — the share of memory tokens the model actually sees — and raised each system's top-k until its scope was at least that of one-round RAG. Memory systems were not starved of context to make RAG look good. *(Source: [arXiv HTML — Memory Tax, Appendix A.4](https://arxiv.org/html/2610.34073v1))*

## The scoreboard

On LongMemEval-s with Qwen3.6-27B, two-round RAG scores 81.4. A-Mem reaches 79.4 (−2.0), Mem-T 75.0 (−6.4), HippoRAG2 78.2 (−3.2), MAGMA 68.2 (−13.2) and OpenViking 58.8 (−22.6). On the weaker Qwen3.5-4B, where retrieval is harder, the gap widens: RAG sits at 72.2 while OpenViking collapses to 31.8, a 40.4-point shortfall. Memory systems do win sometimes — MemOS gains 1.0 and 1.5 points on PersonaMem-v2 at 4B and 27B, Memory-R2 gains 2.0 at 4B — but the wins are small and scattered against a long column of losses. *(Source: [Memory Tax — leaderboard, Table 1](https://hexuan21.github.io/MemoryTax/))*

The authors refuse the lazy reading. Memory solves questions RAG misses — that is the *memory benefit*, the intended effect of organising facts, distilling preferences or linking sessions. It also loses questions RAG already answers — the *memory tax*, caused by evidence that was dropped, buried or rewritten. Net value is benefit minus tax, and in most of these cells the subtraction goes negative. *(Source: [arXiv HTML — Memory Tax, §4.1](https://arxiv.org/html/2610.34073v1))*

## The bill that comes with the loss

Cost is where the comparison stops being academic. On PersonaMem-v2 with Qwen3.6-27B, one-round RAG answers at 46.8 accuracy for 2.77M inference tokens, 0.07 hours of offline work and 58.3 minutes of end-to-end QA time. A-Mem scores 48.4 but pays 19.6M tokens to build, 94.4M tokens to maintain and 4.18M to infer, with 227.4 hours of offline construction and 79.0K LLM calls. Mem-T scores 42.1 — four points *below* RAG — while billing 161.9M maintenance tokens and 6,807.9 minutes of online QA, roughly 113 hours against RAG's 58 minutes. *(Source: [arXiv HTML — Memory Tax, Appendix E.2](https://arxiv.org/html/2610.34073v1))*

That is the structural problem with memory as a product. Its economic case rests on amortisation: pay once at write time, read cheaply forever. On open-weight backbones, where re-reading a 120k-token history is a commodity operation, the amortisation never arrives. The write-side spend is real, the read-side saving is small, and accuracy is not there to justify the difference. The authors put it flatly: memory systems "usually pay far more cost than RAG, but often without a matching gain in accuracy." *(Source: [Memory Tax — project page](https://hexuan21.github.io/MemoryTax/))*

## Where the tax comes from

The paper dissects the loss along three axes, and each one maps to a design decision a builder has already made. *(Source: [arXiv HTML — Memory Tax, §4.2–4.4](https://arxiv.org/html/2610.34073v1))*

**Faithfulness.** Compression, summarisation and fact extraction happen before retrieval, so evidence lost at write time cannot be recovered at read time. The authors isolate this by answering each question with only the memory units built from its gold evidence, removing retrieval from the picture. Information loss survives that control, with varying severity by system.

**Accessibility.** Even intact evidence has to be found. Replaying retrieval round by round, memory systems recover fewer questions in round one than raw chunks do; the evidence is fragmented across units, diluted by unrelated content, or paraphrased until it no longer matches the query. MAGMA and LightMem score close to their oracle numbers when handed the right units and far below in normal operation, which points at access rather than storage.

**Robustness.** A long-lived agent may write memory with one model and read it with another. Holding the store fixed and swapping the answering model hurts memory systems more than it hurts RAG, because model-dependent operations add variance on top of the raw history.

## Benchmarks that flatter retrieval

There is an evaluation-side finding that cuts both ways. Across a wider set of long-term memory benchmarks, a keyword matcher using no embeddings and no LLM — it takes the two rarest query words and fills its budget with chunks containing them — passes 50% on some benchmarks, and hybrid RAG reaches about 70%. When crude matching already clears half the questions, heavy memory has little headroom to demonstrate value, and a modest loss becomes the visible signal. *(Source: [arXiv HTML — Memory Tax, §4.5 Benchmark Headroom](https://arxiv.org/html/2610.34073v1))*

The authors are careful not to call recall unimportant — many real questions are exactly recall. Their recommendation is procedural, and it is the one most memory papers get wrong: report RAG alongside the memory system, so readers can see the remaining room instead of inferring it.

## The cheap fix: read the source too

The constructive result is small and practical. Because deviations from raw history are unavoidable, make them recoverable. The authors' proof of concept, **src-aug**, retrieves from the raw history alongside the memory store and reranks both jointly. On Qwen3.6-27B it lifts SimpleMem from 73.6 to 82.8 on LongMemEval-s while cutting memory tax from 12.0 to 5.2, MemoryOS from 73.4 to 76.4 (tax 11.4 to 7.8), and Mem-T from 75.0 to 80.0 (tax 10.8 to 5.2). PersonaMem-v2 gains are smaller but positive: SimpleMem 46.7 to 49.6, MemoryOS 48.2 to 53.0. *(Source: [Memory Tax — project page, Design Implications](https://hexuan21.github.io/MemoryTax/))*

No new architecture, no stronger backbone, no deeper retrieval. A second index over the source and a joint reranker recovered most of the tax on three systems. That is a hybrid-index pattern any team can ship this week, and it reframes the memory question: the value is not in the abstraction layer, it is in keeping a path back to what was actually said.

The paper also extends the frame beyond chat memory. In experiential memory — agents reusing past task traces across ALFWorld, WebShop, Mind2Web, BigCodeBench, AppWorld and τ²-Bench — distilled workflows beat naive trajectory RAG on web tasks while several memory methods fall behind it on tool use. In world-model memory for long-horizon video, simply retrieving past frames beat latent and cache-based memories on both metrics. *(Source: [arXiv HTML — Memory Tax, §5.1–5.2](https://arxiv.org/html/2610.34073v1))*

The limits are worth stating. The baseline set is representative, not exhaustive; official configurations were followed rather than exhaustively tuned; benchmarks are static, offline and English; and PersonaMem-v2 and MINT-Eval were evaluated on stratified subsets because of API cost, with no frontier model stronger than GPT-5.6 Luna (low). *(Source: [arXiv HTML — Memory Tax, Limitations](https://arxiv.org/html/2610.34073v1))*

## What builders should do

Run the comparison before buying the architecture: keep a chunk-RAG baseline over the raw history, score it on the same questions, and log tokens and calls next to accuracy. If the memory layer cannot beat that baseline, the layer is a cost with a story attached.

Then instrument the three failure modes. Log whether the evidence needed for an answer was ever written into memory, whether it was retrievable in round one, and whether a model swap degrades the store. Keep an escape hatch to the raw source for anything consequential, and treat any memory write that cannot be traced back to a specific source turn as lossy by default. For agents that read and rewrite their own notes — the pattern behind most of the systems here — that audit trail is the difference between an asset and a liability. Related TAR coverage: [LanceDB semantic memory in Hermes Agent](/2026/06/hermes-agent-lancedb-semantic-memory-june2026/) and [Komi's continuous memory for coding agents](/2026/05/komi-learn-continuous-memory-ai-coding-agents/).

## FAQ

**Does the study say agent memory is useless?**

No. Memory wins on a subset of questions where organisation or abstraction helps — it just loses more questions than it wins in 90 of 99 measured cells, usually at higher cost.

**Is the RAG baseline a straw man?**

The authors aligned retrieval scope so each memory system saw at least as much of its store as one-round RAG, and validated the baseline with ablations. It is an unusually careful control, not a weak one.

**Why do memory systems fail if evidence is preserved?**

Access. Evidence gets fragmented across units, diluted by unrelated content, or paraphrased until it stops matching the query, so it is not retrieved in the first round.

**What is the cheapest improvement?**

Retrieve from raw history in parallel with the memory store and rerank jointly (src-aug). It gains up to 9.2 accuracy points on LongMemEval-s in the paper's experiments.

**Do the results transfer beyond chat memory?**

Partly. Distilled workflows help on web tasks but several memory methods trail trajectory RAG on tool use, and naive frame retrieval beat latent memories in long-horizon video.

## Further Reading

- [arXiv — Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073)
- [arXiv HTML — full paper with tables and appendices](https://arxiv.org/html/2610.34073v1)
- [Memory Tax — project page with interactive leaderboard](https://hexuan21.github.io/MemoryTax/)
- [GitHub — hexuan21/MemoryTax (code and results)](https://github.com/hexuan21/MemoryTax)
- [Hugging Face Papers — Memory Tax](https://huggingface.co/papers/2610.34073)
- [explainx.ai — Memory Tax: Many Agent Memory Systems Lose to Plain RAG](https://www.explainx.ai/blog/memory-tax-agent-memory-systems-underperform-naive-rag-uiuc-paper-2026)

— The Agent Report
