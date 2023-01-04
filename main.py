import pygame as pg
import sys
from settings import *
from map import *

class Game:
    
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    # crée un objet Map
    def new_game(self):
        self.map = Map(self)
    
    # met à jour l'affichage de la fenêtre de jeu 
    def update(self):
        # affiche tout ce qui a été dessiné 
        pg.display.flip()
        # met à jour la fréquence de rafraîchissement
        self.clock.tick(FPS)
        # définit le titre de la fenêtre de jeu.
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    # met la fenêtre du jeu en noir, et dessine par dessus
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
    
    # récupère les evènements utilisateur
    def check_events(self):
        for event in pg.event.get():
            ## Quitte le programme quand on ferme la fenêtre ou qu'on appuie sur la touche ECHAP
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    # démarre la boucle du jeu
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()