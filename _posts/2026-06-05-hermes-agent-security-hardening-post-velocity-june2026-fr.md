---
layout: post
title: >
  "Sprint de sécurité post-Velocity d'Hermes Agent — masquage OAuth Google, correction de fuite cron et vague de renforcement"
date: 2026-06-05 14:00:00 +0200
lang: fr
ref: hermes-agent-security-hardening-post-velocity-june2026
permalink: /fr/2026/06/hermes-agent-security-hardening-post-velocity-june2026/
translation_of: /2026/06/hermes-agent-security-hardening-post-velocity-june2026/
author: The Agent Report
categories: ["hermes-agent"]
tags: ["hermes-agent", "nous-research", "open-source", security, "promptware-defense", "oauth-redaction", "agent-security", hardening, "traduction-francaise"]
last_modified_at: 2026-07-03 15:02:32 +0000
hero_image: >
  /assets/images/hero/hero-hermes-agent-security-hardening-post-velocity-june2026.jpg
meta_description: >
  "La version v0.15 Velocity d'Hermes Agent a introduit la défense contre les promptwares — et la semaine suivante, une vague coordonnée de correctifs de sécurité a été déployée : masquage des tokens OAuth Google, assainissement des chemins d'erreur cron, renforcement des modèles par défaut, etc."
description: >
  "La version v0.15 Velocity d'Hermes Agent a introduit la défense contre les promptwares — et la semaine suivante, une vague de correctifs de sécurité a été déployée : masquage des tokens OAuth Google, assainissement des erreurs cron, renforcement des modèles par défaut, etc."
reading_time: 7
---

Il y a une semaine, Hermes Agent v0.15.0 — la « Velocity Release » — a été lancée avec **1 302 commits, 747 PRs fusionnées et 321 contributeurs de la communauté**. Les fonctionnalités phares étaient la refonte à 76 % de `run_agent.py`, la plateforme multi-agents Kanban, les accélérations du démarrage à froid et la `session_search` reconstruite. Mais enfouie dans le changelog se trouvait une fonctionnalité qui pourrait être la plus importante pour les utilisateurs en production : le **système de défense contre les promptwares** — trois couches de protection contre les attaques de type « brainworm ».

Cette semaine, cette fondation sécuritaire s'est épaissie.

Le 5 juin seulement, une vague coordonnée de correctifs a touché la branche `main` : la rédaction des jetons Google OAuth, l'assainissement des informations d'identification dans les chemins d'erreur des tâches cron, le durcissement des modèles par défaut pour éviter des factures accidentelles de 50 $/heure, et plusieurs autres correctifs ciblés. Voici ce qui a changé, pourquoi c'est important, et ce que cela signifie pour l'évolution de la posture de sécurité d'Hermes Agent.

> **Remarque :** Ces correctifs sont fusionnés dans `main` mais n'ont pas encore été étiquetés dans une version. Vous pouvez les suivre dans les [PRs ouvertes](https://github.com/NousResearch/hermes-agent/pulls) et mettre à jour via `hermes update` une fois qu'ils seront dans une branche de version.

## La Défense Contre les Promptwares Qui a Tout Commencé

Avant de plonger dans les correctifs de cette semaine, il est utile de comprendre ce que la v0.15.0 a déjà livré. La « Velocity Release » a introduit une **défense à trois points d'étranglement contre les promptwares** ([#27248](https://github.com/NousResearch/hermes-agent/pull/27248)) :

1.  **`tools/threat_patterns.py`** — ~15 nouveaux modèles d'injection de prompt détectés au moment de l'appel d'outil, couvrant les attaques de type « brainworm » qui tentent d'exfiltrer le contexte ou de modifier le comportement de l'agent.
2.  **Analyse de la mémoire rappelée** — chaque élément de mémoire persistante est analysé pour détecter des modèles d'injection *au moment du chargement*, avant qu'il n'atteigne la fenêtre de contexte de l'agent.
3.  **Marqueurs de délimitation des résultats d'outil** — des délimiteurs injectés autour de chaque sortie d'outil pour empêcher qu'une injection de prompt réussie basée sur des délimiteurs ne contamine les résultats d'outil suivants.

Ensemble, ces défenses ont fait d'Hermes Agent l'un des rares frameworks open source avec une **détection d'injection au moment de l'exécution** — pas seulement un filtrage statique, mais une surveillance comportementale à travers la mémoire, les outils et les sorties. Le framework a été mentionné dans plusieurs synthèses de sécurité pour cette architecture.

## Vague de Correctifs du 5 Juin : Quatre Correctifs de Sécurité en Un Jour

La « Velocity Release » a peut-être livré les fondations, mais la sécurité n'est jamais terminée. Hier a vu quatre PRs significatives axées sur la sécurité fusionnées ou ouvertes :

### 1. Rédaction des Jetons Google OAuth ([#39697](https://github.com/NousResearch/hermes-agent/pull/39697))

