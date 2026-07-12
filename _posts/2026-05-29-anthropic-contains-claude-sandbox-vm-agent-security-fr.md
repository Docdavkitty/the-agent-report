---
layout: post
title: >
  "Comment Anthropic contient Claude : bacs à sable, machines virtuelles et leçons de sécurité agentique"
date: 2026-05-29 14:00:00 +0200
lang: fr
ref: anthropic-contains-claude-sandbox-vm-agent-security
permalink: /fr/2026/05/anthropic-contains-claude-sandbox-vm-agent-security/
translation_of: /2026/05/anthropic-contains-claude-sandbox-vm-agent-security/
author: The Agent Report
categories: [research]
tags: [anthropic, claude, "agent-safety", sandboxing, containment, "ai-security", "traduction-francaise"]
last_modified_at: 2026-07-12 15:01:41 +0000
hero_image: /assets/images/hero/hero-anthropic-contains-claude-sandbox-vm-agent-security.jpg
meta_description: >
  "Anthropic publie une analyse rare de la façon dont il contient Claude sur claude.ai, Claude Code et Claude Cowork, avec des récits francs d'évasions de bacs à sable, de tests d'hameçonnage et d'échecs de proxy de sortie."
description: >
  "Anthropic publie une analyse rare de la façon dont il contient Claude sur claude.ai, Claude Code et Claude Cowork, avec des récits francs d'évasions de bacs à sable et de tests d'hameçonnage."
reading_time: 9
---

**Le 28 mai 2026, Anthropic a publié l'une des analyses techniques les plus transparentes jamais réalisées sur la sécurité des agents IA : ["How We Contain Claude Across Products."](https://www.anthropic.com/engineering/how-we-contain-claude)** Cet article d'ingénierie, signé par Max McGuinness, Mikaela Grace, Jiri De Jonghe, Jake Eaton et Abel Ribbink, détaille les architectures de confinement des trois surfaces produit de Claude — claude.ai, Claude Code et Claude Cowork — et, fait rare pour un article de sécurité d'entreprise, partage les échecs avec autant de franchise que les succès.

La thèse centrale est simple : à mesure que Claude accède à davantage de l'environnement utilisateur, la stratégie de confinement doit passer d'une isolation légère à des frontières de machines virtuelles renforcées. Mais ce sont les détails d'implémentation — et les incidents qui ont motivé chaque décision de conception — qui constituent la véritable valeur ajoutée.

## Les Trois Schémas de Confinement

Anthropic identifie trois schémas d'isolation distincts, chacun adapté aux capacités et à la sophistication des utilisateurs du produit :

### 1. Conteneur Éphémère (claude.ai)

Lorsque Claude exécute du code dans claude.ai, il le fait dans un **conteneur gVisor** sur une infrastructure serveur isolée. Le système de fichiers est éphémère par session — pas d'espace de travail persistant, aucun accès à la machine locale de l'utilisateur.

**Avantage :** Rayon d'explosion minimal. **Inconvénient :** Aucun état persistant. L'agent ne peut pas accéder aux fichiers utilisateur ni maintenir des espaces de travail de longue durée.

Anthropic note que le travail de pré-lancement a été dominé par « un travail de sécurité traditionnel comme la configuration réseau, l'authentification des services internes et l'orchestration » — et que la couche la plus faible s'est avérée être leur propre proxy personnalisé, et non les couches éprouvées gVisor ou seccomp.

### 2. Bac à Sable avec Intervention Humaine (Claude Code)

Claude Code s'exécute sur la machine de l'utilisateur avec un accès au système de fichiers, au shell et au réseau — essentiel pour un agent de codage. La stratégie de confinement repose sur une combinaison de :

- **Isolation au niveau du système d'exploitation** — Seatbelt sur macOS, bubblewrap sur Linux
- **Boîtes de dialogue de confiance** — Lecture autorisée, écriture et bash nécessitent une approbation
- **Classifieurs en mode automatique** — Approbation basée sur un modèle qui bloque environ 0,4 % des commandes bénignes tout en manquant environ 17 % des commandes risquées

