---
layout: post
title: >
  "Hermes Agent franchit 147K étoiles : refonte du cache, maturation accélérée de la plateforme après Tenacity"
date: 2026-05-13 12:00:00 +0200
lang: fr
ref: hermes-agent-147k-stars-cache-overhaul-may13
permalink: /fr/2026/05/hermes-agent-147k-stars-cache-overhaul-may13/
translation_of: /2026/05/hermes-agent-147k-stars-cache-overhaul-may13/
author: The Agent Report
categories: ["hermes-agent"]
tags: [Hermes Agent, Nous Research, "open-source", "cache-architecture", "platform-maturation", "qwen-cloud", "post-tenacity", infrastructure, "traduction-francaise"]
last_modified_at: 2026-08-08 15:14:16 +0000
hero_image: /assets/images/hero/hero-hermes-agent-147k-stars-cache-overhaul-may13.jpg
meta_description: >
  "Hermes Agent franchit 147K étoiles grâce à une refonte du cache améliorant le taux de succès du prompt cache de 66,6% à 83,3%, et un rebranding du fournisseur."
description: >
  "Hermes Agent franchit 147K étoiles grâce à une refonte du cache améliorant le taux de succès du prompt cache de 66,6% à 83,3%, et un rebranding."
reading_time: 6
---

## 🧠 Refonte de l’architecture du cache : le prompt système est désormais statique au niveau des octets

Ces travaux préparent ce qui deviendra la [version fondatrice v0.14.0]({% post_url 2026-05-18-hermes-agent-v0140-foundation-release-may16 %}).

