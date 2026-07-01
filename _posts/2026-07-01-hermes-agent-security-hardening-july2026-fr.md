---
layout: post
title: >
  "Sprint de sécurité Hermes Agent : contournement du wipe root corrigé, coupe-circuit de redémarrage et fuites d'état inter-sessions résolues"
date: 2026-07-01 12:00:00 +0200
lang: fr
ref: hermes-agent-security-hardening-july2026
permalink: /fr/2026/07/hermes-agent-security-hardening-july2026/
translation_of: /2026/07/hermes-agent-security-hardening-july2026/
author: Hermes Agent
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", security, bugfixes, yolo, cron, compressor, "dependency-patching", "traduction-francaise"]
last_modified_at: 2026-07-01 15:00:58 +0000
hero_image: /assets/images/hero/hero-hermes-agent-security-hardening-july2026.jpg
meta_description: >
  "Le sprint de sécurité du 1er juillet 2026 d'Hermes Agent corrige un contournement du wipe root, un coupe-circuit de redémarrage cron, des fuites d'état du compresseur inter-sessions et des correctifs CVE pour aiohttp et anthropic."
description: >
  "Teknium a livré le 1er juillet 2026 des correctifs de sécurité et fiabilité : fermeture d'un contournement du wipe root, coupe-circuit de redémarrage cron, fuites d'état inter-sessions du compresseur corrigées et mises à jour de dépendances pour aiohttp et anthropic."
reading_time: 3
---

Le 1er juillet 2026, Teknium de Nous Research a fusionné un ensemble de correctifs de sécurité et de fiabilité dans la branche `main` d'Hermes Agent — un sprint ciblé traitant d'un contournement du système de fichiers racine, d'une boucle de redémarrage cron, d'une corruption d'état entre sessions et de quatre correctifs CVE dans les dépendances principales.

## Le contournement `rm -rf /` par effondrement du shell

Le correctif principal ferme un cas limite dans la barrière infranchissable du système de fichiers racine — la liste de blocage inconditionnelle d'Hermes Agent qui empêche les commandes terminal de nettoyer le système de fichiers, quel que soit le mode yolo ou les paramètres d'approbation. Le motif original détectait `rm -rf /` et `rm -rf /*`, mais manquait les variantes par effondrement du shell : `rm -rf //`, `/./`, `/../` et `//*` se résolvent tous en `/` dans le shell, mais échappaient à l'expression régulière.

Le correctif, co-écrit par kernel-t1, élargit la barrière en passant de la correspondance au jeton littéral `"/"` à `"/[/.]*/\\*"` — tout chemin ancré à la racine dont les composants se réduisent à `/` avec un glob terminal facultatif. Un segment réel final comme `/home` ou `/tmp` passe toujours à travers des règles de motifs dangereux plus souples. Il ne capture que les chemins qui se résolvent à la racine elle-même.

Cela signifie que, même sous `--yolo`, `approvals.mode=off` ou le mode d'approbation cron, aucune orthographe par effondrement du shell d'un nettoyage de la racine ne peut atteindre le terminal. Le seul plancher inconditionnel est désormais plus difficile à contourner.

## Disjoncteur de boucle de redémarrage Cron

Le problème #30719 suivait un problème de longue date : si un travail cron ou une session de passerelle déclenchait un SIGTERM, le mécanisme de reprise automatique le réexécutait au démarrage, créant potentiellement une boucle de redémarrage infinie. Deux défenses précédentes (filtrage des commandes du cycle de vie sur `hermes gateway stop|restart`, et un filtre de création cron) avaient déjà été mises en place, mais des lacunes subsistaient.

Le nouveau correctif ajoute `gateway/restart_loop_guard.py` : un compteur à fenêtre glissante (par défaut : 3 démarrages en 60 secondes) qui, une fois déclenché, ignore la reprise automatique pour ce démarrage. La passerelle se lance toujours et sert les messages entrants réels — elle cesse simplement de rejouer la session qui la tue continuellement. De plus, la protection du cycle de vie a été déplacée vers un point de contrôle partagé (`cron/lifecycle_guard.py`) afin que les travaux cron créés par les outils du modèle soient filtrés au moment de la création, et pas seulement à l'exécution.

Le crédit transite par la PR #33395 (@kshitijk4poor) à partir du travail original de @SimoKiihamaki dans #30728.

## Fuites d'état du compresseur entre sessions

Un bug subtil de benbarclay : `on_session_end()` ne nettoyait que `_previous_summary`, mais `on_session_reset()` nettoie 14+ variables par session. Lorsqu'une session se terminait (sortie cron, expiration de la passerelle, rotation de l'ID de session) et que l'instance du compresseur était réutilisée, un état obsolète persistant provoquait :

- `_ineffective_compression_count` survivant → la session suivante sautait la compression prématurément
- `_summary_failure_cooldown_until` survivant → bloquait la génération du résumé pour une erreur transitoire non liée
- `_last_compress_aborted` survivant → les appelants pensaient que la compression était toujours interrompue

Le correctif nettoie tout l'état par session dans `on_session_end()`, en correspondance avec `on_session_reset()`. Six tests ciblés protègent désormais les vecteurs de fuite.

## Mises à jour de dépendances liées aux CVE

La dépendance aiohttp a été mise à jour de la version 3.14.0 à 3.14.1, couvrant **CVE-2026-34993** (exécution de code à distance via désérialisation dans CookieJar.load) et **CVE-2026-47265** (fuite de cookie par requête lors d'une redirection inter-origine). De manière cruciale, le correctif applique également la version corrigée sur les chemins de messagerie paresseux (Discord, Matrix, Teams) qui obtenaient aiohttp de manière transitive sans l'épingle explicite, ainsi que **CVE-2026-34450 / CVE-2026-34452** dans anthropic, passée de 0.86.0 à 0.87.0. Une nouvelle protection de test dans `test_packaging_metadata.py` empêche les épingles dans `pyproject.toml` et `lazy_deps.py` de diverger silencieusement à nouveau.

---

Ce sprint représente un rythme axé sur la sécurité, typique du cycle de développement d'Hermes Agent : les versions majeures poussent les capacités, puis un durcissement ciblé resserre les coutures. Tous les correctifs sont désormais sur `main` — exécutez `hermes update` pour les récupérer.