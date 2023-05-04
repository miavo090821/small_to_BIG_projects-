import sys 
import pygame 
import random
from pygame.locals import *
pygame.init()

size = width, height = 320, 240
speed = [2,2]
screen = pygame.display.set_mode(size)
# ballrect = pygame.draw.circle(screen, "blue", [50,50],30,0)

red = 255
green = 255
blue = 255
color = (red, green, blue)
ball_width = 200
ball_height =100

#direction = 'right_down'

directions = ['right_down','right_up','left_up', 'left_down']
a = random.randrange(0, len(directions))
direction = directions[a]
ballrect = pygame.Surface((160, 160), SRCALPHA)
pygame.draw.circle(ballrect, color, [30, 30], 30, 0)
screen.blit(ballrect, (ball_width, ball_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #maths
    red = red - 1 
    colour = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    if red == 0:
        red = 255

    #draw
    pygame.draw.circle(ballrect,colour, [30,30], 30, 0)
    screen.fill((0,0,255))
    screen.blit(ballrect, (ball_width, ball_height))
    
    if direction == 'right_down':
        if ball_height == height - 60 and ball_width < width - 60:
            ball_width += 2
            ball_height -= 2
            direction == 'right_up'
        elif ball_width == width - 60 and ball_height < height - 60:
            ball_width -= 2
            ball_height += 2
            direction == 'left_down'
        elif ball_width == width - 60 and ball_height == height - 60:
            ball_width -= 2
            ball_height -= 2
            direction == 'left_up'
        else:
            ball_width += 2
            ball_height += 2
    if direction == 'right_up':
        if ball_height > 0 and ball_width == width - 60:     
            ball_width -= 2
            ball_height -= 2
            direction = 'left_up'
        if ball_height == 0 and ball_width > 0:      
            ball_width += 2
            ball_height += 2
            direction = 'right_down'
        if ball_width == width - 60 and ball_height == 0:
            ball_width -= 2
            ball_height += 2
            direction = 'left_down'
        else:
            ball_width += 2
            ball_height -= 2
    if direction == 'left_up':
        if ball_width == 0 and ball_height > 0:      
            ball_width += 2
            ball_height -= 2
            direction = 'right_up'
        if ball_width > 0 and ball_height == 0:      
            ball_width -= 2
            ball_height += 2
            direction = 'left_down'
        if ball_width == 0 and ball_height == 0:
            ball_width += 2
            ball_height += 2
            direction = 'right_down'
        else:
            ball_width -= 2
            ball_height -= 2
    if direction == 'left_down':
        if ball_width == 0 and ball_height > 0:      
            ball_width += 2
            ball_height += 2
            direction = 'right_down'
        if ball_width > 0 and ball_height == height - 60:      
            ball_width -= 2
            ball_height -= 2
            direction = 'left_up'
        if ball_width == 0 and ball_height == height - 60:
            ball_width += 2
            ball_height -= 2
            direction = 'right_up'
        else:
            ball_width -= 2
            ball_height += 2

        
    pygame.display.update()
    pygame.time.wait(32) 

