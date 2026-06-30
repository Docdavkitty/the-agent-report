---
layout: post
title: >
  "Hermes Agent franchit 188 000 étoiles GitHub alors que Skills Hub dépasse les 90 000 compétences"
date: 2026-06-10 10:00:00 +0200
lang: fr
ref: hermes-agent-188k-stars-90k-skills-ecosystem-june2026
permalink: /fr/2026/06/hermes-agent-188k-stars-90k-skills-ecosystem-june2026/
translation_of: /2026/06/hermes-agent-188k-stars-90k-skills-ecosystem-june2026/
author: The Agent Report
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", "open-source", ecosystem, "skills-hub", community, "github-stars", plugins, "traduction-francaise"]
last_modified_at: 2026-06-30 15:02:20 +0000
hero_image: >
  /assets/images/hero/hero-hermes-agent-188k-stars-90k-skills-ecosystem-june2026.jpg
meta_description: >
  "Hermes Agent a franchi 188 000 étoiles GitHub et le Skills Hub est passé de 310 à 90 881 compétences sur 12 registres, devenant le framework d'agents open-source à la croissance la plus rapide de 2026 selon Dealroom."
description: >
  "Hermes Agent franchit 188 000 étoiles GitHub tandis que Skills Hub dépasse les 90 000 compétences sur 12 registres. Un aperçu de l'écosystème communautaire qui en fait le framework d'agents open-source à la croissance la plus rapide de 2026."
reading_time: 6
---

