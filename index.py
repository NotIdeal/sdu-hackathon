import pygame
import sys
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

def start_level(apples):
    map = maps.Maps(apples)
    map.draw_map()
def start_game():
    welcome = interface.Label(600, 180, 400, 200, None, background)
    welcome.add_text("Қиындықты таңдаңыз", 80, "Fonts/Capture_it.ttf", (236, 240, 241))

    ez = interface.Button(200, 400, 300, 150, start_level, (0, 255, 127), (144, 220, 144))
    ez.add_text("Оңай", 60, "Fonts/Capture_it.ttf", background)

    medium = interface.Button(600, 400, 300, 150, start_level, (240, 100, 240), (216, 191, 216))
    medium.add_text("Орташа", 60, "Fonts/Capture_it.ttf", background)

    hard = interface.Button(1000, 400, 300, 150, start_level, (220, 20, 60), (245, 183, 177))
    hard.add_text("Қиын", 60, "Fonts/Capture_it.ttf", background)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ez.isActive():
                    start_level(4)
                if medium.isActive():
                    start_level(3)
                if hard.isActive():
                    start_level(2)


        display.fill((51, 51, 51))
        welcome.draw()
        ez.draw()
        medium.draw()
        hard.draw()

        pygame.display.update()
        clock.tick(60)


def show_intro():
    welcome = interface.Label(600, 40, 400, 200, None, background)
    welcome.add_text("Беймарал Айғырдың Оқиғасы", 60, "Fonts/Capture_it.ttf", (236, 240, 241))

    texts = []
    part1 = interface.Label(600, 400, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part1.add_text("Кезінде диді, Беймарал Айғыр деген диді, бір жігіт бопты диді.", 30, "Fonts/Capture_it.ttf", (236, 240, 241))

    part2 = interface.Label(600, 450, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part2.add_text("Ол диді, Сарқан деген қалада тұрыпты диді, сонда өмір сүріпті диді.", 30, "Fonts/Capture_it.ttf",
                   (236, 240, 241))

    part3 = interface.Label(600, 500, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part3.add_text("Оған диді, ол кездері диді, Орыстар ұнамайды екен диді.", 30, "Fonts/Capture_it.ttf",
                   (236, 240, 241))

    part4 = interface.Label(600, 550, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part4.add_text("Сүйтіп диді, ол кішкентай алмаларды диді, солардың терезесіне атып ойнайды екен диді.", 30, "Fonts/Capture_it.ttf",
                   (236, 240, 241))

    part5 = interface.Label(600, 600, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part5.add_text("Солай диді, көңілін диді, көтереді екен диді.", 30, "Fonts/Capture_it.ttf",
                   (236, 240, 241))

    part6 = interface.Label(600, 650, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part6.add_text("Қазір диді, ол пенсияға кетіп диді, орнына сені орынбасар қылып кетті диді.", 30, "Fonts/Capture_it.ttf",
                   (236, 240, 241))

    part7 = interface.Label(600, 700, 400, 150, None, (0, 255, 127), (144, 220, 144))
    part7.add_text("Енді диді, осы ойында диді, айғырсың ба әлде маймылсың ба дәлелде диді!!!", 30, "Fonts/Capture_it.ttf",
                   (236, 240, 241))






    texts.append(part1)
    texts.append(part2)
    texts.append(part3)
    texts.append(part4)
    texts.append(part5)
    texts.append(part6)
    texts.append(part7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        display.fill((51, 51, 51))

        aigyr = pygame.image.load("Images/aigyr.png")
        display.blit(aigyr, (650, 180))


        welcome.draw()

        for text in texts:
            text.draw()

        pygame.display.update()
        clock.tick(60)


def GAME():
    welcome = interface.Label(600, 180, 400, 200, None, background)
    welcome.add_text("Беймарал Айғыр Ойыны", 80, "Fonts/Capture_it.ttf", (236, 240, 241))

    start = interface.Button(300, 400, 400, 150, start_game, (0, 255, 127), (144, 220, 144))
    start.add_text("Бастау", 60, "Fonts/Capture_it.ttf", background)

    exit = interface.Button(900, 400, 400, 150, close, (220, 20, 60), (245, 183, 177))
    exit.add_text("Шығу", 60, "Fonts/Capture_it.ttf", background)

    story = interface.Button(600, 600, 400, 150, show_intro, (240, 100, 240), (216, 191, 216))
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
                    start_game()
                if story.isActive():
                    show_intro()

        display.fill(background)

        start.draw()
        exit.draw()
        story.draw()
        welcome.draw()

        pygame.display.update()
        clock.tick(60)


GAME()
