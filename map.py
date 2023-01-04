import pygame as pg

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, _, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, 1, 1, 1, 1, 1, _, _, 1],
    [1, _, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, _, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    # crée un dictionnaire avec la clef = coordonnées et la valeur la valeur définie dans la mini_map
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value: 
                    self.world_map[(i, j)] = value
        print(self.world_map)
    
    # dessine des rectangles de 100x100 aux positions indiquées par world_map
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
        for pos in self.world_map]