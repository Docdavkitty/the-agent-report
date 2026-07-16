---
layout: post
title: >
  "Block open-source Goose : comment un fichier YAML a étendu un agent IA à 60 % de l'entreprise"
date: 2026-05-27 14:00:00 +0200
lang: fr
ref: block-goose-ai-agent-recipe-runner-scaled-60-percent
permalink: /fr/2026/05/block-goose-ai-agent-recipe-runner-scaled-60-percent/
translation_of: /2026/05/block-goose-ai-agent-recipe-runner-scaled-60-percent/
author: The Agent Report
categories: ["tools-frameworks"]
tags: [goose, block, square, "open-source", mcp, "enterprise-adoption", "agent-framework", "traduction-francaise"]
last_modified_at: 2026-07-16 15:01:57 +0000
hero_image: >
  /assets/images/hero/hero-block-goose-ai-agent-recipe-runner-scaled-60-percent.jpg
meta_description: >
  "Block a open-sourcé Goose, qui s'est étendu à 60 % des 12 000 employés via des fichiers YAML que tout membre peut créer, atteignant 44 000 étoiles GitHub et 368."
description: >
  "Block a open-sourcé Goose, étendu à 60 % des 12 000 employés via des fichiers YAML que tout membre peut créer, atteignant 44 000 étoiles GitHub et 368."
reading_time: 6
---

Block — la société mère de Square, Cash App et Afterpay — a publié **Goose** en tant qu'agent IA open source début 2025. Un an plus tard, l'outil cumule **plus de 44 000 étoiles GitHub, 368 contributeurs et 2 600 forks**. Mais le chiffre clé n'est pas l'adoption open source. C'est l'adoption interne : **environ 60 % des quelque 12 000 employés de Block utilisent Goose chaque semaine**, couvrant 15 profils métiers différents — ingénierie, ventes, design, produit et succès client.

La question qui s'impose est évidente : comment un simple outil CLI peut-il servir à la fois un ingénieur qui débogue un test instable et un chef de produit qui trie un ticket Jira ?

La réponse tient dans un **fichier YAML de 30 lignes**.

## L'architecture : agent local, outils MCP, flux de travail par recette

Goose est un binaire Rust qui s'exécute entièrement sur la machine de l'utilisateur. Il se connecte à n'importe quel grand fournisseur de LLM — Anthropic, OpenAI, Gemini, Mistral, xAI, ou un modèle local via Ollama — et utilise les serveurs **MCP (Model Context Protocol)** comme surface d'outils. L'architecture repose sur trois couches qui évoluent indépendamment :

1. **Le runtime agent** — une boucle centrale (planifier → appeler des outils → évaluer → répéter) qui reste générique.
2. **Le système d'extension** — chaque outil est un serveur MCP. Ajouter un accès GitHub, une intégration Jira ou une API interne est une entrée de configuration, pas une modification de code.
3. **La recette** — un document YAML qui regroupe instructions, extensions requises, paramètres et prompt dans un seul fichier partageable.

La séparation est intentionnelle. L'agent ne décide pas quels outils charger — c'est la recette qui le fait. L'agent ne navigue pas librement dans la tâche — la recette fournit une séquence numérotée avec des points de contrôle.

## À quoi ressemble une recette

Une recette est un fichier YAML que n'importe quel membre de l'équipe peut créer. Voici un exemple abrégé pour la revue d'une pull request GitHub :

```yaml
name: review-pr
description: Examiner une PR GitHub pour identifier les zones à risque
params:
  pr_url:
    type: string
    description: L'URL de la PR GitHub à examiner.
extensions:
  - name: developer
  - name: github
    args: ["-y", "@modelcontextprotocol/server-github"]
prompt: |
  1. Récupérez le diff de la PR et la liste des fichiers modifiés.
  2. Pour chaque fichier, identifiez : les changements de comportement,
     les nouvelles dépendances, les tests manquants, tout ce qui semble bâclé.
  3. Regroupez les résultats par sévérité : doit-corriger, devrait-corriger, détail.
  4. Publiez un seul commentaire de revue avec les résultats regroupés.
```

