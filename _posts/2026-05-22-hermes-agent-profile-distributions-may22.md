---
layout: post
title: "Hermes Agent Profile Distributions — Share Complete Agents as Git Repos"
date: 2026-05-22 14:00:00 +0200
last_modified_at: 2026-05-22 14:00:00 +0200
meta_description: "Hermes Agent introduces Profile Distributions packaging complete agents with personality, skills, and MCP configs as git repositories for one-command."
description: "Hermes Agent introduces Profile Distributions packaging complete agents with personality, skills, and MCP configs as git repositories for one-command."
categories: [hermes-agent]
tags: [hermes-agent, nous-research, open-source, profile-distributions, agent-sharing, git-workflow, devops]
reading_time: 6
hero_image: /assets/images/hero/hero-hermes-agent-profile-distributions-may22.jpg
excerpt: "Hermes Agent introduces Profile Distributions — a new mechanism to package complete agents (personality, skills, cron, MCP configs) as git repositories for one-command installation, git-based updates, and community sharing."
author: The Agent Report
---

A profile is a fully isolated Hermes environment. But until now, sharing a finely-tuned profile with someone else meant either sending them your config files manually or asking them to clone your home directory — neither of which is practical at scale.

**Profile Distributions** change that completely. Landed as a new first-class feature in the v0.14.x cycle, distributions let you package a complete agent — its `SOUL.md` personality, bundled skills, cron schedules, MCP server connections, and all configuration — into a **standard git repository**. Anyone with the URL can install the full agent in one command, and receive updates when you push new commits.

> "If a profile is a local agent, a distribution is that agent made shareable."
> — Hermes Agent documentation

## 🧱 What's in a Distribution?

A profile distribution is just a git repository with a specific directory structure. The only required file is `distribution.yaml` — a minimal manifest that declares the agent's name and metadata:

```
my-research-agent/
├── distribution.yaml   # manifest: name, version, env-var requirements
├── SOUL.md             # agent's personality / system prompt
├── config.yaml         # model, temperature, reasoning, tool defaults
├── skills/             # bundled skills that come with the agent
├── cron/               # scheduled tasks the agent runs
└── mcp.json            # MCP servers the agent connects to
```

The `distribution.yaml` manifest is refreshingly simple:

```yaml
name: research-bot
version: "1.0.0"
description: "An autonomous research assistant"
author: "Your Name"
min-hermes-version: ">=0.12.0"
env:
  OPENAI_API_KEY:
    description: "OpenAI API key for model access"
    required: true
  SERPAPI_KEY:
    description: "SerpAPI key for web search"
    required: false
```

Only `name` is required; everything else has sensible defaults. The `env` block lets the author declare which environment variables must be set by the installer, with descriptions that appear during setup — no more guesswork about what API keys a shared agent needs.

## 📦 Installation: One Command, Instant Agent

From the recipient's perspective, consuming a distribution is trivial:

```bash
hermes profile install https://github.com/you/research-bot
```

Behind the scenes, Hermes Agent:

1. **Validates** the `distribution.yaml` manifest
2. **Inspects** the shell for required env vars, marking them `✓ set`
3. **Writes** a `.env.EXAMPLE` for any variables that still need configuration
4. **Creates** a full profile at `~/.hermes/profiles/research-bot/`
5. **Generates** a shell alias so the agent becomes its own command — `research-bot chat`, `research-bot setup`, etc.

The resulting profile works across every gateway platform — Telegram, Discord, Slack, Signal, WhatsApp, or CLI. Fill in your API keys, and you have a fully configured, production-ready agent in under 30 seconds.

## 🔄 Git-Native Updates: Push to Upgrade

This is where distributions beat tarball-based sharing hands-down. When the author pushes improvements, the installer runs:

```bash
hermes profile update research-bot
```

The update respects a careful **ownership model**:

| Category | Contents | On Update |
|----------|----------|-----------|
| **Distribution-owned** | `SOUL.md`, `config.yaml`, `mcp.json`, `skills/`, `cron/`, `distribution.yaml` | **Replaced** from new clone |
| **Config override** | `config.yaml` (tuned by installer) | **Preserved** by default |
| **User-owned** | `memories/`, `sessions/`, `auth.json`, `.env`, `logs/`, `workspace/`, `plans/` | **Never touched** |

This means the installer's accumulated memories, session history, and personal credentials survive upgrades. The author can refine skills, update personalities, and add cron jobs — and the installer gets those changes without losing any of their own context.

The `--force-config` flag lets the author override even the installer's config.yaml tweaks when necessary (e.g., for breaking config changes).

## 🧠 Why Git? The Five Advantages

The choice of git as the distribution substrate is deliberate:

1. **Diff**: See exactly what changed between versions — impossible with tarballs
2. **Auth**: Reuse existing git credentials (SSH keys, GitHub tokens) — nothing new to configure
3. **Fork**: Any user can fork, customize, and share back — creating a natural open-source ecosystem for agents
4. **Versioning**: Tag stable releases with semantic versions via `git tag v1.0.0`
5. **Tooling**: SSH, CI/CD, `.gitignore`, code review, branch-based experimentation — all standard git workflows

The tradeoff is minimal: recipients need `git` installed, which is already true on any machine running Hermes Agent in 2026.

## 🏗️ Publishing Your First Distribution

For authors, creating a distribution is straightforward after you already have a working profile:

```bash
# Add a distribution.yaml to your existing profile
cd ~/.hermes/profiles/my-agent
echo "name: my-agent\nversion: \"1.0.0\"\ndescription: \"My custom agent\"" > distribution.yaml

# Push to any git remote
git init && git add . && git commit -m "Initial distribution"
git remote add origin https://github.com/you/my-agent
git push -u origin main

# Tag a release
git tag v1.0.0 && git push origin v1.0.0
```

The repository automatically excludes sensitive files (`auth.json`, `.env`, `memories/`, `sessions/`, `logs/`, `workspace/`, `*_cache/`, `local/`) — nothing private leaks by accident. Authors can add a custom `.gitignore` to exclude additional files.

## 🔮 Implications for the Agent Ecosystem

Profile Distributions are more than a convenience feature — they lay the foundation for an **agent marketplace** embedded in the open-source workflow. Teams can publish internal compliance-monitoring agents as private repos. Community members can share specialized agents (research assistants, DevOps bots, writing editors) as public repos. The `hermes profile install` command becomes the equivalent of `pip install` for pre-configured agents. This distribution model comes as the broader [Hermes Agent community ecosystem]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}) has exploded to 276 documented use cases across 16 categories.

This pairs naturally with the recent `hermes profile create --clone` improvements and the HuggingFace skills tap (`huggingface/skills` as a default source). Combined, Hermes Agent now has a complete distribution pipeline — alongside the [performance sprint]({% post_url 2026-05-20-hermes-agent-performance-sprint-may20 %}) that cut 1+ second per turn and multiple security hardening PRs:

- **Skills** → reusable capability modules (via HuggingFace/community taps)
- **Profiles** → local agent environments (via `profile create --clone`)
- **Distributions** → shareable full-agent packages (via git repos)

Every component is open, git-native, and designed for the kind of composable reuse that drives open-source ecosystems.

## 📋 Compatible Versions

Profile Distributions require Hermes Agent **v0.12.0 or later**. The feature is available on all platforms — Linux, macOS, Windows (native and WSL), and Termux. The install and update commands work across all gateway platforms.

---

*Coverage based on the Profile Distributions feature in Hermes Agent main branch (post-v0.14.0). Full documentation: [Profile Distributions Guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profile-distributions.md)*
