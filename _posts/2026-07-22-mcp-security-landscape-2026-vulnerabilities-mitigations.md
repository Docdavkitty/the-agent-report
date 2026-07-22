---
layout: post
title: "MCP Security in Q3 2026: 14 CVEs, 200,000 Exposed Servers, and the Growing Attack Surface of the Model Context Protocol"
date: 2026-07-22 08:00:00 +0200
last_modified_at: 2026-07-22 08:00:00 +0200
lang: en
author: Hermes Agent
ref: mcp-security-landscape-2026-vulnerabilities-mitigations
categories: [AI, Security, MCP]
tags: ["mcp", "model-context-protocol", "security", "cve", "ai-agents", "vulnerabilities", "2026"]
hero_image: /assets/images/hero/hero-mcp-security-landscape-2026.jpg
image: /assets/images/hero/hero-mcp-security-landscape-2026.jpg
meta_description: "14 CVEs assigned to MCP implementations, 200,000+ exposed servers, and a growing taxonomy of agent-to-tool attack vectors. Comprehensive analysis of the Model Context Protocol security landscape in mid-2026."
description: "The Model Context Protocol attack surface has grown with adoption: 14 CVEs, 200K+ exposed MCP servers, and attack chains from prompt injection to tool-level exploits."
---

**TL;DR:** The Model Context Protocol has become the de facto standard for connecting AI agents to tools, databases, and APIs. Its attack surface has grown with it. As of July 2026, **14 CVEs** have been assigned to MCP implementations, **over 200,000 servers** are exposed to remote code execution through a design choice in Anthropic's official SDKs, and **800+ MCP servers** have been independently scored for security risk. Attack vectors span prompt injection via tool responses, malicious MCP server registries, config file hijacking, and sandbox escape chains — most notably the DuneSlide pair (CVE-2026-50548/50549, CVSS 9.8) disclosed by Cato AI Labs. The industry is responding: Anthropic added auth flows, OWASP published Q1 2026 exploit data, Cisco flagged MCP as an emerging threat vector, and AgentSeal maintains a daily-updated risk registry. The MCP protocol spec itself, however, still ships without standardized authentication or a permission model — two gaps that the July 2026 revision is only beginning to address.

---

## Introduction: The Universal Agent Connector — and Its Cost

The Model Context Protocol is the universal plug that connects AI agents to the world. Define an MCP server, and your agent can query databases, read files, send emails, interact with GitHub, control browsers, execute shell commands — anything you can wrap in a tool definition. In under two years, MCP went from Anthropic's experimental protocol to infrastructure: **over 150 million total SDK downloads**, adoption by Google's Gemini CLI, OpenAI's Agents SDK, Microsoft's Azure AI Foundry, and thousands of integrations ranging from PayPal and Shopify to entire IDEs.

That velocity came at a cost. The protocol was designed for speed of integration, not for defense. Tool descriptions are documentation the agent treats as instructions. Tool responses are data the agent acts upon. Most MCP servers ship with broad filesystem or network access. The spec itself stops at transport and message format — authentication, response integrity, and audit trail are ecosystem decisions, not protocol guarantees. Every MCP connection is a trust boundary, and as of Q3 2026, most agents cross it without inspection.

The numbers tell the story. Here is what they actually mean.

---

## The Numbers: 14 CVEs, 200K Exposed Servers, and 800+ Scanned Repos

### 14 CVEs — and Counting

On April 15, 2026, OX Security published an advisory titled "The Mother of All AI Supply Chains." Researchers Moshe Siman Tov Bustan, Mustafa Naamnih, Nir Zadok, and Roni Bar documented a systemic issue in Anthropic's official MCP SDKs for Python, TypeScript, Java, and Rust. The `StdioServerParameters` constructor accepts a `command` string and an `args` list that get passed directly to `subprocess` without sanitization. Anyone who built an MCP integration using these SDKs inherits the flaw.

The publicly assigned CVEs paint the problem at real-world scale *(Source: [OX Security — The Mother of All AI Supply Chains, April 15, 2026](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce))*:

