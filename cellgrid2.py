# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:31:34 2021

@author: Geeta
"""

import pygame
import sys
import random
from pygame.locals import *
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((600,600))
wall1 = pygame.image.load("wall1.png").convert()
wall2 = pygame.image.load("wall2.png").convert()
wall3 = pygame.image.load("wall3.png").convert()
wall4 = pygame.image.load("wall4.png").convert()

array = [wall1,wall2,wall3,wall4]
x = 0
y = 0
for b in range(8):
 for a in range(8):
  screen.blit(random.choice(array),(x,y))
  x = x+150
 x = 0
 y = y+150

pygame.display.update()
while True:
 for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()