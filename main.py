import pygame

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake Game")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()