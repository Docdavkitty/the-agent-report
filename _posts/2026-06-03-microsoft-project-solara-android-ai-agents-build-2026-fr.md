---
layout: post
title: >
  "Project Solara de Microsoft : un OS Android pour agents, pas d'apps — le pari le plus audacieux de Build 2026"
date: 2026-06-03 10:00:00 +0200
lang: fr
ref: microsoft-project-solara-android-ai-agents-build-2026
permalink: /fr/2026/06/microsoft-project-solara-android-ai-agents-build-2026/
translation_of: /2026/06/microsoft-project-solara-android-ai-agents-build-2026/
author: The Agent Report
categories: [industry]
tags: [microsoft, "build-2026", "project-solara", "ai-agents", android, qualcomm, "agent-first", wearable, "traduction-francaise"]
last_modified_at: 2026-07-04 15:01:26 +0000
hero_image: >
  /assets/images/hero/hero-microsoft-project-solara-android-ai-agents-build-2026.jpg
meta_description: >
  "Le Project Solara de Microsoft à Build 2026 est un OS basé sur Android pour agents IA plutôt que d'apps, avec badge Qualcomm et prototypes desk hub, ciblant santé, retail et entreprise."
description: >
  "Le deuxième jour de Build 2026 à San Francisco a dévoilé la vision la plus audacieuse de la conférence : Project Solara, un OS basé sur Android..."
reading_time: 6
---

Le deuxième jour du Build 2026 de Microsoft à San Francisco a dévoilé la vision la plus audacieuse de la conférence à ce jour : **Project Solara**, un système d'exploitation basé sur Android conçu pour exécuter des agents d'IA plutôt que des applications traditionnelles.

Dévoilé mercredi par Stevie Bathiche, vice-président corporate et fellow technique de Microsoft, issu de l'Applied Sciences Group, Solara est une « plateforme de la puce au cloud » qui vise à libérer l'informatique des contraintes du paradigme des applications — en utilisant des agents d'IA qui génèrent des interfaces à la volée et se déplacent de manière fluide entre des appareils spécialisés.

« Les frontières s'effondrent », a déclaré Bathiche. « Vous n'avez pas nécessairement besoin du modèle d'application traditionnel. Vous n'avez pas besoin de la manière traditionnelle de développer des expériences. »

## Qu'est-ce que le Project Solara ?

Solara n'est pas un produit grand public — du moins pas encore. Il s'agit d'une plateforme de référence matérielle construite sur le **Microsoft Device Ecosystem Platform (MDEP)** , une version orientée entreprise du projet open source Android (AOSP). Microsoft ne peut pas l'appeler Android car il ne s'agit pas d'une version sous licence Google, mais le système d'exploitation sous-jacent est bel et bien Android.

L'idée centrale est d'une simplicité trompeuse : au lieu de télécharger, installer et gérer des applications pour chaque tâche, les utilisateurs interagissent avec des agents d'IA qui génèrent des interfaces juste-à-temps en fonction du contexte. Un badge porté sur un cordon, un hub de bureau sur un espace de travail, une paire de lunettes connectées — chaque appareil exécute des agents qui comprennent l'environnement de l'utilisateur et agissent en conséquence.

**Le pari de Microsoft est que les agents, et non les applications, constituent le prochain paradigme informatique** — et que l'entreprise qui a complètement manqué l'ère des applications mobiles peut faire un bond direct vers un monde centré sur les agents.

## Le matériel : Badge et Hub de bureau

Microsoft a présenté deux concepts d'appareils fonctionnels, tous deux construits à partir de composants standard avec des partenaires silicium :

| Concept | Partenaire silicium | Fonctionnalités clés |
|---------|-------------|--------------|
| **Badge Solara** | Qualcomm (puce portable) | 5G, caméra, micro, lecteur d'empreintes, ~1 semaine d'autonomie, accès agent biométrique |
| **Hub de bureau Solara** | MediaTek (silicium IoT) | Écran tactile, micro, caméra, se connecte au PC via Bluetooth, synchronise les tâches entre appareils |

Le badge est conçu pour une interaction mains libres — les professionnels de santé scannent les codes QR des patients, enregistrent et retranscrivent les visites, consignent les signes vitaux et initient des prescriptions directement depuis un appareil portable. Le hub de bureau agit comme un portail dédié aux agents, déchargeant les tâches d'un PC principal et conservant l'état entre les sessions.

Bathiche a expliqué la décision de construire un matériel dédié plutôt que d'utiliser des smartphones : les essais passés dans le domaine de la santé avec des téléphones personnels ont échoué car les patients se sentaient mal à l'aise et les exigences de sécurité entraient en conflit avec la gestion des appareils personnels. Un appareil dédié offre une surface d'attaque plus réduite, une meilleure autonomie et une caméra orientée pour une interaction en face à face.

> « Les ordinateurs continuent de se spécialiser. Les ordinateurs continuent de se rapprocher de vous. » — Stevie Bathiche

## Pourquoi Android et pas Windows

