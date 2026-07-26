---
layout: post
title: >
  "Meta SAM 3.1 — Détection et suivi vidéo en temps réel accélérés par multiplexage et raisonnement global"
date: 2026-05-21 14:00:00 +0200
lang: fr
ref: meta-sam-3-1-video-detection-multiplexing-may21
permalink: /fr/2026/05/meta-sam-3-1-video-detection-multiplexing-may21/
translation_of: /2026/05/meta-sam-3-1-video-detection-multiplexing-may21/
author: The Agent Report
categories: [research]
tags: [meta, sam3, "open-source", "computer-vision", "segment-anything", "video-tracking", "object-detection", "traduction-francaise"]
last_modified_at: 2026-07-26 15:15:19 +0000
hero_image: /assets/images/hero/hero-meta-sam-3-1-video-detection-multiplexing-may21.jpg
meta_description: >
  "Meta lance SAM 3.1 avec Object Multiplex pour un suivi vidéo multi-objets conjoint plus rapide sans perte de précision, améliorant la détection vidéo open-source."
description: >
  "Meta lance SAM 3.1 avec Object Multiplex pour un suivi vidéo multi-objets conjoint plus rapide sans perte de précision, améliorant la vidéo open-source."
reading_time: 8
---

**Meta a publié SAM 3.1, une mise à jour majeure de son modèle Segment Anything Model 3, introduisant Object Multiplex — une architecture à mémoire partagée qui permet un suivi multi-objets conjoint à des vitesses nettement supérieures à SAM 3, sans perte de précision.** Cette mise à jour, publiée discrètement sur GitHub et Hugging Face fin mars, constitue l’amélioration la plus importante du modèle de fondation open source pour la vision par ordinateur de Meta depuis la sortie initiale de SAM 3 en juillet 2025.

