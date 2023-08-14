import pygame

#starts pygame
pygame.init()

#screen size
screen = pygame.display.set_mode((1280, 720)) #800 width, 600 height original

#títle and icon
pygame.display.set_caption("Zombie Invasion")
icon = pygame.image.load("skullLogo.png")
pygame.display.set_icon(icon)

#player
img_player = pygame.image.load("player.png")
player_pos_x = 10
player_pos_y = 328 # screen height / 2 - 32 (image's size 64px/2)

#var to check if screen's player is opened/closed
is_executed = True

def player():
    screen.blit(img_player, (player_pos_x, player_pos_y))

while is_executed:

    #background screen's color
    screen.fill((2, 191, 252))

    # check if user closes the window
    # screen will be shown while 'is_executed' is True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_executed = False

    #we set player's icon on screen
    player()

    pygame.display.update()