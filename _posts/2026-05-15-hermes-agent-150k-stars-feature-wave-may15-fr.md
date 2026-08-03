---
layout: post
title: >
  "Hermes Agent dépasse 150k étoiles – SimpleX Chat, HuggingFace Skills Hub, Deep Crawl et nouvelles fonctionnalités Cron"
date: 2026-05-15 17:00:00 +0200
lang: fr
ref: hermes-agent-150k-stars-feature-wave-may15
permalink: /fr/2026/05/hermes-agent-150k-stars-feature-wave-may15/
translation_of: /2026/05/hermes-agent-150k-stars-feature-wave-may15/
author: The Agent Report
categories: ["hermes-agent"]
tags: [Hermes Agent, Nous Research, "open-source", "150k-stars", "simple-x-chat", "skills-hub", cron, "deep-crawl", "supply-chain-security", frontdesk, "traduction-francaise"]
last_modified_at: 2026-08-03 15:17:41 +0000
hero_image: /assets/images/hero/hero-hermes-agent-150k-stars-feature-wave-may15.jpg
meta_description: >
  "Hermes Agent dépasse 150K étoiles GitHub avec SimpleX Chat gateway, intégration HuggingFace Skills Hub, deep crawl, raisonnement cron par tâche et dépendances."
description: >
  "Hermes Agent dépasse 150K étoiles GitHub avec SimpleX Chat gateway, intégration HuggingFace Skills Hub, deep crawl, raisonnement cron par tâche et"
reading_time: 7
---

## 🌟 150 000 étoiles : l’exécution d’agent qui croît le plus vite

La trajectoire de croissance de Hermes Agent continue de défier les attentes :

| Métrique | 13 mai | 15 mai | Variation |
|--------|--------|--------|--------|
| **Étoiles GitHub** | 147 782 | **151 192** | **+3 410** |
| **Forks** | 23 222 | **23 955** | **+733** |
| **Tickets ouverts** | 10 713 | **11 302** | +589 |
| **Contributeurs actifs** | — | **plus de 15 uniques** en 48h | — |

Avec environ **1 700 nouvelles étoiles par jour**, Hermes Agent a gagné **~24 000 étoiles en 15 jours** depuis la v0.12.0. Le projet est désormais sur le point de dépasser des cadriciels majeurs, porté par la [dynamique de l’écosystème communautaire]({% post_url 2026-05-25-hermes-agent-community-ecosystem-may25 %}) et en bonne voie pour franchir les **155K d’ici le week-end**.

---

## 🆕 SimpleX Chat : une passerelle privée et décentralisée