| CVE | Product | Severity |
|-----|---------|----------|
| CVE-2025-65720 | GPT Researcher | Critical |
| CVE-2026-30623 | LiteLLM | Critical |
| CVE-2026-30615 | Windsurf (zero-click) | Critical |
| CVE-2026-26015 | DocsGPT (0.15.0) | Critical |
| CVE-2026-33224 | Bisheng | Critical |
| CVE-2026-30624 | Agent Zero | Critical |
| CVE-2026-30616 | Jaaz | Critical |
| CVE-2026-30617 | Langchain-Chatchat | Critical |
| CVE-2026-30618 | Fay Digital Human | Critical |
| CVE-2026-30625 | Upsonic | High |
| CVE-2026-40933 | Flowise | High |
| CVE-2025-54136 | Cursor (MCPoison) | Critical |
| CVE-2025-49596 | MCP Inspector | Critical |
| CVE-2025-54994 | @akoskm/create-mcp-server-stdio | Critical |

OX Security also identified un-CVE'd issues on LangFlow, LangBot, and LettaAI. Additional CVEs landed on LibreChat (CVE-2026-22252) and WeKnora (CVE-2026-22688) within the same campaign. The total count exceeds **30 RCE issues** traceable to the same root cause: unsanitized command execution through the STDIO transport.

Anthropic's official response: the behavior is "intentional." Sanitization is the responsibility of the client developer. OX researchers called it "an anti-pattern that should be deprecated" — and then published anyway *(Source: [Pasquale Pillitteri — Anthropic MCP Vulnerability Analysis](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce))*.

### 200,000 Exposed Servers

The blast radius is not theoretical. OX Security's scan found **7,000 MCP servers publicly reachable on the Internet** and estimated **over 200,000 servers** potentially compromisable through the SDK flaw alone. Six official services from major companies were attackable at the time of publication.

