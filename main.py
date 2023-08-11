import pygame

#starts pygame
pygame.init()

#screen size
screen = pygame.display.set_mode((800, 600))

#check if user closes the window
#screen will be shown while 'is_executed' is True
is_executed = True
while is_executed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_executed = False

