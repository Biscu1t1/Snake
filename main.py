import pygame
from pygame.locals import *
import random
import time

class Snake:   
    def __init__(self, home_screen):
        self.home_screen = home_screen
        home_screen.fill((0, 0, 0))
        self.snake_x = 400
        self.snake_y = 250
        self.snake_size = 20
        self.snake_color = (255, 255, 255)
        self.snake = pygame.draw.rect(self.home_screen, self.snake_color, (self.snake_x, self.snake_y, self.snake_size, self.snake_size))
        pygame.display.flip()
        self.direction = "center"

    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"
    
    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    


    def draw(self):
        self.home_screen.fill((0, 0, 0))
        pygame.draw.rect(self.home_screen, self.snake_color, (self.snake_x, self.snake_y, self.snake_size, self.snake_size))
        pygame.display.flip()

    def auto_walk(self):
        if self.direction == "up":
            self.snake_y -= 20
        if self.direction == "down":
            self.snake_y += 20
        if self.direction == "left":
            self.snake_x -= 20 
        if self.direction == "right":
            self.snake_x += 20


        self.draw()
        
  

class Game:
    def __init__(self):
        pygame.init()
        self.screen_x = 800
        self.screen_y = 600
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.snake = Snake(self.screen)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()
        
                    if event.key == K_LEFT:
                        self.snake.move_left() 

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == pygame.QUIT:
                    running = False

            self.snake.auto_walk()
            time.sleep(0.2)
        pygame.quit()






if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.set_caption("Snake Game")

    

    # def draw_apple():
#     pygame.draw.rect(screen, apple_color, (food_x, food_y, food_size, food_size))  # Draw apple

# def eat_apple():
#     if snake_x == food_x and snake_y == food_y:
#         snake_size += 10
#         draw_snake()

   # draw the food + randomise position
    # apple_color = (255, 0, 0)
    # food_size = 20
    # food_x = random.randint(0, screen_x - food_size)
    # food_y = random.randint(0, screen_y - food_size)
    # food_color = (255, 0, 0)
    # pygame.draw.rect(screen, food_color, (food_x, food_y, food_size, food_size))
    # pygame.display.flip()
    # draw_apple()