---
layout: post
title: >
  "Hermes Desktop en préversion publique — L'application native multiplateforme débarque avec le partenariat NVIDIA + Microsoft Computex"
date: 2026-06-03 10:00:00 +0200
lang: fr
ref: hermes-desktop-native-app-computex-2026
permalink: /fr/2026/06/hermes-desktop-native-app-computex-2026/
translation_of: /2026/06/hermes-desktop-native-app-computex-2026/
author: The Agent Report
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", "open-source", "hermes-desktop", "desktop-app", "computex-2026", "nvidia-rtx-spark", openshell, "microsoft-security", "traduction-francaise"]
last_modified_at: 2026-07-04 15:01:51 +0000
hero_image: /assets/images/hero/hero-hermes-desktop-native-app-computex-2026.jpg
meta_description: >
  "Hermes Desktop, l'application native macOS/Windows/Linux pour Hermes Agent, est lancée en préversion publique, peu après l'annonce par Nous Research de l'intégration de NVIDIA RTX Spark, du runtime OpenShell et des primitives de sécurité Microsoft au Computex 2026."
description: >
  "Hermes Desktop, l'application native macOS/Windows/Linux pour Hermes Agent, est en préversion publique, suite aux annonces de Nous Research sur NVIDIA RTX Spark, OpenShell et les primitives de sécurité Microsoft au Computex 2026."
reading_time: 7
---

## 🖥️ Qu'est-ce qu'Hermes Desktop ?

Hermes Desktop n'est pas un produit séparé — c'est un **wrapper Electron natif** autour du même environnement d'exécution Hermes Agent que vous obtenez avec la CLI et la passerelle. Comme le précise la [documentation officielle](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) :

> *« Ce n'est pas un produit séparé ni un clone allégé ; il installe l'environnement d'exécution standard d'Hermes Agent dans la structure standard `~/.hermes` et le pilote via une véritable interface utilisateur. »*

Cela signifie que votre configuration, vos clés API, vos sessions, vos compétences et votre mémoire sont **entièrement partagés** entre la CLI, la TUI, le tableau de bord web et la nouvelle application Desktop. Commencez une conversation dans l'un, reprenez-la dans un autre.

### Fonctionnalités clés

| Fonctionnalité | Description |
|---------|-------------|
| **Interface de chat** | Conversation textuelle complète avec l'agent, avec historique des messages et streaming |
| **Explorateur de fichiers** | Parcourez et prévisualisez le répertoire de travail sans quitter l'application |
| **Mode vocal** | Parlez à Hermes et écoutez les réponses (intégration du microphone macOS) |
| **Paramètres et intégration** | Gérez les fournisseurs, modèles, outils et identifiants via l'interface utilisateur — sans édition YAML |
| **Panneaux de gestion** | Reflet des sous-commandes `hermes` : fournisseurs, sélection de modèles, serveurs MCP, configuration de la passerelle, gestion des sessions |
| **Mises à jour automatiques** | Mises à jour en un clic lorsqu'une nouvelle version est disponible |

### Plateformes prises en charge

- **macOS :** 12+ (`.dmg` signé et notarié)
- **Windows :** 10/11 (installateur NSIS `.exe` ou `.msi`)
- **Linux :** `.AppImage`, `.deb`, `.rpm`

L'installateur Windows est particulièrement remarquable — il regroupe Python via `uv`, un Git portable et ripgrep dans un seul `.exe` qui ne nécessite **aucun droit administrateur ni modification à l'échelle du système**. Le premier lancement appelle `install.ps1` en arrière-plan, provisionnant le tout dans `%LOCALAPPDATA%\hermes`.

---

## 🚀 Installation : Deux méthodes

