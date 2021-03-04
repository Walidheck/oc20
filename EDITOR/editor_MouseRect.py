import pygame
from pygame.locals import *

# couleurs
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Créer un écran
pygame.init()
screen = pygame.display.set_mode((640, 540))

start = (0, 0)
size = (0, 0)
drawing = False
color = BLACK
width = 1
shapes = []


## DRAW RECT

# définir une classe rectangle (avec couleur et épaisseur)
class Shape:
    def __init__(self, rect, color=RED, width=1):
        self.rect = rect
        self.color = color
        self.width = width

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)
        

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # Commande du clavier
        if event.type == KEYDOWN:
            
            # commande pour l'épaisseur
            if event.key == K_1:
                width = 1
            elif event.key == K_2:
                width = 5
            elif event.key == K_3:
                width = 15
            elif event.key == K_4:
                width = 0
       
           # commande pour les couleurs
            elif event.key == K_q:
                color = RED
            elif event.key == K_w:
                color = GREEN
            elif event.key == K_e:
                color = BLUE
            elif event.key == K_r:
                color = YELLOW
            elif event.key == K_t:
                color = CYAN
            elif event.key == K_z:
                color = MAGENTA
            elif event.key == K_u:
                color = BLACK
            elif event.key == K_i:
                color = GRAY
            elif event.key == K_o:
                color = WHITE
             
            # Tab pour dessiner sans pression de souris
            elif event.key == K_TAB:
                drawing = True
            
            # effacer dernier rectangle de liste shapes
            elif event.key == K_BACKSPACE:
                if len(shapes) > 1:
                    shapes.pop()
                    color = shapes[-1].color
                    width = shapes[-1].width
                
            shapes[-1].width = width
            shapes[-1].color = color
                
        # Commande de la souris 
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            s = Shape(Rect(start, (0, 0)), color, width)
            shapes.append(s)
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            shapes[-1].rect.size = size
     

        screen.fill(GRAY)
        for s in shapes:
            s.draw()    
        pygame.display.update()

   
pygame.quit()