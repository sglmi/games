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

running = True
while running:
    clock.tick(FPS)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update sprites

    # draw / render
    screen.fill(BLACK)
    # draw sprites
    pygame.display.flip()

pygame.quit()
