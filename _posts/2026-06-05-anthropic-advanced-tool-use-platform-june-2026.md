---
layout: post
title: "Anthropic's Advanced Tool Use Platform: Programmatic Calling, Advisor Strategy, and the Future of Claude Agents"
date: 2026-06-05 16:00:00 +0200
last_modified_at: 2026-06-05 16:00:00 +0200
author: The Agent Report
categories: [research]
tags: [anthropic, claude, tool-use, agent-infrastructure, api]
description: "Anthropic ships a new wave of agent infrastructure — Programmatic Tool Calling, the Advisor Strategy, Tool Search, Files API, and MCP Connector — redefining how developers build Claude-powered agents."
reading_time: 8
hero_image: /assets/images/hero/hero-anthropic-advanced-tool-use-platform-june-2026.jpg
excerpt: "Anthropic has quietly shipped one of its most consequential developer platform updates to date. Programmatic Tool Calling, the Advisor Strategy, Tool Search, the Files API, and the MCP Connector are now available in public beta — fundamentally changing how Claude agents reason about tools, manage context, and orchestrate complex workflows."
meta_description: "Anthropic has quietly shipped one of its most consequential developer platform updates to date."
---

Anthropic has quietly shipped one of its most consequential developer platform updates to date. Over the past several weeks, a suite of new agent-infrastructure features has moved from research previews into **public beta**: **Programmatic Tool Calling**, the **Advisor Strategy**, **Tool Search**, the **Files API**, and the **MCP Connector**. Combined with the 1M-token context window now available on Claude Sonnet 4, these capabilities fundamentally change how developers build Claude-powered agents.

This isn't just a point-release. It's a new architectural paradigm for tool-use at scale.

## The Context Bloat Crisis — and How Anthropic Solved It

Any developer who has built a serious agent with tool-calling knows the pain. Hook up five MCP servers — Jira, GitHub, Google Drive, Slack, and a database — and you're looking at **50,000+ tokens of tool definitions** before the first real user message is processed. With a 200K context, that leaves only ~150K for actual work. With Opus 4.8's default 1M context the problem is less acute, but the *cost* of that bloat remains: every token costs, and every tool result dumped back into context makes the model's job harder.

Anthropic's solution is a **three-pronged attack** on context pollution.

### 1. Tool Search — Deferred Loading for Massive Tool Libraries

The [Tool Search Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) lets you mark the vast majority of your tools with `defer_loading: true`. Only a lightweight search tool (~500 tokens) is loaded upfront. Tools are discovered on-demand via regex, BM25, or custom search.

**The numbers are striking:**

| Approach | Tokens Consumed Before Work | Context Preserved |
|----------|---------------------------|-------------------|
| Traditional (all tools upfront) | ~77K tokens | ~23K (for a 100K window) |
| Tool Search Tool | ~8.7K tokens | **~91K (95% preserved)** |

On Anthropic's internal MCP evaluations, accuracy jumped from **49% to 74%** for Opus 4, and from **79.5% to 88.1%** for Opus 4.5. For agents with 10+ tools or multiple MCP servers, this is essentially mandatory infrastructure.

### 2. Programmatic Tool Calling — Orchestration Inside the Sandbox

[Programmatic Tool Calling (PTC)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) is arguably the most innovative of the new features. Instead of Claude requesting tools one at a time via API round-trips (each requiring a full model pass), Claude writes **Python orchestration code** that calls your tools from within a code execution sandbox.

A real-world example from Anthropic's documentation illustrates the power:

> Checking budget compliance across 20 employees traditionally requires **20 separate model round-trips** and pulls thousands of expense line items into context. With PTC, a single script runs all 20 lookups in parallel, filters results, and returns only the four employees who exceeded their limits — shrinking what Claude needs to reason over from hundreds of kilobytes to a handful of lines.

**Efficiency gains from internal benchmarks:**

| Metric | Without PTC | With PTC |
|--------|------------|----------|
| Average tokens consumed | 43,588 | 27,297 (**-37%**) |
| Internal knowledge retrieval | 25.6% | 28.5% |
| General intelligent agent (GIA) benchmarks | 46.5% | 51.2% |

