---
layout: post
title: "Openclaw v2026.5.26 Makes Transcripts Core, Ships Faster Gateway and Production-Ready Channels"
date: 2026-05-28 10:00:00 +0000
last_modified_at: 2026-05-28 10:00:00 +0000
meta_description: "Openclaw v2026.5.26 elevates transcripts to a core feature, delivers major gateway performance improvements, brings Telegram/iMessage/WhatsApp/Discord to production readiness, and enhances voice capabilities."
categories: [openclaw]
tags: [openclaw, claw-controller, agent-autonomy, transcripts, gateway-performance]
reading_time: 8
excerpt: "Openclaw v2026.5.26 elevates transcripts from a plugin-level concern to a core system capability, ships a substantially faster gateway with smarter caching, brings four major channels to production-grade stability, and delivers richer realtime voice control. With 375,000+ GitHub stars, the project shows no signs of slowing."
hero_image: /assets/images/hero/hero-openclaw-v2026-5-26-transcripts-core-gateway-performance.jpg
author: The Agent Report
---

Just two days after the [v2026.5.22 release with its 4,100× model-listing optimization]({% post_url 2026-05-26-openclaw-v2026-5-22-4100x-model-listing-meeting-notes %}), Openclaw is back with **v2026.5.26** — a stable release that makes transcripts a first-class core capability, delivers substantial gateway performance improvements, and brings Telegram, iMessage, WhatsApp, and Discord to genuine production-readiness.

With **375,000+ GitHub stars**, **78,200+ forks**, and **61 named contributors** in the release changelog alone, the project continues to consolidate its position as the leading open-source claw controller for AI agents.

## Transcripts Go Core

The defining architectural change in v2026.5.26 is the elevation of **transcripts** from a plugin-level concern to a core system capability. Every agent interaction — whether initiated via CLI, WebChat, media upload, follow-up, hook, or Codex mirror — now flows through a unified transcript pipeline.

### What This Means

- **Transcript-backed meeting summaries** — Agent conversations are captured with full source-provider metadata, cleaned user turns, and media provenance, enabling accurate post-hoc summaries
- **Codex mirror transcripts** — Codex app-server interactions are mirrored into the same transcript store, giving operators a single pane of glass across all agent activity
- **CLI/TUI replay** — Transcripts support deterministic replay with hooks, making debugging and auditing dramatically simpler
- **Media provenance** — Every image, file, and generated asset is tracked with its origin context in the transcript record

The transcript capture happens at the gateway level, not the plugin level, which means **every** conversation path is covered — including system events, hook-generated turns, and fallback routing. This is a foundational change that lays the groundwork for compliance, audit, and training-data pipelines.

```bash
# Access transcripts via the new CLI surface
openclaw transcript list
openclaw transcript view <session-id>
```

## Gateway Performance: Less Rediscovery, Faster Replies

The v2026.5.26 release targets one of the most pervasive sources of latency in agent gateways: **repeated rediscovery of the same information**. The team audited every hot path in the gateway startup and reply pipeline, adding smart caching where it matters most.

### Key Optimizations

| Area | Optimization | Impact |
|------|-------------|--------|
| **Plugin metadata** | Plugin metadata snapshots are cached for the process lifetime | Reply-time skill setup no longer rescans plugin metadata on every turn |
| **Startup warnings** | Startup-warning metadata is cached and reused | Gateway startup avoids repeated filesystem scans |
| **Auth stores** | Auth env snapshots are prepared once and reused | No repeated credential resolution on every request |
| **Model cost indexes** | Model pricing metadata is cached | Usage-cost tracking is near-instant |
| **Channel resolution** | Channel routing is cached per session | No repeated dispatch table rebuilds |
| **Session caches** | Session read paths avoid cloning | Lower memory pressure under load |

The most visible impact is on **visible reply delivery latency**. Telegram typing/progress context is preserved, slash-command startup metadata is lazy-loaded, model hydration on hot paths is avoided, Codex profiler timing is flag-gated, and context compaction maintenance is deferred until after the user-facing reply is sent. The net effect: **users see responses faster**, even as the gateway continues processing background work.

## Four Channels Reach Production Readiness

### Telegram
Telegram receives the most extensive channel update in this release. Inbound text entities are preserved, overlapping DM replies are handled correctly, account-scoped topic caches keep forum context, outbound replies carry proper context, targeted bot-command mentions work reliably, durable group retry targets are maintained, and native progress callbacks keep users informed during long-running operations.

### iMessage
iMessage now handles attachment roots correctly — images saved under `~/Library/Messages/Attachments` are read through the existing inbound path policy. Duplicate local Messages-source accounts are deduplicated at startup, direct DM history is seeded reliably, and image/group media attachment commands work as expected. The development team also addressed the long-standing issue where `channels.imessage.accounts` listing both `default` and a named account would spawn duplicate watchers.

