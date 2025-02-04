import pygame
from pygame.locals import *
import random
import time

class Apple:
    def __init__(self, home_screen):
        self.home_screen = home_screen
        self.apple_color = (255, 0, 0)
        self.food_size = 20
        self.food_x = random.randint(0, 39) * self.food_size
        self.food_y = random.randint(0, 29) * self.food_size
        self.food_color = (255, 0, 0)

    def draw_apple(self):
        pygame.draw.rect(self.home_screen, self.apple_color, (self.food_x, self.food_y, self.food_size, self.food_size))
        pygame.display.flip()



class Snake:   
    def __init__(self, home_screen, snake_length):
        self.snake_length = snake_length
        self.home_screen = home_screen
        self.snake_size = 20
        self.snake_color = (255, 255, 255)

        self.x = [100 - i * self.snake_size for i in range(snake_length)]
        self.y = [100] * snake_length
        
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
    
        # Draw score in a fixed location
        font = pygame.font.SysFont(None, 55)
        score_text = font.render(f"Score: {self.snake_length - 2}", True, (255, 255, 255))
        self.home_screen.blit(score_text, (10, 10))  # Draw score at top-left

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
        self.snake = Snake(self.screen, 2)
        self.snake.draw()

        self.apple = Apple(self.screen)
        self.apple.draw_apple()

    def game_over_screen(self):
        font = pygame.font.SysFont(None, 55)
        game_over_text = font.render("Game Over!" + " ", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
        self.screen.fill((0, 0, 0))

        screen_center_x = self.screen_x // 2
        screen_center_y = self.screen_y // 3

        self.screen.blit(game_over_text, (screen_center_x - game_over_text.get_width() // 2, screen_center_y))
        self.screen.blit(restart_text, (screen_center_x - restart_text.get_width() // 2, screen_center_y + 60))
        self.screen.blit(quit_text, (screen_center_x - quit_text.get_width() // 2, screen_center_y + 120))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:  # Quit
                        pygame.quit()
                        exit()
                    if event.key == K_r:  # Restart the game
                        self.__init__()  # Reinitialize game
                        self.run()

    def is_collision(self , x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + self.snake.snake_size:
            if y1 >= y2 and y1 < y2 + self.snake.snake_size:
                return True

        return False
    
    def is_out_of_bounds(self, x, y):
        if x < 0 or x >= self.screen_x or y < 0 or y >= self.screen_y:
            return True
        return False

    def snake_collision(self):
        # prevent collision at the start of the game
        if self.snake.snake_length < 3:  
            return False

        for i in range(1, self.snake.snake_length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                return True
        return False


    def eat_apple(self):
         if self.snake.x[0] == self.apple.food_x and self.snake.y[0] == self.apple.food_y: 
            self.snake.snake_length += 1
            self.snake.x.append(self.snake.x[-1])  
            self.snake.y.append(self.snake.y[-1])

            # Generate new apple & make sure it doesn't appear on the snake
            while True:
                new_x = random.randint(0, 39) * 20  
                new_y = random.randint(0, 29) * 20

                snake_body = [(self.snake.x[i], self.snake.y[i]) for i in range(self.snake.snake_length)]
                if (new_x, new_y) not in snake_body:  
                    break  

            self.apple.food_x = new_x
            self.apple.food_y = new_y
    

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
            self.apple.draw_apple()
            pygame.display.flip()

            if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.food_x, self.apple.food_y):
                self.eat_apple()

            if self.is_out_of_bounds(self.snake.x[0], self.snake.y[0]):
                self.game_over_screen()
            
            if self.snake_collision():
                self.game_over_screen()
                return

            time.sleep(0.1)
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.set_caption("Snake Game")