La recette s'exécute avec une seule commande :

```bash
goose recipe run review-pr --params pr_url=https://github.com/org/repo/pull/42
```

Le bloc `params` fait de la recette une fonction — vous l'appelez avec différentes entrées au lieu d'en écrire une par tâche. Le bloc `extensions` charge dynamiquement les serveurs MCP pour la durée de l'exécution et les supprime ensuite. Les étapes numérotées du prompt servent de squelette de planification — l'agent ne réinvente pas le flux de travail à chaque fois.

## Pourquoi ce modèle a fait ses preuves à grande échelle

Le format de recette est la percée architecturale qui explique le chiffre d'adoption. Un **fichier YAML est quelque chose qu'un chef de produit peut créer**. Il peut copier une recette écrite par un collègue, modifier le prompt, l'exécuter et voir ce qui se passe — sans déploiement, sans revue de code, sans transfert vers l'ingénierie.

Pour les ingénieurs, la valeur est différente : une recette est un **artefact versionnable** qui vit dans le même dépôt que le code qu'elle manipule. Le flux de travail de revue d'une équipe se trouve dans `recipes/review-pr.yaml` à côté du code du service. Les nouveaux embauchés lisent la recette pour comprendre le flux de travail. Les modifications sont examinées comme n'importe quel autre artefact.

La couche d'extension MCP est le multiplicateur. Chaque nouvelle capacité interne est une construction unique de serveur MCP, puis elle est disponible pour toutes les recettes. Block ne crée pas un "agent de revue de PR" séparé et un "agent de tri de tickets". Ils écrivent **un seul binaire Goose**, puis livrent un répertoire de recettes et un répertoire de serveurs MCP. **La composition fait le reste.** Ce modèle de composition basé sur MCP est un thème central dans notre [Guide ultime des frameworks d'agents IA open source]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).

## Goose est désormais un projet fondation

Dans une décision qui change le calcul des risques pour l'adoption en entreprise, Goose est passé de la gouvernance de Block à la **Agentic AI Foundation sous la Linux Foundation**. L'outil est désormais un projet gouverné par la communauté — aucune entreprise unique ne contrôle sa feuille de route.

Les implications sont significatives. Le risque de gouvernance qui freinait les équipes en entreprise ("et si Block arrêtait d'investir ?") a disparu. L'activité récente de la communauté pointe vers un registre public de recettes, une interopérabilité renforcée des serveurs MCP et des types de paramètres plus riches, y compris les téléchargements de fichiers et les objets structurés.

## Ce que cela signifie pour le secteur

Le modèle de recette de Goose est le signal le plus fort à ce jour que l'avenir des agents IA en entreprise ne repose pas sur de meilleurs modèles — mais sur des **abstractions de flux de travail que les non-ingénieurs peuvent créer**. La recette est un modèle architectural, pas une fonctionnalité propre à Goose. La même structure fonctionne avec les compétences Claude Code, les agents Cursor, ou tout runtime prenant en charge les flux de travail définis en YAML et les outils MCP. Pour une vue d'ensemble de l'évolution des outils agents open source, consultez notre classement des [20 meilleurs outils agents IA open source](/2026/06/top-20-open-source-ai-agent-tools-2026/).

Le message à retenir pour toute équipe construisant des plateformes agents internes : si votre système n'a pas d'équivalent pour la recette, vous allez vous retrouver avec des constructions d'agents sur mesure par équipe. La recette est ce qui permet à un seul outil de servir une entreprise de 12 000 personnes sans avoir à forker.

L'abstraction banale — un fichier YAML avec un nom, un prompt et une liste d'extensions — est ce qui permet d'atteindre 60 % de l'entreprise.