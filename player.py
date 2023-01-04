from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
    
    # définit le mouvement de l'utilisateur dans la map
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        # calcule la position suivante du joueur par rapport à sa position actuelle
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_q]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        # met à jour la nouvelle position du joueur
        self.check_wall_collision (dx, dy)

        # calcule l'angle de vision du joueur par rapport à la map
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    # vérifie qu'il n'y a pas de mur aux coordonnées x,y
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    # calcule les coordonnées en fonction des murs
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy


    # dessine le joueur et sa vision
    def draw(self):
        # dessine la ligne de vision du joueur (commenté lors de l'affichage du raycasting)
        # pg.draw.line(self.game.screen, 'yellow',(self.x * 100, self.y *100),
        #             (self.x * 100 + WIDTH * math.cos(self.angle),
        #              self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        # dessine le joueur
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    # met à jour le joueur
    def update(self):
        self.movement()
    
    # définie la méthode propriété "pos", qui retourne la position en x,y
    # l'utilisation de @property permet d'appeler "Player.pos" au lieu de "Player.pos()"
    @property
    def pos(self):
        return self.x, self.y

    # définie la méthode propriété "map_pos", qui retourne la position avec les entiers x,y
    # retourne la coordonnée du jour arrondi à l'intersection de la grille
    @property
    def map_pos(self):
        return int(self.x), int(self.y)