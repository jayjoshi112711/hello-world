def plot_snake(gamewindow,black1,snk_list,Snake_size1):
    for x,y in snk_list:
        pygame.draw.rect(gamewingow, black1, [x, y, Snake_size1, Snake_size])