**Auteur :** [@briandevans](https://github.com/briandevans) | **Statut :** Fusionnée

Le nettoyeur de secrets existant (`agent/redact.py`) avait une liste de blocage basée sur des préfixes pour détecter les clés API dans les sorties d'outils et les journaux — les jetons OpenAI, Anthropic, xAI étaient tous couverts. Mais les **jetons Google OAuth 2.0 bruts** — qui commencent par `ya29.` — et les **jetons d'actualisation** — qui commencent par `1//` — n'avaient aucune entrée de préfixe. Ils n'étaient rédigés que lorsqu'ils étaient adjacents à un nom de clé JSON.

Cette PR a comblé le **Gap #2** du problème [#39654](https://github.com/NousResearch/hermes-agent/issues/39654) en ajoutant deux nouveaux motifs regex :

```python
r"ya29\.[A-Za-z0-9_-]{20,}",   # Jeton d'accès Google OAuth
r"1//[A-Za-z0-9_-]{20,}",      # Jeton d'actualisation Google OAuth
```

Le suffixe minimum de 20 caractères empêche les courtes chaînes non-jetons (comme `1//foo`) d'être faussement rédigées — confirmé par un cas de test dédié.

C'est important car Hermes Agent interagit avec les services Google via des outils (automatisation du navigateur, Google Drive, Gmail via MCP) et via les flux d'authentification de la Gateway. Un jeton `ya29.` non rédigé dans une sortie d'outil ou un journal d'erreurs pourrait donner accès à l'ensemble de Google Workspace d'un utilisateur.

> **Connexe :** Cela suit le même modèle que le correctif de rédaction de clé xAI (préfixe `xai-`, commit `5613dfe`), également du cycle précédent. Le modèle devient un modèle pour la couverture des informations d'identification spécifiques au fournisseur.

### 2. Rédaction du Chemin d'Erreur LLM Cron ([#39702](https://github.com/NousResearch/hermes-agent/pull/39702))

**Auteur :** [@shivros](https://github.com/shivros) | **Statut :** Ouverte (Brouillon → Prête)

Lorsqu'une tâche cron basée sur un LLM échoue — par exemple, une génération de rapport planifiée ou un briefing nocturne — le message d'exception brut était délivré **textuellement** dans le chat de l'utilisateur (Telegram, Discord, etc.) et persisté en **texte clair dans `jobs.json`**.

Le problème : les messages d'erreur du fournisseur peuvent contenir **des fragments de clé API, des jetons porteurs ou des URL de point de terminaison avec des informations d'identification intégrées**. Un message d'erreur tronqué comme `Authentication failed: sk-proj-...` divulguerait les ~40 premiers caractères d'une clé de session.

Le correctif est une seule ligne : appeler `redact_sensitive_text()` sur `error_msg` immédiatement après sa construction dans `cron/scheduler.py` (ligne ~1900), correspondant au même modèle défensif déjà utilisé dans le chemin du script `no_agent` (lignes 1019–1024). L'import suit la convention établie dans la fonction, et un wrapper `try/except Exception: pass` assure une dégradation gracieuse si la rédaction elle-même échoue.

Les deux revues automatisées (GPT-5.5 et Gemini 3 Flash) ont approuvé le changement comme « correct et atteignant l'objectif déclaré ».

### 3. Durcissement du Modèle par Défaut ([#39708](https://github.com/NousResearch/hermes-agent/pull/39708))

**Auteur :** [@teknium1](https://github.com/teknium1) | **Statut :** Fusionnée

Avant ce correctif, si Hermes Agent ne pouvait pas déterminer quel modèle utiliser (par exemple, en raison d'une configuration incomplète ou d'un fournisseur mal configuré), il **se rabattait silencieusement sur le modèle phare le plus cher de Nous**. Pour les utilisateurs fonctionnant avec une facturation API, cela signifiait des coûts surprises potentiels de 40 à 50 $/heure.

Le correctif garantit que lorsque la logique de résolution de modèle ne trouve pas de correspondance, elle ne remonte pas silencieusement à l'option la plus chère. Au lieu de cela, elle se rabat sur une valeur par défaut raisonnable — ou affiche clairement une erreur afin que l'utilisateur puisse la configurer correctement. Il s'agit à la fois d'un correctif de **sécurité des coûts** et de **sécurité de disponibilité** : personne ne veut voir son budget cron explosé par une mise à niveau silencieuse du modèle.

### 4. Bootstrap Desktop & Correctifs Divers ([#39707](https://github.com/NousResearch/hermes-agent/pull/39707))

**Auteur :** [@teknium1](https://github.com/teknium1) | **Statut :** Fusionnée

Un correctif plus petit mais révélateur : le marqueur de bootstrap Desktop était automatiquement mis de côté par `hermes update` car il n'était pas dans `.gitignore`. Cela signifiait qu'à chaque fois que les utilisateurs exécutaient `hermes update`, ils perdaient leur marqueur d'installation Desktop et devaient relancer le bootstrap. L'entrée `.gitignore` empêche désormais cela.

Bien qu'il ne s'agisse pas d'un correctif de sécurité au sens traditionnel, il empêche un **problème de disponibilité** : les utilisateurs exécutant `hermes update` ne devraient pas perdre leur configuration Desktop.

## Le Tableau de Sécurité Plus Large

Cette vague de correctifs est significative pour ce qu'elle dit de la **maturation de la sécurité d'Hermes Agent** :

| Domaine | Ce Qui a Changé | Risque Réduit |
| :--- | :--- | :--- |
| **Prévention des fuites d'identifiants** | Rédaction OAuth Google ajoutée à la liste de blocage des préfixes | Vol de jeton via les sorties d'outils / journaux |
| **Gestion des erreurs Cron** | Messages d'erreur rédigés avant livraison/persistance | Fuite d'identifiants via les échecs de tâches planifiées |
| **Sélection du modèle** | Pas de repli silencieux vers le modèle le plus cher | Surprises de coûts / choc de facturation |
| **Infrastructure de mise à jour** | Marqueur Desktop exclu du git stash | Disponibilité Desktop après les mises à jour |

La défense contre les promptwares de la « Velocity Release » traitait les **attaques par injection actives** — les exploits de type « brainworm » et l'injection de prompt ad-hoc. Les correctifs de cette semaine traitent les **vecteurs de fuite passifs** — les informations d'identification qui se retrouvent à des endroits où elles ne devraient pas être via un fonctionnement normal. Ensemble, ils forment une défense en profondeur.

## Ce Qui Est Encore en Cours

Tout n'est pas résolu. Le problème [#39654](https://github.com/NousResearch/hermes-agent/issues/39654) — qui a motivé la rédaction Google OAuth — a identifié **deux lacunes** :

- **Gap #1 (reporté) :** Rédaction au niveau de la persistance dans `state.db` — les informations d'identification qui fuient dans la base de données de session ne sont pas encore nettoyées lors de l'écriture.
- **Gap #2 (corrigé) :** Rédaction des journaux/sorties d'outils — traitée par la PR #39697.

La lacune de persistance est un problème plus difficile — elle nécessite soit une rédaction lors de l'écriture (ce qui pourrait détruire les données nécessaires au débogage), soit un magasin d'informations d'identification crypté séparé. Attendez-vous à plus de discussions à ce sujet dans les semaines à venir.

De plus, le bloc `except` de `_process_job` à `cron/scheduler.py:2087–2089` passe `str(e)` à `mark_job_run()` sans rédaction. Ce chemin ne se déclenche que pour les exceptions d'infrastructure, pas pour les erreurs de fournisseur LLM, donc le risque est plus faible — mais un audit complet finirait par l'aborder.

## Les Contributions de Sécurité de la Communauté Sont en Hausse

Une tendance notable : les PRs axées sur la sécurité proviennent de plus en plus de **contributeurs de la communauté**, et pas seulement des mainteneurs principaux. La PR #39697 venait de [@briandevans](https://github.com/briandevans), la PR #39702 de [@shivros](https://github.com/shivros). Cela correspond à un modèle plus large :

- 19 problèmes étiquetés « sécurité » ont été fermés dans la v0.15.0 seulement
- Le système de défense contre les promptwares était une conception collaborative de la communauté ([#27248](https://github.com/NousResearch/hermes-agent/pull/27248))
- La compétence `hermes-agent` inclut des modèles de durcissement de la sécurité soumis par les membres de la communauté

Pour les organisations qui évaluent Hermes Agent pour une utilisation en production, c'est un signal positif : la surface de sécurité est activement auditée par une large communauté, et pas seulement par une petite équipe interne.

## Le Point à Retenir

La version v0.15 « Velocity » concernait la **vitesse et l'échelle** — démarrages à froid plus rapides, recherche plus rapide, itération plus rapide. La semaine qui a suivi a concerné la **sécurité et la stabilité** — fermeture des voies de fuite d'identifiants, durcissement de la gestion des erreurs et prévention des surprises de coûts.

C'est le rythme d'un projet open source en maturation : de grandes versions de fonctionnalités suivies de sprints de durcissement ciblés. Pour les utilisateurs en production, le message est clair : Hermes Agent est construit avec la sécurité opérationnelle comme une préoccupation de premier ordre, et non comme une réflexion après coup.

Si vous exécutez Hermes Agent en production — ou si vous l'évaluez pour un déploiement — ces correctifs valent la peine d'être suivis. Les correctifs de rédaction d'identifiants et de modèle par défaut à eux seuls traitent deux des points douloureux les plus courants pour les déploiements d'agents auto-hébergés : **la fuite d'identifiants** et **les coûts API inattendus**.

Restez à l'écoute. Le sprint de durcissement post-v0.15 est toujours en cours, et d'autres correctifs sont probables avant la prochaine version étiquetée.