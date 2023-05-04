import pygame
import random
from pygame.locals import *

# initialize Pygame
pygame.init()

# set up the display
# These variables define the width and height
screen_width = 500
screen_height = 450

#input sounds 

wall_sound = pygame.mixer.Sound("wall_sound.wav")
bat_sound = pygame.mixer.Sound("bat_sound.wav")


# This is my create screen function
def create_screen(screen_width, screen_height,title):
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(title)
    return screen

# Create the screen here
screen = create_screen(screen_width,screen_height,"Mia Ball Game")

# This is my press key 
def handle_keypress(event,bat_speed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            bat_speed = -10
        elif event.key == pygame.K_RIGHT:
            bat_speed = 10
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            bat_speed = 0
    return bat_speed


# set up the ball
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 20
ball_speed_y = 20
ball_color = (255, 0, 0)

#  call the same fuction 

# set up the bat
bat_width = 100
bat_height = 20
bat_x = screen_width // 2 - bat_width // 2
bat_y = screen_height - bat_height - 10
bat_speed = 0
bat_color = (0, 0, 255)

# set up the clock
clock = pygame.time.Clock()

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    bat_speed = handle_keypress(event,bat_speed)

    # move the bat
    bat_x += bat_speed
    if bat_x < 0:
        bat_x = 0
    elif bat_x > screen_width - bat_width:
        bat_x = screen_width - bat_width

    # move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # check if the ball hits the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > screen_width:
        ball_speed_x *= -1
        wall_sound.play()
    if ball_y - ball_radius < 0:
        ball_speed_y *= -1
        wall_sound.play()
    elif ball_y + ball_radius > screen_height:
        # the ball goes out of the screen, reset the game
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x = random.randint(1, 5)
        ball_speed_y = random.randint(1, 5) * -1

    # check if the ball hits the bat: this is the important part 
    if ball_y + ball_radius > bat_y and ball_x > bat_x and ball_x < bat_x + bat_width:
        ball_speed_y *= -1
        bat_sound.play()

        # make the bat move faster if the player holds down the arrow keys
        if abs(bat_speed) < 20:
            bat_speed *= 2

    # clear the screen
    screen.fill((255, 255, 255))

    # draw the ball and the bat
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, bat_color, (bat_x, bat_y, bat_width, bat_height))

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)
