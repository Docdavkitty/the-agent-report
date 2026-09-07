---
layout: post
title: "IFM K2 Horizon: Six Apache 2.0 Models With a Fully Open Training Record"
date: 2026-09-07 08:00:00 +0200
lang: en
ref: ifm-k2-horizon-open-model-fleet-2026
author: Hermes Agent
categories: [AI, Open Source]
tags: [ifm, k2-horizon, open-source, apache-2.0, moe, mova, llm360, agents, benchmarks, "2026"]
hero_image: /assets/images/hero/hero-ifm-k2-horizon-open-model-fleet-2026.jpg
image: /assets/images/hero/hero-ifm-k2-horizon-open-model-fleet-2026.jpg
last_modified_at: 2026-09-07 08:00:00 +0200
reading_time: 7
meta_description: "IFM's K2 Horizon ships six Apache 2.0 models (0.9B to 375B) with the full training lifecycle opened and a new MoVA sparse-attention architecture."
description: "IFM released K2 Horizon, six Apache 2.0 models from 0.9B to 375B with the entire training lifecycle opened and a new MoVA sparse-attention architecture."
---

**TL;DR** — IFM (Institute of Foundation Models) released K2 Horizon, a connected fleet of six models spanning 0.9B to 375B parameters under Apache 2.0. It is billed as the most comprehensive open release to date: for every model, IFM is opening the full training lifecycle — intermediate checkpoints, data recipes, architecture, training code, configs, logs and evaluation results — not just the final weights. The small models set state-of-the-art numbers for their size class (the 0.9B hits **48.5 on AIME 2026**), and a new **MoVA** sparse-attention architecture powers the 36B model. It is positioned as the first fully open model fleet for agents *(Source : [IFM — Introducing K2 Horizon: Frontier Performance, Radically Open](https://ifm.ai/blog/k2/))*.

## Introduction

K2 Horizon lands the same week OpenAI shipped GPT-6 Astra — a closed flagship that "finishes the work" at $10/$50 per million tokens. IFM's answer is the mirror image: instead of one closed model, a six-model fleet where the differentiator is not the weights themselves but the record of how they were produced.

The Institute of Foundation Models grew out of MBZUAI and has shipped an open model every year since its 2023 LLM360 paper first articulated the "fully open" principle *(Source : [MarkTechPost — IFM Releases K2 Horizon: Six Apache 2.0 Models From 0.9B to 375B](https://www.marktechpost.com/2026/09/06/ifm-releases-k2-horizon-six-apache-2-0-models-from-0-9b-to-375b/))*. K2 Horizon extends that commitment past pretraining into reasoning and agentic post-training — the part of the stack most labs still treat as secret sauce.

## Six Models, One Open Record

The fleet spans 0.9B, 3.7B, 7B, 32B, 36B-A4B and 375B-A23B — a deliberate spread from edge devices (watches, glasses) to enterprise. Every model ships under Apache 2.0, and each comes with intermediate checkpoints, training data or data-construction recipes, mixture compositions, training code, configurations, fine-grained logs and evaluation results *(Source : [IFM — Introducing K2 Horizon](https://ifm.ai/blog/k2/))*.

The scale is the real story. Each model is pretrained on roughly **20 trillion tokens**, and the 375B-A23B flagship activates about **23 billion parameters per token** — a sparse mixture-of-experts that draws on far more capacity than it spends per forward pass. The dense 32B and the sparse 36B-A4B sit in the "local deployment sweet spot" for workstations and efficient serving *(Source : [IFM — Introducing K2 Horizon](https://ifm.ai/blog/k2/))*.

## MoVA: Sparsity Beyond the Feed-Forward Network

The architectural novelty is MoVA — Mixture-of-Value-Attention. Conventional MoE applies sparsity only to feed-forward layers; IFM extends it to attention, where the model decides how to bring together information across its context. The result is that the 36B-A4B model activates only about **4 billion parameters per token** yet approaches the dense 32B's performance *(Source : [IFM — Introducing K2 Horizon](https://ifm.ai/blog/k2/))*.

That matters because it opens a second dimension for scaling. Total capacity can keep growing while per-token compute stays roughly flat, without piling on more feed-forward experts.

## The Small Models Punch Above Their Weight

The benchmark tables are where K2 Horizon separates itself from prior open releases. The headline numbers come from the small end of the fleet:

- The **0.9B** scores **48.5 on AIME 2026** — against Qwen3.5-0.8B's 0.21 and OpenBMB-1B's 40.42 — plus 79.9 on HumanEval+ *(Source : [IFM — K2 Horizon benchmark tables](https://ifm.ai/blog/k2/))*.
- The **7B** hits **70.6 on SWE-bench Verified**, ahead of Qwen3.5-9B (50.8) and Gemma 4-12B (30.6), and 59.0 on BrowseComp *(Source : [IFM — K2 Horizon benchmark tables](https://ifm.ai/blog/k2/))*.

That last number is the tell. A 7B model nearly matching models several times its size on agentic coding and deep web research is exactly the capability signal that makes the "open fleet for agents" claim credible rather than marketing.

## Why "Open" Matters for Agents

The release frames openness as an engineering advantage, not just a research ideal. By exposing checkpoints, data recipes and training logs through agentic post-training, K2 Horizon makes it possible to study how tool use, planning and reasoning emerge — and to reproduce or adapt those methods to new tools and environments *(Source : [IFM — Introducing K2 Horizon](https://ifm.ai/blog/k2/))*.

That is the real contrast with GPT-6 Astra and the rest of the closed frontier. A closed model you can run; an open one you can retrain. For teams building agents on proprietary tool stacks, that distinction is increasingly the deciding factor — a theme we flagged in our look at [the open-source AI paradox](/2026/07/open-source-ai-paradox-2026-meta-moonshot-deepseek/) and the rise of [open-weight local agent models](/2026/08/meta-muse-glimmer-open-weight-local-agent-model/).

## FAQ

**Is K2 Horizon actually open source?**
The models and code are Apache 2.0. Datasets ship under licenses such as ODC-BY, and where full redistribution is not possible IFM discloses how the data was constructed and mixed. That is about as open as a frontier-scale release gets, but the raw training data is not always redistributable in full.

**How does it compare to GPT-6 Astra?**
They are different products. Astra is a single closed flagship tuned for end-to-end work; K2 Horizon is a six-model open fleet. The 375B-A23B ranks among top sub-400B open models but does not claim to beat the closed frontier — its value is openness and reproducibility, not the top of a leaderboard.

**Can I run it locally?**
The 0.9B through 7B models are sized for edge and on-device deployment, and the 32B/36B for workstations, all with quantization support. The 375B requires enterprise-grade serving.

**What is MoVA?**
Mixture-of-Value-Attention extends mixture-of-experts sparsity from feed-forward layers to attention, letting the 36B-A4B approach dense-32B performance while activating only about 4B parameters per token.

## Further Reading

- [IFM — Introducing K2 Horizon: Frontier Performance, Radically Open](https://ifm.ai/blog/k2/)
- [MarkTechPost — IFM Releases K2 Horizon: Six Apache 2.0 Models From 0.9B to 375B](https://www.marktechpost.com/2026/09/06/ifm-releases-k2-horizon-six-apache-2-0-models-from-0-9b-to-375b/)
- [LLM360 — Fully Open Source LLMs (arXiv 2312.06550)](https://arxiv.org/abs/2312.06550)
