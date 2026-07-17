---
layout: post
title: >
  "Openclaw v2026.5.22 : listing de modèles 4 100 fois plus rapide, plugin Notes de réunion et refonte majeure du packaging"
date: 2026-05-26 10:00:00 +0000
lang: fr
ref: openclaw-v2026-5-22-4100x-model-listing-meeting-notes
permalink: /fr/2026/05/openclaw-v2026-5-22-4100x-model-listing-meeting-notes/
translation_of: /2026/05/openclaw-v2026-5-22-4100x-model-listing-meeting-notes/
author: The Agent Report
categories: [openclaw]
tags: [openclaw, "claw-controller", "agent-autonomy", "performance-optimization", "enterprise-packaging", "traduction-francaise"]
last_modified_at: 2026-07-17 15:02:03 +0000
hero_image: >
  /assets/images/hero/hero-openclaw-v2026-5-22-4100x-model-listing-meeting-notes.jpg
meta_description: >
  "Openclaw v2026.5.22 offre un gain de vitesse de 4 100x pour les appels de listing de modèles, un plugin Notes de réunion avec capture vocale Discord et un packaging repensé."
description: >
  "Openclaw v2026.5.22 accélère de 4 100x les appels de listing de modèles, ajoute un plugin Notes de réunion avec capture vocale Discord et une refonte complète du packaging."
reading_time: 7
---

Le train de releases d'Openclaw ne montre aucun signe de ralentissement. Le 24 mai 2026, le projet a livré **v2026.5.22** — une version stable qui intègre ce qui pourrait être l'optimisation de performance la plus impressionnante de l'histoire du projet, accompagnée d'un nouveau plugin Meeting Notes et d'une refonte complète du packaging et de la sécurité.

Avec **375 000+ étoiles GitHub**, **78 000+ forks** et **381 contributeurs** pour cette seule version (dont de nombreux nouveaux noms), la trajectoire d'Openclaw, passant d'un projet open-source prometteur à une plateforme d'infrastructure agent sérieuse, continue de s'accélérer.

## Le jalon de performance 4 100×

Le chiffre phare de la v2026.5.22 est difficile à ignorer : **les appels de liste de modèles sont passés d'environ 20 secondes à ~5 millisecondes** — une amélioration de 4 100×. Voici comment l'équipe y est parvenue :

| Optimisation | Description |
|---|---|
| **Préchauffage de l'état d'authentification** | Les cartes d'état d'authentification des fournisseurs sont désormais préchauffées au démarrage de la passerelle, de sorte que les appels `/models` court-circuitent la découverte par fournisseur au lieu de bloquer sur des appels API en direct |
| **Instantanés immuables des métadonnées des plugins** | Le catalogue des plugins, la configuration des canaux et les cartes d'alias SDK sont mis en cache sous forme d'instantanés immuables réutilisés entre les lecteurs de démarrage, de configuration, de modèle et de secrets |
| **Travail de démarrage chargé paresseusement** | Les gestionnaires principaux, le runtime ACPX intégré et les plugins inactifs au démarrage ne sont plus chargés avant les signaux de santé/disponibilité — la passerelle se déclare saine *avant* de terminer l'initialisation de l'arbre des plugins |
| **Cartes d'alias SDK mises en cache** | Les cartes d'alias de surface publique sont mises en cache, et les sondages de chemins macOS Linuxbrew non pertinents sont entièrement ignorés |
| **Évitement des vérifications redondantes de canaux** | Les lectures du catalogue de canaux stables au niveau du processus éliminent les vérifications répétées des limites de canaux groupés lors de la répartition de la passerelle |

Pour les développeurs et les équipes utilisant Openclaw en production, cela signifie **une énumération quasi instantanée des modèles** — fini de regarder un indicateur de chargement pendant que la passerelle sonde chaque fournisseur. Le point de terminaison `/models` ressemble désormais à une recherche dans un cache local plutôt qu'à une opération de découverte distribuée.

