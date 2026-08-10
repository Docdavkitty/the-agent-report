---
layout: post
title: >
  "Sprint post-Tenacity de l'agent Hermes : 143K étoiles, nouvelle compétence Finance, et 179 PRs fusionnées en 4 jours"
date: 2026-05-11 12:00:00 +0200
lang: fr
ref: hermes-agent-post-tenacity-sprint-may11
permalink: /fr/2026/05/hermes-agent-post-tenacity-sprint-may11/
translation_of: /2026/05/hermes-agent-post-tenacity-sprint-may11/
author: The Agent Report
categories: ["hermes-agent"]
tags: [Hermes Agent, Nous Research, "open-source", "post-tenacity", "community-momentum", "stocks-finance", "kanban-diagnostics", "platform-maturation", "traduction-francaise"]
last_modified_at: 2026-08-10 15:11:14 +0000
hero_image: /assets/images/hero/hero-hermes-agent-post-tenacity-sprint-may11.jpg
meta_description: >
  "L'agent Hermes mène un sprint post-Tenacity avec des PRs communautaires corrigeant les régressions, actualisant la documentation et renforçant la stabilité."
description: >
  "Sprint post-Tenacity d'Hermes Agent avec des PRs communautaires corrigeant les régressions, actualisant la documentation et renforçant la stabilité."
reading_time: 6
---

La version **Hermes Agent v0.13.0 « Tenacity »** est sortie le 7 mai, avec des tableaux Kanban multi-agents, la persistance de `/goal`, les Checkpoints v2 et 8 correctifs de sécurité de priorité P0. Quatre jours plus tard, le projet n’a pas seulement maintenu son élan – il s’est **accéléré**.

Depuis le 8 mai, le dépôt GitHub est passé d’environ 138 000 à **143 510 étoiles** (+5 500 en 96 heures), et **179 pull requests ont été fusionnées** par **13 contributeurs distincts**. Voici ce qui a atterri dans la fenêtre qui a suivi immédiatement Tenacity.

## 📈 Croissance explosive des étoiles

Avec environ **1 375 nouvelles étoiles par jour**, Hermes Agent est [désormais le runtime d’agent IA à la croissance la plus rapide sur GitHub]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}) de loin :

| Jalon                      | Étoiles | Date       | Jours |
|----------------------------|---------|------------|-------|
| v0.12.0 Curator            | 127K    | 30 avril   | —     |
| Vague communautaire        | 131K    | 4 mai      | +4    |
| i18n + Cycle de vie des compétences | 135K | 6 mai      | +2    |
| v0.13.0 Tenacity           | 138K    | 7 mai      | +1    |
| **Aujourd’hui**            | **143,5K** | **11 mai** | **+4** |

Le projet a gagné **~16 500 étoiles en 11 jours** depuis la v0.12.0 – une trajectoire qui ne montre aucun signe de ralentissement – et il allait livrer [la v0.14.0 « Foundation » seulement 9 jours plus tard]({% post_url 2026-05-18-hermes-agent-v0140-foundation-release-may16 %}). Le nombre de forks a atteint **22 406** et le dépôt compte désormais **9 960 tickets ouverts** (témoignant de l’ampleur de l’engagement communautaire).

## 🆕 Nouvelles compétences et fonctionnalités

### Compétence Finance & Bourse

