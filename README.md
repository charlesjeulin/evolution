# Projet Evolution

***

## Description

Ce projet simule l'évolution des créatures dans un environnement en utilisant Pygame et Matplotlib. Le projet est divisé en quatre étapes, chacune ajoutant des fonctionnalités et des complexités supplémentaires.

## Structure du projet

Le projet est organisé comme suit :

- `evolution/`
  - `venv/` - Environnement virtuel Python
  - `images/` - Images utilisées dans la simulation
  - `stage_1.py` - Première étape de la simulation
  - `stage_2.py` - Deuxième étape de la simulation
  - `stage_3.py` - Troisième étape de la simulation
  - `stage_4.py` - Quatrième étape de la simulation

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

Chaque étape de la simulation peut être exécutée indépendamment. Voici la commandes pour exécuter chaque étape :

```sh
cd evolution
python nom_du_fichier.py
```

## Détails des fichiers Python et Approches Mathématiques

### `stage_1.py`

**Description :**

Le programme de la première étape met en place une simulation simple où les créatures se déplacent aléatoirement dans un environnement donné. Les probabilités de naissance (B), de mort (D) et de reproduction (R) sont constantes.

**Approche Mathématique :**
- \( N \) : Nombre de créatures
- \( B \) : Taux de naissance
- \( D \) : Taux de mortalité

Équation de base :

$$ N = \frac{B}{D} $$

Cela signifie que le nombre de créatures à l'équilibre est déterminé par le rapport entre le taux de naissance et le taux de mortalité.

***

### `stage_2.py`

**Description :**

Cette étape ajoute des graphiques en temps réel pour visualiser l'évolution du nombre de créatures et leur équilibre au fil du temps.

**Approche Mathématique :**
- \( B(t) \) et \( D(t) \) : Taux de naissance et de mortalité en fonction du temps

Équation modifiée pour inclure l'évolution temporelle :

$$ D = B + N \cdot R - N \cdot D $$

À l'équilibre :

$$ D = B $$

Cette équation montre que le taux de mortalité est égal au taux de naissance à l'équilibre, ajusté par les contributions des taux de reproduction et de mortalité en fonction du nombre de créatures.

***

### `stage_3.py`

**Description :**

Cette étape introduit des mutations et des générations avec des caractéristiques de reproduction et de mortalité différentes. Les créatures peuvent muter en changeant de couleur, représentant différentes générations.

**Approche Mathématique :**
- \( M \) : Taux de mutation
- \( R \) : Taux de reproduction (peut varier avec les mutations)
- Génération 1 (Gen 1) et Génération 2 (Gen 2) avec des comportements distincts

Équation avec mutations :

$$ D = B_1 + (R_1 - D) \cdot N + R_1 \cdot M $$

Sans mutations :

$$ D = B_1 + (R_1 - D) \cdot N $$

La mutation est incluse en ajoutant un terme qui représente le taux de mutation multiplié par le taux de reproduction.

***

### `stage_4.py`

**Description :**

Cette étape continue d'affiner les mutations et les dynamiques inter-générationnelles, introduisant des caractéristiques distinctes pour chaque génération de créatures.

**Approche Mathématique :**
- Compétition entre générations
- Introduction de taux de mutation spécifiques pour chaque génération

Équation avec compétition et mutations :

$$ D = B_2 + (R_2 \cdot (1 - M) - D) \cdot N + R_2 \cdot M \cdot N $$

À l'équilibre :

$$ D = R_2 \cdot N $$

Cela montre que le taux de mortalité est ajusté par les taux de reproduction et de mutation spécifiques à chaque génération, en tenant compte de la compétition entre générations.

### Diagrammes et Graphiques

**Graphiques en Temps Réel :**
- **Nombre de Créatures (N) au fil du temps :** Montre comment le nombre de créatures évolue, atteint un équilibre, et réagit aux mutations.
- **Taux de Naissance vs Taux de Mortalité :** Visualise les dynamiques d'équilibre et les points de basculement lorsque les mutations sont introduites.


### Contrôles

Pendant l'exécution de la simulation, utilisez les touches suivantes pour interagir :

↑ : Augmente le FPS de 10

↓ : Diminue le FPS de 10

R : Réinitialise la simulation

## Auteur

Ce projet a été développé par Charles JEULIN.