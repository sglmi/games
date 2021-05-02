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
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.speedx = 1 

    def update(self):
        self.rect.x += self.speedx

all_sprites = pygame.sprite.Group()
snake = Snake()
all_sprites.add(snake)

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
