import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode((640, 240))

drawing = False
points = []
running = True
mode = 'polygon'

point_list = []

# définir une classe rectangle (avec couleur et épaisseur)
class Shape:
    def __init__(self, rect, color=RED, width=1):
        self.rect = rect
        self.color = color
        self.width = width

    
       
class Rectangle(Shape):
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)
    
    
class Polygon(Shape):
    
    def draw(self):
        if len(self.points)>1:
            self.rect = pygame.draw.lines(screen, RED, True, points, 3)

        


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(points) > 0:
                    points.pop()
                    
            if event.key == K_SPACE:
                print('end editing')
                point_list.append(points)
                points = []
                
            if event.key == K_p:
                mode = 'polygon'
                print('mode =', mode)

            if event.key == K_r:
                mode = 'rectangle'
                print('mode =', mode)

                
                

        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True

        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            points[-1] = event.pos
            
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(points) > 0:
                    points.pop()
            
    screen.fill(GRAY)
    if len(points)>1:
        rect = pygame.draw.lines(screen, RED, True, points, 3)
        
    for p in point_list:
        if len(p)>1:
            pygame.draw.lines(screen, RED, True, p, 3)

    pygame.display.update()

pygame.quit()

    