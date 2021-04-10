import pygame

from utils import Color
from utils import Setting

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(Color.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Setting.WIDTH / 2, Setting.HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > Setting.WIDTH:
            self.rect.right = 0