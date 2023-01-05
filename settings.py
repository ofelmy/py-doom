import math

# Constantes de configurations de la fenêtre pygame
# RES = WIDTH, HEIGHT = 1600, 900
RES = WIDTH, HEIGHT = 800,600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT //2
FPS = 60

# Constantes de configuration du joueur
PLAYER_POS = 1.5,5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# Constante de configuration du RayCasting
FOV = math.pi / 3               # angle de vision du joueur
HALF_FOV = FOV / 2
## nombre de rayons qui seront calculés
# plus on divise par un grand nombre plus la qualité sera faible
NUM_RAYS = WIDTH // 2           
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS    # angle entre 2 rayons
MAX_DEPTH = 20

# Distance de la localisation de l'écran
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)

SCALE = WIDTH // NUM_RAYS