## Plugin Meeting Notes : Transcription alimentée par les agents

Un tout nouveau **plugin Meeting Notes** fait ses débuts dans la v2026.5.22 en tant que plugin externe uniquement source, avec un contrat de fournisseur source SDK défini en dehors du package npm principal. Les capacités clés incluent :

- **Capture automatique** — Commence automatiquement l'enregistrement des transcriptions de réunion lorsqu'une session vocale Discord rejoint
- **Importations manuelles de transcriptions** — Importer des transcriptions de réunions existantes pour la recherche et la récupération
- **Accès CLI** — Commande complète `openclaw meeting-notes` avec opérations en lecture seule
- **Discord comme première source en direct** — Les canaux vocaux Discord sont la première source de capture en direct, le contrat SDK permettant à des fournisseurs tiers de créer des intégrations supplémentaires

L'architecture du plugin est remarquable : il est livré en tant que **plugin uniquement source en dehors de la distribution principale**, suivant le modèle d'externalisation établi dans le cycle bêta v2026.5.12. Cela permet de garder le package npm principal léger tout en offrant des fonctionnalités riches via l'écosystème de plugins.

```bash
# Installer le plugin meeting-notes
openclaw plugins add openclaw/meeting-notes

# Afficher les notes capturées
openclaw meeting-notes list
```

## Avancées du SDK Plugin

Au-delà du plugin Meeting Notes, le SDK Plugin a reçu plusieurs améliorations fondamentales :

- **Expéditeur de sondage générique** — Un nouvel expéditeur de sondage par message de canal permet aux plugins de créer et de gérer des sondages sur n'importe quel canal
- **API des fournisseurs d'intégration** — Les plugins peuvent désormais déclarer et enregistrer des capacités de fournisseur d'intégration via un contrat formel
- **Aides de workflow de session au niveau des lignes** — Dépréciation de `loadSessionStore` au profit d'une gestion granulaire des sessions au niveau des lignes, plus composable et testable
- **Réutilisation du registre de plugins compatible** — La passerelle réutilise désormais les registres de plugins compatibles lors de la répartition, évitant un chargement redondant

Ces améliorations du SDK abaissent la barrière pour les développeurs tiers tout en offrant aux utilisateurs avancés un contrôle plus granulaire sur l'état des sessions et les stratégies d'intégration.

## Refonte du packaging et de la sécurité pour les entreprises

L'un des changements les plus importants de la v2026.5.22 est invisible pour les utilisateurs finaux mais crucial pour les adoptants en entreprise : une **refonte complète du packaging et de l'intégrité**.

### Tarballs npm plus petits

Le package de distribution npm **exclut désormais les images et les ressources de documentation**, réduisant considérablement la taille du téléchargement. Pour les équipes déployant Openclaw sur des flottes de serveurs, cela se traduit par des installations plus rapides et une consommation de bande passante réduite.

### Intégrité Shrinkwrap

Chaque package npm Openclaw publié est désormais livré avec un **fichier shrinkwrap généré**, épinglant toutes les versions de dépendances transitives :

```bash
# Le shrinkwrap est inclus dans le tarball publié
npm install -g openclaw  # Installation reproductible garantie
```

Toutes les modifications de lockfile et de shrinkwrap nécessitent désormais une révision explicite avant fusion, empêchant la dérive accidentelle des dépendances. Les étapes de vérification `pnpm check` s'exécutent via un gestionnaire enfant géré pour éviter les avertissements de dépréciation de shell-argv de Node.js.

### Vérifications d'intégrité des packages

Une nouvelle étape de validation de release effectue **des vérifications d'intégrité des packages avant publication**, empêchant les artefacts QA privés de fuir dans le package npm publié. Cela répond à une classe de préoccupations liées à la chaîne d'approvisionnement que les équipes de sécurité des entreprises soulèvent fréquemment.

## QA-Lab : Scénarios d'agents personnels

Le banc d'essai automatisé QA-Lab continue son expansion avec la v2026.5.22, ajoutant :