PTC is especially transformative for three patterns:
- **Large data aggregation**: filter/aggregate billions of rows before Claude sees any
- **Multi-step dependent workflows**: call tools in loops, with conditional branching
- **Parallel operations**: fan out 50 API calls simultaneously

The feature requires the `code_execution` tool and is available on all Opus 4.5+ and Sonnet 4.5+ models.

### 3. Advisor Strategy — Dual-Model Intelligence Without the Orchestration Tax

The [Advisor Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) implements a pattern that agent architects have wanted for years: pair a **fast, cheap executor model** (Sonnet 4.6 or Haiku 4.5) with a **high-intelligence advisor model** (Opus 4.8) — all inside a single API call.

When the executor hits a complex decision point, it emits a `server_tool_use` block. The server transparently runs a separate inference pass on the advisor model, passing the full conversation transcript. The advisor produces a plan (typically 400–700 text tokens with ~1,400 total including thinking), and the executor continues, informed by the advice.

**Architecture flow:**

```
Executor (Sonnet 4.6) → hits complex decision
  → emits advisor tool signal
    → Server runs Opus 4.8 on full transcript
      → Advisor returns plan (400-700 tokens)
        → Executor continues with advice
```

The result: near-Opus quality on the hard decisions, while the bulk of generation happens at Sonnet rates. The advisor model is **billed separately** at its own rate, but because it's only invoked on the hard turns, the total cost is often lower than running Opus as executor end-to-end.

**Supported executor + advisor pairs:**

| Executor | Available Advisors |
|----------|-------------------|
| Haiku 4.5 | Opus 4.7, Opus 4.8 |
| Sonnet 4.6 | Opus 4.7, Opus 4.8 |
| Opus 4.6 | Opus 4.7, Opus 4.8 |
| Opus 4.7 | Opus 4.8 |
| Opus 4.8 | Opus 4.8 |

## Files API and MCP Connector — Extending the Reach

Two additional features round out the platform update:

**The Files API** (public beta) lets you upload files and reference them in the Messages API and code execution tool. Instead of base64-encoding large documents into messages, you upload once and reference by ID. This is a significant quality-of-life improvement for document-heavy workflows.

**The MCP Connector** (public beta) allows connecting to remote MCP servers directly from the Messages API — no need for a separate MCP client or proxy. Combined with the Tool Search, this makes it practical to offer agents access to dozens of external services without blowing through token limits.

## 1M Context Window — Now on Sonnet 4

Anthropic also made the **1M-token context window** available in beta for Claude Sonnet 4 on both the API and Amazon Bedrock. While Opus 4.8 already defaults to 1M, bringing it to the Sonnet tier means that cost-sensitive developers can now handle entire codebases, book-length documents, or multi-hour conversation histories without breaking the bank.

## What This Means for Agent Developers

Taken together, these features represent a coherent platform vision:

1. **Context is expensive** — defer it, filter it, and keep it out of the model until it's needed (Tool Search, PTC)
2. **Intelligence is expensive** — use a cheap executor by default; call in the heavy artillery only when the problem demands it (Advisor Strategy)
3. **Integration shouldn't be** — connect to any MCP server directly from the API; reference files without encoding gymnastics (MCP Connector, Files API)

For developers building production agents, the path is clear. The era of jamming every tool definition into a single model call and hoping for the best is over. Anthropic has built the infrastructure for **surgical, cost-aware, context-efficient agent architecture** — and it's all available in public beta today.

## Getting Started

All features are available on the [Claude API](https://platform.claude.com/docs/en/release-notes/overview) and Claude Platform on AWS. Programmatic Tool Calling and the Advisor Tool require beta headers (`code_execution_20260120` and `advisor-tool-2026-03-01` respectively). The Files API, MCP Connector, and Tool Search are also in public beta.

As always, check the [Claude API documentation](https://platform.claude.com/docs/en/home) for the latest compatibility matrix, pricing, and migration guides.
