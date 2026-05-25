---
layout: post
title: "Git-Surgeon: Giving AI Agents Scalpel-Like Precision Over Git History"
date: 2026-05-18 12:00:00 +0200
last_modified_at: 2026-05-18 12:00:00 +0200
categories: tools-frameworks
tags: [git-surgeon, ai-coding-agents, git-tools, agent-workflows, version-control]
reading_time: 7
excerpt: "AI coding agents break when they hit interactive git commands. Git-Surgeon solves this with hunk-level precision — letting agents stage, unstage, commit, and rewrite history without ever needing a prompt. Here's how it works and why it matters."
hero_image: /assets/images/hero/hero-git-surgeon-agentic-git-control.jpg
author: The Agent Report
---

One of the most frustrating limitations of today's AI coding agents is their inability to handle interactive git workflows. Ask Claude Code or Codex to "commit the frontend changes separately from the backend changes" and you'll likely watch it reach for `git add -p` — an interactive command that requires a human at the keyboard. When that fails, agents often resort to destructive workarounds like `git checkout` to discard changes and start over.

**Enter [git-surgeon](https://github.com/raine/git-surgeon): a Rust-powered CLI tool that gives AI agents surgical control over git without a single interactive prompt.**

In just its first days on GitHub, git-surgeon has already attracted 94 stars and growing. Written in Rust, it provides git primitives specifically designed for autonomous consumption — stable hunk IDs, machine-readable output formats, and agent-ready skill integrations for Claude Code, Codex, and OpenCode.

## The Problem: Git Wasn't Built for Robots

Interactive git commands like `git add -p` were designed for developers sitting at a terminal. They present hunks one at a time, ask `Stage this hunk? [y/n/q/a/d/j/J/e/?]`, and wait for keyboard input. AI agents, which operate through non-interactive shell execution, simply cannot use them.

The workarounds agents currently use are painful:

```
❯ commit the changes separately

⏺ Bash(git diff internal/bot/listing_handler.go)
  ⎿  diff --git ... +83 lines

⏺ Let me reset and make the changes in two separate commits.

⏺ Bash(git checkout internal/bot/listing_handler.go)   ← about to destroy changes
  ⎿  Interrupted
```

The agent, unable to selectively stage hunks, either gives up or takes a sledgehammer approach — committing everything together or losing changes entirely. For agents working on complex codebases with multiple intertwined changes, this is a fundamental blocker.

## How Git-Surgeon Fixes It

Git-surgeon solves this by exposing git's internal hunk machinery through a stable, non-interactive CLI. The key commands:

### Inspecting Hunks

```bash
$ git-surgeon hunks
ac34353  internal/bot/listing_handler.go (+6 -3)
15baf94  internal/bot/listing_handler.go (+10 -2)
7c6ef9e  internal/auth/login.go (+4 -1)
4eefac8  internal/bot/listing_handler.go (+2 -1)
```

Each hunk gets a **stable hash ID** derived from its content. The agent can reference these IDs across sessions — the same hunk always has the same ID until it changes.

### Selective Committing

```bash
# Commit specific hunks by ID in one step
$ git-surgeon commit ac34353 15baf94 7c6ef9e -m "allow edit commands during attribute input"

$ git-surgeon commit 4eefac8 bbba931 -m "add logging for attribute prompts"
```

The agent can now split a single working tree into multiple clean, focused commits — exactly what version control best practices demand.

### Line-Level Precision

```bash
# Stage specific lines within a hunk
$ git-surgeon stage ac34353 --lines 1-3,5
```

This allows splitting a single hunk across multiple commits when it contains unrelated changes. If a hunk modifies both an error message and adds logging, the agent can stage and commit each logical change separately.

### History Rewriting

Git-surgeon goes beyond staging and committing. It gives agents the ability to rewrite history:

```bash
# Split a commit that mixes concerns
$ git-surgeon split HEAD~1

# Fold staged changes into an earlier commit
$ git-surgeon fold abc1234

# Selectively undo hunks from previous commits
$ git-surgeon undo 7c6ef9e
```

This means an agent can retroactively clean up commits after the fact — splitting a messy commit into focused ones, folding fixup commits into the right place, or removing a change that turned out to be wrong.

## Agent-First Design

Git-surgeon ships with built-in skill integrations for the three major coding agents:

```bash
# Claude Code
git-surgeon install-skill --claude

# OpenCode
git-surgeon install-skill --opencode

# Codex
git-surgeon install-skill --codex
```

For Claude Code users, there's also a plugin marketplace option:

```bash
claude plugin marketplace add raine/git-surgeon
claude plugin install git-surgeon@git-surgeon
```

The skill files teach the agent how to use git-surgeon's commands, what output format to expect, and how to interpret hunk IDs. This dramatically reduces the prompt engineering burden on the user — the agent loads the skill once and knows exactly what git surgery tools are available.

## The Architecture: Built in Rust for Performance

Git-surgeon is written in Rust, which gives it several advantages for agentic workflows:

- **Fast startup time** — critical when agents call it dozens of times in a loop
- **No runtime dependencies** — a single binary, no Python/Bash/Node requirements
- **Safe memory handling** — no risk of memory corruption when processing large diffs
- **Cross-platform** — works on Linux, macOS, and Windows

The tool works by parsing git's internal diff output and maintaining a stable index of hunks. It never wraps interactive commands — everything goes through git's plumbing layer directly.

## Real-World Impact

For developers who frequently work with AI coding agents, git-surgeon solves a daily frustration. Instead of manually sorting through agent-generated changes and cherry-picking what to commit, you can let the agent do it:

1. Agent generates changes across multiple files
2. Agent runs `git-surgeon hunks` to see what it has
3. Agent logically groups hunks by feature or concern
4. Agent commits each group with a descriptive message
5. Result: a clean git history, fully agent-driven

As one early user noted: *"The moment where an agent can cleanly separate its own changes into focused commits is the moment you stop reviewing every diff line-by-line."*

## The Bigger Picture

Git-surgeon is part of a broader trend in the AI agent ecosystem: **building tools that meet agents where they are, rather than forcing agents to emulate human workflows.**

Just as [Vercel's Zero](https://github.com/vercel-labs/zero) rethinks compiler output for agent consumption, git-surgeon rethinks version control interaction. Both recognize that the next generation of developer tools needs to speak two languages: one for humans and one for machines.

The traditional approach has been to build better agents that can navigate human-targeted UIs. The emerging approach is to **make the tools themselves agent-native** — exposing the same functionality through stable, structured, non-interactive interfaces.

Git-surgeon is available now at **[github.com/raine/git-surgeon](https://github.com/raine/git-surgeon)**. Install with:

```bash
curl -fsSL https://raw.githubusercontent.com/raine/git-surgeon/main/scripts/install.sh | bash
```

Or via Cargo: `cargo install git-surgeon`.