Lors de notre dernier [état des lieux de l'écosystème Hermes Agent]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}) le 25 mai, les chiffres étaient déjà impressionnants : **165 000 étoiles GitHub, 27 300 forks et plus de 310 compétences communautaires**. Deux semaines plus tard, ces chiffres semblent bien modestes.

Au 10 juin 2026, le dépôt [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) a franchi la barre des **188 781 étoiles GitHub** — soit un gain de plus de 23 000 étoiles en environ deux semaines. Le Skills Hub répertorie désormais **90 881 compétences réparties dans 12 registres**, contre quelques centaines auparavant. Et [Dealroom](https://dealroom.co) a officiellement désigné Hermes Agent comme **le framework d'agents open-source à la croissance la plus rapide de 2026**.

> « L'agent IA open-source auto-améliorant de Nous Research a désormais accumulé plus de 180 000 étoiles GitHub en moins de quatre mois depuis son lancement le 25 février. » — [Ewan Mak, Medium](https://medium.com/@tentenco/hermes-agent-desktop-app-everything-you-need-to-know-about-nous-researchs-self-improving-ai-agent-3cb59bd31e5f)

L'histoire en surface, c'est la croissance. L'histoire plus profonde est *structurelle* — l'écosystème se réorganise autour de la découvrabilité, de la curation et d'une infrastructure de plugins qui n'existait pas il y a deux semaines.

## Le Skills Hub : de quelques centaines à 90 881 compétences

Le changement le plus spectaculaire est le Skills Hub. Fin mai, la communauté partageait les compétences de manière informelle — GitHub gists, fils Reddit, épingles Discord. Le [Skills Hub officiel](https://hermes-agent.nousresearch.com/docs/skills/) a changé la donne.

Répertoriant désormais **90 881 compétences dans 12 registres**, le Hub s'actualise automatiquement deux fois par jour et inclut les contributions de NVIDIA/skills (ajouté aux sources fiables dans la [v0.16.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5)), aux côtés des registres communautaires. Une compétence installée via le Hub n'est pas qu'un simple téléchargement de fichier — c'est un artefact versionné et auditable que le **Curator** intégré d'Hermes peut noter, élaguer et consolider automatiquement.

L'écosystème des compétences a également engendré sa propre métacouche : [lobehub.com](https://lobehub.com/skills/aradotso-trending-skills-awesome-hermes-agent) propose désormais un marché de compétences tendance pour Hermes Agent, mis à jour quotidiennement, avec des phrases de déclenchement et des exemples d'utilisation pour chaque compétence.

## La couche de curation : Awesome Lists et Atlas

Il y a deux semaines, trouver des outils communautaires signifiait parcourir Reddit ou rechercher sur GitHub. Aujourd'hui, il existe trois surfaces de découverte majeures :

| Ressource | Étoiles | Description |
|---|---|---|
| [SamurAIGPT/awesome-hermes-agent](https://github.com/SamurAIGPT/awesome-hermes-agent) | Nouveau | Liste organisée complète — compétences, plugins, outils, intégrations, modèles de déploiement. Mise à jour il y a 2 jours. |
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | En croissance | Guide de l'écosystème organisé avec des flux de sécurité et des boucles d'évolution. Mise à jour il y a 1 semaine. |
| [Hermes Atlas](https://hermesatlas.com/) (ksimback/hermes-ecosystem) | Carte communautaire | Plus de 100 outils cartographiés avec des données GitHub en direct et une recherche alimentée par l'IA. Publication du rapport « The State of Hermes — May 2026 ». |

C'est le signe classique d'un écosystème open-source en maturation : le projet n'a plus besoin de vous dire ce qui est disponible — la communauté construit la carte.

## Nouvelle infrastructure de plugins : Hermes LCM

La version Surface v0.16.0 a officiellement introduit l'[emplacement du plugin de moteur de contexte](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin), et la communauté a répondu immédiatement. **[stephenschoettler/hermes-lcm](https://github.com/stephenschoettler/hermes-lcm)** — publié il y a seulement deux jours — est un plugin de gestion de contexte sans perte (Lossless Context Management) qui remplace le résumé par défaut avec perte par un **moteur de contexte basé sur un DAG**.

Au lieu que l'agent résume périodiquement et supprime les anciens messages (l'approche standard qui perd inévitablement en nuance), LCM construit un graphe orienté acyclique du contexte de la conversation. Chaque message, appel d'outil et résultat est préservé — le moteur élague simplement le parcours du graphe, pas les données. Pour les agents de longue durée qui opèrent sur plusieurs jours ou semaines (tâches cron, opérateurs d'infrastructure, assistants de recherche), c'est transformateur.

L'architecture du plugin elle-même est significative : elle signifie que la communauté peut désormais étendre les composants internes d'Hermes à des points d'extension bien définis, plutôt que de forker le noyau.

## Signaux grand public : « STARTUP EDITION » et attention médiatique

La croissance de l'écosystème est remarquée en dehors des cercles de développeurs. Un récapitulatif [« STARTUP EDITION » de juin 2026](https://blog.mean.ceo/hermes-agent-news-june-2026/) sur blog.mean.ceo présente Hermes Agent explicitement aux fondateurs et investisseurs, mettant en avant l'architecture auto-hébergée et toujours active comme différenciateur par rapport aux agents SaaS. Plusieurs publications Medium ont publié des guides approfondis ([Ewan Mak](https://medium.com/@tentenco/hermes-agent-desktop-app-everything-you-need-to-know-about-nous-researchs-self-improving-ai-agent-3cb59bd31e5f), [ThePlanetTools](https://theplanettools.ai/blog/hermes-desktop-nous-research-open-source-gui-app-june-2026)), et un [guide Substack](https://nervegna.substack.com/p/hermes-agent-desktop-the-full-guide) guide désormais les concepteurs de produits, les chefs de produit et les directeurs marketing à travers des cas d'utilisation concrets.

Le [Hermes Agent Challenge sur DEV](https://dev.to/challenges/hermes-agent-2026-05-15) — couvert [dans notre dernier rapport]({% post_url 2026-06-01-hermes-agent-challenge-results-may-2026 %}) — a produit 14 projets communautaires, mais les effets d'entraînement se poursuivent : plusieurs participants au défi ont depuis publié leurs projets en tant que dépôts open-source autonomes, alimentant ainsi l'écosystème.

## Qu'est-ce qui alimente cette croissance ?

Trois facteurs structurels sont à l'origine de cette accélération :

1. **La Surface Release (v0.16.0)** est sortie le 5 juin avec 874 commits, 542 PR fusionnées et Hermes Desktop — une application native pour macOS, Windows et Linux. L'accès au bureau a abaissé la barrière de « configurer un outil en ligne de commande » à « télécharger et commencer à discuter ».

2. **La boucle d'auto-évolution** — [hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) avec DSPy + GEPA, [couverte le 8 juin]({% post_url 2026-06-08-hermes-agent-self-evolution-dspy-gepa-june2026 %}) — signifie qu'Hermes peut désormais *améliorer ses propres compétences*, créant une boucle de rétroaction où plus d'utilisation produit de meilleures compétences, ce qui attire plus d'utilisateurs.

3. **La maturité de l'architecture des plugins** — l'emplacement du plugin de moteur de contexte, l'intégration MCP et le système de profils signifient que la communauté peut construire à la périphérie sans attendre l'équipe centrale. Le plugin hermes-lcm est passé du concept au dépôt publié en moins d'une semaine.

## Ce qu'il faut surveiller

Le jalon des 188 000 étoiles atteindra probablement les 200 000+ d'ici quelques semaines. Mais la trajectoire la plus intéressante est celle du Skills Hub : s'il maintient ne serait-ce qu'une fraction de son taux de croissance actuel, Hermes Agent disposera de la plus grande bibliothèque de compétences de tous les frameworks d'agents open-source — et de loin.

L'écosystème des plugins en est encore à ses balbutiements. L'emplacement du moteur de contexte est le premier d'une API de plugins qui deviendra probablement plus large. Les projets communautaires comme SkillClaw (une boucle d'évolution post-tâche au-dessus de la création de compétences intégrée d'Hermes) et les outils émergents de gestion de flotte suggèrent que la prochaine vague concernera la *coordination de plusieurs instances Hermes* — pas seulement l'exécution d'une seule.

Pour l'instant, les chiffres racontent une histoire claire : Hermes Agent ne fait pas que croître. Il développe l'infrastructure institutionnelle — registres de compétences, listes organisées, API de plugins, cartes communautaires — qui transforme un projet populaire en une plateforme.