Le contributeur communautaire **Mibayy** a livré une nouvelle **[compétence optionnelle pour la finance et la bourse](https://github.com/NousResearch/hermes-agent/pull/23587)** qui intègre les données de Yahoo Finance sans nécessiter de clé API. Cette compétence offre :

- Des cotations boursières en temps réel et des données historiques
- Un suivi de portefeuille
- Un résumé du marché et des performances sectorielles
- Aucune inscription externe à une API nécessaire – elle utilise les points d’accès publics de Yahoo Finance

C’est un ajout important pour les développeurs qui construisent des agents assistants financiers ou des tâches cron de surveillance des marchés.

### Diagnostic Kanban : `stranded_in_ready`

Le responsable du projet **Teknium** a ajouté un **[diagnostic stranded_in_ready](https://github.com/NousResearch/hermes-agent/pull/23578)** pour le système Kanban – une nouvelle vérification qui fait remonter les tâches bloquées dans la colonne « Ready » sans qu’aucun worker ne leur soit assigné. Cela facilite l’identification des tableaux bloqués et le déblocage des flux de travail.

### Compétence Test d’API / Débogage REST-GraphQL

La compétence `api-testing` a été **[renommée et déplacée](https://github.com/NousResearch/hermes-agent/pull/23589)** en `rest-graphql-debug`, fournissant une compétence structurée pour tester des points d’accès API, valider les réponses et déboguer les services REST et GraphQL directement depuis l’agent.

## ⚡ Performances et fiabilité

### Cadence adaptative pour Telegram

**wilsen0** a contribué une **[optimisation des performances de la passerelle Telegram](https://github.com/NousResearch/hermes-agent/pull/23588)** qui ajuste dynamiquement la cadence des messages et ajoute un chemin rapide adaptatif pour les réponses courtes. Résultat : des réponses plus vives sur Telegram sans heurter les limites de débit de l’API.

### Cache pour les erreurs 402 des fournisseurs

**Teknium** a livré un **[correctif pour les tempêtes de tentatives de reconnexion aux fournisseurs](https://github.com/NousResearch/hermes-agent/pull/23597)** – lorsqu’un fournisseur de LLM retourne une erreur 402 (Paiement requis), l’agent met désormais en cache le fournisseur comme « malade » avec une durée de vie (TTL) plutôt que de réessayer à chaque appel. Cela évite des échecs de facturation en cascade et réduit la charge sur les API.

### Arguments supplémentaires pour Docker + Horodatages

**Mibayy** a contribué les fonctionnalités **[docker_extra_args et display.timestamps](https://github.com/NousResearch/hermes-agent/pull/23599)** pour le terminal et l’outillage CLI, offrant aux utilisateurs un contrôle plus fin sur l’exécution des conteneurs Docker et la visibilité des horodatages dans la sortie de l’agent.

## 🔧 Nix et infrastructure

### Correction du point d’entrée des conteneurs Nix

**Siddharth Balyan** a corrigé un **[problème critique de point d’entrée des conteneurs Nix](https://github.com/NousResearch/hermes-agent/pull/23633)** : `chown -R` supprimait le bit `setgid`, ce qui cassait l’accès des groupes hostUsers dans les environnements Nix. Cela améliore la compatibilité de Hermes Agent avec les déploiements basés sur Nix – un cas d’usage de plus en plus important à mesure que le projet s’étend au-delà des configurations Docker classiques.

### extraDependencyGroups pour Nix

Le même contributeur a ajouté des **[extraDependencyGroups pour les suppléments d’environnements virtuels scellés](https://github.com/NousResearch/hermes-agent/pull/21817)**, facilitant la gestion de l’arbre de dépendances de Hermes Agent dans les environnements NixFlake.

## 🔒 Sécurité

### Assainissement des variables d’environnement dans les commandes rapides

**0xbyt4** a livré un **[correctif de sécurité](https://github.com/NousResearch/hermes-agent/pull/23595)** qui assainit les variables d’environnement et caviarde la sortie dans les commandes rapides, refermant ainsi un vecteur potentiel de fuite d’information. Le correctif supprime également l’état inscriptible `_pending_messages`, réduisant ainsi la surface d’attaque globale.

### Alertes en cas d’échec de parsing YAML

Une nouvelle **[amélioration de la sécurité de la configuration](https://github.com/NousResearch/hermes-agent/pull/23585)** apportée par **Teknium** fait que Hermes Agent émet désormais un avertissement fort en cas d’échec de parsing YAML, plutôt que de basculer silencieusement vers les valeurs par défaut. Cela empêche des bugs de mauvaise configuration subtils où un `config.yaml` cassé passait inaperçu jusqu’à l’exécution.

## 🧠 Pouls de la communauté

La fenêtre post-Tenacity a vu des contributions d’un ensemble diversifié de membres de la communauté :

| Contributeur        | PR notable |
|---------------------|------------|
| **Mibayy**          | Compétence Finance & Bourse, arguments Docker supplémentaires |
| **wilsen0**         | Optimisation de la cadence adaptative pour Telegram |
| **Siddharth Balyan**| Point d’entrée des conteneurs Nix, groupes de dépendances |
| **0xbyt4**          | Nettoyage de l’indicateur de saisie Discord, assainissement des variables d’environnement |
| **kjames2001**      | Dépassement d’édition Telegram : fractionnement et livraison |
| **eloklam**         | Nettoyage du test de recherche Kanban |
| **Gutslabs**        | Trois correctifs défensifs issus de la PR #1974 |

> « Voilà à quoi ressemble l’open source à grande échelle – 179 PR en 4 jours couvrant la sécurité, la performance, l’infrastructure et de nouvelles compétences. La sortie de Tenacity a fait la une, mais le sprint communautaire est la véritable histoire. » — The Agent Report

## 🔭 Perspectives

Au rythme actuel d’environ **45 PR fusionnées par jour**, la prochaine version (v0.14.0) pourrait arriver d’ici une semaine. Les points à surveiller :

- **Maturité de Kanban** : Le diagnostic `stranded_in_ready` suggère l’arrivée prochaine de fonctionnalités de fiabilité plus poussées pour Kanban
- **Écosystème Nix** : Plusieurs PR liées à Nix signalent une demande croissante pour le déploiement en entreprise
- **Pipeline de nouvelles compétences** : Les compétences financières et de test d’API témoignent d’un élargissement de la couverture métier de Hermes Agent
- **143K+ et en hausse** : À ce rythme, la barre des 150K étoiles sera probablement franchie dans la semaine

Pour les développeurs qui n’ont pas essayé Hermes Agent depuis la version v0.12.0 « Curator » – ou ceux qui ont rejoint le projet lors de la vague Tenacity – c’est le moment idéal pour explorer les améliorations post-version. Le projet est disponible sur [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) et documenté sur [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com).