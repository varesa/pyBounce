import pygame
import sys
import time

from Ball import Ball

numberOfBalls = 1

pygame.init()
screen = pygame.display.set_mode([800, 600])

balls = []

for x in range(numberOfBalls):
        balls.append(Ball())

running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        running = False

