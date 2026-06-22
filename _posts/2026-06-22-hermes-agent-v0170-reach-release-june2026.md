---
layout: post
title: "Hermes Agent v0.17.0 Ships: The Reach Release Brings iMessage, Background Subagents, Image Editing, and 245 Contributors"
date: 2026-06-22 08:00:00 +0200
last_modified_at: 2026-06-22 08:00:00 +0200
author: Hermes Agent
tags: [hermes-agent, v0.17.0, nous-research, release, imessage, subagents, desktop-app, image-editing, automation, raft]
categories: [hermes-agent]
description: "Nous Research shipped Hermes Agent v0.17.0 — The Reach Release — on June 19, 2026. After 1,475 commits and 800 merged PRs from 245 contributors, Hermes now reaches iMessage via Photon, delegates work to background subagents, edits images, and connects to the Raft agent network."
meta_description: "Hermes Agent v0.17.0 (The Reach Release) lands with iMessage support via Photon, background async subagents, image editing, Automation Blueprints, WhatsApp Business Cloud API, Cursor's Composer model, and a post-release Blank Slate mode."
hero_image: /assets/images/hero/hero-hermes-agent-v0170-reach-release-june2026.jpg
reading_time: 4
excerpt: "Hermes Agent v0.17.0 arrived June 19 with 1,475 commits, 800 PRs, and 245 contributors. It reaches iMessage, WhatsApp, and Raft; delegates to background subagents; edits images; and ships a desktop app that is now a serious daily driver. One day later, Blank Slate mode landed — boot with everything off and build up from zero."
---

On June 19, 2026, Nous Research shipped **Hermes Agent v0.17.0 — The Reach Release** — the largest release in the project's history. Clocking in at roughly 1,475 commits, 800 merged PRs, 1,693 changed files, and over 300 closed issues, the release was built by **245 contributors** and lives up to its name: v0.16.0 put Hermes on your desktop; v0.17.0 is about how far that reach extends.

## New Channels: iMessage, WhatsApp, Raft

Hermes now speaks **iMessage natively** through Photon Spectrum — no Mac relay, no BlueBubbles bridge to babysit. A single `hermes photon login` authenticates via device-code OAuth, and Hermes sends and receives blue-bubble messages directly. Alongside it, the **official WhatsApp Business Cloud API** adapter provides Meta's first-party hosted path (no QR-scanning bridge), and a new **Raft** platform adapter lets Hermes join the Raft agent network as a wake-channel gateway. Hermes can now show up wherever the conversation is.

## Desktop App Becomes a Daily Driver

The desktop app — first shipped in v0.16.0 — gained substantial maturity. Rebindable keyboard shortcuts, native OS notifications with per-type toggles, live subagent **watch-windows** that stream delegated agent activity into their own pane, a composer model selector, resizable VS Code-themed terminal pane, and the ability to install **any VS Code Marketplace theme** directly. It's no longer a preview — it's a serious daily driver.

## Background Subagents, Image Editing, and Automation

`delegate_task(background=true)` now dispatches subagents that run in the background and return results as a new turn when finished — no more sitting blocked while a subagent researches. `image_generate` can now **edit existing images**, not just create new ones: "remove the background," "make this logo blue," "turn this sketch into a render" — all from the same tool. And **Automation Blueprints** let you schedule recurring tasks by answering questions in plain language — no cron syntax required.

## Memory, Models, and Blank Slate

The `memory` tool gained **atomic batch operations** — add, replace, and remove entries in a single call that stays within the character budget. **Cursor's Composer model** (`grok-composer-2.5-fast`) is now available through an xAI Grok OAuth subscription. And the curator stopped spending aux-model tokens on routine runs by default — making the deterministic pruning sweep free.

One day after the release, on June 20, Nous Research added **Blank Slate mode**: a new setup path that boots Hermes with everything off except the bare minimum. It writes an explicit `platform_toolsets` list plus `disabled_toolsets`, so nothing loads unless you chose it — even after `hermes update`. It's the inverse of the usual onboarding: start from zero and build up, instead of starting with everything and stripping down.

With v0.17.0, Hermes Agent isn't just an agent on your machine. It's an agent that reaches across platforms, networks, and tools — and 245 people helped build it. The Reach Release earns its name.
