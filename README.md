# Space Shooter

Petit jeu de tir 2D en Python avec Pygame, inspiré de Space Invaders.
Projet d'apprentissage de la programmation orientée objet.

## Fonctionnalités
- Déplacement et tir du joueur
- Ennemis qui apparaissent et tirent de façon aléatoire
- Collisions, score et points de vie
- Écran de Game Over avec score final

## Installation
```
python -m venv venv
.\venv\Scripts\activate
python -m pip install pygame-ce
```

## Lancer le jeu
```
python main.py
```

## Commandes
- Flèches gauche / droite : se déplacer
- Espace : tirer

## Structure du code
- `classes.py` : les classes `Personnage`, `Joueur`, `Ennemi`, `Projectile` et `Jeu`
- `main.py` : la boucle principale et l'affichage