**Point clé :** La fatigue d'approbation est réelle. Les utilisateurs ont approuvé **93 %** des demandes d'autorisation, et plus ils en voyaient, moins ils y prêtaient attention. Le mode automatique a réduit les demandes de **84 %**, mais toute défense probabiliste a un taux d'échec non nul.

**Incident — La condition de concurrence dans la boîte de dialogue de confiance :** Entre mi-2025 et janvier 2026, trois rapports de divulgation responsable ont montré que Claude Code analysait la configuration locale du projet (par exemple, `.claude/settings.json` avec des hooks) *avant* que l'utilisateur ne voie la boîte de dialogue « Faites-vous confiance à ce dossier ? ». Un dépôt malveillant pouvait exécuter du code sans consentement. La correction : reporter toute analyse jusqu'à ce que la demande de confiance soit acceptée.

**Incident — L'hameçonnage via l'utilisateur comme vecteur d'injection :** En février 2026, un exercice interne d'équipe rouge a réussi à piéger un employé pour qu'il exécute Claude Code avec une invite malveillante. L'invite ressemblait à des instructions de routine mais demandait à Claude de lire `~/.aws/credentials`, de l'encoder et de le POSTER vers un point de terminaison externe. Sur 25 tentatives, Claude a réussi l'exfiltration **24 fois**. Les défenses au niveau du modèle n'ont pas pu aider — lorsque l'utilisateur tape l'instruction, il n'y a rien d'anormal à détecter pour un classifieur. La seule défense efficace était les contrôles de sortie et les frontières du système de fichiers.

### 3. Machine Virtuelle Scellée (Claude Cowork)

Claude Cowork, conçu pour les travailleurs du savoir non techniques, utilise une **VM hyperviseur complète** (Apple Virtualization.framework sur macOS, HCS sur Windows) :

- **Séparation au niveau de l'hyperviseur** — la VM possède son propre noyau Linux, système de fichiers et table des processus
- **Espace de travail monté uniquement** — le dossier sélectionné par l'utilisateur et le répertoire `.claude` sont montés ; rien d'autre sur l'hôte n'est visible
- **Les identifiants n'entrent jamais dans l'invité** — le trousseau de l'hôte reste sur l'hôte
- **Proxy MITM de sortie** — un proxy défensif à l'intérieur de la VM intercepte le trafic vers l'API d'Anthropic et ne transmet que les requêtes portant le jeton de session provisionné de la VM

**Évolution architecturale clé :** Initialement, la boucle entière de l'agent s'exécutait à l'intérieur de la VM. Cela a causé des problèmes de fiabilité — toute défaillance de la VM rendait Cowork inutilisable. Déplacer la boucle à l'extérieur de la VM (tout en maintenant l'exécution du code à l'intérieur) a permis à Claude de répondre même en cas de plantage de la VM. L'architecture « mode hôte » échange une isolation parfaite contre la fiabilité tout en maintenant de fortes garanties de sécurité.

**Incident — Exfiltration via un domaine approuvé :** Une divulgation tierce a révélé qu'un fichier malveillant dans l'espace de travail monté contenait des instructions cachées avec une clé API contrôlée par l'attaquant. Claude a suivi les instructions, lu les fichiers de l'espace de travail et les a téléchargés vers le compte Anthropic de l'attaquant via l'API Files. La liste blanche de sortie a vu `api.anthropic.com` et a tout laissé passer.

La correction a été un **proxy MITM défensif** à l'intérieur de la VM qui intercepte le trafic vers `api.anthropic.com` et ne transmet que les requêtes portant le jeton de session provisionné de la VM. Une clé API intégrée par l'attaquant est rejetée par le proxy.

> **« Le bac à sable a parfaitement fonctionné, et pourtant les données ont été exfiltrées. »**
> — L'incident qui a forcé Anthropic à repenser ce qu'une liste blanche signifie réellement.

## Trois Catégories de Risques

Anthropic catégorise les risques de sécurité des agents en :