### WhatsApp
WhatsApp regains proper group/media behavior with restored ack identity and group-drop warnings. The update also fixes media path resolution when `OPENCLAW_HOME` differs from the OS home directory.

### Discord
Discord voice playback reliability is significantly improved. Large model picker menus are now bucketed alphabetically when the provider list exceeds 25 items. Media captions are merged into a single message, gateway metadata is routed through the configured proxy, numeric channel IDs work for outbound sends, self-reply echoes are suppressed, and wake-name matching is tightened without breaking fuzzy wake phrases.

## Voice and Talk: Full Realtime Control

The voice subsystem receives a major architectural upgrade in v2026.5.26. The team extracted a **shared realtime voice SDK** that provides common primitives for turn-context tracking, output activity monitoring, consult question matching, speakable-result extraction, and alias-aware forced-consult coordination. This SDK is then reused across Discord, browser voice, Google Meet, and all other voice surfaces.

Key capabilities now available:

- **Realtime Talk runs** can be inspected, steered, cancelled, or followed up from both the Web UI and Discord voice
- **Wake-name handling** is more tolerant of ambient noise without letting ambient speech falsely trigger agents
- **iOS Talk mode** now features direct realtime voice sessions, a compact toolbar status indicator, and responsive voice waveform feedback
- **Android** gains the pair-new-gateway action with improved offline voice recovery
- **Google Meet** command bridges reuse the shared output activity tracking for local barge-in detection

## Safer Content Boundaries

Security hardening continues with several important improvements:

- **Browser snapshot reads** now honor SSRF policy before ChromeMCP or direct CDP reads
- **System-event text** cannot spoof nested prompt markers — untrusted plugin/channel labels are sanitized before they reach the prompt
- **Fetched file text** is wrapped as external content with metadata boundaries
- **ClickClack** inbound sender allowlists are applied before agent dispatch
- **Stale device tokens** are rejected during rotation
- **Serialized tool-call text** is scrubbed from visible replies

The team also enabled the **default auth rate limiter** for remote non-browser HTTP gateway auth failures when `gateway.auth.rateLimit` is unset, while preserving the loopback exemption for local development.

## Providers, Codex, and Local Models

The provider layer sees steady improvements across the board:

- **Named auth profiles** allow multiple login configurations per provider, with migration support for Hermes, OpenCode, and Codex auth profiles
- **OpenAI sampling params** are now forwarded through the gateway
- **Codex app-server resume/timeout/usage-limit recovery** is hardened — Codex turn timeouts stay inside the Codex runtime boundary so they don't poison shared app-server clients
- **xAI usage limits** are surfaced in status output
- **Ollama** receives top-p normalization to ensure consistent generation behavior
- **Local approval resolution** is fixed for plugin command paths
- **Memory/local embeddings** now run GGUF embeddings in an isolated worker sidecar — if the native embedding process crashes, the gateway degrades gracefully to keyword search instead of taking down the entire system

## Observability Gets Richer

v2026.5.26 introduces several observability improvements that make it easier to understand what the gateway is doing:

- **Activity tab** — A new ephemeral tab in the Control UI shows sanitized live tool activity summaries without persisting raw telemetry
- **Gateway secret-prep traces** — The diagnostics pipeline now traces secret preparation, making it easier to debug auth failures
- **Model stream progress** — Users can see streaming progress for model responses
- **Explicit fast-mode status** — The TUI now shows when fast-mode is active
- **OpenTelemetry LLM spans** — Content spans are now emitted through the OTLP exporter, giving operators full visibility into model interactions
- **Alertable telemetry** — Blocked tools, model failover, stale sessions, liveness warnings, oversized payloads, and webhook ingress all generate actionable signals

## The Big Picture

Openclaw v2026.5.26 is a **consolidation release** — it takes capabilities that were scattered across plugins, channels, and undocumented code paths and pulls them into a coherent, performant, observable core. Transcripts as a first-class feature, a faster gateway through smarter caching, and four channels reaching genuine production readiness represent meaningful progress toward the project's vision of being the universal control plane for AI agents.

The release follows a familiar pattern: a feature-packed stable release ([v2026.5.22]({% post_url 2026-05-26-openclaw-v2026-5-22-4100x-model-listing-meeting-notes %})) is followed by a hardening release that fixes edge cases, shores up performance, and closes security gaps. With v2026.5.27-beta.1 already published today (May 28) — bringing Pixverse video generation, enhanced security boundaries, and more reliable Codex runs — the release cadence remains relentless.

```bash
npm install -g openclaw
```

---

*Openclaw v2026.5.26 is available now via `npm install -g openclaw`. Full release notes on [GitHub](https://github.com/openclaw/openclaw/releases/tag/v2026.5.26).*
