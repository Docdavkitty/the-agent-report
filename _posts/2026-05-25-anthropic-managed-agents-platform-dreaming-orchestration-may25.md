---
layout: post
title: "Anthropic's Agent Platform: Dreaming & Multiagent Go GA"
date: 2026-05-25 15:00:00 +0200
last_modified_at: 2026-05-25 15:00:00 +0200
meta_description: "Explore Anthropic's Claude Managed Agents platform going GA with Dreaming self-improvement, multiagent orchestration, and Outcomes validation for autonomous agent workflows."
categories: [industry]
tags: [anthropic, claude, managed-agents, multiagent, dreaming, orchestration, outcomes, sandbox, advisor-model]
reading_time: 6
hero_image: /assets/images/hero/hero-anthropic-managed-agents-platform-dreaming-orchestration-may25.jpg
excerpt: "Anthropic's Claude Managed Agents platform is now generally available with three headline features — Dreaming, multiagent orchestration, and Outcomes — that together represent a step-change in how agents self-improve, collaborate, and validate their own output. Add self-hosted sandboxes, the new Advisor tool, and programmatic tool calling, and the picture is clear: infrastructure, not intelligence, is now the bottleneck."
author: The Agent Report
---

Three weeks after the **Code with Claude 2026** developer conference in San Francisco, Anthropic's agent platform story is snapping into focus — and it's bigger than a model update. The company has shipped a suite of capabilities that fundamentally change what Claude agents can do without human intervention: [self-improvement between runs]({% post_url 2026-05-24-moss-self-evolving-ai-agents-rewrite-code %}), coordinated multi-agent teams, and rubric-driven output validation that sends agents back to revise until they get it right.

## Dreaming: Agents That Learn While You Sleep

The most conceptually ambitious feature is **[Dreaming]({% post_url 2026-05-07-anthropic-managed-agents-dreaming-outcomes %})** — a scheduled process that reviews past agent sessions, identifies patterns, and curates memory for future runs. The name is apt: like biological sleep consolidating memories, Dreaming lets Claude Managed Agents improve between deployments by learning from what worked and what didn't.

In practice, this means an agent deployed on a nightly schedule doesn't start from scratch each run. It carries forward insights, avoids repeating mistakes, and builds institutional knowledge over time. Combined with the newly launched **Memory for Managed Agents** (public beta), which provides filesystem-based persistent memory with audit logs and API control, agents can now accumulate context across sessions in a way that was previously only possible with custom scaffolding.

## Multiagent Orchestration: Divide and Conquer, Natively

The second pillar is **multiagent orchestration**. A lead agent can now delegate to specialist sub-agents working in parallel on a shared filesystem — each with its own model, prompt, and tool set. Full traceability is preserved in the Claude Console, addressing one of the hardest problems in multi-agent systems: observability.

This isn't just a convenience feature. The architectural pattern mirrors what GitHub, Vercel, and Cognition described on stage at Code with Claude: splitting exploration from editing, using smaller models for routine tasks and larger ones for hard decisions. Anthropic's own **advisor tool** — now in public beta on the API — formalizes this: a Haiku-level executor handles the bulk of work, calling a more expensive Opus-level advisor only when strategic guidance is needed. GitHub's Mario Rodriguez called the approach "high-frequency trading for tokens," targeting cache-hit rates above 94%.

This native multi-agent architecture differs from frameworks like CrewAI or LangGraph, which require explicit coordination logic in code. Anthropic embeds the pattern at the platform level — agents discover, delegate, and report back automatically, with full traceability through the Claude Console. For teams already in the Anthropic ecosystem, this dramatically reduces the operational overhead of multi-agent setups.

## Outcomes: The Agent That Grades Itself

**Outcomes** is the third piece, and arguably the most practical for production teams. You define a rubric; a separate grader model evaluates the agent's output against it. If the result doesn't meet the bar, the grader sends the agent back to revise — iterating until the standard is met. Anthropic's internal benchmarks show a **+10 point improvement on task success rates** for the hardest problems when Outcomes is enabled.

This is agentic quality control at the platform level. It shifts the developer's role from debugging individual failures to defining what "good" looks like.

## Beyond the Headlines: Sandboxes, Tunnels, and Programmatic Tool Calling

The platform story extends beyond the three headline features. On **May 19**, Anthropic shipped **self-hosted sandboxes** (public beta) and **MCP tunnels** (research preview). Self-hosted sandboxes let enterprises run tool execution on their own infrastructure — Cloudflare, Daytona, Modal, and Vercel are launch partners — while MCP tunnels connect agents to internal databases and APIs through a single outbound connection, no inbound firewall rules required.

Meanwhile, **programmatic tool calling** has graduated to general availability. Instead of round-tripping each tool call through the model, Claude now writes Python scripts inside its code execution sandbox that orchestrate all tools in a single pass. Results from early adopters show **37% fewer tokens consumed** and significantly lower latency for multi-step workflows.

## The Bigger Picture: 80× Revenue Growth and the Infrastructure Bottleneck

Anthropic disclosed at Code with Claude that Q1 2026 revenue grew **80×** on an annualized basis against a planned 10×, reaching $30 billion annualized. [Usage-based pricing]({% post_url 2026-05-26-anthropic-claude-agent-credits-metered-pricing %}) is driving consumption so aggressively that enterprise customers are exhausting token budgets within months.

But the most telling line came from Jess Yan and Lance Martin's Managed Agents session: **"Infrastructure, not intelligence, is now the bottleneck for production agents."** Every feature in this wave — Dreaming, multiagent orchestration, Outcomes, self-hosted sandboxes, MCP tunnels — addresses that exact bottleneck. It's no longer about whether the model is smart enough; it's about whether the platform can run it safely, reliably, and economically at scale.

Dario Amodei reiterated his prediction that a **one-person billion-dollar company** will appear in 2026. Two-person AI-powered companies have already crossed $1B valuations. With the platform layer maturing this fast, the prediction is starting to look conservative.

---

*Sources: [Anthropic Code with Claude SF 2026 recap](https://claude.com/blog/code-w-claude-sf-2026-sf), [Claude Managed Agents updates](https://claude.com/blog/claude-managed-agents-updates), [InfoQ coverage](https://www.infoq.com/news/2026/05/code-with-claude), [Claude API Docs — Advisor Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool), [Programmatic Tool Calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)*
