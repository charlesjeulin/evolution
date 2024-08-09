# Projet Evolution

***

## Introduction

Ce projet simule l'évolution des créatures dans un environnement en utilisant Pygame et Matplotlib.
Le projet est divisé en quatre étapes, chacune ajoutant des fonctionnalités et des complexités supplémentaires.

## Table des Matières

- [Présentation](#présentation)
- [Structure du projet](#structure-du-projet)
- [Dépendances](#dépendances)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Contrôles](#contrôles)
- [Crédits](#crédits)

## Présentation

Qu'est-ce que l'evolution ? Pourquoi les choses existent ?
 
- Parce qu'elles sont nées
- Parce qu'elles ne sont pas mortes

Exemples :

1. Les gouttes de pluie naissent beaucoup et meurent peu
2. Les planètes naissent peu et meurent peu

On observe que chaque chose a l'air d'atteindre un équilibre en fonction de son taux de naissance et de mort.

***

Supposons que les créatures naissent et meurent selon des taux constants B et D.

On observe que si le taux de naissance est égal au taux de mortalité, la taille de la population atteint un équilibre.

$$ B = D $$

Or chaque créature a une chance de mourir donc :

$$ D = N \cdot D $$

**L'équation à l'équilibre devient :**

$$ B = N \cdot D $$

Le problème est que dans la vraie vie une créature ne peut pas naitre toute seule.

Heureusement, les créatures peuvent se reproduire.

Donc maintenant, le taux de naissance est ajusté par le taux de reproduction.

$$ B = B + N \cdot R $$

**L'équation à l'équilibre devient :**

$$ B + N \cdot R = N \cdot D $$

$$ N = \frac{B}{D - R} $$

Mais si jamais la chance de reproduction est plus grande que la chance de mort, la taille de la population va être négative ce qui casse notre équation.

Voir `stage_1.py`

***

Pour rendre notre équation plus réaliste, on va essayer de supprimer l'hypothèse que les créatures naissent toutes seules (B).

On sait que :

$$ B = D $$

Donc, on va avoir le changement possible avec :

$$ &Delta; = B - D = 0 $$

$$ &Delta; = f(N) $$

$$ &Delta; = B + R \cdot N - D \cdot N $$

$$ &Delta; = B + (R - D) \cdot N $$

Si B est égale à 0, une population peut atteindre l'extinction.

Si la probabilité de reproduction est plus grande que la probabilité de mort, la population va augmenter.

Voir `stage_2.py`

***

Maintenant que les créatures ne peuvent pas naitre toutes seules, comment les créatures peuvent elles apparaitre ?

La réponse est les mutations.

En effet, lors de la reproduction, il y a une chance que la créature naisse avec des caractéristiques différentes. Par exemple, une créature peut naitre avec une chance de reproduction plus grande.

La probabilité de se reproduire est donc ajustée par la probabilité de mutation (M) :

$$ R = R \cdot (1 - M) $$

Exemple :

- Génération 1 : 
    - \( B_1 = 1 \)
    - \( D_1 = 0.1 \)
    - \( R_1 = 0.05 \)
    - \( M_1 = 0.1 \)

$$ &Delta; = B_1 + (R_1 - D) \cdot N $$

On remplace R par R * (1 - M) pour prendre en compte les mutations :

$$ &Delta; = B_1 + (R_1 \cdot (1 - M_1) - D_1) \cdot N_1 $$

- Génération 2 :
    - \( B_2 = 0 \)
    - \( D_2 = 0.1 \)
    - \( R_2 = 0.05 \)
    - \( M_2 = 0 \)

$$ &Delta; = B_2 + (R_2 - D_2) \cdot N_2 + mutations $$

Si on simplifie l'équation de la gen 1, on obtient :

$$ &Delta; = B_1 + R_1 \cdot N_1 - R_1 \cdot M_1 \cdot N_1 - D_1 \cdot N_1 $$

On peut donc dire que les créatures créées par mutation sont égales à :

$$ mutations = R_1 \cdot M_1 \cdot N_1 $$

Donc l'équation de la gen 2 devient :

$$ &Delta; = B_2 + (R_2 - D_2) \cdot N_2 + R_1 \cdot M_1 \cdot N_1 $$

Ainsi, on a maintenant une population qui peut apparaitre sans naitre toute seule, et qui peut évoluer avec des mutations.

Voir `stage_3.py`

Dans cette simulation, on a 4 populations :

- Gen 1 (Bleue)
    - Peut naitre toute seule
    - Peut se reproduire
    - Peut muter en Gen 2_1 (Rouge) et Gen 2_2 (Verte)


- Gen 2_1 (Rouge)
    - Ne peut pas naitre toute seule
    - Peut se reproduire
    - Peut muter en Gen 3 (Orange), `faible chance de mutation`


- Gen 2_2 (Verte)
    - Ne peut pas naitre toute seule
    - Peut se reproduire
    - Ne peut pas muter


- Gen 3 (Orange)
    - Ne peut pas naitre toute seule
    - Peut se reproduire, `forte chance de reproduction`
    - Ne peut pas muter

Les stats font que si la population orange apparait, elle va prendre le dessus sur les autres populations et grandir exponentiellement sans limites.

***

Dans la vraie vie, une population ne peut pas augmenter indéfiniment. Il y a des limites.

Par exemple, si une population de lapins augmente, les renards vont aussi augmenter pour les manger.

On va repartir de notre équation :

$$ &Delta; = (R - D) \cdot N $$

On va ajouter un terme qui va réguler la population si elle est trop importante, en fonction de la population et d'un coefficient C :

$$ terme = C \cdot N $$

$$ &Delta; = (R - D - C \cdot N) \cdot N $$

Ainsi, si le terme pou réguler la population est en fonction du nombre total de créatures de toutes les générations, il va y avoir une compétition entre les générations.

**Carrying capacity :** C'est la capacité de charge de l'environnement, c'est-à-dire le nombre maximum de créatures que l'environnement peut supporter.

**Logistic growth :** C'est un modèle mathématique qui décrit la croissance d'une population en fonction de la capacité de charge de l'environnement.

Voir `stage_4.py`

***

**Conclusion :**

Les éléments clés de l'évolution sont la `réplication`, la `mutation` et la `compétition`.

La réplication est la capacité de se reproduire, la mutation est la capacité de changer, et la compétition est la capacité de survivre.

## Structure du projet

Le projet est organisé comme suit :

- `evolution/`
  - `venv/`
  - `images/`
  - `stage_1.py`
  - `stage_2.py`
  - `stage_3.py`
  - `stage_4.py`

## Dépendances

- Python 3.7 ou supérieur
  - Pygame
  - Matplotlib

## Installation

1. Clonez le dépôt :
```sh
git clone https://github.com/charlesjeulin/evolution
cd evolution
```

2. Créez et activez un environnement virtuel :
```sh
python3 -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
```

3. Installez les dépendances :
```sh
pip install pygame matplotlib
```

## Utilisation

Chaque étape de la simulation peut être exécutée indépendamment. Voici la commande pour exécuter une simulation :

```sh
cd evolution
python nom_du_fichier.py
```

### Contrôles

Pendant l'exécution d'une simulation, utilisez les touches suivantes pour interagir :

↑ : Augmente le FPS de 10

↓ : Diminue le FPS de 10

R : Réinitialise la simulation

## Crédits

Vidéos youtube de Primer : [`https://www.youtube.com/@PrimerBlobs`](https://www.youtube.com/@PrimerBlobs)