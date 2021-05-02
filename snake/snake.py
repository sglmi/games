import random

import pygame


# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

class Snake(pygame.sprite.Sprite):
    block_x = 25
    block_y = 25
    block_size = (block_x, block_y)

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(Snake.block_size)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.speedx = 5 
        self.speedy = 5

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedy

class Food(pygame.sprite.Sprite):
    block_x = 25
    block_y = 25
    block_size = (block_x, block_y)

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(Food.block_size)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # position
        self.rect.x = random.randrange(0, WIDTH - Food.block_x)
        self.rect.y = random.randrange(0, HEIGHT - Food.block_y)

all_sprites = pygame.sprite.Group()
snake = Snake()
food = Food()
all_sprites.add(snake)
all_sprites.add(food)

running = True
while running:
    clock.tick(FPS)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update sprites
    all_sprites.update()
    # draw / render
    screen.fill(BLACK)
    # draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
