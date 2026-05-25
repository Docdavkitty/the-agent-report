---
layout: post
title: "Bleeding Llama — Critical Ollama Memory Leak Exposes User Prompts, System Instructions, and Environment Secrets"
date: 2026-05-14 14:00:00 +0200
last_modified_at: 2026-05-14 14:00:00 +0200
categories: [research]
tags: [meta, llama, open-source, ollama, security-vulnerability, local-llm, llm-security]
hero_image: /assets/images/hero/hero-bleeding-llama-ollama-memory-leak.jpg
reading_time: 7
excerpt: "Cyera Research has disclosed a critical unauthenticated memory leak vulnerability in Ollama — the de facto standard for running Llama models locally. Dubbed 'Bleeding Llama,' the bug allows attackers to exfiltrate user prompts, system prompts, and environment variables from any exposed Ollama server with just three API calls. With ~300,000 servers exposed online, this is the most serious Ollama security issue to date."
author: The Agent Report
---

**Ollama — the open-source platform that powers local Llama inference for hundreds of thousands of developers — has a critical vulnerability that lets attackers siphon every user's conversation history, system prompts, and machine environment variables straight from the server's heap memory.**

Discovered by **Cyera Research** and published this week, "Bleeding Llama" (no CVE assigned yet) exploits an out-of-bounds heap read in Ollama's GGUF file parsing code. The attack requires no authentication, works on default Ollama installations, and can be executed in three API calls. With an estimated **300,000 Ollama servers exposed on the public internet**, the blast radius is enormous.

## What Is Bleeding Llama?

Bleeding Llama is an out-of-bounds heap read vulnerability in Ollama's model creation pipeline. It lives in the code that converts model tensor data from one precision format to another — specifically, the `ConvertToF32` and `WriteTo` functions that handle GGUF (GGML Universal Format) files.

Here's the short version: **GGUF files are just binary blobs.** Anyone can craft one by hand, setting tensor shapes to arbitrary values. Ollama trusts those values, reads past the end of the actual data buffer, and copies whatever happens to be sitting in heap memory into the output model file. That leaked data then gets exfiltrated via Ollama's own push-to-registry API.

## How the Exploit Works

The attack chain involves exactly three API calls:

### Step 1: Upload a Crafted GGUF File (`POST /api/blobs/sha256:[digest]`)

The attacker uploads a hand-crafted GGUF file where the tensor's `shape` field claims there are **1 million elements** — while the actual data is far smaller. Since GGUF is a binary format with no integrity checks, Ollama accepts it without question.

### Step 2: Create a Model (`POST /api/create`)

The attacker calls `/api/create` with the uploaded file, setting the `quantize` parameter to request conversion from F16 to F32. This triggers `WriteTo` → `ConvertToF32`, which iterates over the tensor using the attacker-controlled element count. It reads far past the buffer boundary, pulling arbitrary heap contents into the output. The model name is set to something like `http://attacker-server.com/exfil/model:tag`.

The trick is clever: F16 → F32 conversion is **lossless**, meaning the leaked heap data arrives on disk completely intact — no quantization noise to obscure the sensitive payload.

### Step 3: Push the Model (`POST /api/push`)

The attacker calls `/api/push` with the same model name. Ollama parses the HTTP URI and uploads the entire model — heap detritus, user prompts, and all — straight to the attacker's server.

### What Gets Leaked

According to Cyera's research, the leaked heap memory can contain:

- **User prompts and messages** sent to any model running on the server
- **System prompts** from all loaded models
- **Environment variables** from the host machine (API keys, tokens, credentials)
- **Tool outputs** when Ollama is connected to agents like Claude Code or Codex

> *"Imagine a large enterprise with 10,000+ employees using Ollama as their AI chat. An attacker can learn basically anything about the organization — API keys, proprietary code, customer contracts, and much more."*
> — Cyera Research

## Root Cause: `unsafe` in Go

Ollama is written in Go, a memory-safe language. But the GGUF tensor conversion code uses Go's `unsafe` package — the escape hatch for low-level memory operations:

```go
func ConvertToF32(src unsafe.Pointer, srcType ggmlType, numElements int) []float32 {
    // loops over src buffer reading numElements — no bounds check
}
```

The `numElements` parameter comes directly from the GGUF file's tensor metadata. There is **zero validation** that the declared element count matches the actual buffer size. A crafted GGUF file with an inflated shape causes the loop to walk straight off the end of the allocated memory.

## The Scope of Exposure

Ollama, by default, listens on **all interfaces (0.0.0.0)** with **no authentication**. Cyera estimates **~300,000 exposed Ollama servers** on the public internet. Any of these can be compromised with the three-call attack sequence.

For developers running Ollama locally (127.0.0.1), the risk is lower but not zero — malware or a malicious browser extension on the same machine can reach the unprotected API endpoint.

## Why This Matters for the AI Agent Ecosystem

Ollama has become the **backbone of local AI agent infrastructure**. Developers routinely connect it to:

- **Claude Code** and **Codex** for agentic coding workflows
- **OpenClaw** and other desktop automation agents
- **Obsidian-Semantic** and note-taking AI tools
- **Custom agent frameworks** running on local hardware

When an agent sends prompts, code, or tool outputs to a local Llama model via Ollama, all that data flows through the Ollama server's heap. A successful Bleeding Llama exploit on a shared or exposed server leaks **everything** — including proprietary code, internal documentation, and tool execution outputs that agents have processed.

## Mitigation Steps

Until Ollama releases a patched version, administrators should take the following steps immediately:

1. **Bind to localhost only** — Set `OLLAMA_HOST=127.0.0.1` or configure your firewall to block external access to port 11434
2. **Add authentication** — Use a reverse proxy (nginx, Caddy) with HTTP basic auth or an API key
3. **Network segmentation** — If Ollama must be accessible on a LAN, restrict access to trusted subnets only
4. **Monitor /api/create and /api/push endpoints** — Anomalous model creation followed by push to external domains is a red flag
5. **Watch for updates** — Ollama's latest [v0.24.0-rc0](https://github.com/ollama/ollama/releases/tag/v0.24.0-rc0) (May 14) does not explicitly mention this fix, but subsequent releases may include a patch

## The Bigger Picture

Bleeding Llama is the latest in a growing pattern of critical vulnerabilities in AI infrastructure tools. As the industry rushes to deploy local LLMs and AI agents, the security posture of the underlying tooling has not kept pace. Ollama's 170K GitHub stars and 100M+ Docker pulls make it a high-value target — and this vulnerability turns it into a data sieve.

For the Llama ecosystem, the takeaway is stark: **popularity does not equal security.** Organizations relying on Ollama for sensitive AI workloads need to treat it as a critical attack surface, not a turnkey solution.

---

*The full Bleeding Llama research paper is available on [Cyera's website](https://www.cyera.com/research/bleeding-llama-critical-unauthenticated-memory-leak-in-ollama).*
