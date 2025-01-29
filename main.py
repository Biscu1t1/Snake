import pygame
from pygame.locals import *

def draw_snake():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, snake_color, (snake_x, snake_y, snake_size, snake_size))  # Draw snake
    pygame.display.flip()
        

if __name__ == "__main__":
    pygame.init()

    # set the screen size
    screen_x = 800
    screen_y = 600
    screen = pygame.display.set_mode((screen_x, screen_y))
    
    # draw the snake
    snake_x = 400
    snake_y = 250
    snake_size = 20
    snake_color = (255, 255, 255)
    draw_snake()

    pygame.display.set_caption("Snake Game")


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    snake_y -= 10
                    draw_snake()
                if event.key == K_DOWN:
                    snake_y += 10
                    draw_snake()    
                if event.key == K_LEFT:
                    snake_x -= 10
                    draw_snake()    
                if event.key == K_RIGHT:
                    snake_x += 10
                    draw_snake()    
            elif event.type == pygame.QUIT:
                running = False
    pygame.quit()