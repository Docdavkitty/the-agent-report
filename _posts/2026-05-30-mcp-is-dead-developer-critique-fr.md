---
layout: post
title: >
  "MCP est-il mort ? Analyse des doutes des développeurs sur le protocole de contexte de modèle"
date: 2026-05-30 09:00:00 +0200
lang: fr
ref: mcp-is-dead-developer-critique
permalink: /fr/2026/05/mcp-is-dead-developer-critique/
translation_of: /2026/05/mcp-is-dead-developer-critique/
author: The Agent Report
categories: ["tools-frameworks"]
tags: [MCP, "model-context-protocol", "tool-use", "developer-experience", "agent-infrastructure", "traduction-francaise"]
last_modified_at: 2026-07-11 15:01:27 +0000
hero_image: /assets/images/hero/hero-mcp-is-dead-developer-critique.jpg
meta_description: >
  "Le protocole de contexte de modèle (MCP) devait être le grand unificateur, un standard pour que les agents IA interagissent avec les outils et services nécessaires à leur travail."
description: >
  "Le protocole autrefois salué comme l'« USB-C de l'IA » est désormais critiqué. Les développeurs de Quandri ont analysé les chiffres, et le bilan est accablant pour le contexte."
reading_time: 8
---

Le Model Context Protocol (MCP) devait être le grand unificateur — une norme permettant aux agents d'IA de dialoguer avec les outils et services dont ils ont besoin pour accomplir leurs tâches. Lancé fin 2024, il a rapidement été sacré « l'USB-C de l'écosystème IA », adopté par Anthropic, OpenAI et un nombre croissant de fournisseurs d'outils.

