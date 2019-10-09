import random
import pygame
x=pygame.init()
clock=pygame.time.Clock()
#Creating a window
screen_width=1000
screen_height=600
gameWindow=pygame.display.set_mode((1000,600))
pygame.display.set_caption("My First Game Window...")
snake_size=15
snake_x=20
snake_y=50
velocity_x=0
velocity_y=0
#Game specific Variable
exit_game=False
game_over=False
color=[(255,0,0),(0,255,0),(0,0,255),(0,0,0)]
i=0
food_x=random.randint(0,screen_width)
food_y=random.randint(0,screen_height)

#Creating game looop
while not exit_game:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-10
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=10
                velocity_x=0
    if(i==3):
        i=0
    snake_x += velocity_x
    snake_y += velocity_y
    gameWindow.fill((255,255,255))
    pygame.display.update()
    #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,Snake_size,Snake_size])
    pygame.draw.rect(gameWindow,color[i],[snake_x,snake_y,15,15])
    pygame.draw.rect(gameWindow,(12,54,78),[food_x,food_y,snake_size,snake_size])
    pygame.display.update()
    i+=1
pygame.quit()
quit()