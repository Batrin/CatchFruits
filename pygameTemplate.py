import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

pygame.init()
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Catch Fruits")
clock = pygame.time.Clock()


BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True
while running:
    screen.fill(BLACK)
    pygame.display.flip()

    #catch event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
