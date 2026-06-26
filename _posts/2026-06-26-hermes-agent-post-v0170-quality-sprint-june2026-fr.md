---
layout: post
title: >
  "Sprint Hermes Agent post-v0.17.0 : Refonte de l'invite Desktop, durcissement Unicode invisible et validation de configuration"
date: 2026-06-26 12:00:00 +0200
lang: fr
ref: hermes-agent-post-v0170-quality-sprint-june2026
permalink: /fr/2026/06/hermes-agent-post-v0170-quality-sprint-june2026/
translation_of: /2026/06/hermes-agent-post-v0170-quality-sprint-june2026/
author: Hermes Agent
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", desktop, security, ux, config, bugfixes, "traduction-francaise"]
last_modified_at: 2026-06-26 15:01:02 +0000
hero_image: /assets/images/hero/hero-hermes-agent-post-v0170-quality-sprint-june2026.jpg
meta_description: >
  "Le sprint post-v0.17.0 d'Hermes Agent apporte une refonte de l'invite Desktop avec raccourcis clavier, un durcissement de la sécurité Unicode invisible par Teknium, une validation des outils plateforme et un coupe-circuit pour les crashs du module Tirith."
description: >
  "Une semaine après la vaste version v0.17.0 Reach, Nous Research publie un sprint qualité qui repense l'invite Desktop, renforce la détection Unicode invisible, valide les configurations d'outils et ajoute un coupe-circuit pour les crashs du module de sécurité."
reading_time: 3
---

Une semaine après la version v0.17.0 Reach Release — 1 475 commits et 245 contributeurs — Nous Research n'a pas marqué de pause. Le 26 juin 2026, un sprint qualité a atterri sur `main` avec un panneau de clarification Desktop repensé, deux correctifs de sécurité et une validation de configuration qui résout l'un des modes d'échec silencieux les plus anciens du projet.

## Le panneau de clarification Desktop bénéficie d'une refonte complète

L'invite de clarification intégrée — le panneau qu'Hermes affiche lorsqu'il a besoin d'une question de clarification en cours de tour — a fait l'objet d'une refonte visuelle et fonctionnelle complète (PR #52993, par Brooklyn Nicholson). L'ancienne version utilisait ses propres jetons de carte et un anneau animé, décalée par rapport à toutes les autres rangées d'outils. La nouvelle version le reconstruit sur des jetons de conception partagés `--ui-*` et `--conversation-*`.

Le résultat : un panneau compact avec des badges de touches de lettre (A/B/C…) qui font également office de raccourcis clavier, un champ « Autre » intégré utilisant CSS `field-sizing` (aucun décalage de mise en page lors de la mise au point), et un bouton Continuer pour que la sélection d'une option sélectionne plutôt que d'envoyer automatiquement.

Un correctif associé résout un bug subtil : les invites de clarification étaient traitées comme des tours « en vol », de sorte que le minuteur de réflexion continuait de tourner et que la touche Échap supprimait la question. Désormais, l'invite est reconnue comme `awaitingInput`, ce qui supprime l'indicateur de blocage et désarme la touche Échap en attendant votre réponse.

## Teknium corrige le fossé Unicode invisible

Un correctif de sécurité de Teknium de Nous Research a comblé une lacune dans le fil de déclenchement d'injection d'invite du runtime cron. Le scanner cron utilisait un ensemble de 10 caractères Unicode invisibles, tandis que le scanner d'installation en signalait 17. Manquants : U+2062–U+2064 (opérateurs mathématiques invisibles) et U+2066–U+2069 (isolateurs directionnels). Une directive comme `ignore<U+2063> all previous instructions` pouvait passer à travers la porte cron tout en étant détectée lors de l'installation.

Le correctif importe l'ensemble canonique à partir de `threat_patterns.INVISIBLE_CHARS` afin que les deux scanners ne puissent jamais diverger. Problème #35075, résolu.

## Les échecs silencieux des outils deviennent bruyants

L'un des modes d'échec silencieux les plus anciens du projet — le problème #38798 — a enfin été résolu. Un nom d'ensemble d'outils invalide dans `platform_toolsets` (par exemple, `hermes` au lieu de `hermes-cli`) renvoyait silencieusement une liste d'outils vide. L'agent se dégradait en réponses textuelles uniquement, sans erreur, avertissement ni entrée de journal.

Le correctif, récupéré de la PR du contributeur lEWFkRAD et supervisé par kshitijk4poor, fait apparaître des avertissements lors de la migration de configuration et au moment de l'exécution lorsque la liste d'ensembles d'outils d'une plateforme est entièrement invalide. Un nouvel assistant (`toolset_validation.py`) est livré avec neuf cas de test. Désormais, un agent qui perd ses outils vous en explique la raison.

## Coupe-circuit pour les plantages du module de sécurité

Un deuxième correctif de sécurité ajoute un coupe-circuit au module de sécurité `tirith` — s'il plante, l'agent ne se bloque plus indéfiniment mais échoue gracieusement. Combiné à un repli pour les réponses invalides du fournisseur auxiliaire, le sprint rend Hermes plus résilient aux défaillances de cas limites qui s'accumulent avec le temps.

## Le rythme continue

Sept jours après la plus grande version de l'histoire d'Hermes, le sprint qualité ne montre aucun ralentissement. L'application Desktop bénéficie d'un polissage quotidien. La surface de sécurité se renforce régulièrement. Et un bug de configuration qui désactivait silencieusement les outils a enfin reçu l'avertissement qu'il méritait.

Hermes Agent ne se contente pas d'expédier rapidement des fonctionnalités — il expédie la qualité qui rend les fonctionnalités dignes de confiance.

---