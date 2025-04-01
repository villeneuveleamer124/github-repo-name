import pygame
from pygame import *
from time import sleep
pygame.init()

screen = display.set_mode((800, 600))
clock = time.Clock()
game_font = pygame.font.Font("freesan.ttf", 35)
text_surface = game_font.render("Hello, World!", True, (255, 255, 255))

while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (100, 100))
    display.update()
