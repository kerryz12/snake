# Snake game remake
# Author: Kerry Zhang

import sys
import pygame
import time
import random
from pygame.locals import *

random.seed()
#The number of pixels the snake moves in one "tick"
PIXELS_PER_TICK = 50
#The amount of time which passes before the snake moves again (will actually be longer)
TICK_TIME = 0.1

def main():
    pygame.init()

    window_size = width, height = 800, 800
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Snake")

    font = pygame.font.SysFont("Times New Roman", 64)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)

    food = pygame.image.load("food.gif")
    score = 0

    replace = pygame.image.load("replace.gif")

    food_location = x, y = random.randrange(2, 14) * 50, random.randrange(2, 14) * 50
    screen.blit(food, food_location)
    foodrect = food.get_rect()
    foodrect = foodrect.move(food_location)
    pygame.display.flip()
    food_collected = 0

    speed = [PIXELS_PER_TICK, 0]
    snakepos_x = [0]
    snakepos_y = [0]
    length = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    speed = [0,-PIXELS_PER_TICK]
                elif event.key == pygame.K_a:
                    speed = [-PIXELS_PER_TICK,0]
                elif event.key == pygame.K_s:
                    speed = [0,PIXELS_PER_TICK]
                elif event.key == pygame.K_d:
                    speed = [PIXELS_PER_TICK,0]

        screen.fill(black)
        for i in range(length - 1, -1, -1):
            if i == 0:
                snakepos_x[0] += speed[0]
                snakepos_y[0] += speed[1]
            else:
                snakepos_x[i] = snakepos_x[i - 1]
                snakepos_y[i] = snakepos_y[i - 1]
            pygame.draw.rect(screen, green, [snakepos_x[i] + 1, snakepos_y[i] + 1, 48, 48])
        pygame.display.flip()

        if snakepos_x[0] < 0 or snakepos_x[0] > 800 or snakepos_y[0] < 0 or snakepos_y[0] > 800:
            speed = [0, 0]
            screen.blit(font.render('You lost!', True, white, black),(300,300))
            screen.blit(font.render('Score: {}'.format(score), True, white, black), (300, 400))
            pygame.display.flip()
            time.sleep(1)
            sys.exit()

        if snakepos_x[0] == x and snakepos_y[0] == y:
            food_collected = 1
            screen.fill(black)
            for i in range(length - 1, -1, -1):
                pygame.draw.rect(screen, green, [snakepos_x[i] + 1, snakepos_y[i] + 1, 48, 48])
            screen.blit(replace,foodrect)
            pygame.display.flip()
            snakepos_x.append(0)
            snakepos_y.append(0)
            length += 1

        for a in range(1,length,1):
            if snakepos_x[0] == snakepos_x[a] and snakepos_y[0] == snakepos_y[a]:
                speed = [0, 0]
                screen.blit(font.render('You lost!', True, white, black),(300,300))
                screen.blit(font.render('Score: {}'.format(score), True, white, black), (300, 400))
                pygame.display.flip()
                time.sleep(1)
                sys.exit()

        if food_collected == 1:
            food_location = x, y = random.randrange(1, 15) * 50, random.randrange(1, 15) * 50
            for b in range(length):
                while x == snakepos_x[b] and y == snakepos_y[b]:
                    food_location = x, y = random.randrange(1, 15) * 50, random.randrange(1, 15) * 50
                    b = 0
            screen.blit(food, food_location)
            foodrect = food.get_rect()
            foodrect = foodrect.move(food_location)
            pygame.display.flip()
            food_collected = 0
            score += 1
        else:
            screen.blit(food, food_location)
            pygame.display.flip()

        time.sleep(TICK_TIME)

main()