Mais la lune de miel pourrait être terminée. Une [nouvelle analyse accablante](https://www.quandri.io/engineering-blog/mcp-is-dead) de Quandri Engineering, combinée à un [débat animé sur Hacker News](https://news.ycombinator.com/item?id=48330436) (195 points, 174 commentaires), a sérieusement entaché la réputation du MCP. Le verdict ? Le MCP dévore le contexte, manque de fiabilité et chevauche considérablement les outils CLI et API existants qui fonctionnent déjà parfaitement.

## Problème 1 : Il dévore la fenêtre de contexte

Le constat le plus accablant de l'analyse de Quandri est le volume de tokens consommé par les définitions d'outils MCP. Dans leur pile réelle (serveurs MCP Linear, Notion, Slack et Postgres), **les seules définitions d'outils ont consommé plus de 21 000 tokens** — soit 10,5 % d'une fenêtre de contexte Claude 200K, et **16,5 % des 128K de GPT-4o**.

| Serveur MCP | Outils | Tokens estimés |
|-------------|--------|----------------|
| Linear      | 42     | ~12 807        |
| Notion      | 14     | ~4 039         |
| Slack       | 12     | ~3 792         |
| Postgres    | 9      | ~438           |
| **Total**   | **77** | **~21 077**    |

Le problème est architectural. Chaque définition d'outil inclut son schéma JSON — paramètres, descriptions, types de retour — et chacun est chargé dans le contexte, que le modèle l'utilise ou non. Linear à lui seul fournit 42 définitions d'outils (~12 807 tokens), même si vous n'utilisez jamais que `get_issue` et `save_issue`.

> **Analogie du restaurant tirée de l'article :** « Vous vous asseyez et 10 menus sont étalés sur la table. Il n'y a plus de place pour la nourriture. »

**Mise à jour :** Depuis ces mesures, Claude Code a déployé [Tool Search with Deferred Loading](https://docs.anthropic.com/claude/docs/tool-use), qui charge les schémas d'outils MCP à la demande et réduit l'utilisation du contexte de plus de 85 %. Ce problème spécifique est donc en voie d'atténuation — mais les préoccupations architecturales demeurent.

## Problème 2 : Faible fiabilité opérationnelle

Les problèmes de fiabilité du MCP sont plus difficiles à écarter. L'équipe de Quandri a documenté plusieurs modes de défaillance découlant de l'architecture du MCP :

| Problème | Détail |
|----------|--------|
| Échec d'initialisation, ré-authentification répétée | Nécessite de démarrer et de maintenir un processus séparé |
| Réponses IA plus lentes | Aller-retour vers un serveur externe à chaque appel d'outil |
| Mort d'outil en cours de session | Le processus du serveur MCP plante en milieu de conversation |
| Permissions opaques | Incertitude sur les permissions réelles de chaque outil |

Les chiffres de performance sont sans appel. L'auteur de l'article original a comparé Jira MCP à son API REST directe : **MCP était 3× plus lent par appel, et 9,4× plus lent au premier appel** en incluant la surcharge d'initialisation. Ce n'est pas un problème spécifique à Jira — c'est architectural. Chaque serveur MCP ajoute une couche de processus entre le LLM et l'API sous-jacente.

## Problème 3 : Chevauchement avec les CLI/API existants

Peut-être la critique la plus fondamentale : le MCP duplique des fonctionnalités qui existent déjà et fonctionnent mieux.

| Aspect | CLI / API | MCP |
|--------|-----------|-----|
| Parité humain-machine | Mêmes commandes pour humains et LLM | N'existe que dans les conversations LLM |
| Composabilité | Pipes, jq, grep librement combinables | Verrouillé sur le format de retour du serveur |
| Débogage | Reproductible immédiatement dans le terminal | Reproductible uniquement dans le contexte de la conversation |
| Données d'apprentissage | Déjà appris à partir de man pages, StackOverflow | Nécessite des définitions d'outils séparées |
| Coût d'installation | Déjà installé pour la plupart | Configuration du serveur, authentification, gestion des processus nécessaires |

La comparaison des tokens est brutale. Pour consulter le même ticket Linear :

- **Approche CLI :** ~200 tokens au total (50 pour la commande curl, 150 pour la réponse)
- **Approche MCP :** ~12 957 tokens au total (12 807 pour les définitions d'outils toujours chargées, 150 pour l'appel réel)

C'est **65× plus de tokens** pour la même opération.

### L'alternative centrée sur la CLI

L'alternative proposée est élégamment simple : fournir les outils CLI existants aux LLM. Les LLM ont déjà appris à partir de man pages, de StackOverflow et de millions de gists GitHub. Ils savent déjà construire des commandes curl, les passer dans jq et grep les résultats. Aucun nouveau protocole n'est nécessaire.

```bash
# Approche CLI — fonctionne aujourd'hui, aucun serveur MCP nécessaire
curl -s -H "Authorization: Bearer $LINEAR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ issue(id: \"ISSUE-ID\") { title state { name } assignee { name } } }"}' \
  https://api.linear.app/graphql
```

## Quelle est la véritable histoire ?

Soyons justes : le MCP ne va pas disparaître du jour au lendemain. L'investissement dans l'écosystème est considérable — Anthropic a [acquis Stainless](https://the-agent-report.com/2026/05/anthropic-acquires-stainless-sdk-mcp-agent-frontier) spécifiquement pour accélérer les outils MCP, et des plateformes majeures comme GitHub, Notion et Linear ont déployé des serveurs MCP officiels. Le protocole résout un vrai problème : fournir une interface standardisée pour que les agents d'IA interagissent avec des services externes.

Mais la critique soulève des questions importantes sur la **philosophie architecturale**. L'approche « SSH dans une machine et utilise la CLI » qui a rendu les LLM comme Claude Code et Codex si efficaces est fondamentalement plus simple que le modèle du serveur MCP. Elle ne nécessite aucune nouvelle infrastructure, aucune négociation de protocole, aucune gestion séparée du cycle de vie des processus.

Comme l'a résumé un commentateur sur HN : *« MCP donne l'impression de résoudre un problème qui n'existe pas — nous avions déjà des interfaces fonctionnelles entre logiciels. La percée, c'est que les LLM peuvent désormais utiliser ces mêmes interfaces. »*

## En résumé

Le [post original « MCP is dead »](https://www.quandri.io/engineering-blog/mcp-is-dead) — qui donne son nom à ce débat — est peut-être volontairement provocateur. Mais les données qui le sous-tendent sont réelles. Pour les équipes qui construisent des workflows d'agents d'IA aujourd'hui, le choix entre MCP et l'accès direct CLI/API n'est pas idéologique : c'est un coût mesurable en tokens, en latence et en fiabilité.

L'approche la plus intelligente ? **Ne choisissez pas.** Utilisez MCP pour ce qu'il fait bien (découverte standardisée, prototypage rapide, compatibilité avec l'écosystème) et revenez aux appels CLI/API directs pour les opérations à haute fréquence et sensibles à la latence. Les meilleures architectures d'agents seront agnostiques — prenant en charge les deux protocoles de manière transparente.

*Quelle est votre expérience avec MCP ? Misez-vous sur le protocole ou explorez-vous des alternatives centrées sur la CLI ? Partagez vos réflexions dans la discussion sur [Hacker News](https://news.ycombinator.com/item?id=48330436).*