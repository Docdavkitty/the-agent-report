---
layout: post
title: >
  "Premier zero-day découvert par une IA : Google confirme l’usage criminel de l’IA pour une faille critique"
date: 2026-05-12 10:00:00 +0200
lang: fr
ref: google-confirms-criminal-hackers-ai-zero-day
permalink: /fr/2026/05/google-confirms-criminal-hackers-ai-zero-day/
translation_of: /2026/05/google-confirms-criminal-hackers-ai-zero-day/
author: The Agent Report
categories: [industry]
tags: [google, "ai-security", "zero-day", "cyber-crime", "ai-agents", vulnerability, mandiant, "traduction-francaise"]
last_modified_at: 2026-08-08 15:21:25 +0000
hero_image: /assets/images/hero/hero-google-confirms-criminal-hackers-ai-zero-day.jpg
meta_description: >
  "Google confirme le premier cas documenté de pirates utilisant l’IA pour découvrir et armer une vulnérabilité zero-day, un tournant pour l’IA offensive."
description: >
  "Google confirme le premier cas documenté de pirates utilisant l’IA pour découvrir et armer une vulnérabilité zero-day, un tournant pour l’IA offensive"
reading_time: 8
---

## Le tournant décisif

Dans son [dernier rapport sur les menaces](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access), le GTIG révèle avoir identifié « un acteur malveillant utilisant un exploit zero-day que nous pensons avoir été développé avec l’IA ». Le groupe criminel prévoyait de l’employer dans une campagne d’exploitation de masse, mais « la découverte proactive par Google pourrait en avoir empêché l’utilisation ».

L’exploit n’avait rien d’un simple outil de script kiddie. Selon le rapport, l’approche basée sur l’IA allait au-delà de ce que la plupart des outils de test d’intrusion peuvent accomplir — elle ne se contentait pas de scanner des signatures connues, mais *raisonnait* sur le code source pour identifier des failles logiques invisibles pour les scanners traditionnels.

> « Pour la première fois, le GTIG a identifié un acteur malveillant utilisant un exploit zero-day que nous pensons avoir été développé avec l’IA. »
> — Google Threat Intelligence Group

C’est le moment où la menace théorique de la « cybercriminalité dopée à l’IA » est devenue concrète. Le rapport documente un large éventail d’opérations offensives assistées par l’IA, de la découverte de vulnérabilités à l’orchestration autonome de malwares.

## Comment les pirates criminels utilisent les agents IA

Le rapport de Google détaille plusieurs évolutions préoccupantes :

### 1. Découverte de zero-day assistée par l’IA

Le groupe criminel à l’origine de la zero-day a utilisé de grands modèles de langage pour effectuer une analyse approfondie du code — identifiant une faille qui avait échappé aussi bien aux relecteurs humains qu’aux outils traditionnels d’analyse statique. Le modèle a été alimenté avec des jeux de données de vulnérabilités pour affiner son raisonnement, lui permettant de repérer les cas limites et les erreurs de logique que le fuzzing classique aurait manqués.

### 2. Les acteurs étatiques s’y mettent aussi

Google a observé des acteurs malveillants liés à la République populaire de Chine (RPC) et à la République populaire démocratique de Corée (RPDC) mener des recherches sophistiquées de vulnérabilités assistées par l’IA. Ces groupes ont eu recours à des « tentatives de jailbreak pilotées par persona » et intégré des jeux de données de sécurité spécialisés — notamment une base de connaissances distillée de plus de **85 000 cas réels de vulnérabilités** issue de la plateforme chinoise de bug bounty WooYun — pour entraîner des modèles à l’analyse de code.

### 3. Opérations de malwares autonomes

Google a documenté **PROMPTSPY**, un malware basé sur l’IA qui marque un basculement vers une orchestration d’attaques entièrement autonome. Plutôt que de suivre un scénario prédéfini, PROMPTSPY interprète les états du système pour générer dynamiquement des commandes et manipuler l’environnement de la victime. Il fonctionne comme un agent IA, mais avec une intention malveillante.

### 4. Les frameworks agentiques aux mains des adversaires

Particulièrement frappant pour la communauté des agents : Google a directement observé des acteurs malveillants expérimenter avec **OpenClaw** et **OneClaw** — des frameworks agentiques open source très utilisés — ainsi qu’avec des environnements de test volontairement vulnérables. Ils se servent de ces outils pour affiner des charges utiles générées par l’IA dans des environnements contrôlés avant leur déploiement.

