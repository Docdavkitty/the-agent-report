---
layout: post
title: "Hermes Agent v0.11 : les nouveautés du runtime IA open source"
date: 2025-04-28 10:00:00 +0200
lang: fr
ref: hermes-agent-v011-release
permalink: /fr/2025/04/hermes-agent-v011-release/
translation_of: /2025/04/hermes-agent-v011-release/
author: The Agent Report
categories: ["hermes-agent"]
tags: [Hermes Agent, Nous Research, release, "open-source", "traduction-francaise"]
last_modified_at: 2026-08-23 12:18:49 +0000
hero_image: /assets/images/hero/hero-04-28-hermes-agent-v011-release.jpg
meta_description: >
  "Hermes Agent v0.11 apporte un support MCP amélioré, de nouveaux outils et un routage multi-modèles optimisé pour le runtime open source de Nous Research."
description: >
  "Hermes Agent v0.11 offre un support MCP amélioré, de nouveaux outils et un routage multi-modèles optimisé dans le runtime open source de Nous Research."
reading_time: 5
---

Hermes Agent, le runtime d'agent IA open source de Nous Research, évolue régulièrement. La version 0.11 introduit plusieurs améliorations significatives pour les développeurs qui créent des applications agentiques.

## Intégration MCP améliorée

La mise à jour la plus notable est une intégration plus poussée avec le **Model Context Protocol (MCP)**. Hermes prend désormais en charge :

- Un client MCP natif pour se connecter à tout serveur compatible MCP
- La découverte automatique des outils et des ressources des serveurs MCP
- Un repli transparent lorsque les serveurs MCP sont indisponibles

Cela fait d'Hermes l'un des frameworks d'agents les plus compatibles avec MCP disponibles. Pour en savoir plus sur MCP, lisez notre [analyse approfondie du protocole]({% post_url 2025-04-28-mcp-protocol-agentic-tool-use %}).

## Nouveaux ensembles d'outils

La version 0.11 introduit un système d'ensembles d'outils affiné qui permet aux développeurs de restreindre les capacités des agents de manière plus granulaire :

- **Ensemble d'outils navigateur** — Navigation et interaction avec un navigateur headless
- **Ensemble d'outils terminal** — Exécution sécurisée de commandes shell
- **Ensemble d'outils fichiers** — Opérations de lecture/écriture avec restrictions de chemin
- **Ensemble d'outils web** — Requêtes HTTP et recherche web
- **Ensemble d'outils vision** — Capacités d'analyse d'images

Chaque ensemble d'outils peut être activé ou désactivé pour chaque agent, offrant un contrôle précis sur ce à quoi chaque agent peut accéder.

## Routage multi-modèles

Les agents peuvent désormais être configurés pour utiliser différents modèles pour différentes tâches :

```yaml
agent:
  reasoning_model: deepseek-v4-pro
  code_model: claude-sonnet-4
  vision_model: gpt-4o
```

Cela permet aux développeurs d'optimiser le coût et les capacités par tâche plutôt que d'utiliser un seul modèle pour tout.

## Prise en main

Hermes Agent fonctionne sur toute machine Linux et peut être installé via pip :

```bash
pip install hermes-agent
hermes setup
```

Le projet est entièrement open source sous licence MIT. Consultez la [documentation](https://hermes-agent.nousresearch.com) et le [dépôt GitHub](https://github.com/nousresearch/hermes) pour plus de détails. Pour un contexte plus large sur l'écosystème des agents open source, consultez notre [guide ultime des frameworks d'agents]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).