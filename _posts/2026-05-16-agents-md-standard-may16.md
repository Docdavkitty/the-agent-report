---
layout: post
title: "AGENTS.md: How a Simple Text File Became the Must-Have Standard for Guiding AI Coders"
date: 2026-05-16 10:00:00 +0200
last_modified_at: 2026-05-16 10:00:00 +0200
meta_description: "Over 60,000 open-source projects adopt AGENTS.md, a simple Markdown file telling AI coding agents how to behave, becoming essential infrastructure."
categories: [tools-frameworks]
tags: [AGENTS-dot-md, coding-agents, open-source, developer-tools, AI-standards, agent-guidance]
reading_time: 6
hero_image: /assets/images/hero/hero-agents-md-standard-may16.jpg
excerpt: "Over 60,000 open-source projects have adopted AGENTS.md — part of the [open-source agent framework ecosystem]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}) — a simple Markdown file format that tells AI coding agents how to behave. In a world of increasingly autonomous code editors, this humble convention might be the most important infrastructure you've never heard of."
author: The Agent Report
---

**A quiet standardization movement is reshaping how AI coding agents interact with codebases.** [AGENTS.md](https://agents.md/), an open format for guiding coding agents, has crossed **60,000 open-source projects** — and the number is accelerating. Think of it as a README, but for the AI that's about to edit your files.

The premise is beautifully simple: place a `AGENTS.md` file in your repository's root, and any AI coding agent that encounters it will read the file to understand your project's conventions, constraints, and expectations. No configuration files. No JSON schemas. No API keys. Just Markdown.

And it's working. The [Hacker News thread](https://news.ycombinator.com/item?id=agentsmd) that brought AGENTS.md to over **800 points** this week reveals a community that has been independently creating similar files for months — `CLAUDE.md`, `COPILOT_INSTRUCTIONS.md`, `.cursorrules` — all solving the same problem: **how do you tell an AI agent how to behave in your project?**

## The Problem AGENTS.md Solves

Modern AI coding agents — Claude Code, GitHub Copilot, Cursor, OpenCode — as tracked in our [state of agent engineering 2026]({% post_url 2026-05-23-state-of-agent-engineering-2026-langchain-datadog %}), and dozens more — are increasingly autonomous. They don't just autocomplete the next token; they read your codebase, plan multi-file edits, run tests, and commit changes.

But here's the uncomfortable truth: **no AI agent can read your mind**. Every project has unwritten rules:

- "We use tabs, not spaces, even though the linter doesn't enforce it."
- "Don't touch the `vendor/` directory — it's pinned."
- "All database migrations must be reviewed by the team lead."
- "Use `std::unique_ptr` instead of raw pointers in new code."
- "The test suite is fragile; always run it twice before committing."

Without explicit guidance, agents make reasonable but wrong decisions — and those decisions compound across thousands of projects. AGENTS.md gives project maintainers a single place to encode these rules in plain language.

## What Goes in an AGENTS.md

Based on analysis of the most-starred AGENTS.md files in the wild, common sections include:

- **Project identity**: What this project is, who maintains it, what architecture it follows
- **Conventions**: Coding style, naming conventions, testing patterns, commit message format
- **Restrictions**: Files or directories the agent should never modify
- **Workflows**: How to run tests, build, lint, and deploy
- **Dependencies**: Which packages are preferred, which are banned
- **Review process**: What constitutes a "done" PR and how to submit changes
- **Agent-specific instructions**: "If you're Claude Code, use this prompt. If you're Copilot, use that one."

One maintainer of a popular Rust crate shared their AGENTS.md:

```markdown
# AGENTS.md for `rusty-cache`

## Identity
You are maintaining a high-performance caching library. 
Correctness > Performance > Ergonomics.

## Restrictions
- Never use `unsafe` unless absolutely necessary and documented.
- Do not modify `benchmarks/` — they are upstream benchmarks.
- The `ffi/` module is auto-generated; do not edit manually.

## Workflows
- Tests: `cargo test --all-features`
- Lint: `cargo clippy -- -D warnings`
- Benchmark: `cargo bench --bench cache_bench`

## Commit Style
- Prefix: `fix:`, `feat:`, `docs:`, `refactor:`, `perf:`
- Reference issue numbers in footers
```

## Why 60,000 Projects — And Growing

The adoption curve is steep because AGENTS.md solves a coordination problem that affects **every** project using AI coding tools. Unlike proprietary formats like `CLAUDE.md` (Anthropic) or `.cursorrules` (Cursor), AGENTS.md is:

1. **Vendor-neutral**: Any agent can read it. The spec is a single webpage with no corporate owner.
2. **Human-readable**: Your teammates can read and edit it without special tools.
3. **Git-tracked**: Changes to agent behavior are versioned alongside your code.
4. **Composable**: Multi-repo projects can have AGENTS.md at each level, with inheritance semantics.
5. **Backward-compatible**: Existing `.claude.md` or `.cursorrules` files can be symlinked or migrated incrementally.

The format's simplicity is its killer feature. One contributor described it as "Markdown with emergent semantics" — just write what you want the agent to know, and well-trained agents will figure out the rest.

## The Network Effect

AGENTS.md is experiencing a classic **network effect**: the more projects adopt it, the more agent tooling supports it. Already:

- **Claude Code** natively reads AGENTS.md as its primary configuration file
- **Copilot** treats it as a priority instruction source
- **OpenCode** uses it for project-level context injection
- **Cursor** falls back to AGENTS.md if `.cursorrules` is absent
- **Continue.dev** includes it in the agent's system prompt
- **Qwen3.6's tool-calling mode** references AGENTS.md when operating in repository context

The format is also gaining traction beyond coding. Developers are experimenting with AGENTS.md for:
- **Documentation agents**: How to structure and update docs
- **DevOps agents**: How to manage CI/CD pipelines
- **Security agents**: Rules for vulnerability scanning and reporting
- **Review agents**: Code review guidelines and priorities

## The "You Should Write an Agent" Connection

This week's companion post, ["You Should Write an Agent"](https://fly.io/blog/everyone-write-an-agent/) (1,070 points), argues that the most impactful thing a developer can do right now is build small, focused agents for specific tasks. AGENTS.md is the foundation that makes this vision practical — without a standard way to tell agents what to do, every agent project reinvents the wheel.

> "They're like riding a bike: easy, and you don't get it until you try." — The Fly Blog

The two trends — building agents and telling agents what to do — are converging into something bigger: an **agent-native development workflow** where project-embedded guidance files become as essential as linter configs and CI pipelines.

## What's Coming Next

The AGENTS.md community is actively developing:

- **A formal specification** with validation tools
- **Schema support** for structured agent instructions
- **Inheritance chains** for monorepo and multi-package projects
- **Agent capability declaration** — letting projects signal which tools the agent may use
- **Integration with package managers** (npm `agents.md`, Cargo.toml `[package.agents]`)

The beauty of AGENTS.md is that none of this requires breaking changes. It's Markdown. It always works. The spec just documents what agents already do.

## The Bigger Picture

AGENTS.md represents something rare in the AI industry: a grassroots standard that emerged from practitioners, not from a corporate playbook. It's the DNS of the agent era — invisible infrastructure that makes everything else work.

In a week that also brought us OpenCode, Qwen3.6-35B-A3B, Kiro (a new agentic IDE), and Agent Safehouse, AGENTS.md might be the least glamorous announcement — and the most enduring. Because before you can run an agent on your code, you need to tell it who you are. And that's exactly what AGENTS.md does.

---

*Sources: [AGENTS.md](https://agents.md/), [Hacker News discussion](https://news.ycombinator.com/item?id=agentsmd), [You Should Write an Agent](https://fly.io/blog/everyone-write-an-agent/), [Kiro: A new agentic IDE](https://kiro.dev/blog/introducing-kiro/), [Agent Safehouse](https://agent-safehouse.dev/)*
