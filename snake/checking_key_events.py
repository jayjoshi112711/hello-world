import pygame
x=pygame.init()

#Creating a window
gameWindow=pygame.display.set_mode((1000,600))
pygame.display.set_caption("My First Game Window...")

#Game specific Variable
exit_game=False
game_over=False

#Creating game looop
while not exit_game:

    for event in pygame.event.get():
        gameWindow.fill((251, 76, 21))
        pygame.display.update()
        for i in range(1000):
            continue
        gameWindow.fill((100,123,200))
        pygame.display.update()

pygame.quit()
quit()