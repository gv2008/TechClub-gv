# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:43:03 2021

@author: Geeta
"""

import pygame
import sys
import random
from pygame.locals import *
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((600,600))
cell1 = pygame.image.load("cell1.png").convert()
cell2 = pygame.image.load("cell2.png").convert()
array = [cell1,cell2]
x = 0
y = 0
for b in range(8):
 for a in range(8):
  screen.blit(random.choice(array),(x,y))
  x = x+75
 x = 0
 y = y+75

pygame.display.update()
while True:
 for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()