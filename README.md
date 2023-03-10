# Py-Doom

Création du jeu Doom en python.

## sources

* [Youtube: Creating a DOOM-style 3D Game in Python from Scratch. Pygame Tutorial](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1ZTZHMteEJWRVNkM0RVRWNmYVhyZHVrTE1uUXxBQ3Jtc0tucF9aS2FUdG9tdDlCdl9jQm5pcUVZelJIZl9iREtmVl8zNFVfczVHQTlycUlBSDh6SlE2dHRLRXZmRzFBYVctXzZ4V3RFdXlEeGdXVk5QclFNYUlKOXlaUUFfNTdfUHdCc0FWTmdNdVQ4QmFvTDVMRQ&q=https%3A%2F%2Fgithub.com%2FStanislavPetrovV%2FDOOM-style-Game&v=ECqUrT7IdqQ)
* [github: StanislavPetrovV
/
DOOM-style-Game](https://github.com/StanislavPetrovV/DOOM-style-Game)
* [Sprite Database: Doom](https://spritedatabase.net/game/760)

## pré-requis

* pygame

```shell
pip install pygame
```

## Etapes

Chaque étape sera dans un commit différent

### Etape 1 : création de la structure

Création des fichier python suivants:

```shell
└ py-doom
  ├ main.py
  ├ map.py
  ├ object_renderer.py
  ├ player.py
  ├ raycasting.py
  └ setting.py
```

### Etape 2: création de la class Game

Création d'une class python de gestion de l'espace pygame.

On peut lancer le jeu :

```shell
python.exe .\main.py
```

### Etape 3: création de la map

Crée et gère la map

### Etape 4: Création du joueur

Crée le joueur, gère ses mouvements, et indique la direction de sa vision

### Etape 5: Gère la collision du joueur avec les murs

vérifie que le joueur ne peut pas traverser les murs

### Etape 6: Prépare le ray casting

Scanne l'ensemble des points qui devront être affichés par rapport à la vision du joueur

### Etape 7: commencer le rendu 3D en ray-casting

pour chaque rayon de vision du joueur, un rectangle vertical est dessiné.

### Etape 8: améliore le rendu

Corrige l'effet fish-eye
calcule la couleur du mur en fonction de sa distance au joueur.