SAM 3.1 s’appuie sur la base de [SAM 3](https://github.com/facebookresearch/sam3) (Segment Anything with Concepts), le modèle unifié de Meta pour la segmentation sur requête dans les images et les vidéos. Contrairement à [SAM 2](https://github.com/facebookresearch/sam2), qui pouvait segmenter n’importe quel objet mais nécessitait des passages d’inférence distincts pour chaque concept, SAM 3 a introduit la capacité de segmenter exhaustivement toutes les instances d’un concept à vocabulaire ouvert en utilisant une simple phrase de texte, un exemple visuel ou une combinaison de requêtes. SAM 3.1 va plus loin en rendant le suivi vidéo multi-objets considérablement plus efficace.

## Qu’est-ce que SAM 3 ?

SAM 3 est un modèle de fondation en vision par ordinateur développé par **Meta Superintelligence Labs (MSL)**, dirigé par une large équipe de chercheurs comprenant Nicolas Carion, Laura Gustafson, ainsi que les responsables de projet Piotr Dollar, Kate Saenko et Christoph Feichtenhofer. Le modèle est décrit dans l’article *« SAM 3: Segment Anything with Concepts »* et est disponible sous licence de recherche sur GitHub, où il a déjà récolté près de **10 000 étoiles** et plus de **1 400 forks**.

L’architecture est un modèle de 848 millions de paramètres combinant un détecteur et un traqueur partageant un encodeur de vision :

| Composant | Architecture | Rôle |
|-----------|-------------|------|
| **Détecteur** | Basé sur DETR, conditionné par le texte, la géométrie et des exemples visuels | Identifie les objets correspondant à une requête conceptuelle |
| **Traqueur** | Architecture encodeur-décodeur du transformer SAM 2 | Suit les objets segmentés à travers les images vidéo |
| **Encodeur** | Réseau dorsal de vision partagé | Extrait des caractéristiques pour la détection et le suivi |

### Ce qui différencie SAM 3 de SAM 2

L’innovation phare de SAM 3 est la **segmentation conditionnée par les concepts**. Là où SAM 2 pouvait segmenter « tout » à partir de requêtes par point, boîte ou masque, SAM 3 peut segmenter « tout ce qui correspond à ce concept » en langage naturel. Il s’agit d’un paradigme fondamentalement différent :

- **Requête textuelle** : « Trouve toutes les voitures rouges » → segmente chaque voiture rouge dans l’image ou la vidéo
- **Exemples visuels** : Montrez une instance → segmentez toutes les instances similaires
- **Requêtes combinées** : « Trouve ce type d’oiseau » + un exemple image → segmentation conceptuelle précise

Cette capacité est rendue possible par le détecteur du modèle basé sur DETR, conditionné simultanément par des représentations textuelles, des caractéristiques géométriques et des exemples visuels. Le détecteur produit des boîtes englobantes et des masques pour chaque instance du concept cible, tandis que le traqueur maintient l’identité à travers les images.

## SAM 3.1 : ce qui a changé

SAM 3.1, publié le 27 mars 2026, introduit **Object Multiplex** — une nouvelle approche à mémoire partagée pour le suivi multi-objets conjoint.

### Le problème du multiplex

Dans SAM 3, le suivi de plusieurs objets distincts nécessitait d’exécuter le traqueur indépendamment pour chaque objet ou concept. Pour suivre simultanément des « piétons », des « véhicules » et des « panneaux de signalisation » dans une vidéo, il fallait trois passages d’inférence distincts — chacun consommant une mémoire GPU proportionnelle au nombre d’instances détectées.

Cette approche évolue linéairement avec le nombre de concepts suivis, saturant rapidement la mémoire GPU pour les scènes complexes.

### Object Multiplex : la solution

L’Object Multiplex de SAM 3.1 introduit une **banque mémoire partagée** dans laquelle tous les objets suivis lisent et écrivent simultanément. Au lieu de maintenir des états mémoire distincts par objet ou par concept, le multiplexeur utilise une représentation mémoire unique et unifiée qui stocke les caractéristiques de toutes les instances suivies :

| Fonctionnalité | SAM 3 (avant) | SAM 3.1 (avec Multiplex) |
|----------------|---------------|--------------------------|
| **Architecture mémoire** | États mémoire par objet | Mémoire multiplexée partagée |
| **Suivi multi-concepts** | Séquentiel, O(n) passes | Conjoint, un seul passage O(1) |
| **Mémoire GPU** | Évolue avec le nombre d’objets | Quasi constante quel que soit le nombre d’objets |
| **Traitement par image** | Indépendant par objet | Par lots avec caractéristiques partagées |

Le résultat est une **inférence nettement plus rapide** — Meta annonce des gains de vitesse sans sacrifier la précision sur les benchmarks SA-V et YT-Temporal-1B. Le multiplexeur gère automatiquement les occlusions, la ré-entrée d’objets et l’assignation d’identité, en s’appuyant sur un raisonnement global sur l’ensemble de la banque mémoire.

### Raisonnement global

SAM 3.1 ajoute également des **capacités de raisonnement global** — le modèle peut désormais prendre en compte le contexte vidéo complet pour ses décisions de suivi. Plutôt que des prédictions image par image basées sur un contexte local, le raisonnement global permet au modèle de :

- Ré-identifier les objets qui quittent temporairement le cadre
- Résoudre les scénarios d’occlusion ambigus en raisonnant à travers les instants
- Maintenir une identité cohérente des objets même lors de mouvements rapides

C’est particulièrement important pour les applications de surveillance, d’analyse sportive, de suivi de la faune et de conduite autonome, où les objets sortent et rentrent régulièrement dans le cadre.

## Benchmarks et performances

Meta a publié une série de points de contrôle améliorés sur [Hugging Face (facebook/sam3.1)](https://huggingface.co/facebook/sam3.1) en même temps que SAM 3.1. Ces nouveaux checkpoints montrent :

- **Benchmark SA-V** : performances compétitives ou améliorées sur la précision de segmentation vidéo
- **YT-Temporal-1B** : résultats solides sur la compréhension vidéo à grande échelle
- **Débit en temps réel** : augmentation spectaculaire des images par seconde pour les scénarios de suivi multi-objets

Le jeu de données SA-Co, publié avec SAM 3, continue de servir de benchmark d’évaluation principal. Il comprend :
- **SA-Co/Gold** : benchmarks d’images vérifiés par des humains avec syntagmes nominaux annotés
- **SA-Co/Silver** : benchmarks d’images annotés automatiquement à plus grande échelle
- **SA-Co/VEval** : jeu de données d’évaluation vidéo avec masques d’instances et identifiants uniques d’objets

## Comment utiliser SAM 3.1

SAM 3.1 nécessite Python 3.12+, PyTorch 2.7+ et un GPU compatible CUDA avec CUDA 12.6+. L’installation est simple :

```bash
git clone https://github.com/facebookresearch/sam3.git
cd sam3
pip install -e .
```

Utilisez ensuite le modèle pour la segmentation d’images par requête textuelle :

```python
from sam3.model_builder import build_sam3_image_model
from sam3.model.sam3_image_processor import Sam3Processor

model = build_sam3_image_model()
processor = Sam3Processor(model)

inference_state = processor.set_image("photo.jpg")
output = processor.set_text_prompt(
    state=inference_state,
    prompt="all red cars"
)
```

Ou pour le suivi vidéo avec le nouveau multiplexeur :

```python
from sam3.model_builder import build_sam3_video_predictor

predictor = build_sam3_video_predictor()
# SAM 3.1 utilise automatiquement Object Multiplex
# pour le suivi multi-concepts
```

## Le contexte plus large

SAM 3.1 arrive à un moment où Meta mise à la fois sur la vision par ordinateur open source et sur ses Superintelligence Labs (MSL) — la même division derrière [le modèle Muse Spark à code source fermé de Meta]({% post_url 2026-05-26-meta-muse-spark-hybrid-strategy-2026 %}). La famille SAM est l’une des contributions open source les plus réussies de Meta, le SAM original cumulant plus de 54 000 étoiles GitHub et SAM 2 près de 20 000.

Cette sortie témoigne également de l’engagement continu de Meta en faveur de **modèles de vision à poids ouverts**, alors même que son modèle de langage phare (Llama 4) reste non diffusé et que son modèle Muse Spark est uniquement accessible en mode hébergé. SAM 3.1 est entièrement open source, avec les poids du modèle disponibles sur Hugging Face et le code sur GitHub — une stratégie qui a érigé les modèles de vision de Meta en standards de facto pour la recherche comme pour les applications commerciales.

Pour l’écosystème IA au sens large, l’architecture de multiplexage de SAM 3.1 constitue une contribution technique importante. Le motif de suivi à mémoire partagée pourrait influencer d’autres domaines nécessitant un raisonnement multi-instances — du suivi multi-agent en robotique à la détection simultanée d’objets dans les systèmes autonomes. Cela reflète la transition plus large vers les architectures multi-agents que nous avons documentée dans notre [Guide ultime des frameworks d’agents IA open source]({% post_url 2026-05-27-ultimate-guide-open-source-ai-agent-frameworks %}).

## Résumé

| Aspect | Détail |
|--------|--------|
| **Modèle** | SAM 3.1 (Segment Anything Model 3.1) |
| **Innovation clé** | Object Multiplex — suivi multi-objets à mémoire partagée |
| **Date de sortie** | 27 mars 2026 (modèle mis à jour le 16 mai) |
| **Paramètres** | 848M |
| **Licence** | Licence de recherche (poids ouverts) |
| **GitHub** | [facebookresearch/sam3](https://github.com/facebookresearch/sam3) |
| **Hugging Face** | [facebook/sam3.1](https://huggingface.co/facebook/sam3.1) |
| **Article** | [SAM 3: Segment Anything with Concepts](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/) |

SAM 3.1 n’a peut-être pas l’éclat d’une nouvelle sortie de grand modèle de langage, mais pour quiconque construit des systèmes de vision par ordinateur nécessitant une détection et un suivi d’objets à vocabulaire ouvert en temps réel, c’est l’une des publications les plus pratiques de l’année — et un rappel que les contributions open source de Meta en IA vont bien au-delà de la famille Llama.