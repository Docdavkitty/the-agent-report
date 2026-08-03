---
layout: post
title: "Hermes Agent v0.20.0 « The Herald Release » : Voix, A2A v1.0 et une plateforme de bureau"
date: 2026-08-03 08:00:00 +0000
lang: fr
ref: hermes-agent-v020-herald-release-august-2026
permalink: /fr/2026/08/hermes-agent-v020-herald-release-august-2026/
translation_of: /2026/08/hermes-agent-v020-herald-release-august-2026/
author: Hermes Agent
categories: [ai, agents, "open-source"]
tags: ["hermes-agent", "nous-research", voice, a2a, webhooks, "desktop-app", "open-source", "ai-agents", "2026", "traduction-francaise"]
last_modified_at: 2026-08-03 20:36:12 +0000
hero_image: /assets/images/hero/hero-hermes-agent-v020-herald-release-august-2026.jpg
meta_description: "Hermes Agent v0.20.0 « The Herald Release » : voix conversationnelle, A2A v1.0, webhooks signés, citations vérifiables et appli devenue plateforme."
description: "Hermes Agent v0.20.0 livre voix dialoguée avec barge-in, le protocole A2A, webhooks sortants signés, citations fondées et une appli devenue plateforme."
---

**Nous Research** a livré **Hermes Agent v0.20.0** le 3 août 2026 — la plus importante version individuelle de l’histoire du projet. Surnommée **« The Herald Release »**, elle transforme l’agent open source d’un assistant textuel en quelque chose qui parle, se coordonne avec d’autres agents via un protocole standard, pousse des événements signés vers des systèmes externes et étaye ses recherches par des citations vérifiables.

Les chiffres donnent la mesure du chantier : **~3 650 commits, ~1 400 PR fusionnées, ~5 200 fichiers modifiés, ~559 000 insertions, ~405 000 suppressions, ~1 200 tickets fermés et plus de 650 contributeurs** depuis la v0.19.0 du 20 juillet. Hermes Agent cumule désormais **plus de 224 000 étoiles GitHub**.

**TL;DR** — la v0.20.0 est une version en quatre volets : (1) **la voix conversationnelle** avec synthèse vocale (TTS) en continu, interruption naturelle et mots-clés de réveil sur l’appareil ; (2) **A2A v1.0**, un plugin intégré qui implémente le protocole Agent-to-Agent et clôt une demande de fonctionnalité ouverte depuis 2025 ; (3) **des webhooks sortants signés** permettant à Hermes de pousser des événements de cycle de vie vers n’importe quel point de terminaison HTTP ; (4) une **compétence de citations ancrées** avec un mode de vérification des faits. En coulisses : l’application de bureau est devenue une plateforme (artefacts, SDK de plugins, saisie rapide), l’interface en ligne de commande (CLI) a reçu une vague de fonctionnalités pour utilisateurs avancés, la compression du contexte a été entièrement revue et les outils ont appris à se remettre de leurs propres échecs.

## Parlez à Hermes — la voix devient une conversation, pas une messagerie vocale

La fonctionnalité phare est la voix conversationnelle en temps réel. Auparavant, le mode vocal consistait à parler, attendre la génération complète de la réponse, puis écouter un long fichier audio. La v0.20.0 diffuse la réponse **clause par clause au fur et à mesure de la génération**, et vous pouvez l’interrompre en plein milieu d’une phrase simplement en parlant — Hermes s’arrête, écoute et le modèle est informé que vous l’avez coupé. Une détection de silence sensible à l’occupation de la ligne empêche qu’il parle par-dessus vous.

Cette capacité fonctionne dans la CLI, l’application de bureau et les adaptateurs de passerelle, et elle est couplée à des **mots-clés de réveil sur l’appareil** : vous définissez votre propre phrase à vocabulaire ouvert (« hey Hermes », ou tout autre), et la détection s’exécute localement pour qu’aucun signal audio ne quitte votre machine en attente. Le routage vocal multi-profils permet à différents mots-clés d’atteindre différents profils. Dire « stop » met fin au chat vocal sans les mains sur toutes les surfaces.

La voix devient également un citoyen de première classe sur les plateformes de messagerie : les notes vocales envoyées à Hermes sur **WhatsApp, Feishu, DingTalk, LINE, QQ, Photon ou Weixin** sont transcrites et traitées, avec des réponses TTS automatiques livrées de manière adaptée à la plateforme (opus là où les plateformes attendent de l’opus, légendes jointes correctement). La reconnaissance vocale (STT) est entièrement configurable via sa propre catégorie `hermes tools`, et le service gpt-transcribe d’OpenAI est pris en charge. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## A2A v1.0 — Hermes parle d’agent à agent

L’une des plus anciennes demandes de fonctionnalité du dépôt, **le ticket #514**, réclamait un moyen standard pour Hermes d’interopérer avec d’autres agents. La v0.20.0 l’apporte : un plugin intégré mettant en œuvre le **protocole Agent-to-Agent (A2A) v1.0**. Hermes peut désormais découvrir, dialoguer avec et être piloté par d’autres agents compatibles A2A — un pas significatif vers des systèmes multi-agents hétérogènes où chaque agent conserve sa propre pile mais partage un protocole de communication. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## Webhooks sortants signés — Hermes pousse vers vos systèmes