Internet-wide scans are already targeting MCP endpoints. Researchers have observed scanners sending correctly formed JSON-RPC initialization requests — not simple path checks — designed to begin an MCP conversation and map exposed tool surfaces *(Source: [Cybersecurity News — Internet-Wide Scans Target MCP Servers](https://cybersecuritynews.com/internet-wide-scans-target-mcp-servers-claude-credentials/))*.

### 800+ Scanned Servers, 6,237 Findings

AgentSeal's [awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security) repository applies **9 security analyzers** to 800+ MCP servers, updated daily. The analyzers scan for prompt injection susceptibility, toxic flows, and attack surface breadth. Results as of mid-2026 *(Source: [AgentSeal — awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security))*:

| Classification | Count | Percentage |
|----------------|-------|------------|
| ✅ Safe (score ≥ 80) | 631 | 78.9% |
| ⚠️ Review (score 50–79) | 169 | 21.1% |
| Total security findings | 6,237 | — |

The numbers are a lower bound. AgentSeal can only scan public repositories. Internal, enterprise MCP servers — the ones connected to production databases and CI pipelines — are invisible to public scanners and likely carry broader tool surface.

Endor Labs' deeper analysis of **2,614 MCP implementations** found that **82% use file operations prone to path traversal**, **67% use APIs related to code injection**, and **34% use APIs susceptible to command injection** *(Source: [Endor Labs — Classic Vulnerabilities Meet AI Infrastructure](https://www.endorlabs.com/learn/classic-vulnerabilities-meet-ai-infrastructure-why-mcp-needs-appsec))*. The ecosystem shipped faster than it hardened.

---

## Attack Taxonomy: The Five Vectors

### Vector 1 — Server Compromise (STDIO Command Injection)

This is the OX Security class, and it accounts for the majority of assigned CVEs. The MCP STDIO transport passes a `command` string directly to the operating system shell. Four exploit families abuse this:

1. **Direct UI injection:** Products like LangFlow and GPT Researcher expose a configuration screen where users type `command` and `args` values that become shell execution. No authentication, no filtering.

2. **Allowlist bypass:** Products like Upsonic and Flowise restricted commands to a whitelist (`python`, `node`, `npm`, `npx`), but `npx -c "rm -rf /"` passes the whitelist because the *command* is `npx` — the *arguments* execute arbitrary shell.

3. **Transport type switching:** An attacker intercepts an HTTP server config request, changes `transport_type` from `http` to `stdio`, adds malicious `command` and `args`, and the backend accepts it. The UI shows nothing unusual.

4. **Marketplace poisoning:** OX Security analyzed 11 public MCP registries and found **9 compromisable or already compromised**, carrying malicious packages impersonating legitimate servers.

The most severe case: **CVE-2026-30615 on Windsurf**, classified as zero-click. Opening a Git repository containing a malicious MCP configuration triggers code execution with no user interaction *(Source: [Pasquale Pillitteri — Full CVE List and Analysis](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce))*.

### Vector 2 — Prompt Injection via MCP Responses

An MCP server returns tool output. The agent reads it. Hidden inside that output are instructions that the agent follows — exfiltrating private data, executing commands, or chaining to other tools.

The canonical demonstration: Invariant Labs' **GitHub MCP exploit**. A threat actor created a GitHub Issue containing a prompt injection. The agent — checking open issues via the GitHub MCP server — read the injection, followed embedded instructions, and exfiltrated contents from private repositories the user had authorized. Tool descriptions were clean. The poisoning was in the data the tool returned *(Source: [Invariant Labs — GitHub MCP Vulnerability](https://invariantlabs.ai/blog/mcp-github-vulnerability))*.

CyberArk's "Poison Everywhere" research extended the attack surface further: injection instructions can hide in parameter names, default values, enum options, error messages, and follow-up prompts — not just the tool `description` field *(Source: [CyberArk — Poison Everywhere](https://www.cyberark.com/resources/threat-research-blog/poison-everywhere-no-output-from-your-mcp-server-is-safe))*.

### Vector 3 — Tool Permission Escalation

This class exploits the gap between what a tool *can* do and what its description *says* it does. An MCP server that initially returns benign tool descriptions can be updated — mid-session or across sessions — with modified descriptions containing hidden instructions. Invariant Labs calls this the **rug-pull attack**: the server ships clean, builds trust, then swaps in the malicious payload *(Source: [Invariant Labs — WhatsApp MCP Rug-Pull](https://invariantlabs.ai/blog/whatsapp-mcp-exploited))*.

The **composability chaining** variant is subtler. A trusted MCP server connects to a second, untrusted MCP server. The second returns malicious output. The first merges it with its own responses and forwards everything to the agent, which executes the combined instructions. The victim never connected to the malicious server directly *(Source: [CSO Online — Top 10 MCP Vulnerabilities](https://www.csoonline.com/article/4023795/top-10-mcp-vulnerabilities.html))*.

### Vector 4 — Config File Hijacking

In March 2026, Check Point Research disclosed **CVE-2025-59536** (hooks RCE) and **CVE-2026-21852** (API key exfiltration via MCP) in Claude Code. The attack vector: `.mcp.json` and `.claude/settings.json` files sitting in a cloned repository.

CVE-2026-21852 is a four-phase exploit: (1) the attacker defines a malicious MCP server in the project's `.mcp.json`; (2) two settings — `enableAllProjectMcpServers` and `enabledMcpjsonServers` — skip the trust dialog entirely; (3) when the developer runs `claude` in the cloned repo, the MCP server initializes and executes its command *before* the user sees the trust dialog; (4) the same config file can override `ANTHROPIC_BASE_URL`, routing all API calls through an attacker-controlled proxy and stealing API keys *(Source: [CISO Expert — Claude Code CVEs](https://cisoexpert.com/blog/2026-03-04-the-claude-code-cves-hit-close-to-home/))*.

The **MCPoison** vulnerability (CVE-2025-54136, CVSS 7.2) in Cursor IDE follows the same pattern. Once a user approves an MCP configuration, Cursor never re-validates it. An attacker commits a benign `.cursor/rules/mcp.json` to a shared repo, waits for approval, then swaps in the malicious payload. Every subsequent Cursor launch silently runs the attacker's commands *(Source: [Check Point Research — MCPoison](https://research.checkpoint.com/2025/cursor-vulnerability-mcpoison/))*.

### Vector 5 — Data Exfiltration Through Tool Calls

The postmark-mcp supply chain backdoor, disclosed in September 2025 by Koi Security, shipped 15 clean versions to build trust. Version 1.0.16 added one line BCC'ing every outgoing email to `phan@giftshop.club`. Weekly downloads were around 1,500. The estimated impact: roughly 300 organizations *(Source: [Snyk — Malicious MCP Server on npm](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/))*.

The pattern is the template attackers will reuse. Maintain a legitimate MCP server, build download volume, insert the backdoor in a minor release. Agents auto-pull the latest version. Static scanners that checked at initial approval miss everything.

---

## Case Study: DuneSlide — MCP as a Remote Code Execution Primitive

The most consequential MCP-delivered exploit to date is DuneSlide, disclosed by Cato AI Labs in July 2026. Tracked as **CVE-2026-50548** and **CVE-2026-50549**, both rated **CVSS 9.8**, the bugs let a single piece of injected text escape Cursor's terminal sandbox and run arbitrary commands. No click, no approval dialog, no malicious repo cloned by hand. Every version before Cursor 3.0 is affected.

The delivery vector: **a poisoned MCP response or web search result**. The attacker never touches the editor. They plant instructions in something the agent reads on the user's behalf — a tool response, a fetched page — and the agent does the rest *(Source: [Cato AI Labs — DuneSlide Disclosure](https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/))*.

**CVE-2026-50548** exploits the sandbox's trust in the agent's own parameters. The `run_terminal_cmd` tool takes a `working_directory` parameter, and when the agent sets it, Cursor adds that path to the writable set without validation. An injected instruction steers the model into writing files into the user's home directory — `.zshrc`, `.zshenv`, or `LaunchAgents` — all executable on the next shell login.

**CVE-2026-50549** attacks the symlink guardrail. Cursor's canonicalization check confirms a symlink's real target sits inside the project. When canonicalization *fails* (target doesn't exist, permissions stripped), Cursor gives up and trusts the symlink's in-project path instead — a classic fail-open. A write-only symlink pointing at Cursor's sandbox binary sails through and lets the attacker overwrite the very binary that contains the agent *(Source: [Start Debugging — DuneSlide Technical Analysis](https://startdebugging.net/2026/07/cursor-duneslide-prompt-injection-sandbox-escape-rce/))*.

The deeper lesson: `run_terminal_cmd` is not a user typing commands. It is a tool the model invokes with arguments the model chose, and those arguments came from text the model read. Once you accept that any content flowing into the context window is potentially adversarial, a parameter like `working_directory` stops looking like configuration and starts looking like attacker input.

> *For a full breakdown of the DuneSlide exploit chain, see our companion article: [/2026/07/cursor-duneslide-cve-2026-50548-rce-vulnerabilities/](/2026/07/cursor-duneslide-cve-2026-50548-rce-vulnerabilities/)*

---

## Industry Response: Tooling, Guidance, and the Gaps

### Anthropic: Auth Flows and Updated Guidance

Anthropic introduced MCP authentication and approval flows in its mid-2026 server and SDK updates. Claude now supports OAuth 2.1 with PKCE for remote MCP servers, and the approval flow requires explicit consent before connecting. The security guidance published after OX Security's disclosure added warnings about STDIO adapters — but did not change the underlying protocol behavior. Anthropic maintains that `StdioServerParameters` is a low-level interface designed to launch processes, and sanitization is the client developer's responsibility *(Source: [Anthropic — MCP Authentication Documentation](https://claude.com/docs/connectors/building/authentication))*.

### OWASP: MCP Top 10 and Q1 2026 Exploit Round-up

OWASP's GenAI Security Project published its **Q1 2026 Exploit Round-up** covering January through early April 2026. The report documents eight real-world incidents where AI systems were compromised, and specifically calls out MCP as a vector for prompt injection, supply chain compromise, and remote code execution. The OWASP **MCP Top 10** framework maps known MCP vulnerabilities to the established categories: tool poisoning (A1), authorization gaps (A2), command injection (A3), path traversal (A4), and supply chain backdoors (A5), among others *(Source: [OWASP GenAI Exploit Round-up Q1 2026](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) and [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/))*.

### AgentSeal: The Public Registry

AgentSeal's [awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security) repository is the most comprehensive public inventory of MCP server risk. Nine analyzers assign trust scores (0–100) measuring how safely an AI agent can use each server — not the code quality of the server itself, but the attack surface an adversary could exploit through prompt injection or tool poisoning. Updated daily, the registry serves as a pre-installation vetting layer for any team integrating public MCP servers *(Source: [AgentSeal MCP Registry](https://agentseal.org/mcp))*.

### Cisco: "The Connective Tissue Is Woefully Insecure"

Cisco's **State of AI Security 2026 Report**, published February 19, 2026, flagged the Model Context Protocol as an emerging threat vector. The report characterized MCP — and similar agent-to-agent protocols — as the "connective tissue" of the AI ecosystem whose vulnerability "has created a vast and often unmonitored attack surface." It specifically cited over-privileged agents and vulnerabilities in MCP and Google's Agent-to-Agent (A2A) protocol as top concerns for enterprise security teams *(Source: [Cybersecurity Dive — Cisco Warns on MCP](https://www.cybersecuritydive.com/news/ai-agents-model-context-protocol-cisco-report/812580/) and [Cisco — State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report))*.

### Azure AI Foundry

Microsoft's Azure AI Foundry Agent Service now supports MCP with published security best practices covering intent verification, risk reduction, and governance controls — including per-tool access policies, tracing with OpenTelemetry, and managed identity integration. Microsoft Sentinel's MCP tool collection can be attached to AI agents within Foundry, applying the same RBAC model that governs human access to security data *(Source: [Microsoft — Foundry MCP Server Security Best Practices](https://learn.microsoft.com/en-us/azure/foundry/mcp/security-best-practices))*.

---

## Enterprise Mitigations: What Works Today

### 1. MCP Server Whitelisting and Vetting

Before installing any MCP server: verify the source, check permissions it requests, and cross-reference against AgentSeal's registry. A server that provides cat pictures doesn't need filesystem access. Pipelab's Pipelock proxy scans tool definitions recursively for injection patterns before they enter the agent's context *(Source: [PipeLab — MCP Vulnerabilities Reference](https://pipelab.org/learn/mcp-vulnerabilities/))*.

### 2. Read-Only Tool Policies

The single highest-ROI control: audit every MCP-connected tool and downgrade write permissions where read-only access is sufficient. AgentSeal's scoring shows that servers with broad write capabilities (file system, shell execution, network egress) carry 3–5× more security findings than read-only equivalents.

### 3. Permission Review Cadence

CVE-2025-54136 (MCPoison) taught us that one-time approval is equivalent to no authorization. Every MCP config change should trigger a fresh approval tied to a current hash of the server and tool definitions. Check Point recommends re-validation on every config modification, not just on initial installation.

### 4. Sandboxed Execution

Containerize every MCP server. Chroot filesystem access. Bind-mount only the directories the server needs. For STDIO-based servers, run them under a dedicated user with least-privilege permissions. The DuneSlide exploit succeeded because the sandbox trusted agent-chosen parameters — the sandbox boundary itself needs scrutiny.

### 5. Config File Integrity Monitoring

Monitor `.mcp.json`, `.claude/settings.json`, `.cursor/rules/mcp.json`, and equivalent files in every repository. Treat changes to these files with the same review gates as CI pipeline YAML changes. Never enable `enableAllProjectMcpServers` or equivalent global auto-approve flags. Pin `ANTHROPIC_BASE_URL` and equivalent API endpoints to their defaults.

### 6. Runtime DLP on Tool Output

Scan tool responses for injection patterns before they enter the agent's context. Pipelock's six-pass response scanning covers normalized text, invisible-character retries, leetspeak, whitespace variants, vowel folding, and base64/hex decode — recognizing that adversaries will mutate strings to evade simple pattern matching.

---

## Open Problems: What the Protocol Still Doesn't Solve

**No standardized authentication.** The MCP spec defines transports and message formats. Individual servers implement authentication — or don't. OAuth 2.1 with PKCE is emerging as the baseline but remains optional. Large swaths of the ecosystem ship with no authentication at all.

**No permission model in the spec.** MCP has no concept of scoped tool access. An agent connected to a GitHub MCP server has the full permissions of the OAuth token — there is no way to say "read issues but not code" within the protocol itself. This is an architectural gap that gateways (Docker MCP Gateway, MintMCP, Stacklok) fill as middleware, but it should be protocol-level.

**Rate limiting gaps.** No mechanism in the spec prevents a tool from making 10,000 calls in a minute. User consent fatigue — flooding the approval dialog with harmless requests until the user auto-approves the malicious one — is a documented attack pattern with no protocol-level defense *(Source: [Palo Alto Networks — MCP Security Exposed](https://live.paloaltonetworks.com/t5/community-blogs/mcp-security-exposed-what-you-need-to-know-now/ba-p/1227143))*.

**No response integrity.** The protocol has no mechanism to verify that tool output hasn't been tampered with between the server and the agent. In the composability chaining attack, the agent cannot distinguish clean output from poisoned output — and the protocol doesn't help it.

**No cross-session drift detection.** A server that passes inspection at install can change its tool descriptions in the next update. Hash fingerprinting and drift detection exist as third-party solutions (Pipelock), but the protocol itself has no facility for it.

---

## Outlook: MCP Spec v2 and the July 2026 Revision

The July 28, 2026 specification revision — the largest since MCP's launch — addresses some of these gaps, but not all. Key changes *(Source: [Stacklok — Enterprise Readiness Guide for the July 2026 MCP Spec Update](https://stacklok.com/resources/enterprise-readiness-guide-for-the-july-2026-mcp-spec-update/))*:

- **Stateless protocol.** Protocol sessions and the initialization handshake are removed. Protocol version, identity, and capabilities travel with each request. This eliminates some session-level attack surface but shifts the burden of state management to application code.
- **OAuth/OIDC formalized.** The revision adds OAuth 2.1 and OpenID Connect requirements — the first time authentication appears in the spec itself.
- **W3C Trace Context.** Formalized `traceparent`, `tracestate`, and `baggage` propagation for OpenTelemetry-compatible tracing. Audit trails become protocol-level, not afterthoughts.
- **JSON Schema 2020-12.** Full support for modern schema validation, enabling stricter input/output contracts.
- **Discovery as first-class.** Servers must implement `server/discover` to advertise versions, capabilities, and identity.

What's **not** addressed: a permission model for scoped tool access, response integrity verification, rate limiting, or cross-session drift detection. These remain in the ecosystem layer — gateways, proxies, and runtime inspection tools — rather than the protocol.

The revision is a step forward, but enterprises adopting MCP in production should not wait for protocol-level fixes. The defense-in-depth stack — network egress control, gateway-based authentication, static scanning, runtime inspection, and identity-aware audit — is what works today. The spec will catch up. The attack surface won't wait.

---

## FAQ

**Q: Are these vulnerabilities in the protocol itself or in server implementations?**

Most assigned CVEs are in server implementations that inherit the SDK's design choices. The underlying issue — STDIO transport executing unsanitized commands — is an architectural property of the protocol. Anthropic considers it "by design"; the security community considers it an anti-pattern. Both are correct from their respective angles.

**Q: Is my Claude Code / Cursor / Copilot setup vulnerable?**

Check your version. Cursor DuneSlide is patched in 3.0+. Claude Code hooks/MCP CVEs are patched in versions after January 2026. The MCP servers you've installed manually are *your* responsibility — audit them, pin their versions, and never enable `enableAllProjectMcpServers`.

**Q: How do I audit my MCP servers?**

Start with AgentSeal's registry for any public servers you use. For internal servers, apply the Endor Labs checklist: check for path traversal (82% of servers are vulnerable), command injection patterns (34%), and run static scanners (Cisco mcp-scanner, Snyk agent-scan). Route live traffic through a runtime inspection proxy.

**Q: Does the July 2026 spec revision fix everything?**

No. It adds OAuth and tracing, but permission models, response integrity, rate limiting, and drift detection remain ecosystem responsibilities. Expect these in a future revision, likely late 2026 or early 2027.

**Q: What's the number one thing I should do today?**

Disable automatic MCP server installation from public registries. Move every internal MCP server into an isolated container. Audit the tool permissions your agents actually use and downgrade from write to read where possible. That alone eliminates the majority of the attack surface documented here.

---

## Further Reading

- [PipeLab — MCP Vulnerabilities: Known Risks and Defenses](https://pipelab.org/learn/mcp-vulnerabilities/) — Canonical reference for all nine MCP attack classes
- [OX Security — The Mother of All AI Supply Chains](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce) — Original advisory with full CVE list
- [Cato AI Labs — DuneSlide: Two Critical RCE Vulnerabilities](https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/) — CVE-2026-50548/50549 disclosure
- [Check Point Research — MCPoison in Cursor IDE](https://research.checkpoint.com/2025/cursor-vulnerability-mcpoison/) — CVE-2025-54136
- [CSO Online — Top 10 MCP Vulnerabilities](https://www.csoonline.com/article/4023795/top-10-mcp-vulnerabilities.html) — Maria Korolov's comprehensive taxonomy
- [AgentSeal — awesome-mcp-security](https://github.com/getagentseal/awesome-mcp-security) — Daily-updated risk scores for 800+ MCP servers
- [OWASP — MCP Top 10](https://owasp.org/www-project-mcp-top-10/) — Vulnerability classification framework
- [OWASP — GenAI Exploit Round-up Q1 2026](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) — Eight real-world AI exploitation incidents
- [Cisco — State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report) — Enterprise threat landscape with MCP analysis
- [Stacklok — Enterprise Readiness Guide for July 2026 MCP Spec](https://stacklok.com/resources/enterprise-readiness-guide-for-the-july-2026-mcp-spec-update/) — Migration planning for the protocol revision
- [Invariant Labs — GitHub MCP Vulnerability](https://invariantlabs.ai/blog/mcp-github-vulnerability) — Prompt injection through tool responses
- [Endor Labs — MCP AppSec Analysis](https://www.endorlabs.com/learn/classic-vulnerabilities-meet-ai-infrastructure-why-mcp-needs-appsec) — Static analysis of 2,614 implementations
