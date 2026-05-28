---
layout: post
title: "LLMs Corrupt Your Documents When You Delegate — Inside the DELEGATE-52 Study"
date: 2026-05-10 08:00:00 +0200
last_modified_at: 2026-05-10 08:00:00 +0200
meta_description: "Frontier models silently corrupt ~25% of document content during long delegation workflows, per a new benchmark. Serious implications for the vibe coding era."
categories: research
tags: safety delegation document-integrity trust research
reading_time: 7
excerpt: "A new benchmark reveals that even frontier models like Gemini 3.1 Pro, Claude 4.6 Opus, and GPT 5.4 silently corrupt ~25% of document content during long delegation workflows. The findings have serious implications for the 'vibe coding' era."
hero_image: /assets/images/hero/hero-llms-corrupt-documents-delegation.jpg
author: The Agent Report
---

A new paper dropped on arXiv this week titled **"LLMs Corrupt Your Documents When You Delegate"** — and its findings are as disturbing as the title suggests. The researchers introduce **DELEGATE-52**, a benchmark spanning 52 professional domains, and discover that even the best frontier models systematically degrade documents during long delegated workflows.

The punchline: **Frontier models corrupt an average of 25% of document content** by the end of extended interactions. Not edge cases. Not toy tasks. Real documents across coding, crystallography, and music notation.

## The DELEGATE-52 Benchmark

The research team — Laban, Schnabel, and Neville — designed DELEGATE-52 to simulate what they call the **"delegated work" paradigm**. This is the interaction pattern where you ask an LLM to *do something* in a document rather than just *answer a question*. If you've ever asked an AI agent to "refactor this file," "update this spreadsheet," or "edit this research paper," you've used delegation.

The benchmark covers **52 professional domains**, including:

- **Software engineering** — code refactoring, bug fixing, test generation
- **Crystallography** — structure data editing
- **Music notation** — score transcription and arrangement
- **Legal documents** — contract clause modification
- **Medical records** — patient data formatting
- **Scientific papers** — citation management, figure descriptions

Each task requires **long, multi-step document editing workflows** — exactly the kind of thing AI agents are being marketed to do — as documented in our [complete guide to AI agents in 2026]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %}).

## The Results: Systematic Degradation

The key finding is stark: **every model tested causes document degradation over time**. The corruption is not random — it's *systematic* and *compounding*.

| Model | Document Corruption Rate |
|-------|------------------------|
| **Gemini 3.1 Pro** | ~25% |
| **Claude 4.6 Opus** | ~25% |
| **GPT 5.4** | ~25% |
| Other models | Worse — up to 60%+ |

What does "corruption" look like? The paper identifies several failure modes:

1. **Sparse but severe errors** — A single incorrect edit that cascades
2. **Silent deletions** — Entire paragraphs or code blocks removed without notice
3. **Format corruption** — Document structure (headings, indentation, markup) degraded
4. **Semantic drift** — Content gradually shifted away from intended meaning
5. **Cross-document contamination** — Information leaking between distractor files

The researchers note that degradation is **exacerbated** by:
- **Document size** — larger documents suffer more
- **Length of interaction** — more steps = more corruption
- **Presence of distractor files** — irrelevant files in the context window increase error rates

## Why Agentic Tool Use Doesn't Help

Perhaps the most concerning finding: **agentic tool use does not improve performance — a finding that complicates the [state of agent engineering]({% post_url 2026-05-23-state-of-agent-engineering-2026-langchain-datadog %}) narrative on DELEGATE-52**.

This contradicts the prevailing wisdom that giving agents tools (search, edit, read) makes them more reliable. The paper's experiments show that even with tool access, models still introduce errors at roughly the same rate. The problem isn't tooling — it's fundamental to how LLMs process and regenerate document content.

> *"Agentic tool use does not improve performance on DELEGATE-52, and degradation severity is exacerbated by document size, length of interaction, or presence of distractor files."*

This has profound implications for the entire "agentic coding" movement. If giving an agent more tools doesn't fix document corruption, then the reliability bottleneck is in the model itself — not the scaffolding around it.

## What This Means for "Vibe Coding"

The paper explicitly calls out **vibe coding** (the practice of letting AI agents write and modify code autonomously) as a use case that demands trust. Trust that the agent will faithfully execute the task without introducing errors.

The DELEGATE-52 results suggest that trust is currently **misplaced**.

For developers using Claude Code, Codex, or Cursor in autonomous mode, the implication is clear: **you cannot rely on agents to maintain document integrity over long sessions**. Every multi-step edit carries a ~25% chance of silently corrupting something.

This connects directly to tools like [re_gent](https://github.com/regent-vcs/re_gent) — the "Git for AI Agents" that launched on HN the same week — which provide step-level audit trails precisely because agents are unreliable delegates.

## The Research Methodology

The team tested 19 LLMs across the 52-domain benchmark. Each task involved:

1. A source document in a professional format (code, LaTeX, spreadsheet, structured data)
2. A series of edit instructions (e.g., "add error handling to the request handler")
3. Automated comparison of input vs. output documents
4. Human validation of detected corruptions

The corruption metric measured **content-level changes** that deviated from the instructions — not just formatting differences, but actual semantic or structural errors introduced by the model.

## Implications for the Agent Ecosystem

DELEGATE-52 arrives at a critical moment for the AI agent industry. Here's what it means for different stakeholders:

### For Agent Framework Builders

The message is: **don't assume your model backend is reliable**. Build guardrails, diff-checkers, and rollback mechanisms into your agent frameworks. Every edit should be reviewed before acceptance.

### For Enterprise Deployments

If you're deploying agents in regulated industries (finance, healthcare, legal), DELEGATE-52 is a **red alert**. A 25% corruption rate on document edits is unacceptable for any production system. You need:
- Human-in-the-loop verification
- Automated integrity checks after every agent edit
- Full audit trails (see re_gent above)

### For Model Developers

The paper is a challenge to Frontier AI labs: **delegation reliability is now a benchmark**. If your model can't maintain document integrity over 10+ steps, it's not ready for autonomous agentic use.

### For Individual Developers

**Always review agent output.** Especially in long sessions. Consider using version control tools (Git, or agent-specific ones like re_gent) to track every change. When an agent says "I refactored the module," verify that it actually did what you asked.

## Looking Ahead

DELEGATE-52 is a wake-up call. The "vibe coding" era promised productivity gains from delegation — but delegation requires trust, and trust requires reliability. Current models don't deliver it.

The good news is that this is now a **measurable problem** with a **benchmark** to track progress. Future models will be evaluated on DELEGATE-52, and the 25% corruption rate will (hopefully) drop over time.

Until then: trust, but verify. And back up your documents.

---

*Paper: ["LLMs Corrupt Your Documents When You Delegate"](https://arxiv.org/abs/2604.15597) — Laban, Schnabel, Neville. arXiv:2604.15597.*
