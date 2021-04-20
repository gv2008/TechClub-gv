# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:53:22 2021

@author: Geeta
"""

import pygame
import sys
from pygame.locals import *
#clock = pygame.time.Clock()
          
import time
pygame.init()
pygame.display.init()

def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Blitting an image over another image")
bgd = pygame.image.load("plainorangebackground.png").convert()
image1 = pygame.image.load("player1.png").convert()


x = 0
y = 0
while True:
    screen.blit(bgd,(0,0))
    screen.blit(image1,(x,y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                x -= 50
                screen.blit(bgd,(0,0))   
                screen.blit(image1,(x,y))
                pygame.display.update()
                time.sleep(0.5)
            if event.key == K_RIGHT:
                x = x+50
                screen.blit(bgd,(0,0))   
                screen.blit(image1,(x,y))
                pygame.display.update()
                time.sleep(0.5)
            if event.key == K_UP:
                y-= 50
                screen.blit(bgd,(0,0))
                screen.blit(image1,(x,y))
                pygame.display.update()
                time.sleep(0.5)
            if event.key == K_DOWN:
                y+= 50
                screen.blit(bgd,(0,0))
                screen.blit(image1,(x,y))
                pygame.display.update()
                time.sleep(0.5)
    events()
                
            
