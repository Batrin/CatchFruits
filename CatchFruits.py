import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Basket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT -30)
    def update(self):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rect.x -= 10
                if event.key == pygame.K_RIGHT:
                    self.rect.x += 10
                if self.rect.left > WIDTH :
                    self.rect.x = 0
                if self.rect.right < 0 :
                    self.rect.x = WIDTH

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch Fruits")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
basket = Basket()
all_sprites.add(basket)

running = True
while running:
    clock.tick(FPS)

    #catch event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    print("Second")

pygame.quit()
