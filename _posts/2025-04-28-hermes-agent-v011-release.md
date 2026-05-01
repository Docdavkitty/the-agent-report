---
title: "Hermes Agent v0.11: What's New in the Open-Source AI Runtime"
date: 2025-04-28 10:00:00 +0200
categories: hermes-agent
tags: [Hermes Agent, Nous Research, release, open-source]
reading_time: 5
hero_image: /the-agent-report/assets/images/hero/hero-04-28-hermes-agent-v011-release.jpg
excerpt: "Hermes Agent 0.11 brings enhanced MCP support, new toolsets, and improved multi-model routing. Here's what's changed."
---

Hermes Agent, the open-source AI agent runtime from Nous Research, has been steadily evolving. Version 0.11 introduces several significant improvements for developers building agentic applications.

## Enhanced MCP Integration

The most notable update is deeper integration with the **Model Context Protocol (MCP)**. Hermes now supports:

- Native MCP client for connecting to any MCP-compatible server
- Auto-discovery of tools and resources from MCP servers
- Seamless fallback when MCP servers are unavailable

This makes Hermes one of the most MCP-compatible agent frameworks available.

## New Toolsets

Version 0.11 introduces a refined toolset system that lets developers restrict agent capabilities more granularly:

- **Browser toolset** — Headless browser navigation and interaction
- **Terminal toolset** — Secure shell command execution
- **File toolset** — Read/write operations with path restrictions
- **Web toolset** — HTTP requests and web search
- **Vision toolset** — Image analysis capabilities

Each toolset can be enabled or disabled per-agent, giving precise control over what each agent can access.

## Multi-Model Routing

Agents can now be configured to use different models for different tasks:

```yaml
agent:
  reasoning_model: deepseek-v4-pro
  code_model: claude-sonnet-4
  vision_model: gpt-4o
```

This lets developers optimize for cost and capability per-task rather than using a single model for everything.

## Getting Started

Hermes Agent runs on any Linux machine and can be installed via pip:

```bash
pip install hermes-agent
hermes setup
```

The project is fully open-source under the MIT license. Check the [documentation](https://hermes-agent.nousresearch.com) and [GitHub repo](https://github.com/nousresearch/hermes) for more details.
