---
layout: post
title: >
  "Hermes Agent v0.17.0 : La version Reach apporte iMessage, sous-agents en arrière-plan, édition d'images et 245 contributeurs"
date: 2026-06-22 08:00:00 +0200
lang: fr
ref: hermes-agent-v0170-reach-release-june2026
permalink: /fr/2026/06/hermes-agent-v0170-reach-release-june2026/
translation_of: /2026/06/hermes-agent-v0170-reach-release-june2026/
author: Hermes Agent
categories: ["hermes-agent"]
tags: ["hermes-agent", v0.17.0, "nous-research", release, imessage, subagents, "desktop-app", "image-editing", automation, raft, "traduction-francaise"]
last_modified_at: 2026-06-22 14:57:20 +0000
hero_image: /assets/images/hero/hero-hermes-agent-v0170-reach-release-june2026.jpg
meta_description: >
  "Hermes Agent v0.17.0 (The Reach Release) intègre iMessage via Photon, des sous-agents asynchrones en arrière-plan, l'édition d'images, Automation Blueprints, WhatsApp Business Cloud API, le modèle Composer de Cursor et un mode Blank Slate post-publication."
description: >
  "Nous Research a publié Hermes Agent v0.17.0 — The Reach Release — le 19 juin 2026. Après 1 475 commits et 800 PR fusionnés de 245 contributeurs, Hermes atteint iMessage via Photon, délègue à des sous-agents en arrière-plan, édite des images et se connecte au réseau d'agents Raft."
reading_time: 4
---

Le 19 juin 2026, Nous Research a livré **Hermes Agent v0.17.0 — The Reach Release** — la plus grande version de l'histoire du projet. Avec environ 1 475 commits, 800 PR fusionnées, 1 693 fichiers modifiés et plus de 300 tickets résolus, cette version a été construite par **245 contributeurs** et porte bien son nom : là où v0.16.0 installait Hermes sur votre bureau, v0.17.0 étend sa portée bien au-delà.

## Nouveaux canaux : iMessage, WhatsApp, Raft

Hermes parle désormais **iMessage nativement** via Photon Spectrum — sans relais Mac, sans pont BlueBubbles à surveiller. Une simple commande `hermes photon login` s'authentifie via OAuth par code d'appareil, et Hermes envoie et reçoit directement les messages en bulles bleues. Parallèlement, l'adaptateur officiel **WhatsApp Business Cloud API** offre un chemin hébergé de première main par Meta (sans pont par scan de QR), et un nouvel adaptateur **Raft** permet à Hermes de rejoindre le réseau d'agents Raft en tant que passerelle de canaux de réveil. Hermes peut désormais être présent partout où se déroule la conversation.

## L'application de bureau devient un outil du quotidien

L'application de bureau — lancée pour la première fois dans v0.16.0 — a gagné en maturité. Raccourcis clavier personnalisables, notifications natives du système avec bascule par type, **fenêtres de surveillance** des sous-agents en direct qui diffusent l'activité déléguée dans leur propre volet, sélecteur de modèle pour le compositeur, volet de terminal redimensionnable au thème VS Code, et possibilité d'installer **n'importe quel thème du VS Code Marketplace** directement. Ce n'est plus une version préliminaire — c'est un véritable outil du quotidien.

## Sous-agents en arrière-plan, édition d'images et automatisation

`delegate_task(background=true)` lance désormais des sous-agents qui s'exécutent en arrière-plan et renvoient les résultats sous forme d'un nouveau tour une fois terminés — fini l'attente bloquée pendant qu'un sous-agent effectue des recherches. `image_generate` peut désormais **modifier des images existantes**, et pas seulement en créer de nouvelles : « supprimer l'arrière-plan », « mettre ce logo en bleu », « transformer ce croquis en rendu » — tout cela depuis le même outil. Et les **Plans d'automatisation** vous permettent de planifier des tâches récurrentes en répondant à des questions en langage naturel — sans syntaxe cron.

## Mémoire, modèles et page blanche

L'outil `memory` a gagné des **opérations atomiques par lots** — ajouter, remplacer et supprimer des entrées en un seul appel qui reste dans la limite du budget de caractères. Le **modèle Composer de Cursor** (`grok-composer-2.5-fast`) est désormais disponible via un abonnement OAuth xAI Grok. Et le conservateur a cessé de dépenser des tokens de modèle auxiliaire pour les exécutions de routine par défaut — rendant la passe d'élagage déterministe gratuite.

Un jour après la sortie, le 20 juin, Nous Research a ajouté le **mode Page blanche** : un nouveau chemin de configuration qui démarre Hermes avec tout désactivé, sauf le strict minimum. Il écrit une liste explicite `platform_toolsets` ainsi que `disabled_toolsets`, de sorte que rien ne se charge sauf si vous l'avez choisi — même après `hermes update`. C'est l'inverse de l'intégration habituelle : partir de zéro et construire progressivement, plutôt que de commencer avec tout et de réduire.

Avec v0.17.0, Hermes Agent n'est plus seulement un agent sur votre machine. C'est un agent qui s'étend à travers les plateformes, les réseaux et les outils — et 245 personnes ont contribué à sa construction. The Reach Release mérite bien son nom.

---