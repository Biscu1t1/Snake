import pygame
from pygame.locals import *
import random
import time

class Apple:
    def __init__(self, home_screen):
        self.home_screen = home_screen
        self.apple_color = (255, 0, 0)
        self.food_size = 20
        self.food_x = random.randint(0, 800 - self.food_size)
        self.food_y = random.randint(0, 600 - self.food_size)
        self.food_color = (255, 0, 0)

    def draw_apple(self):
        pygame.draw.rect(self.home_screen, self.apple_color, (self.food_x, self.food_y, self.food_size, self.food_size))
        pygame.display.flip()

class Snake:   
    def __init__(self, home_screen, snake_length):
        self.snake_length = snake_length
        self.home_screen = home_screen
        self.snake_size = 20

        self.x = [self.snake_size]*snake_length
        self.y = [self.snake_size]*snake_length
        self.snake_x = 400
        self.snake_y = 250
        self.snake_color = (255, 255, 255)
        pygame.display.flip()
        self.direction = "center"

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"
    
    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"

    


    def draw(self):
        self.home_screen.fill((0, 0, 0))
        for i in range(self.snake_length):
            pygame.draw.rect(self.home_screen, self.snake_color, (self.x[i], self.y[i], self.snake_size, self.snake_size))
        pygame.display.flip()

    def auto_walk(self):

        for i in range(self.snake_length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if self.direction == "up":
            self.y[0] -= self.snake_size
        if self.direction == "down":
            self.y[0] += self.snake_size
        if self.direction == "left":
            self.x[0] -= self.snake_size 
        if self.direction == "right":
            self.x[0] += self.snake_size


        self.draw()
        
  

class Game:
    def __init__(self):
        pygame.init()
        self.screen_x = 800
        self.screen_y = 600
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.snake = Snake(self.screen, 3)
        self.snake.draw()

        self.apple = Apple(self.screen)
        self.apple.draw_apple()

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
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
            self.apple.draw_apple()

            time.sleep(0.2)
        pygame.quit()






if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.set_caption("Snake Game")
