---
layout: post
title: "Git for AI Agents — re_gent Brings Version Control to Agent Workflows"
date: 2026-05-10 08:00:00 +0200
categories: tools-frameworks
tags: version-control agent-tooling devtools claude-code open-source
reading_time: 6
excerpt: "re_gent (290★ GitHub / 115 points HN) brings Git-like version control to AI coding agents — tracking every tool call, session, and prompt with full auditability. We dive into how it works, why it matters, and what the community is saying."
hero_image: /assets/images/hero/hero-regent-git-for-ai-agents.jpg
---

*You're five minutes deep into a Claude Code session. The agent just refactored three files, added a test suite, and somewhere in the chaos — broke the build. Which change did it? Which *prompt* caused it? You scroll through your terminal history, looking for answers. There has to be a better way.*

There is now. Enter **re_gent**, an open-source version control system purpose-built for AI coding agents. It landed on Hacker News this weekend with **115 points** and crossed **290 GitHub stars** within days — and it might be one of the most practical devtools to emerge from the agent era.

## The Problem: Agents Have No Audit Trail

AI coding agents — Claude Code, Codex, Cursor — are rewriting how we build software. But they introduce a fundamental gap: **agent activity has no version control of its own.**

Think about it. Git tracks what *you* did. But when an agent runs autonomously:

- Which prompt generated that line of code?
- What tool call changed that file?
- Which session introduced the bug?
- How do you rewind to "before the refactor"?

The current answer is: `/compact` and pray. Or copy-paste your entire conversation into a fresh chat. Or just accept the chaos.

re_gent solves this with three primitives that should have existed from day one:

- **`rgt log`** — what did this agent session do?
- **`rgt blame`** — which prompt wrote this line?
- **`rgt rewind`** — restore to any previous step

## How re_gent Works

Under the hood, re_gent stores agent activity in a `.regent/` directory (analogous to `.git/`):

```
.regent/
├── objects/       # Content-addressed blobs (BLAKE3 hashing)
├── refs/          # Session pointers (one per agent)
├── index.db       # SQLite query index
└── config.toml
```

Every **tool call** an agent makes becomes a **Step**:

```go
Step {
  parent:      <previous-step-hash>
  tree:        <workspace-snapshot>
  transcript:  <conversation-delta>
  cause: {
    tool_name: "Edit"
    args:      <what-changed>
    result:    <tool-output>
  }
  session_id:  "claude-20260502-143021"
  timestamp:   "2026-05-02T14:30:21Z"
}
```

Steps form a **DAG** (directed acyclic graph). Each session runs on its own branch. Common ancestors get deduplicated. The result is Git-level auditability for everything your agents do.

### Practical Commands

```bash
# See what your agent did
$ rgt log

Step a1b2c3d  |  2 min ago  |  Edit
│ File: src/handler.go
│ Added error handling to request handler
│ +5 lines, -2 lines

# Blame a specific line
$ rgt blame src/handler.go:42

Line 42: func handleRequest(w http.ResponseWriter, r *http.Request) {
Step:    a1b2c3d4e5f6
Session: claude-20260502-143021
Tool:    Edit
Prompt:  "Add error handling to the request handler"

# Track multiple concurrent sessions
$ rgt sessions

claude-20260502-143021  |  3 steps  |  Last: 2 min ago
claude-20260502-091534  |  7 steps  |  Last: 2 hours ago
```

## Why This Matters for the Agent Ecosystem

The timing of re_gent's release is perfect. We're entering a phase where:

1. **Multi-agent workflows** are becoming common — multiple agents editing the same codebase simultaneously
2. **Agent-in-the-loop CI/CD** means agents are touching production code regularly
3. **Regulatory scrutiny** around AI-generated code is increasing — auditors want provenance
4. **Debugging agent failures** requires understanding the *sequence* of decisions, not just the final state

re_gent addresses all of these. It's essentially **Git, but for the conversation-to-code pipeline**.

## Community Reception

The HN discussion surfaced several interesting threads:

> *"This is brilliant. Does it only work with Claude right now? Will it work with any agent built on the Claude Agent SDK?"*

The project is designed to be agent-agnostic — it hooks into tool calls at the filesystem level, so it should work with Claude Code, Codex, Cursor, and any agent that modifies files. The README explicitly lists Claude Code compatibility, but the architecture is general-purpose.

> *"None of these X-for-agents seem to motivate why they don't use X."*

This is a fair critique — agents *can* use regular Git. But the difference is granularity: Git tracks commits (human-level intentions), while re_gent tracks **tool calls** (agent-level actions). A single human commit might encompass dozens of agent steps. re_gent preserves that intermediate history.

> *"Agents can use git FWIW, and you can tell them to search old sessions..."*

True — but that depends on the agent remembering to commit, and on the agent knowing *what* to commit. re_gent is automatic and agent-aware. No "git add; git commit" prompt engineering required.

## Installation and Getting Started

```bash
# macOS / Linux (Homebrew)
brew tap regent-vcs/tap
brew install regent

# Or via Go
go install github.com/regent-vcs/regent/cmd/rgt@latest

# Initialize in your project
cd your-project
rgt init
```

That's it. Once initialized, every tool call your agent makes is automatically captured. No manual commits, no configuration, no cognitive overhead.

## The Bigger Picture

re_gent is part of a broader wave of **agent-native infrastructure** that's emerging. We've seen:

- Agent-to-data safety frameworks (covered [yesterday](/2026/05/09/agent-to-data-safety/))
- Agent-specific control flow languages ([Agents Need Control Flow](/2026/05/08/agents-need-control-flow-not-prompts/))
- Inference engines optimized for agentic workloads ([TokenSpeed](/2026/05/07/tokenspeed-lightseek-inference-engine-agentic-workloads/))

And now: agent-native version control.

The pattern is clear: as agents become first-class citizens in our development workflows, we need first-class tooling to manage them. re_gent fills a hole that somehow remained unfilled for two years of the agent era. It's about time.

---

*re_gent is Apache 2.0 licensed. Source on [GitHub](https://github.com/regent-vcs/re_gent). HN discussion [here](https://news.ycombinator.com/item?id=48063548).*
