import random
from enum import Enum

import pygame


# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

class Snake(pygame.sprite.Sprite):
    block_x = 25
    block_y = 25
    block_size = (block_x, block_y)

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(Snake.block_size)  # snake head
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.speedx = 5 
        self.speedy = 5
        self.direction = Direction.LEFT
        self.score = 0
    
    def crawl(self, direction):
        if direction == Direction.LEFT:
            self.rect.x -= self.speedx
        if direction == Direction.RIGHT:
            self.rect.x += self.speedx
        if direction == Direction.UP:
            self.rect.y -= self.speedy
        if direction == Direction.DOWN:
            self.rect.y += self.speedy

    def is_eat(self, food):
        is_collision = pygame.sprite.collide_rect(self, food)
        if is_collision:
            return True
        return False

    def grow(self):
        """ Grow snake body with the amount of score
            if score was 8 snake body need to be 8 time of block size.

            I have the head of snake green block 
            I need to add next surface after head
            Every time I make the snake I will increase the body
            meaning all images drown again plus new  block
            """
        #print(dir(self.image))
        self.image = pygame.Surface((Snake.block_x * self.score , Snake.block_y))  # snake body
        self.image.fill(GREEN)
        #self.image.blit(screen, self.rect)
        #print(self.image.get_rect())

         

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.direction = Direction.LEFT
        if key_pressed[pygame.K_RIGHT]:
            self.direction = Direction.RIGHT 
        if key_pressed[pygame.K_UP]:
            self.direction = Direction.UP
        if key_pressed[pygame.K_DOWN]:
            self.direction = Direction.DOWN
        self.crawl(self.direction)

        print(self.rect)

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

    # if snake eat a food
    if snake.is_eat(food):
        snake.score += 1
        food.kill()
        # create new food
        food = Food()
        all_sprites.add(food)
        # grow snake body
        snake.grow() 

    # update sprites
    all_sprites.update()
    # draw / render
    screen.fill(WHITE)
    # draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
