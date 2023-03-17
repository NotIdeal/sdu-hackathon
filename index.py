import pygame
import sys
import random
from math import *
import physics_engine
import objects
import maps
import interface

pygame.init()
pygame.display.set_caption('Beimaral Aigyr CITY')
width = 1600
height = 900
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

physics_engine.init(display)
objects.init(display)
maps.init(display)
interface.init(display)

background = (51, 51, 51)

def close():
    pygame.quit()
    sys.exit()

def start_game(map):
    map.draw_map()

def show_into():
    pass

def GAME():
    map = maps.Maps()

    welcome = interface.Label(600, 180, 400, 200, None, background)
    welcome.add_text("Беймарал Айғыр Ойыны", 80, "Fonts/Capture_it.ttf", (236, 240, 241))

    start = interface.Button(300, 400, 400, 150, start_game, (0, 255, 127), (144, 220, 144))
    start.add_text("Бастау", 60, "Fonts/Capture_it.ttf", background)

    exit = interface.Button(900, 400, 400, 150, close, (220, 20, 60), (245, 183, 177))
    exit.add_text("Шығу", 60, "Fonts/Capture_it.ttf", background)

    story = interface.Button(600, 600, 400, 150, show_into, (240, 100, 240), (216, 191, 216))
    story.add_text("Кіріспе", 60, "Fonts/Capture_it.ttf", background)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.isActive():
                    exit.action()
                if start.isActive():
                    start_game(map)

        display.fill(background)

        start.draw()
        exit.draw()
        story.draw()
        welcome.draw()

        pygame.display.update()
        clock.tick(60)

GAME()
