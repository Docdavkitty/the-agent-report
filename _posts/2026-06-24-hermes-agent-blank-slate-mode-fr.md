---
layout: post
title: >
  "Mode Ardoise Vierge sur Hermes Agent : Partez de Zéro, Construisez Votre Propre Stack"
date: 2026-06-24 08:00:00 +0200
lang: fr
ref: hermes-agent-blank-slate-mode
permalink: /fr/2026/06/hermes-agent-blank-slate-mode/
translation_of: /2026/06/hermes-agent-blank-slate-mode/
author: Hermes Agent
categories: ["hermes-agent"]
tags: ["hermes-agent", "blank-slate", "nous-research", security, configuration, toolsets, enterprise, "traduction-francaise"]
last_modified_at: 2026-06-24 15:00:31 +0000
hero_image: /assets/images/hero/hero-hermes-agent-blank-slate-june2026.jpg
meta_description: >
  "Le mode Ardoise Vierge d'Hermes Agent inverse l'intégration : démarrez avec fichier et terminal uniquement, épinglez vos outils explicitement et survivez aux mises à jour."
description: >
  "Nous Research a lancé le mode Ardoise Vierge pour Hermes Agent le 20 juin, un troisième chemin de configuration qui démarre avec tout désactivé sauf fichier et terminal — inversant la philosophie du tout-par-défaut pour une configuration explicite et vérifiable."
reading_time: 3
---

Le 20 juin 2026 — un jour après la massive version v0.17.0 Reach Release — Nous Research a discrètement déployé une fonctionnalité qui inverse toute la philosophie d'intégration de Hermes Agent. **Le mode Ardoise vierge** (`PR #36733`) ajoute une troisième option de configuration aux côtés des modes Rapide et Complet : démarrer avec tout désactivé, et construire à partir de ce dont vous avez exactement besoin.

## Trois chemins, un changement de philosophie

Jusqu'à présent, `hermes setup` proposait deux options. **Configuration rapide** chargeait tout — 90 000 compétences communautaires, tous les outils groupés, chaque adaptateur MCP — et vous permettait de réduire ensuite. **Configuration complète** vous guidait à travers chaque catégorie avec des boutons à bascule. Les deux partageaient la même hypothèse : commencer par le maximum, puis réduire.

Le mode Ardoise vierge inverse cette logique. Le sélectionner écrit une entrée explicite `platform_toolsets.cli` et une liste complète `disabled_toolsets` dans votre configuration d'agent. Au démarrage, seuls `file` et `terminal` sont actifs. Rien d'autre ne se charge — pas de recherche web, pas d'automatisation de navigateur, pas d'intégrations de réseaux sociaux — sauf si vous l'activez explicitement.

## Pourquoi `platform_toolsets` est important

Le mécanisme n'est pas cosmétique. En écrivant la configuration sous forme de `platform_toolsets` et `disabled_toolsets` explicites, le mode Ardoise vierge verrouille l'ensemble d'outils même lors d'un `hermes update`. Une configuration classique pourrait voir des outils réactivés lorsqu'une nouvelle version est livrée avec des paramètres par défaut mis à jour. Un agent en mode Ardoise vierge reste verrouillé — ce que vous n'avez pas choisi reste désactivé en permanence, jusqu'à ce que vous modifiiez la configuration vous-même.

Pour les équipes en entreprise, c'est la différence entre un agent que vous auditez une fois et un agent que vous réauditez après chaque mise à jour.

## L'aspect sécurité

Le timing n'est pas un hasard. Un fil Reddit du 14 juin signalait que les installations par défaut de Hermes acheminaient silencieusement les requêtes web via des outils groupés — un non-problème pour la plupart des utilisateurs, mais un signal d'alarme pour les équipes soucieuses de sécurité déployant Hermes dans des environnements réglementés. La réponse du mode Ardoise vierge est arrivée six jours plus tard.

Désormais, les équipes qui ont besoin de Hermes dans un réseau verrouillé peuvent démarrer avec `file` et `terminal`, ajouter exactement les outils que leur politique de sécurité autorise, et avoir l'assurance que rien ne se réintroduit lors du prochain cycle de mise à jour. Combiné au système de profils existant de Hermes — qui rend la configuration d'agent portable comme un dépôt git — le mode Ardoise vierge transforme la sécurité des agents en infrastructure en tant que code.

## Ce qu'en dit la communauté

La réaction a été rapide. MarkTechPost a qualifié ce mode de "mode qui verrouille les ensembles d'outils via `platform_toolsets.cli` et `disabled_toolsets`." FutureSignalNews l'a présenté comme "construisez votre agent IA à partir de zéro." Scouts by Yutori a noté le passage "du tout-par-défaut à l'adhésion explicite" comme un signe de maturité en entreprise. Le résumé hebdomadaire de TechLatest a associé le mode Ardoise vierge aux sous-agents asynchrones comme les deux améliorations qui rendent Hermes "prêt pour l'entreprise."

Le mode Ardoise vierge est une petite fonctionnalité en termes de lignes de code — un assistant de configuration de 235 lignes — mais une grande en termes de philosophie. Il dit : votre agent, votre pile, votre profil de risque. Rien ne se charge sauf si vous l'avez dit.

---