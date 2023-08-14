import pygame
import random

# starts pygame
pygame.init()

# screen size
screen = pygame.display.set_mode((1280, 720)) #800 width, 600 height original

# títle and icon
pygame.display.set_caption("Zombie Invasion")
icon = pygame.image.load("skullLogo.png")
pygame.display.set_icon(icon)

# player
img_player = pygame.image.load("player.png")
player_pos_x = 10
player_pos_y = 328 # screen height / 2 - 32 (image's size 64px/2)
player_movement = 0

# zombies
img_zombie = pygame.image.load("zombi.png")
zombie_pos_x = random.randint(0,608) # screen width / 2 - 32 (image's size 64px/2)
zombie_pos_y = random.randint(0,328) # screen height / 2 - 32 (image's size 64px/2)
zombie_x_movement = -50
zombie_y_movement = 0.3

# var to check if screen's player is opened/closed
is_executed = True

# function to draw player's skin in his position X and Y
def player(x, y):
    screen.blit(img_player, (x, y))

# function to draw zombie's skin in his position X and Y
def zombie(x, y):
    screen.blit(img_zombie, (x, y))

while is_executed:

    # background screen's color
    screen.fill((2, 191, 252))

    # check if user closes the window
    # screen will be shown while 'is_executed' is True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_executed = False

        # check if player keep pressed KEYs left / right and his movement speed 0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_movement = -0.5
            if event.key == pygame.K_DOWN:
                player_movement = 0.5

        # check if player is NOT pressing any key then reset player movement's to 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_movement = 0

    # set player position depending on player_movement's var value
    player_pos_y += player_movement

    # keep player inside borders
    if player_pos_y <= 0:
        player_pos_y = 0
    elif player_pos_y >= 656: # 720 (height) - 64px (image's size skin)
        player_pos_y = 656

    # set zombie position depending on zombie_y_movement's var value
    zombie_pos_y += zombie_y_movement

    # keep zombies inside borders
    if zombie_pos_y <= 0:
        zombie_y_movement = 0.3
        zombie_pos_x += zombie_x_movement
    elif zombie_pos_y >= 656: # 720 (height) - 64px (image's size skin)
        zombie_y_movement = -0.3
        zombie_pos_x += zombie_x_movement

    # we set player's skin on screen
    player(player_pos_x, player_pos_y)
    zombie(zombie_pos_x, zombie_pos_y)

    # update
    pygame.display.update()