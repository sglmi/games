import pygame

from pygame.locals import (QUIT, K_ESCAPE)
from snake import Snake

from utils import Color
from utils  import Setting




pygame.init()

screen = pygame.display.set_mode((Setting.WIDTH, Setting.HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
snake = Snake(screen)
all_sprites.add(snake)
running = True
while running:
    clock.tick(Setting.FPS)

    # user inputs / events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
    # update
    all_sprites.update()

    # draw / render
    screen.fill(Color.BLACK)
    all_sprites.draw(screen)    
    pygame.display.flip()

pygame.quit()