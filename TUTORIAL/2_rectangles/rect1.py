import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img = pygame.image.load('bird.png')
img.convert()


rect = img.get_rect()
print(rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, RED, r2)
    pygame.display.flip()

pygame.quit()