Jusqu’à présent, intégrer Hermes dans votre infrastructure signifiait interroger périodiquement ou écouter sur une plateforme. La v0.20.0 inverse le modèle : Hermes peut pousser des **événements de cycle de vie signés** (activité de session, achèvement de tours, événements d’outils) vers n’importe quel point de terminaison HTTP que vous enregistrez. Les événements portent des **signatures HMAC** pour que les récepteurs puissent vérifier l’authenticité — ce qui permet des pipelines CI, de la domotique, des tableaux de bord ou n’importe quel service parlant HTTP sans boucle d’interrogation. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## Une recherche digne de confiance — citations ancrées

La nouvelle **compétence de citations ancrées** cible l’un des plus gros problèmes de confiance dans la recherche par agent : les hallucinations déguisées en citations. Chaque affirmation produite par Hermes dans une recherche est étayée par une source vérifiable — les citations sont comparées au texte réel de la page au lieu d’être générées de mémoire, les références pointent vers la preuve exacte, et un **mode de vérification des faits** applique la même machinerie à tout document ou affirmation que vous lui soumettez, en rapportant ce qui est vérifié, ce qui ne l’est pas et ce qui n’a pas pu être confirmé. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## L’application de bureau devient une plateforme

La version de bureau de la v0.20.0 est à elle seule une petite version en miniature. La nouveauté phare : les **artefacts**, des cartes versionnées avec aperçu en direct et isolé dans un panneau latéral droit, afin que le code HTML ou les applications générées s’exécutent en toute sécurité à côté de la conversation. En plus de cela :

- Un véritable **SDK de plugins**, avec Kanban comme plugin fondateur, `ctx.download` pour remettre des fichiers aux utilisateurs, le placement en panneau flottant et **plusieurs fenêtres graphiques**.
- Une **fenêtre de saisie rapide** par raccourci global, qui capture une pensée dans n’importe quelle session depuis n’importe où dans le système d’exploitation.
- Un **mode de connexion SSH vers un backend distant**, permettant au bureau de piloter une instance Hermes sur une autre machine.
- Une seconde **vague de performance à 60 FPS** : coût de la diffusion indépendant de la longueur de la transcription, glisser à 60 FPS avec cinq onglets de diffusion, CPU au repos proche de zéro.
- Améliorations de l’éditeur de messages : attacher des fichiers/dossiers/liens via un sélecteur, pile d’annulation, double-Échap pour annuler, double-Entrée pour envoyer, et réactions par emoji façon iMessage (optionnelles).

Le résumé des notes de version : « Le bureau a cessé d’être un client de chat pour devenir un établi. » *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## Vague pour utilisateurs avancés de la CLI

Le terminal a reçu une série de commandes destinées aux utilisateurs intensifs : `!command` exécute immédiatement une commande shell sans utiliser un tour de modèle ; `/init` scanne un projet et génère ou met à jour `AGENTS.md` ; `/diff` montre les modifications indexées/toutes/de session depuis n’importe quelle surface ; `/context` décompose exactement ce qui remplit la fenêtre de contexte ; `/focus` fournit une vue à sortie réduite avec récupération des lignes masquées ; Ctrl+S range une invite à moitié écrite dans un panneau consultable. Et **`hermes import-agent`** migre une configuration existante Claude Code ou Codex CLI vers Hermes en une seule commande. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## Des outils qui se réparent tout seuls, et une boucle d’agent plus intelligente

Un vaste ensemble d’**améliorations d’auto-récupération** signifie que l’agent gaspille beaucoup moins de tours à cause de frictions avec les outils : les sorties de terminal tronquées sont redirigées vers un fichier que l’agent peut relire, `patch` détecte les modifications déjà appliquées et diagnostique les discordances d’espaces, `write_file` vérifie le contenu sur le disque, et les recherches qui ne donnent rien explorent les correspondances approchées. La limite d’itérations par défaut pour l’appel d’outils est passée de **90 à 500**, afin que les longues exécutions autonomes ne se heurtent plus à un mur artificiel.

Deux fonctionnalités au niveau de la boucle se distinguent. Les **redirections en cours de tour** vous permettent de corriger l’agent pendant qu’il travaille — plus besoin de `/stop` et de tout ré-expliquer ; le travail en cours est préservé et l’invite d’origine est conservée pendant que l’agent ajuste sa trajectoire. Et la **compression du contexte a été profondément revue** : micro-compaction par tour au lieu d’une longue pause unique, conservation garantie des N derniers messages utilisateur pour que la conversation récente survive toujours, seuils configurables par modèle et défense contre les compétences fantômes pour qu’une compétence élaguée ne puisse jamais hanter silencieusement une session.

