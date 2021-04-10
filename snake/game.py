import pygame

import time 


def draw_snake(screen, head_x, head_y):
    global snake_head
    # display snake_head in x, y corrdinate
    screen.fill((255, 255, 255))
    screen.blit(snake_head, (head_x, head_y))
    pygame.display.flip()

def main():
    global snake_head
    pygame.init()

    # create main window
    screen = pygame.display.set_mode((640, 400))

    # load snake head
    snake_head = pygame.image.load("assets/images/head_right.png").convert()
    # snake head position
    head_x = 100
    head_y = 100
    
    draw_snake(screen, head_x, head_y)

    running = True
    while running:

        # fill screen with background color every while loop iteration.
        # Basically clear the screen.
        #screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    head_y -= 10
                    draw_snake(screen, head_x, head_y)
                if event.key == pygame.K_LEFT:
                    head_x -= 10
                    draw_snake(screen, head_x, head_y)
                if event.key == pygame.K_DOWN:
                    head_y += 10 
                    draw_snake(screen, head_x, head_y)
                if event.key == pygame.K_RIGHT:
                    head_x += 10 
                    draw_snake(screen, head_x, head_y)
            if event.type == pygame.QUIT:
                running = False
         
        # clean main window and draw everything again
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