- **Accessoires de rejeu JSONL mockés et organisés** — Rejeu déterministe des réponses API des fournisseurs pour des tests reproductibles
- **Rapport de première dérive** — Identifie automatiquement la première divergence dans le comportement de l'agent lors des vérifications de parité d'exécution
- **Scénarios de récupération après échec d'agent personnel** — Tests que les agents peuvent récupérer après des échecs d'exécution sans intervention humaine
- **Couverture du cycle de vie du plugin Codex** — Tests de bout en bout pour les chemins d'installation, de mise à jour et de suppression du plugin Codex
- **Sentinelle de mise à niveau automatique optionnelle** — Scénarios `update.run` qui valident que le chemin de mise à niveau ne casse pas les fonctionnalités existantes

À chaque release, QA-Lab devient plus complet — signalant la maturation d'Openclaw vers une ingénierie de fiabilité de niveau entreprise.

## Corrections Discord et navigateur

Au-delà des fonctionnalités phares, la v2026.5.22 livre d'importantes corrections de qualité de vie :

- **Plafonds de durée de vie des rappels Discord** — `agentComponents.ttlMs` impose désormais un maximum de 24 heures sur la durée de vie du registre de rappels Discord, empêchant l'accumulation de rappels obsolètes
- **Déduplication WebChat** — Correction d'une condition de concurrence où les sessions WebChat pouvaient générer des gestionnaires de messages en double
- **Nettoyage du cycle de vie de la passerelle** — Préservation de l'état du cycle de vie lors des réinitialisations de canaux de la passerelle, empêchant les abonnements obsolètes de survivre aux redémarrages
- **Assainissement des images du navigateur** — Les limites sont désormais correctement appliquées pour les captures d'écran et les instantanés étiquetés

## Sprint de documentation

La version inclut une mise à jour massive de la documentation couvrant **Signal configPath, les paramètres par défaut des sujets génériques Telegram, le repli Termux home, la connexion automatique macOS VM, la récupération WhatsApp QR/408, les invites de langue de sortie cron, les diagnostics CDP, les importations de la liste blanche du SDK Plugin, la configuration Bitwarden SecretRef, les déploiements EasyRunner, les guides d'installation Upstash Box, et plus encore**. 164+ contributeurs sont nommés dans le journal des modifications, soulignant l'élan communautaire extraordinaire du projet.

## La vue d'ensemble

Openclaw v2026.5.22 représente une version où **la maturité de l'infrastructure rattrape la vélocité des fonctionnalités**. L'amélioration de performance de 4 100× n'est pas seulement un trophée de benchmark — elle change fondamentalement la réactivité de la passerelle lors de la configuration des fournisseurs. Le plugin Meeting Notes ouvre une nouvelle catégorie de produits pour la productivité alimentée par les agents. Et la refonte du packaging répond au #1 des obstacles au déploiement en entreprise : l'intégrité de la chaîne d'approvisionnement. Cette version suit de près l'introduction du [Policy Plugin pour la conformité en tant que code]({% post_url 2026-05-21-openclaw-v2026-5-20-beta1-policy-plugin-compliance %}) dans l'orchestration des agents.

Le projet compte désormais **375 000+ étoiles GitHub** avec **78 000+ forks**. La version stable est disponible immédiatement. Pour les développeurs évaluant le paysage des agents open-source, notre [Guide complet des agents IA]({% post_url 2026-05-26-complete-guide-to-ai-agents-2026 %}) fournit un aperçu complet de la manière dont des plateformes comme Openclaw s'intègrent dans l'écosystème plus large.

```bash
npm install -g openclaw
```

Pour ceux qui exécutent des versions bêta, `npm update -g openclaw` récupère directement la dernière version stable.

---

*Openclaw v2026.5.22 est disponible dès maintenant via `npm install -g openclaw`. Notes de version complètes sur [GitHub](https://github.com/openclaw/openclaw/releases/tag/v2026.5.22).*