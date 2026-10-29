import math


# game settings
WIDTH, HEIGHT = 1200, 800
FPS = 60
TILE = 100
HALF_HEIGHT = HEIGHT / 2
HALF_WIDTH = WIDTH / 2
FPS_POS = (WIDTH - 65, 5)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 4 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# sprite settings
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1

# texture settings
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# player settings
player_speed = 2
player_pos = HALF_WIDTH, HALF_HEIGHT
player_angle = 0

# colors
BACKGROUND_COLOR = (30, 30, 30)
POINT_COLOR = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKYBLUE = (0, 186, 255)
RED = (255, 0, 0)
