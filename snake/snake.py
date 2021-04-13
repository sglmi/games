import pygame

from utils import Color
from utils import Setting

import pygame

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(Color.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Setting.WIDTH / 2, Setting.HEIGHT / 2)
        self.speedx = 5
        self.speedy = 5
        self.direction = None
    def update(self):
        self.key_pressed = pygame.key.get_pressed()
        if self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5

        if self.key_pressed[pygame.K_LEFT]:
            self.direction = 'left'
        if self.key_pressed[pygame.K_RIGHT]:
            self.direction = 'right'
        if self.key_pressed[pygame.K_UP]:
            self.direction = 'up'
        if self.key_pressed[pygame.K_DOWN]:
            self.direction = 'down'


class Food(pygame.sprite.Sprite):
    pass