L'une des décisions techniques les plus surprenantes est le choix d'Android plutôt que Windows. La raison tient à la flexibilité matérielle : MDEP est conçu pour des appareils plus petits et moins puissants pour lesquels Windows n'a jamais été optimisé. Pourtant, il inclut toujours l'essentiel pour l'informatique d'entreprise : gestion des correctifs et des mises à jour OTA, vérifications de l'intégrité des appareils, Microsoft Defender, Intune et connexion via Entra ID.

Cela positionne Solara non pas comme un remplacement de Windows, mais comme une plateforme complémentaire pour des terminaux spécialisés. Le hub de bureau, par exemple, se connecte à un PC Windows, partageant le contexte et transférant les tâches entre les environnements.

## Des pilotes entreprises déjà en place

Microsoft a sécurisé cinq partenaires pilotes pour commencer à tester les appareils Solara dans des environnements réels :

- **AccuWeather** — intelligence météorologique pilotée par agent
- **Best Buy** — assistance agent en magasin
- **CVS Health** — agents de flux de travail dans le domaine de la santé
- **Levi's** — agents de vente au détail et de gestion des stocks
- **Target** — applications agent en magasin

Le PDG de Qualcomm, Cristiano Amon, a rejoint Nadella sur scène pour discuter de la vision commune, la qualifiant de « passage des applications à l'informatique centrée sur les agents ». Qualcomm apporte son expertise en matière de puces portables et IoT pour alimenter le facteur de forme du badge, ce dernier fonctionnant prétendument sur la plateforme en seulement trois jours après l'échange des chipsets.

## Le paysage concurrentiel

Solara entre dans un domaine de plus en plus encombré de paris sur des plateformes centrées sur les agents. **Google** poursuit des concepts d'interface agent similaires, présentés à l'I/O 2026. **Amazon** continue d'étendre les capacités d'Alexa. **OpenAI** développe prétendument son propre concept de téléphone à agent d'IA utilisant le silicium de MediaTek et Qualcomm — les mêmes partenaires avec lesquels Microsoft travaille.

Ce qui différencie Solara, selon Microsoft, est l'orientation prioritaire vers l'entreprise. Alors qu'un appareil agent grand public pourrait devoir gérer tous les scénarios possibles, les appareils Solara sont conçus pour des contextes organisationnels spécifiques — gérés, sécurisés et limités à des flux de travail définis. Le hub de bureau sait qu'il appartient à un employé spécifique, se connecte à son PC de travail et exécute uniquement les agents autorisés.

## Ce qui manque : Les modèles

L'aveu le plus honnête de l'équipe de Microsoft est que Solara attend que les modèles d'IA rattrapent la vision. Les concepts d'appareils sont réels et fonctionnent, mais les agents qui les rendraient véritablement utiles — conscients du contexte, multi-étapes, fiables et rapides — ne sont pas encore tout à fait là.

> *« Rien ne fonctionne, mais l'entreprise est déterminée à y investir de l'argent. »* — Ars Technica

Cela est cohérent avec la stratégie d'IA plus large de Microsoft : faire de gros paris tôt, investir massivement et itérer rapidement. L'entreprise a engagé des milliards dans l'infrastructure d'IA, et Solara représente le point d'aboutissement logique de cet investissement — un matériel conçu dès le départ pour un monde centré sur les agents, et non adapté de l'ère des applications.

## Analyse : Pourquoi c'est important

Le Project Solara est bien plus qu'un concept visionnaire. Il signale la direction stratégique de Microsoft pour l'ère informatique post-application :

1. **L'informatique se spécialise** — le smartphone et l'ordinateur portable polyvalents sont complétés par des appareils spécialisés pour des contextes spécifiques (travail, santé, vente au détail)
2. **Les agents éliminent la complexité des applications** — pas d'installation, pas de mises à jour, pas de contraintes de facteur de forme ; interfaces générées à la demande
3. **L'informatique d'entreprise est le levier** — l'adoption par les consommateurs d'appareils agents peut prendre des années, mais les organisations avec des flux de travail gérés sont prêtes aujourd'hui
4. **Le cloud est l'épine dorsale** — chaque appareil Solara fonctionne sur Azure, liant les ventes de matériel à la consommation cloud
5. **Microsoft suit sa propre voie** — avec le partenariat OpenAI désormais non exclusif depuis avril 2026, l'entreprise construit une pile d'IA indépendante, du silicium au système d'exploitation en passant par le cloud

Le badge et le hub de bureau ne parviendront peut-être jamais dans les rayons sous leur forme actuelle. Mais le message du Build 2026 est indubitable : Microsoft croit que l'application n'est plus l'unité fondamentale de l'informatique. L'agent l'est — et l'entreprise construit la plateforme pour le prouver.

*Sources : [GeekWire](https://www.geekwire.com/2026/inside-microsofts-project-solara-a-new-platform-for-devices-that-run-ai-agents-instead-of-apps), [Ars Technica](https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps), [Qualcomm](https://www.qualcomm.com/news/onq/2026/06/project-solara-agent-first-computing), [Windows Forum](https://windowsforum.com/threads/microsoft-project-solara-agent-first-badges-and-desk-devices-for-chip-to-cloud-work.421817)*