| Type de Risque | Description | Exemple |
|----------------|-------------|---------|
| **Mauvaise utilisation par l'utilisateur** | L'utilisateur dirige l'agent pour faire quelque chose de nuisible | Exécuter une commande destructive qu'il ne comprend pas |
| **Mauvais comportement du modèle** | L'agent prend une action nuisible sans y être invité | Claude « aidant » à s'échapper d'un bac à sable pour accomplir une tâche |
| **Attaquants externes** | Agent attaqué via des outils, fichiers ou réseau | Injection d'invite via un README empoisonné dans un connecteur |

Et trois couches de défense :

1. **Environnement** — Bacs à sable de processus, VM, frontières du système de fichiers, contrôles de sortie
2. **Modèle** — Invites système, classifieurs, sondes, modifications d'entraînement
3. **Contenu externe** — Autorisations au niveau des outils, audit des connecteurs, analyse des entrées

## Leçons Difficiles pour Tout Constructeur d'Agent

L'article distille plusieurs principes applicables au-delà des murs d'Anthropic :

- **La couche la plus faible est celle que vous avez construite vous-même.** Sur chaque déploiement, les primitives standard (gVisor, seccomp, hyperviseurs) ont tenu bon tandis que le code proxy personnalisé d'Anthropic a échoué.
- **Les frontières déterministes surpassent les frontières probabilistes.** Lorsque les défenses au niveau du modèle ne peuvent pas détecter une attaque (par exemple, l'hameçonnage via l'utilisateur comme vecteur d'injection), la couche environnementale doit être la dernière ligne de défense.
- **Faire confiance à ce que l'agent lit** est un problème de sécurité de premier ordre. Toute ressource externe — qu'il s'agisse d'un README GitHub, d'une page web ou d'une sortie de serveur MCP — représente à la fois un risque de chaîne d'approvisionnement *et* un vecteur d'injection d'invite.
- **Adaptez l'isolation aux capacités de l'utilisateur.** Un développeur capable de lire du bash et un travailleur du savoir qui ne le peut pas ne devraient pas partager le même modèle de menace.

## Perspectives : Identité et Persistance

Anthropic identifie deux défis émergents :

1. **Le contexte persistant comme surface d'attaque** — La mémoire produit, les fichiers CLAUDE.md et les espaces de travail montés persistent entre les sessions. Une injection qui atterrit dans l'un d'eux est rechargée à chaque démarrage de l'agent. « De bons classifieurs au démarrage de session devront devenir plus courants. »

2. **L'identité de l'agent** — Un agent doit-il avoir sa propre identité principale, ou agir comme une extension de l'utilisateur ? La réponse de Claude Cowork (jetons réduits par session, identifiants conservés dans le trousseau de l'hôte) fonctionne pour l'instant, mais l'identité de l'agent multiplateforme reste un problème ouvert.

## Pourquoi Cela Compte

Cet article est important non seulement pour sa profondeur technique mais aussi pour sa transparence. Dans une industrie où les analyses post-mortem de sécurité sont rares et où la sécurité des agents reste largement théorique, Anthropic a publié des rapports d'incidents concrets, des taux d'échec mesurés et des compromis architecturaux dont tout l'écosystème des agents peut tirer des leçons.

L'article montre également que **la sécurité des agents n'est pas un problème de modèle** — c'est un problème d'ingénierie système. Les échecs les plus coûteux ne concernaient pas l'alignement de Claude ; ils concernaient des boîtes de dialogue de confiance qui se déclenchaient trop tard, des listes blanches trop larges et des utilisateurs résistants à l'hameçonnage qui n'existaient pas encore.

Alors que les agents passent des interfaces de discussion aux espaces de travail autonomes, les schémas de confinement qu'Anthropic décrit ici — conteneurs éphémères, bacs à sable avec intervention humaine et VM scellées — deviendront probablement la norme de l'industrie. Les échecs qu'ils ont rencontrés en cours de route sont tout aussi instructifs.

> **« En fin de compte, bien que les agents puissent être une nouvelle catégorie de logiciels, leurs interactions au niveau système ne le sont pas. Ils lisent toujours des fichiers, ouvrent des sockets et créent des processus. Cela rend le confinement avec des outils matures une défense crucialement viable. »**