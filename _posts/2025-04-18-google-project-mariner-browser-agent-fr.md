---
layout: post
title: "Project Mariner de Google : des agents dans le navigateur"
date: 2025-04-18 16:00:00 +0200
lang: fr
ref: google-project-mariner-browser-agent
permalink: /fr/2025/04/google-project-mariner-browser-agent/
translation_of: /2025/04/google-project-mariner-browser-agent/
author: The Agent Report
categories: [research, industry]
tags: [Google, "browser-agents", Gemini, "Project-Mariner", "traduction-francaise"]
last_modified_at: 2026-08-25 12:24:39 +0000
hero_image: /assets/images/hero/hero-04-18-google-project-mariner-browser-agent.jpg
meta_description: >
  "Google dévoile Project Mariner, un agent de navigateur Gemini qui parcourt des sites, remplit des formulaires et exécute des tâches multi-étapes dans Chrome."
description: >
  "Google dévoile Project Mariner, un agent de navigateur Gemini qui parcourt des sites, remplit des formulaires et réalise des tâches multi-étapes autonomes."
reading_time: 5
---

Google a dévoilé **Project Mariner**, un agent expérimental basé sur le navigateur et propulsé par Gemini. Ce prototype peut naviguer sur des sites web, remplir des formulaires, extraire des données et accomplir des tâches web en plusieurs étapes — le tout via une extension Chrome.

## Fonctionnement

Project Mariner combine les capacités de vision de Gemini, qui servent à comprendre la mise en page des pages web, avec un modèle d’action spécialisé qui détermine l’interaction suivante. Le système :

1. Capture l’état actuel du navigateur
2. Identifie les éléments pertinents de la page
3. Planifie une séquence d’actions
4. Exécute via le Chrome DevTools Protocol
5. S’adapte en fonction des résultats

## Cas d’utilisation en démonstration

Dans les démonstrations de Google, Project Mariner a pris en charge :

- **Recherche de produits** — Comparaison des prix chez plusieurs détaillants
- **Planification de voyage** — Recherche de vols, comparaison des options et remplissage des formulaires de réservation
- **Extraction de données** — Récupération de données structurées depuis plusieurs pages web dans un tableur
- **Automatisation de formulaires** — Remplissage de formulaires de candidature sur plusieurs pages

## Paysage concurrentiel

Project Mariner arrive sur un marché déjà encombré, aux côtés de :

- **Claude Computer Use** (Anthropic) — Ordinateur complet, pas seulement le navigateur (voir notre [analyse approfondie de l’utilisation de l’ordinateur par Claude]({% post_url 2025-04-26-claude-computer-use-gui-agents %}))
- **Operator** (OpenAI) — Agent basé sur le navigateur en avant-première
- **Browser Use** (open source) — Framework d’agent de navigateur piloté par la communauté

Ce qui distingue Project Mariner, c’est son **intégration profonde avec Chrome** — comme il est développé par Google, il a accès à des composants internes du navigateur auxquels les agents tiers ne peuvent pas accéder.

## Confidentialité et sécurité

Google a mis en place plusieurs garde-fous :

- Les utilisateurs doivent activer explicitement l’agent à chaque session
- Les actions sensibles (paiements, connexions) nécessitent une confirmation manuelle
- L’agent fonctionne dans un contexte de navigateur isolé
- Toutes les actions sont journalisées pour permettre à l’utilisateur de les examiner

Project Mariner n’a pas encore été rendu public, mais cela témoigne de l’engagement sérieux de Google dans le domaine des agents. Pour en savoir plus sur les ambitions de Google en matière d’agents, consultez nos articles sur [l’agent Remy de Google]({% post_url 2026-05-06-google-remy-agent-openclaw-rival %}) et [AlphaEvolve de DeepMind]({% post_url 2026-05-08-deepmind-alphaevolve-mainstream %}).