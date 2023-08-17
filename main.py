import pygame
import random
import math

# starts pygame
pygame.init()

# screen size
screen = pygame.display.set_mode((800, 600)) #800 width, 600 height original

# títle and icon
pygame.display.set_caption("Zombie Invasion")
icon = pygame.image.load("img/skullLogo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("img/background.jpg")

# player
img_player = pygame.image.load("img/player.png")
player_pos_x = 368 # screen width / 2 - 32 (image's size 64px/2)
player_pos_y = 500 # screen width / 2 - 32 (image's size 64px/2)
player_movement = 0

# zombies
img_zombie = []
zombie_pos_x = []
zombie_pos_y = []
zombie_x_movement = []
zombie_y_movement = []

img_zombie = pygame.image.load("img/zombie.png")
zombie_pos_x = random.randint(0, 736) # screen width / 2 - 32 (image's size 64px/2)
zombie_pos_y = random.randint(50, 200) # screen height / 2 - 32 (image's size 64px/2)
zombie_x_movement = 0.3 # zombie speed
zombie_y_movement = 10 # zombie speed at getting close

# bullets
img_bullet = pygame.image.load("img/bullet.png")
bullet_pos_x = 0
bullet_pos_y = 500 # screen width / 2 - 32 (image's size 64px/2)
bullet_x_movement = 0
bullet_y_movement = 0.4 # bullet speed
bullet_visible = False

# var to check if screen's player is opened/closed
is_executed = True

#score
score = 0

# function to draw player's skin in his position X and Y
def player(x, y):
    screen.blit(img_player, (x, y))

# function to draw zombie's skin in his position X and Y
def zombie(x, y):
    screen.blit(img_zombie, (x, y))

# function to draw bullets
def shoot_bullets(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(img_bullet, (x + 16, y + 10))  # adjust bullet's position

# function to detect collisions
def is_colission(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False

while is_executed:
    # background screen's image
    screen.blit(background, (0, 0))

    # check if user closes the window
    # screen will be shown while 'is_executed' is True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_executed = False

        # check if player keep pressed KEYs left / right and his movement speed 4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_movement = -1
            if event.key == pygame.K_RIGHT:
                player_movement = 1
            if event.key == pygame.K_SPACE: # shoot key
                if bullet_visible == False:
                    bullet_pos_x = player_pos_x
                    shoot_bullets(bullet_pos_x, bullet_pos_y)

        # check if player is NOT pressing any key then reset player movement's to 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_movement = 0

    # set player position depending on player_movement's var value
    player_pos_x += player_movement

    # keep player inside borders
    if player_pos_x <= 0:
        player_pos_x = 0
    elif player_pos_x >= 736: # 720 (height) - 64px (image's size skin)
        player_pos_x = 736

    # set zombie position depending on zombie_y_movement's var value
    zombie_pos_x += zombie_x_movement

    # keep zombies inside borders
    if zombie_pos_x <= 0:
        zombie_x_movement = 0.3
        zombie_pos_y += zombie_y_movement
    elif zombie_pos_x >= 656: # 720 (height) - 64px (image's size skin)
        zombie_x_movement = -0.3
        zombie_pos_y += zombie_y_movement

    # reset shooting once bullet get out of screen
    if bullet_pos_y <= -64:
        bullet_pos_y = 500
        bullet_visible = False

    # bullet direction once shot
    if bullet_visible:
        shoot_bullets(bullet_pos_x, bullet_pos_y)
        bullet_pos_y -= bullet_y_movement

    # check if exist colission between bullets and zombies
    colission = is_colission(zombie_pos_x, zombie_pos_y, bullet_pos_x, bullet_pos_y)
    if colission:
        bullet_pos_y = 500
        bullet_visible = False
        score += 1
        print(score)
        zombie_pos_x = random.randint(0, 736)  # screen width / 2 - 32 (image's size 64px/2)
        zombie_pos_y = random.randint(50, 200)  # screen height / 2 - 32 (image's size 64px/2)

    # we set player's and zombie skin on screen
    player(player_pos_x, player_pos_y)
    zombie(zombie_pos_x, zombie_pos_y)

    # update
    pygame.display.update()