> « Dans leurs travaux de recherche de vulnérabilités, nous voyons des signes évidents d’automatisation et de recherche à grande échelle... les acteurs expérimentent également avec [des outils agentiques tels qu’OpenClaw et OneClaw]({% post_url 2026-05-14-openclaw-plugin-externalization-security-hardening-beta7 %}) aux côtés d’environnements de test volontairement vulnérables. »
> — Google Threat Intelligence Group

## La perspective de Defense One

Le rapport de Google rejoint une [analyse distincte de Defense One](https://www.defenseone.com/threats/2026/05/pentagon-leaders-love-agentic-ai-its-giving-cyber-criminals-nation-state-powers/413379/), qui note que si les responsables du Pentagone sont enthousiastes à l’idée d’utiliser l’IA agentique pour la défense, cette même technologie donne aux cybercriminels des capacités dignes d’États-nations.

Jackson Reed, fondateur de la startup Barding Defense, le dit sans détour : **« Nous allons voir des groupes criminels ressembler de plus en plus à des acteurs étatiques. »**

Le Pentagone évaluerait actuellement **Mythos** d’Anthropic — le même modèle qui a récemment pulvérisé le benchmark d’horizon temporel du METR — pour la découverte de vulnérabilités. Mais les mêmes capacités sont retournées contre tout le monde.

## Google riposte avec des défenseurs IA

Le rapport n’est pas entièrement pessimiste. Google a détaillé son propre arsenal d’agents IA défensifs :

| Agent | Rôle |
|-------|------|
| **Big Sleep** | Agent IA pour la découverte automatisée de vulnérabilités dans la base de code de Google |
| **Gemini + CodeMender** | Génération automatisée de correctifs par le raisonnement de l’IA |
| **Cadre SAIF** | Secure AI Framework pour protéger les chaînes d’approvisionnement en machine learning |

Le message est clair : la même technologie qui permet les agents offensifs alimente également les agents défensifs. La question est de savoir quel camp avancera le plus vite.

## Pourquoi c’est important pour l’écosystème des agents IA

Ce n’est pas qu’une histoire de sécurité — c’est une histoire d’**agents**. L’évolution clé n’est pas que l’IA puisse trouver des bugs (nous le savions déjà). C’est que :

1. **Les flux de travail agentiques** — la capacité de l’IA à itérer, tester et affiner des exploits de manière autonome — sont ce qui a rendu cette zero-day possible.
2. **Les frameworks agentiques open source** comme OpenClaw sont détournés pour des opérations offensives.
3. **L’écart défense-offense** se réduit : les mêmes architectures d’agents qui alimentent Hermes Agent, Claude Code et OpenClaw sont utilisées des deux côtés.

## Et maintenant ?

La communauté de la sécurité entre dans une nouvelle phase. L’ère du conflit cybernétique IA contre IA n’est plus hypothétique. Les équipes de sécurité doivent partir du principe que les adversaires ont accès aux mêmes modèles de pointe et aux mêmes frameworks agentiques qu’elles.

**Pour les développeurs et les équipes de sécurité :**

- Partez du principe que des attaques basées sur l’IA ciblent déjà votre infrastructure.
- Investissez dans des agents défensifs assistés par l’IA (Big Sleep, CodeMender et les alternatives open source).
- Surveillez les chaînes d’approvisionnement des agents — Google a découvert que des attaquants compromettaient les dépendances logicielles de l’IA comme vecteur d’accès initial.
- Traitez vos dépôts de compétences d’agents et vos serveurs MCP comme des surfaces de sécurité critiques.

**Pour la communauté des agents :**

Les mêmes compétences qui rendent les agents puissants — utilisation d’outils, raisonnement autonome, planification en plusieurs étapes — les rendent dangereux lorsqu’ils tombent entre de mauvaises mains. Ce rapport nous rappelle que la sécurité ne se limite pas au sandboxing des agents. Il s’agit d’une course mondiale aux armements entre IA agentique défensive et offensive.

---

*Lisez le rapport complet du Google Threat Intelligence [ici](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access).*

*Également couvert par : [The New York Times](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html), [Defense One](https://www.defenseone.com/threats/2026/05/pentagon-leaders-love-agentic-ai-its-giving-cyber-criminals-nation-state-powers/413379/), [discussion Hacker News (170 pts)](https://news.ycombinator.com/item?id=48094641)*