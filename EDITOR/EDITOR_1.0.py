import pygame
from pygame.locals import *

# couleurs
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# créer un écran
pygame.init()
screen = pygame.display.set_mode((640, 540))

start = (0, 0)
size = (0, 0)
drawing = False