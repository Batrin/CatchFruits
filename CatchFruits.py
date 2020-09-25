import pygame
import random
from random import randint

WIDTH = 800
HEIGHT = 600
FPS = 30

BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FLAG = 0
SCORE = 0
fruitsCounter = 0
SCORE_STR = "Your score is : "
BASKET_SPEED = 10
SECOND_LEVEL_BASKET_SPEED = 15

#класс корзинки
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT -30)


#класс фрукта
class Fruits(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(0, WIDTH) , HEIGHT / 2)




pygame.init()
font = pygame.font.Font(None, 70)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch Fruits")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
basket = Basket()
fruit = Fruits()
all_sprites.add(basket, fruit)

running = True
while running:
    clock.tick(FPS)

    #catch event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #изменение скорости фруктов в зависимости от счетчика фруктов
    if fruitsCounter < 5 :
        fruit.rect.y += 4
    elif (fruitsCounter >= 5 and fruitsCounter <= 15):
        fruit.rect.y += 7
        BASKET_SPEED = SECOND_LEVEL_BASKET_SPEED
    elif (fruitsCounter > 15 and fruitsCounter <= 25):
        fruit.rect.y += 9
    elif fruitsCounter > 25:
        fruit.rect.y += 12

    #отлавливание нажатий на кнопки движения корзинки
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            basket.rect.x -= BASKET_SPEED
        if event.key == pygame.K_RIGHT:
            basket.rect.x += BASKET_SPEED
        if basket.rect.left > WIDTH :
            basket.rect.x = 0
        if basket.rect.right < 0 :
            basket.rect.x = WIDTH

    #проверка на то, что фрукт попал в корзинку
    if (fruit.rect.left > basket.rect.left and
       fruit.rect.right < basket.rect.right and
       fruit.rect.bottom >= basket.rect.top):
           fruit.rect.x = randint(0, WIDTH)
           fruit.rect.y = 0
           fruitsCounter += 1
    #иначе, если не попал в коризнку
    elif fruit.rect.top > HEIGHT:
       fruit.rect.x = randint(0, WIDTH)
       fruit.rect.y = 0
    text = font.render(str(fruitsCounter), True, [255, 255, 255])
    textpos = (WIDTH / 2, 10)
    all_sprites.update()
    screen.fill(BLACK)
    screen.blit(text, textpos)
    print(FLAG)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