### Méthode 1 : Nouvelle installation avec prise en charge Desktop

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --include-desktop
```

Cette commande provisionne l'environnement d'exécution de l'agent et construit l'application Desktop en une seule passe.

### Méthode 2 : Ajouter Desktop à une installation Hermes existante

Si vous avez déjà Hermes Agent installé, exécutez simplement :

```bash
hermes desktop
```

La commande installe les dépendances Node de l'espace de travail, construit l'application Electron non empaquetée et la lance — le tout en utilisant votre configuration, vos clés, sessions et compétences existantes.

---

## 🔬 Sous le capot : Comment ça fonctionne

L'application Desktop empaquetée ne contient que le **shell Electron**. Au premier lancement, elle installe l'environnement d'exécution Hermes Agent dans `HERMES_HOME` (`~/.hermes` sur macOS/Linux, `%LOCALAPPDATA%\hermes` sur Windows) — **exactement la même structure qu'une installation CLI**.

Le moteur de rendu React communique avec un backend `hermes dashboard --tui` via les API standard de la passerelle. Cela signifie que l'application est essentiellement une interface frontale soignée pour la même boucle d'agent éprouvée qui alimente la CLI, le tableau de bord web et la passerelle.

Pour les développeurs souhaitant compiler à partir des sources :

```bash
cd apps/desktop
npm run dev          # Moteur de rendu Vite + Electron, démarre le backend Python
```

Les indicateurs supplémentaires incluent `--skip-build` (lancer une version existante), `--cwd PATH` (définir le répertoire de projet initial) et `--fake-boot` (tester l'interface utilisateur de démarrage avec des délais déterministes).

---

## 🏢 L'annonce du Computex 2026 : NVIDIA RTX Spark + OpenShell + Microsoft

Un jour seulement avant le lancement de Desktop, Nous Research a fait sensation au **Computex 2026** à Taipei. Le 1er juin, l'équipe a tweeté :

> *« Nous travaillons en étroite collaboration avec @nvidia pour garantir qu'Hermes Agent fonctionne parfaitement sur leur nouveau @NVIDIARTXSpark superchip et s'intègre avec le nouvel environnement d'exécution OpenShell, qui connecte Hermes aux @Microsoft primitives de sécurité. »*

Il s'agit d'un **partenariat à trois niveaux** :

### 1. Superchip NVIDIA RTX Spark

Le nouveau **RTX Spark** de NVIDIA — un système sur puce basé sur ARM combinant un GPU Blackwell RTX avec un CPU Grace à 20 cœurs — a été officiellement dévoilé au Computex. Développé en collaboration avec MediaTek, le Spark est conçu pour les charges de travail d'IA sur PC compacts et ordinateurs portables. Des partenaires tels qu'ASUS, Dell, HP, Lenovo et MSI prévoient de commercialiser des appareils équipés de Spark à l'automne 2026.

Le billet de blog de NVIDIA mentionne explicitement Hermes Agent :

> *« RTX Spark et NVIDIA OpenShell offrent aux utilisateurs d'Hermes un environnement puissant et sécurisé pour que les agents puissent fonctionner et travailler à vos côtés. »*

### 2. Environnement d'exécution OpenShell

**OpenShell** est le nouvel environnement d'exécution de NVIDIA pour les agents d'IA locaux, développé en partenariat avec Microsoft. Il permet aux utilisateurs de définir ce à quoi les agents peuvent accéder ou non, d'acheminer les requêtes vers des modèles locaux en fonction des préférences de confidentialité et d'obscurcir les données personnelles dans les requêtes envoyées aux services cloud. Il s'agit d'une pièce d'infrastructure essentielle pour rendre les environnements d'exécution d'agents locaux prêts pour la production.

### 3. Primitives de sécurité Windows de Microsoft

L'environnement d'exécution OpenShell connecte Hermes Agent aux **nouvelles primitives de sécurité Windows de Microsoft** — des contrôles au niveau du système d'exploitation régissant la vérification d'identité, le confinement des processus et l'application des politiques pour les applications d'agents. Cela apporte des garanties de sécurité basées sur le matériel à l'exécution autonome des agents, répondant à l'un des obstacles les plus courants au déploiement en entreprise.

---

## 📊 La trajectoire

La croissance d'Hermes Agent continue de s'accélérer. Le projet a dépassé les **172 000 étoiles GitHub** — l'environnement d'exécution d'agent d'IA le plus étoilé — avec plus de **1 000 demandes d'extraction fusionnées** rien qu'au cours des deux dernières semaines, sur le cycle de versions v0.15.0/0.15.1/0.15.2.

Le lancement de Desktop comble une lacune évidente : bien qu'Hermes Agent soit déjà puissant en tant qu'outil CLI, passerelle de messagerie et tableau de bord web, il lui manquait une **expérience de bureau native soignée** pour les utilisateurs quotidiens. L'aperçu public change cela — et avec des installateurs préconstruits pour les trois principales plateformes, plus un chemin Windows sans administrateur, la barrière à l'entrée n'a jamais été aussi basse.

> *« Un agent open-source sous licence MIT qui conserve les compétences et la mémoire sur Telegram, Discord, Slack, WhatsApp, Signal, e-mail et CLI change l'économie du déploiement d'assistants IA pour les petites équipes : pas de verrouillage fournisseur, pas de perte de contexte par session. »* — AI Weekly

---

## 🔮 Ce que cela signifie pour l'écosystème des agents

La combinaison d'Hermes Desktop + NVIDIA RTX Spark + primitives de sécurité Microsoft est plus qu'une série de lancements — c'est un signal que **les environnements d'exécution d'agents open-source passent des outils de développement à l'infrastructure grand public**.

1. **Expérience utilisateur axée sur le bureau** — Hermes Desktop apporte la même mémoire persistante, la génération automatique de compétences et la passerelle multicanal à une interface graphique native que tout le monde peut installer et utiliser
2. **Partenariat matériel** — L'intégration NVIDIA Computex signifie qu'Hermes Agent fonctionnera nativement sur la prochaine génération de PC IA qui arrivera sur le marché cet automne
3. **Sécurité d'entreprise** — Les primitives de sécurité Microsoft répondent aux préoccupations de conformité et de gouvernance qui ont empêché de nombreuses entreprises de déployer des agents autonomes

Pour les développeurs qui utilisent déjà Hermes Agent, la transition est transparente : `hermes desktop` lance l'application en utilisant votre configuration existante. Pour les nouveaux venus, l'installateur `--include-desktop` offre un chemin en une seule commande de zéro à un agent fonctionnel, auto-améliorant, avec une interface d'application native.

---

## 📦 Résumé de ce qui est livré

| Élément | Statut | Date |
|------|--------|------|
| **Hermes Desktop (aperçu public)** | ✅ En ligne | 2 juin 2026 |
| **Hermes Agent v0.15.2** | ✅ Inclus | 29 mai 2026 |
| **Intégration NVIDIA RTX Spark** | ✅ Annoncé au Computex | 1er juin 2026 |
| **Environnement d'exécution OpenShell** | ✅ Aperçu | 1er juin 2026 |
| **Primitives de sécurité Microsoft** | ✅ Aperçu | 1er juin 2026 |
| **Expédition du matériel RTX Spark** | 📅 Automne 2026 | Partenaires listés |

Essayez Hermes Desktop dès aujourd'hui :

```bash
# Nouvelle installation avec l'application Desktop
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --include-desktop

# Installation existante
hermes desktop
```

*Restez à l'écoute — l'analyse approfondie de la version Velocity de cette semaine et la couverture du Computex ne sont que le début. L'écosystème Hermes évolue plus rapidement que jamais.*