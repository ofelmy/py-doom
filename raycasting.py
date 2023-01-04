import pygame as pg
import math
from settings import *

class RayCasting: 
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        # angle du 1er rayon par rapport à l'horizontale
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            
            # calcule les coordonnées des points d'intersection du rayon avec les horizontales de la map
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            
            depth_hor = (y_hor - oy) / sin_a    # distance entre le joueur et le 1er point de croisement avec l'horizontale
            x_hor = ox + depth_hor * cos_a      # distance entre la coordonnée x du joueur et la coordonnée x du 1er point de croisement avec l'horizontale

            delta_depth = dy / sin_a            # distance entre le 1er point de croisement du rayon et le point suivant de croisement
            dx = delta_depth * cos_a            # distance entre la coordonnée x du 1er point de croisement du rayon et la coordonnée x du point de croisement suivant

            # boucle sur l'ensemble des intersections du rayon (au maximum 20)
            for i in range(MAX_DEPTH):
                    tile_hor = int(x_hor), int(y_hor)
                    # on arrête la boucle si on rencontre un mur
                    if tile_hor in self.game.map.world_map:
                        break
                    x_hor += dx
                    y_hor += dy
                    depth_hor += delta_depth

            # calcule les coordonnées des points d'intersection du rayon avec les verticales de la map
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            
            depth_vert = (x_vert - ox) / cos_a  # distance entre le joueur et le 1er point de croisement avec la verticale
            y_vert = oy + depth_vert * sin_a    # distance entre la coordonnée y du joueur et la coordonnée y du 1er point de croisement avec la verticale

            delta_depth = dx / cos_a            # distance entre le 1er point de croisement du rayon et le point suivant de croisement
            dy = delta_depth * sin_a            # distance entre la coordonnée y du 1er point de croisement du rayon et la coordonnée y du point de croisement suivant

            # boucle sur l'ensemble des intersections du rayon (au maximum 20)
            for i in range(MAX_DEPTH):
                    tile_vert = int(x_vert), int(y_vert)
                    # on arrête la boucle si on rencontre un mur
                    if tile_vert in self.game.map.world_map:
                        break
                    x_vert += dx
                    y_vert += dy
                    depth_vert += delta_depth

            # on récupère 2 points d'intersections avec un mur (1 sur la verticale, 1 sur l'horizontale). On choisit le plus proche du joueur
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # affiche les rayons (debug)
            pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
                        (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()