Le changement le plus marquant depuis Tenacity est la **[PR #24778](https://github.com/NousResearch/hermes-agent/pull/24778) — une refonte complète de la stratégie de mise en cache des prompts de Hermes Agent**, fusionnée par **Teknium** le 13 mai.

### Le problème

Le prompt système était reconstruit à chaque appel API. La fonction `_build_system_prompt_parts()` s’exécutait à l’intérieur de la boucle par appel sur le chemin de longue durée, redérivant la couche volatile (horodatage + instantané mémoire + profil utilisateur) à chaque tour. Résultat : les octets mutaient en cours de conversation dès que la minute changeait ou qu’une mémoire était écrite, invalidant ainsi les caches de prompt en amont chez OpenRouter, Portal et Anthropic.

> *"L’historique (système + tous les messages sauf les 1 ou 2 derniers) doit être statique au sein d’une session. La mise en cache repose sur une stabilité binaire parfaite."* — description de la PR #24778

### La solution

La solution est élégante par sa simplicité : le prompt système est désormais construit **une fois par session** et rejoué textuellement à chaque tour. Principaux changements :

- **~715 lignes supprimées** de `run_agent.py` — la branche du cache de préfixe longue durée, sa durée de vie et le drapeau `_supports_long_lived_anthropic_cache` ont été intégralement retirés
- **`prompt_caching.py` simplifié** — une seule disposition (`system_and_3`) remplace l’approche complexe multi-blocs : 4 points de rupture (système + 3 derniers messages), tous avec `cache_ttl`
- **Clés de configuration supprimées** — `prompt_caching.long_lived_prefix` et `prompt_caching.long_lived_ttl` retirées de `hermes_cli/config.py`
- **Fichier de test entier supprimé** — `test_prompt_caching_live.py` était le test live longue durée ; il disparaît avec la fonctionnalité

### Le résultat

Le diff au format filaire est éloquent : l’ANCIENNE disposition atteignait un taux de succès cumulé du cache de **66,6 %** sur 8 tours (un unique miss en milieu de session lorsque l’empreinte SHA du bloc système changeait). La nouvelle disposition mono-bloc atteint **83,3 %** — soit une amélioration de **16,7 points de pourcentage** de l’efficacité du cache.

Pour les utilisateurs qui font tourner Hermes Agent à l’échelle — en particulier ceux qui sollicitent les points de terminaison Portal ou Anthropic — cela se traduit directement par une **latence réduite, moins d’appels API et des coûts diminués**.

---

## 🏷️ Étiquetage unifié du client Portal

La **[PR #24779](https://github.com/NousResearch/hermes-agent/pull/24779)** introduit un nouveau module `portal_tags.py` qui marque chaque requête Hermes à destination de Nous Portal avec `client=hermes-client-v<version>` (aujourd’hui : `client=hermes-client-v0.13.0`).

L’astuce : l’étiquette est extraite dynamiquement de `hermes_cli.__version__` au moment de la requête. Lorsqu’une prochaine version fera évoluer la chaîne de version, tous les points d’appel vers Portal enverront automatiquement la nouvelle étiquette — **aucune autre modification de code n’est nécessaire**. La mise à jour de version par expression régulière du script de release se propage automatiquement partout.

Cette approche remplace le marqueur ad hoc `client=aux` issu de la [#24194](https://github.com/NousResearch/hermes-agent/pull/24194) par un mécanisme unifié, versionné, qui couvre **toutes** les voies Portal — boucle principale de l’agent, client auxiliaire, résumés de compression et replis de l’outil web.

---

## ☁️ Qwen Cloud : Alibaba change de marque

La **[PR #24835](https://github.com/NousResearch/hermes-agent/pull/24835)** renomme le fournisseur `alibaba` de « Alibaba Cloud (DashScope) » en **« Qwen Cloud »** et le déplace de la position 24 à la position 6 dans le sélecteur de fournisseurs — juste au-dessus de Xiaomi MiMo, en dessous d’OpenAI Codex.

Cela reflète le changement de marque en cours dans l’écosystème chinois de l’IA : les offres d’IA générative d’Alibaba vivent désormais sous la marque **Qwen**, et Hermes Agent suit le mouvement. L’identifiant interne `alibaba` et la variable `DASHSCOPE_API_KEY` restent inchangés — seul le libellé à destination de l’utilisateur a été déplacé.

---

## 🆕 Le pipeline de fonctionnalités de la v0.14.0 prend forme

Si les commits fusionnés racontent une histoire, les **PR ouvertes** depuis le 11 mai donnent un aperçu de ce qui arrivera dans la prochaine version :

| PR | Fonctionnalité | Auteur |
|----|----------------|--------|
| [#24936](https://github.com/NousResearch/hermes-agent/pull/24936) | Commande CLI `hermes gateway send-message` | jwickers |
| [#24938](https://github.com/NousResearch/hermes-agent/pull/24938) | Canal de mise à jour des releases | Sunwo0u |
| [#24926](https://github.com/NousResearch/hermes-agent/pull/24926) | Respect de `display.show_reasoning` sur les complétions de chat du serveur API | Zavianx |
| [#24811](https://github.com/NousResearch/hermes-agent/pull/24811) | Primitives de suspension/reprise pour les tâches longues sur Kanban | shanewas |
| [#24925](https://github.com/NousResearch/hermes-agent/pull/24925) | Recherche de session : chargement contextuel seul (fenêtré) via FTS5 | shanewas |
| [#24916](https://github.com/NousResearch/hermes-agent/pull/24916) | Progression des outils avec tampon pour les plateformes sans édition (Weixin) | rzbdz |
| [#24423](https://github.com/NousResearch/hermes-agent/pull/24423) | En-têtes `X-Hermes-User-*` / `Chat-*` pour l’identité multi-utilisateur | gsskk |

La PR de **suspension/reprise Kanban** ([#24811](https://github.com/NousResearch/hermes-agent/pull/24811)) est particulièrement notable — elle ajoute des primitives de suspension/reprise de premier ordre pour les tâches Kanban de longue durée, étendant ainsi le système de tableau multi-agents durable livré avec la v0.13.0.

---

## 🔧 Corrections et durcissement sur toute la pile

Les plus de 40 commits depuis le 11 mai couvrent l’ensemble de la surface de la plateforme Hermes Agent :

### Sécurité
- **Contournement des confirmations DELETE corrigé** (`80374d4d`) — un drapeau DOTALL dans le motif d’approbation permettait une injection de retour à la ligne pour contourner les confirmations DELETE
- **Correction de l’injection `--no-sandbox` du navigateur** ([#24930](https://github.com/NousResearch/hermes-agent/pull/24930)) — `--no-sandbox` est désormais injecté via `cmd_parts` plutôt que `AGENT_BROWSER_CHROME_FLAGS`

### Multiplateforme
- **Support CLI CJK** — utilisation de `display-width` pour les étiquettes d’en-tête de la boîte de réponse ([#24843](https://github.com/NousResearch/hermes-agent/pull/24843) par NorethSea)
- **Correction du scrollback TUI sous tmux** — le tampon de défilement est vidé au démarrage pour éviter les fuites ([#24843](https://github.com/NousResearch/hermes-agent/pull/24843))
- **Correction du crash de la CLI Windows** — la complétion des `@-file` ne plante plus quand les chemins ne sont pas décodables en cp1252 ([#24843](https://github.com/NousResearch/hermes-agent/pull/24843))

### Plateformes de messagerie
- **Telegram** — réaction « en cours » retirée en cas d’annulation du traitement ([#24628](https://github.com/NousResearch/hermes-agent/pull/24628)), helper de fil de discussion pour les résultats de confirmation par slash
- **LINE** — utilisation de `build_source` au lieu de `create_source` inexistant
- **WeCom (WeChat Work)** — corrections de la remontée d’état de reconnexion WebSocket
- **Signal** — messages de groupe provenant d’appareils liés traités dans le chemin syncMessage
- **WhatsApp** — délai d’expiration de `npm install` rendu configurable
- **Email** — implémentation de `send_voice()` pour l’envoi de pièces jointes audio ([#24931](https://github.com/NousResearch/hermes-agent/pull/24931))

### Infrastructure
- **Docker** — propriété de `.venv` corrigée pour que `lazy_deps` puisse installer les paquets de la plateforme ([#24841](https://github.com/NousResearch/hermes-agent/pull/24841))
- **CI** — délai d’attente des jobs e2e porté à 15 minutes, ripgrep installé dans les jobs e2e
- **Systemd** — délai de redémarrage réduit
- **Changement de modèle** — `config.context_length` obsolète effacé lors du changement de modèle

---

## 📊 En chiffres (11 mai → 13 mai)

| Métrique | 11 mai | 13 mai | Évolution |
|----------|--------|--------|-----------|
| **Étoiles GitHub** | 143 510 | **147 782** | **+4 272** |
| **Forks** | 22 406 | **23 222** | **+816** |
| **Issues ouvertes** | 9 960 | **10 713** | +753 |
| **Commits** | — | **40+** en 48 h | — |
| **Contributeurs** | 13 uniques en 4 jours | **25+** en 2 jours | — |

> *"Avec environ 2 136 nouvelles étoiles par jour depuis le 11 mai, Hermes Agent continue d’être le runtime d’agent IA à la croissance la plus rapide sur GitHub. Le projet est en bonne voie pour franchir les **150K étoiles** dans la semaine."* — The Agent Report

## 🔭 Prochaines étapes

Le cycle de release de la v0.14.0 se dessine clairement. Sur la base des PR ouvertes et de la densité des correctifs fusionnés, voici les points à surveiller :

- **Efficacité du cache** — le changement rendant le prompt système statique en octets est le genre d’amélioration architecturale sur laquelle les gains s’accumulent
- **Maturité du Kanban** — les primitives de suspension/reprise annoncent une gestion du cycle de vie des tâches de niveau entreprise
- **Étendue des plateformes** — le support Weixin (progression des outils tamponnée) et les en-têtes API multi-utilisateurs suggèrent des cas d’usage croissants en entreprise/collaboration
- **Outillage CLI** — la commande `send-message` et les fonctionnalités de canal de release rendent Hermes Agent plus opérable à grande échelle
- **150K étoiles** — au rythme actuel, ce cap devrait être atteint en quelques jours, pas en semaines

Pour les développeurs qui suivent l’évolution d’Hermes Agent : la période post-Tenacity n’est pas une phase de refroidissement — c’est une **phase de construction**. Le travail d’infrastructure qui arrive aujourd’hui (architecture de cache, outillage fournisseur, durcissement des plateformes) permet la prochaine vague de fonctionnalités.

---

*Couverture basée sur l’activité GitHub entre le 11 et le 13 mai 2026. Journal complet des commits : [`main...main`](https://github.com/NousResearch/hermes-agent/compare/v2026.5.7...main)*