**[PR #26208](https://github.com/NousResearch/hermes-agent/pull/26208)** par le contributeur communautaire **Mibayy** ajoute **SimpleX Chat** en tant que plateforme de passerelle Hermes — apportant Hermes Agent à l’un des réseaux de messagerie les plus respectueux de la vie privée.

SimpleX ([simplex.chat](https://simplex.chat)) se distingue des autres plateformes de messagerie : il n’y a **aucun identifiant utilisateur persistant**. Chaque contact est identifié par un identifiant interne opaque généré au moment de la connexion. Il n’y a pas de serveur à compromettre, pas d’annuaire à fuiter.

L’adaptateur se connecte à un démon `simplex-chat` local via WebSocket, écoute les messages entrants et envoie les réponses. Initialement proposé dans la PR #2558 comme une intégration modifiant le cœur, il a été remanié dans l’architecture de plugin, ce qui le rend facile à installer et à maintenir indépendamment.

> *« SimpleX n’a pas d’identifiants utilisateur, pas d’email, pas de numéro de téléphone — les meilleurs candidats pour le trafic de l’agent Hermes »* — description de la PR

Il s’agit d’un ajout significatif pour les développeurs qui construisent des applications d’agent sensibles à la confidentialité — des cas d’usage médicaux, juridiques ou journalistiques où les métadonnées des messages ne peuvent pas être exposées.

---

## 🧠 Skills Hub : HuggingFace/skills devient un tap par défaut de confiance

**[PR #2549](https://github.com/NousResearch/hermes-agent/pull/2549)**, fusionnée par **kshitijk4poor**, ajoute le **catalogue officiel de compétences de HuggingFace** aux taps GitHub par défaut de Hermes Agent et le classe comme **source de confiance** — aux côtés des taps `openai/skills` et `anthropics/skills` existants.

Cela signifie que les utilisateurs ont désormais accès à la bibliothèque croissante de compétences **huggingface/skills** de HuggingFace, sans configuration supplémentaire. L’intégration couvre :

- `tools/skills_guard.py` — `huggingface/skills` ajouté à `TRUSTED_REPOS`
- `tools/skills_hub.py` — `GitHubSource.DEFAULT_TAPS` inclut le nouveau tap
- Documentation — répertorié sous les taps par défaut et les exemples de sources de confiance

Le catalogue de compétences de HuggingFace s’est rapidement étoffé, couvrant tout, de l’inférence multimodale au traitement de jeux de données — ce qui en fait un ajout naturel à l’écosystème de compétences de Hermes Agent.

---

## 🕸️ Crawl4AI Deep Crawl : scraping web local et récursif

**[PR #26213](https://github.com/NousResearch/hermes-agent/pull/26213)** par **breakneo** ajoute un nouvel outil intégré `crawl4ai_deep_crawl` à la boîte à outils web — un **explorateur web local, récursif et multi-pages** propulsé par Crawl4AI avec **aucun coût d’API externe**.

Fonctionnalités principales :

- **Exploration récursive** — suit les liens, extrait le Markdown, avec contrôle configurable de la profondeur
- **Exécution locale** — s’exécute entièrement sur la machine de l’utilisateur, sans appel à des API tierces
- **Repli intelligent** — détecte automatiquement `crawl4ai` dans le venv de Hermes, se replie sur `~/tasklines/browser/.venv/bin/python`
- **Respectueux de la sécurité** — respecte les vérifications de politique SSRF et de site web existantes de Hermes
- **Retour de progression** — l’analyse de la sortie standard basée sur une sentinelle gère les journaux de progression de Crawl4AI

Pour les utilisateurs ayant besoin d’analyser des sites web ou de scraper de la documentation (le cas d’usage canonique pour l’utilisation d’outils d’agent), cet outil élimine le besoin d’API de scraping web payantes.

---

## ⏰ Cron évolue : raisonnement par tâche et recherche par nom

Deux améliorations majeures du cron sont arrivées le 15 mai :

### Effort de raisonnement par tâche

**[PR #26214](https://github.com/NousResearch/hermes-agent/pull/26214)** par **evaclawdbot** ajoute une substitution `reasoning_effort` pour les tâches cron individuelles. Les tâches planifiées peuvent désormais opter pour un raisonnement plus profond ou plus léger du modèle, indépendamment du paramètre global de l’agent interactif.

```yaml
# A low-effort daily check-in
- name: daily_summary
  schedule: "0 9 * * *"
  reasoning_effort: low

# A deep-analysis weekly report
- name: weekly_research
  schedule: "0 8 * * 1"
  reasoning_effort: high
```

Ceci complète le modèle initié par les substitutions par tâche du modèle, du fournisseur et de l’URL de base — donnant aux utilisateurs du cron une flexibilité totale sans sacrifier les paramètres globaux par défaut.

### Recherche de tâche par nom

**[PR #26226](https://github.com/NousResearch/hermes-agent/pull/26226)** par **buntingszn** ajoute une **recherche basée sur le nom** pour les opérations de mutation du cron. `hermes cron run my_job_name` fonctionne désormais directement, au lieu de nécessiter l’identifiant hexadécimal. Le système gère l’ambiguïté avec des messages d’erreur clairs lorsque deux tâches partagent le même nom.

### Recettes de portes de pré-exécution avec WakeAgent

**Teknium** a également intégré **[PR #26229](https://github.com/NousResearch/hermes-agent/pull/26229)** — documentation pour trois recettes de portes de pré-exécution utilisant le mécanisme `script` + `wakeAgent` existant :

- **Porte de modification de fichier** — ne s’exécute que si le mtime d’un fichier a changé
- **Porte de drapeau externe** — ne s’exécute que si un fichier de drapeau existe
- **Porte de comptage SQL** — ne s’exécute que si une condition de base de données est remplie

Ces modèles offrent aux utilisateurs une exécution conditionnelle du cron sans aucun coût de code supplémentaire.

---

## 🏗️ Frontdesk : un runtime de worker toujours disponible

**[PR #26261](https://github.com/NousResearch/hermes-agent/pull/26261)** par **wkimdevai-legend** introduit le runtime **frontdesk** — une nouvelle couche architecturale ambitieuse pour le routage de premier plan toujours disponible et les voies de workers en arrière-plan.

C’est encore à ses débuts (PR ouverte), mais la portée est substantielle :

- Routage de premier plan toujours disponible et voies de workers en arrière-plan
- Métadonnées de registre de tâches pour une orchestration durable
- Échafaudage de voies worker/reviewer avec surfaces d’importation de revue
- Sémantique d’annulation et alignement TUI/passerelle/CLI
- Documentation produit/PRD complète incluse dans la PR

Le système frontdesk ouvre la voie à un avenir où Hermes Agent fonctionnerait comme un service d’arrière-plan persistant avec une gestion appropriée du cycle de vie des processus — une étape majeure vers une infrastructure d’agent de qualité entreprise.

---

## 🔒 Sécurité de la chaîne d’approvisionnement : limites supérieures des dépendances codifiées

**[PR #24226](https://github.com/NousResearch/hermes-agent/pull/24226)** par **Siddharth Balyan** ajoute des limites supérieures strictes à **5 dépendances non contraintes** et documente formellement la **politique de verrouillage de la chaîne d’approvisionnement** du projet.

C’est une réponse directe à deux incidents récents de l’industrie :

- **Campagne de la chaîne d’approvisionnement Mini Shai-Hulud** (mai 2026)
- **Compromission de litellm** (mars 2026)

La PR ajoute des limites supérieures à `hindsight-client`, `pyyaml`, `httpx`, `pydantic` et `requests`, et intègre la politique dans la documentation des contributeurs afin que les futures PR ne réintroduisent pas de contraintes lâches.

> *« Codifier la politique de verrouillage des dépendances qui a été établie dans les PR #2810 et #9801 mais jamais documentée pour les contributeurs. »* — description de la PR #24226

---

## 🎤 Nouveau fournisseur TTS : SenseAudio

**[PR #26262](https://github.com/NousResearch/hermes-agent/pull/26262)** par **QWERTY0205** enregistre **SenseAudio** comme nouveau fournisseur TTS, suivant le même modèle de répartition que MiniMax.

SenseAudio expose un point de terminaison `t2a_v2` de type MiniMax qui renvoie de l’audio MP3 encodé en hexadécimal. Configuration :

- Authentification via la variable d’environnement `SENSEAUDIO_API_KEY`
- Modèle par défaut : `senseaudio-tts-1.5-260319`
- Voix par défaut : `female_0033_b`
- URL de base par défaut : `https://api.senseaudio.cn`

---

## 🔧 Points forts des corrections et du durcissement

Au-delà des nouvelles fonctionnalités, les dernières 48 heures ont vu un volume impressionnant de corrections de qualité de vie :

| Domaine | Changement | PR/Commit |
|------|--------|-----------|
| **Mode YOLO** | Avertissement rouge dans la bannière + barre d’état lorsque `--yolo` est actif | [#26239](https://github.com/NousResearch/hermes-agent/pull/26239) par **Mibayy** |
| **Génération d’images** | Message de configuration exploitable avec lien d’inscription FAL + statut de la passerelle | [#26222](https://github.com/NousResearch/hermes-agent/pull/26222) par **Teknium** |
| **ACP** | `hermes acp --setup-browser` initialise les outils du navigateur pour les installations de registre | [#26211](https://github.com/NousResearch/hermes-agent/pull/26211) par **Teknium** |
| **WhatsApp** | Délai d’expiration rapide en cas de blocage de `sendMessage` de Baileys (60s par défaut) | [#26215](https://github.com/NousResearch/hermes-agent/pull/26215) par **Wysie** |
| **Outils web** | Correction du bug `asyncio.gather` — une seule URL en échec ne rejette plus tous les résultats | par **Nidhi Singh** |
| **Slack** | Le texte de commande contenant uniquement des espaces ne provoque plus d’`IndexError` | par **nidhi-singh02** |
| **UA du fournisseur** | `User-Agent` défini lors des récupérations du modèle de profil du fournisseur pour éviter les 403 de WAF | par **teknium1** |
| **Telegram** | Les bulles de progression des outils défilent avant d’atteindre les limites de messages de la plateforme | [#26208](https://github.com/NousResearch/hermes-agent/pull/26208) par **Qwinty** |
| **Runtime Codex** | Trois bugs de corruption de configuration corrigés dans le chemin de migration Hermes↔Codex | Plusieurs PRs de **kshitijk4poor**, **Steve Kelly**, **zccyman** |
| **Drapeaux d’environnement** | Exiger des valeurs véridiques explicites pour les variables d’environnement de session chez tous les consommateurs | [#26254](https://github.com/NousResearch/hermes-agent/pull/26254) par **teknium1** |
| **CTRL+J** | La saisie de nouvelle ligne fonctionne désormais sur l’interface en ligne de commande macOS | par **flowioo** |

---

## 📊 En chiffres : le sprint post-Tenacity en perspective

| Période | Étoiles ajoutées | Fonctionnalités clés |
|--------|------------|--------------|
| 7–11 mai (post-Tenacity) | +5 500 | Compétence finance, diagnostics Kanban, corrections Nix |
| 11–13 mai | +4 272 | Refonte du cache, étiquetage Portal, Qwen Cloud |
| **13–15 mai** | **+3 410** | **SimpleX, Skills Hub HF, exploration profonde, raisonnement cron, politique de chaîne d’approvisionnement** |
| **Total depuis v0.12.0 (30 avr.)** | **+24 192** | — |

Le rythme est remarquable : environ **1 600 nouvelles étoiles par jour en moyenne** sur toute la période post-Tenacity, sans signe de ralentissement.

---

## 🔭 Et ensuite ?

Sur la base du pipeline de PR ouvertes et de la densité des commits, plusieurs thèmes se dégagent pour la v0.14.0 :

1. **Runtime Frontdesk** — s’il est fusionné, ce serait l’un des changements architecturaux les plus significatifs depuis Tenacity, permettant un fonctionnement persistant de l’agent en arrière-plan
2. **Maturité du cron** — le raisonnement par tâche, la recherche par nom et les portes de pré-exécution parachèvent le sous-système cron en une plateforme de planification de premier ordre
3. **Étendue de la messagerie** — SimpleX porte le nombre de plateformes encore plus haut, avec des correctifs de fiabilité WhatsApp garantissant que les passerelles existantes sont prêtes pour la production
4. **Interopérabilité Codex** — l’avalanche de corrections de migration Codex suggère que Hermes Agent est en train de devenir le runtime par défaut pour les utilisateurs de Codex, ce qui ajouterait une croissance significative du nombre d’utilisateurs
5. **Durcissement de la chaîne d’approvisionnement** — la PR sur la politique de dépendances indique que Nous Research prend au sérieux la défense de la chaîne d’approvisionnement après une compromission

À cette cadence, la **v0.14.0** pourrait arriver d’ici une semaine — et les 160 000 étoiles pourraient ne pas être loin derrière.

---

*Couverture basée sur l’activité GitHub entre le 13 et le 15 mai 2026. Nombre d’étoiles au 15 mai 2026 à 16:00 UTC. Journal de commits complet : [`main...main`](https://github.com/NousResearch/hermes-agent/compare/v2026.5.7...main)*