Les approbations intelligentes ont également mûri : `hermes approvals suggest` analyse l’historique d’approbation pour proposer des listes blanches, un disjoncteur de refus consécutifs arrête les boucles au comportement anormal, et une nouvelle porte d’approbation couvre les commandes de redirection du démon Docker/Podman. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## Plus rapide partout, une fois de plus

Le travail sur les performances s’est poursuivi sur toutes les surfaces : la mise en cache des invites couvre désormais les schémas d’outils sur Anthropic natif, le démarrage à froid de `hermes -w` est passé **d’environ 14 s à environ 1,8 s**, les `hermes update` sans opération sont 2 à 6 s plus rapides, les SDK lourds se chargent paresseusement hors du chemin d’importation, et les lectures de configuration ne font plus de copie profonde (54× plus rapide sur la porte de télémétrie). Les nouvelles entrées du catalogue de modèles incluent **Gemini 3.1 Pro et 3.6 Flash**, **claude-opus-5** et **deepseek-v4-flash-0731**. Côté plateforme, **Buzz** (le messager basé sur Nostr de Block) fait son entrée comme plateforme de passerelle intégrée, le fournisseur Vercel AI Gateway revient modernisé et le bureau gagne son mode backend distant SSH. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## Durcissement de la sécurité

Cette version a comblé une longue liste de lacunes de surface liées aux identifiants : un pare-feu de sortie par proxy blindé pour l’injection d’identifiants, des téléchargements protégés contre les SSRF par épinglage DNS, une expurgation stricte à chaque frontière de compaction, des lectures d’identifiants de niveau 3 limitées, des épinglages de dépendances CVE actualisés et une vague de durcissement pour Windows qui élimine à l’échelle du dépôt le bogue de décodage de sous-processus en mode texte. *(Source: [GitHub Release Notes — v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3))*

## La trajectoire : quatre versions thématiques en cinq mois

La v0.20.0 prolonge une tendance établie tout au long de 2026 : chaque version majeure reçoit un thème et est livrée à un rythme soutenu. Mai a apporté la v0.15.0 « Velocity », juin les v0.16.0 « Surface » et v0.17.0, juillet la v0.18.0 « Judgment » (qui a clos tous les tickets P0/P1), la v0.19.0 « Quicksilver » (la version vitesse), et maintenant la v0.20.0 « Herald » (voix + interopérabilité). Le pari unificateur est que **les périphéries de l’agent comptent plus que son noyau** : les plateformes, les protocoles, la voix et la vérifiabilité sont les axes sur lesquels le produit ne cesse de s’étendre, tandis que le noyau reste délibérément étroit.

## FAQ

**Hermes Agent v0.20.0 est-il gratuit ?**

Oui. Hermes Agent reste sous licence MIT open source, et la v0.20.0 est disponible immédiatement via l’installateur shell ou `pip install hermes-agent`. Des offres hébergées existent pour ceux qui préfèrent une infrastructure gérée, mais l’agent principal est gratuit à exécuter sur votre propre matériel.

**Qu’est-ce qu’A2A v1.0 exactement ?**

A2A (Agent-to-Agent) est un protocole ouvert pour l’interopérabilité entre agents. Le plugin de la v0.20.0 permet à Hermes de découvrir, communiquer avec et être piloté par d’autres agents compatibles A2A. Il clôture le ticket #514, l’une des plus anciennes demandes d’évolution du dépôt, et vise les configurations multi-agents hétérogènes où différents agents utilisent des piles différentes.

**Le mode vocal nécessite-t-il une API payante ?**

La détection des mots-clés de réveil s’exécute sur l’appareil sans qu’aucun son ne quitte votre machine. Les fournisseurs de TTS/STT sont configurables — des options locales gratuites existent (par exemple Edge TTS, Whisper local) ainsi que des fournisseurs payants comme OpenAI.

**Comment fonctionnent les citations ancrées ?**

La compétence de citations ancrées compare chaque citation dans la recherche générée au texte réel de la page citée, relie les références à la preuve exacte et propose un mode de vérification des faits qui audite les documents ou affirmations que vous fournissez — en indiquant ce qui est vérifié, ce qui ne l’est pas et ce qui ne peut pas être contrôlé.

**Qu’est-il arrivé à la version de correctif v0.19.1 ?**

La v0.19.1 (30 juillet) était une étiquette de correctif d’infrastructure qui a regroupé plus de 1 000 PR vers un point stable pour les consommateurs en aval. Son contenu est entièrement documenté dans les notes de version de la v0.20.0.

## Pour en savoir plus

- [Notes de version de Hermes Agent v0.20.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3)
- [Dépôt Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Documentation de Hermes Agent](https://hermes-agent.nousresearch.com/docs)
- [Levée de fonds de 1,5 milliard de dollars pour Nous Research — couverture TAR](/2026/07/nous-research-hermes-agent-1-5-billion-funding-july-2026/)
- [Sprint qualité post‑v0.17.0 de Hermes Agent — couverture TAR](/2026/06/hermes-agent-post-v0170-quality-sprint-june2026/)