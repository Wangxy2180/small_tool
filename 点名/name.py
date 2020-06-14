import pygame
import sys
from random import randint
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("随机点名")

font1 = pygame.font.Font("msyh.ttf", 100)

white = 255, 255, 255
black = 0, 0, 0

stop = True
flag = False

with open("人名.txt", "r") as f:
    lst = f.readlines()

lst = [i.strip() for i in lst]

num = lst[0]
mouse_up = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mouse_up = event.button
            flag = True

    if mouse_up == 1 and flag == True:
        stop = not stop
    flag = False
    if not stop:
        num = lst[randint(0, len(lst)-1)]
        
    screen.fill(white)
    textImage = font1.render(str(num), True, black)
    textRect = textImage.get_rect()
    textRect.center = (500,250)
    # screen.blit(textImage, (140, 180))
    screen.blit(textImage, textRect)
    pygame.display.update()
    
