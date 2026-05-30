---
layout: post
title: "MCP Is Dead? A Deep Dive Into Why Developers Are Questioning the Model Context Protocol"
date: 2026-05-30 09:00:00 +0200
last_modified_at: 2026-05-30 09:00:00 +0200
categories: [tools-frameworks]
tags: [MCP, model-context-protocol, tool-use, developer-experience, agent-infrastructure]
reading_time: 8
author: The Agent Report
hero_image: /assets/images/hero/hero-mcp-is-dead-developer-critique.jpg
excerpt: "The protocol once hailed as the 'USB-C of AI' is now under fire. Developers at Quandri ran the numbers — and they paint a damning picture of context bloat, reliability issues, and architectural overlap with existing CLI tools."
---

The Model Context Protocol (MCP) was supposed to be the great unifier — a standard way for AI agents to talk to the tools and services they need to get work done. Launched in late 2024, it was quickly anointed "the USB-C of the AI ecosystem," adopted by Anthropic, OpenAI, and a growing ecosystem of tool providers.

But the honeymoon may be over. A [devastating new analysis](https://www.quandri.io/engineering-blog/mcp-is-dead) from Quandri Engineering, combined with a [heated Hacker News debate](https://news.ycombinator.com/item?id=48330436) (195 points, 174 comments), has put a serious dent in MCP's reputation. The verdict? MCP eats context, has low reliability, and overlaps significantly with existing CLI and API tools that already work perfectly well.

## Problem 1: It Devours the Context Window

The most damning finding from Quandri's analysis is the sheer volume of tokens consumed by MCP tool definitions. In their real-world stack (Linear, Notion, Slack, and Postgres MCP servers), **tool definitions alone consumed over 21,000 tokens** — that's 10.5% of a Claude 200K context window, and **16.5% of GPT-4o's 128K context**.

| MCP Server | Tools | Estimated Tokens |
|------------|-------|-----------------|
| Linear     | 42    | ~12,807         |
| Notion     | 14    | ~4,039          |
| Slack      | 12    | ~3,792          |
| Postgres   | 9     | ~438            |
| **Total**  | **77** | **~21,077**    |

The problem is architecture-level. Every tool definition includes its JSON schema — parameters, descriptions, return types — and every single one is loaded into context, regardless of whether the model will ever use it. Linear alone ships 42 tool definitions (~12,807 tokens), even if you only ever use `get_issue` and `save_issue`.

> **Restaurant analogy from the article:** "You sit down and 10 menus are spread across the table. There's no room left for actual food."

**Update:** Since these measurements were taken, Claude Code has rolled out [Tool Search with Deferred Loading](https://docs.anthropic.com/claude/docs/tool-use), which loads MCP tool schemas on-demand and reduces context usage by 85%+. So this specific problem is being mitigated — but the architectural concerns remain.

## Problem 2: Low Operational Reliability

MCP's reliability issues are harder to dismiss. The Quandri team documented several failure modes that stem from MCP's architecture:

| Issue | Detail |
|-------|--------|
| Init failure, repeated re-auth | Requires starting and maintaining a separate process |
| Slower AI responses | External server round-trip on every tool call |
| Mid-session tool death | MCP server process crashes mid-conversation |
| Opaque permissions | Unclear what permissions each tool actually has |

The performance numbers are stark. The original article's author benchmarked Jira MCP against its REST API directly: **MCP was 3× slower per call, and 9.4× slower on first call** including initialization overhead. This isn't a Jira-specific problem — it's architectural. Every MCP server adds a process layer between the LLM and the underlying API.

## Problem 3: Overlaps with Existing CLI/API

Perhaps the most fundamental critique: MCP duplicates functionality that already exists and works better.

| Aspect | CLI / API | MCP |
|--------|-----------|-----|
| Human-machine parity | Same commands for humans and LLMs | Only exists inside LLM conversations |
| Composability | Pipes, jq, grep freely combinable | Locked to server return format |
| Debugging | Reproduce immediately in terminal | Only reproducible inside conversation context |
| Training data | Already learned from man pages, StackOverflow | Requires separate tool definitions |
| Install cost | Mostly already installed | Server setup, auth, process management needed |

The token comparison is brutal. To look up the same Linear issue:

- **CLI approach:** ~200 tokens total (50 for the prompt curl command, 150 for the response)
- **MCP approach:** ~12,957 tokens total (12,807 for tool definitions always loaded, 150 for the actual call)

That's **65× more tokens** for the same operation.

### The CLI-First Alternative

The alternative proposed is elegantly simple: provide existing CLI tools to LLMs. LLMs already learned from man pages, StackOverflow, and millions of GitHub gists. They already know how to construct curl commands, pipe through jq, and grep through results. No new protocol needed.

```bash
# CLI approach — works today, no MCP server needed
curl -s -H "Authorization: Bearer $LINEAR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issue(id: \"ISSUE-ID\") { title state { name } assignee { name } } }"}' \
  https://api.linear.app/graphql
```

## What's the Real Story?

Let's be fair: MCP isn't going anywhere overnight. The ecosystem investment is significant — Anthropic [acquired Stainless](https://the-agent-report.com/2026/05/anthropic-acquires-stainless-sdk-mcp-agent-frontier) specifically to accelerate MCP tooling, and major platforms like GitHub, Notion, and Linear have shipped official MCP servers. The protocol solves a real problem: providing a standardized interface for AI agents to interact with external services.

But the critique raises important questions about **architectural philosophy**. The "SSH into a box and use CLI" approach that made LLMs like Claude Code and Codex so effective is fundamentally simpler than the MCP server model. It requires no new infrastructure, no protocol negotiation, no separate process lifecycle management.

As one HN commenter put it: *"MCP feels like solving a problem that doesn't exist — we already had working interfaces between software and software. The breakthrough is that LLMs can now use those same interfaces."*

## The Bottom Line

The [original "MCP is dead" post](https://www.quandri.io/engineering-blog/mcp-is-dead) — which gives its name to this debate — may be intentionally provocative. But the data behind it is real. For teams building AI agent workflows today, the choice between MCP and direct CLI/API access isn't ideological: it's a measurable cost in tokens, latency, and reliability.

The smartest approach? **Don't choose.** Use MCP for what it's good at (standardized discovery, rapid prototyping, ecosystem compatibility) and fall back to direct CLI/API calls for high-frequency, latency-sensitive operations. The best agent architectures will be agnostic — supporting both protocols transparently.

*What's your experience with MCP? Are you doubling down on the protocol or looking at CLI-first alternatives? Share your thoughts in the discussion on [Hacker News](https://news.ycombinator.com/item?id=48330436).*
