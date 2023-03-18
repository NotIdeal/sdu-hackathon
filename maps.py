import pygame
import sys

import physics_engine
import objects
import interface

pygame.init()
width = None
height = None
display = None
clock = pygame.time.Clock()

ground = 45

d_velocity = 2.0


def init(screen):
    global width, height, display
    display = screen
    (width, height) = display.get_rect().size
    height -= ground
    interface.init(display)


def all_rest(windows, apples, blocks):
    threshold = 0.40
    for window in windows:
        if window.velocity.magnitude >= threshold:
            return False

    for apple in apples:
        if apple.velocity.magnitude >= threshold:
            return False

    for block in blocks:
        if block.velocity.magnitude >= threshold:
            return False

    return True


def close():
    pygame.quit()
    sys.exit()


class Maps:
    def __init__(self):
        self.level = 1
        self.max_level = 15
        self.color = {'background': (51, 51, 51)}
        self.score = 0

    def check_win(self, windows, apples):
        if windows == []:
            return True
        if (not windows == []) and apples == []:
            return False

    def pause(self):
        pause_text = interface.Label(600, 180, 400, 200, None, self.color['background'])
        pause_text.add_text("Ойын тоқтатылды", 80, "Fonts/Capture_it.ttf", (236, 240, 241))

        replay = interface.Button(250, 400, 500, 100, self.draw_map, (0, 255, 127), (144, 220, 144))
        replay.add_text("Қайтадан", 60, "Fonts/Capture_it.ttf", self.color['background'])

        resume = interface.Button(900, 400, 500, 100, None, (240, 100, 240), (216, 191, 216))
        resume.add_text("Жалғастыру", 60, "Fonts/Capture_it.ttf", self.color['background'])

        exit = interface.Button(650, 600, 300, 100, close, (220, 20, 60), (245, 183, 177))
        exit.add_text("Шығу", 60, "Fonts/Capture_it.ttf", self.color['background'])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_p:
                        return
                    if event.key == pygame.K_ESCAPE:
                        return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if replay.isActive():
                        replay.action()
                    if resume.isActive():
                        return
                    if exit.isActive():
                        exit.action()

            replay.draw()
            resume.draw()
            exit.draw()
            pause_text.draw()

            pygame.display.update()
            clock.tick(60)

    def draw_map(self):
        apples = []
        windows = []
        blocks = []
        walls = []
        self.score = 0
        
        ground_level = 40
        for i in range(3):
            new_apple = physics_engine.Apple(40 * i + 10 * i, height - 40, 30, None, "APPLE")
            apples.append(new_apple)

        if self.level == 0:
            windows.append(physics_engine.Window(1400, height - 40, ground_level))
        if self.level == 2:
            windows.append(physics_engine.Window(1100, height - 40, ground_level))
            windows.append(physics_engine.Window(1500, height - 40, ground_level))

            blocks.append(physics_engine.Block(1300, height - 60, 60))
        elif self.level == 3:
            windows.append(physics_engine.Window(1000, height - ground_level, 20))
            windows.append(physics_engine.Window(1400, height - ground_level, 20))

            blocks.append(physics_engine.Block(1200, height - 60, 60))
            blocks.append(physics_engine.Block(1200, height - 2 * 35, 60))
            blocks.append(physics_engine.Block(1500, height - 60, 60))
        elif self.level == 4:
            windows.append(physics_engine.Window(1200, 500 - 60, 30))
            windows.append(physics_engine.Window(1300, height - 60, 30))

            walls.append(objects.Slab(1000, 450, 500, 20))

            blocks.append(physics_engine.Block(1100, height - 100, 100))
        elif self.level == 1:
            windows.append(physics_engine.Window(1300, 500 - 60, 25))
            windows.append(physics_engine.Window(1300, height - 60, 25))

            walls.append(objects.Slab(500, 640, 100, height / 4))
            walls.append(objects.Slab(1000, 450, 500, 30))

            blocks.append(physics_engine.Block(1150, 500 - 100, 100))
            blocks.append(physics_engine.Block(1100, height - 100, 100))
        elif self.level == 6:
            apples.append(physics_engine.Apple(180, height - ground_level, 20, None, "APPLE"))

            windows.append(physics_engine.Window(1100, 500 - 60, 25))
            windows.append(physics_engine.Window(1300, 500 - 60, 25))
            windows.append(physics_engine.Window(1200, height - 60, 25))

            walls.append(objects.Slab(1200, 250, 30, 200))
            walls.append(objects.Slab(1000, 450, 500, 30))
        elif self.level == 7:
            windows.append(physics_engine.Window(1100, height - 60, 25))
            windows.append(physics_engine.Window(1200, height - 60, 25))

            walls.append(objects.Slab(700, 250, 30, height - 250))
        elif self.level == 8:
            windows.append(physics_engine.Window(1100, height - 60, 25))
            windows.append(physics_engine.Window(1450, height - 60, 25))

            blocks.append(physics_engine.Block(1250, height - 100, 100))
            blocks.append(physics_engine.Block(1250, height - 2 * 60, 100))

            walls.append(objects.Slab(700, 400, 30, height - 400))
        elif self.level == 9:
            windows.append(physics_engine.Window(1100, height - 60, 25))
            windows.append(physics_engine.Window(1450, height - 60, 25))

            blocks.append(physics_engine.Block(1250, height - 100, 100))
            blocks.append(physics_engine.Block(1250, height - 2 * 60, 100))
            blocks.append(physics_engine.Block(900, height - 100, 100))

            walls.append(objects.Slab(900, 400, 500, 30))

        self.start_level(apples, windows, blocks, walls)
    def replay_level(self):
        self.level -= 1
        self.draw_map()

    def start_again(self):
        self.level = 1
        self.draw_map()

    def level_cleared(self):
        self.level += 1

        level_cleared_text = interface.Label(600, 180, 400, 200, None, self.color['background'])
        if self.level <= self.max_level:
            level_cleared_text.add_text("Деңгей " + str(self.level - 1) + " өтілді!", 80, "Fonts/Capture_it.ttf",
                                        (236, 240, 241))
        else:
            level_cleared_text.add_text("Барлық деңгей өтілді!", 80, "Fonts/Capture_it.ttf", (236, 240, 241))

        score_text = interface.Label(650, 350, 300, 100, None, self.color['background'])
        score_text.add_text("Ұпай: " + str(self.score), 55, "Fonts/Capture_it.ttf", (236, 240, 241))

        replay = interface.Button(250, 500, 500, 100, self.replay_level, (0, 255, 127), (144, 220, 144))
        replay.add_text("Қайтадан", 60, "Fonts/Capture_it.ttf", self.color['background'])

        if self.level <= self.max_level:
            next = interface.Button(900, 500, 500, 100, self.draw_map, (240, 100, 240), (216, 191, 216))
            next.add_text("Жалғастыру", 60, "Fonts/Capture_it.ttf", self.color['background'])
        else:
            next = interface.Button(900, 500, 500, 100, self.start_again, (0, 255, 127), (144, 220, 144))
            next.add_text("Басынан", 60, "Fonts/Capture_it.ttf", self.color['background'])

        exit = interface.Button(650, 700, 300, 100, close, (220, 20, 60), (245, 183, 177))
        exit.add_text("Шығу", 60, "Fonts/Capture_it.ttf", self.color['background'])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if replay.isActive():
                        replay.action()
                    if next.isActive():
                        next.action()
                    if exit.isActive():
                        exit.action()

            replay.draw()
            next.draw()
            exit.draw()
            level_cleared_text.draw()
            score_text.draw()

            pygame.display.update()
            clock.tick(60)

    def level_failed(self):
        level_failed_text = interface.Label(600, 180, 400, 200, None, self.color['background'])
        level_failed_text.add_text("Деңғей өтілмеді!", 80, "Fonts/Capture_it.ttf", (236, 240, 241))

        score_text = interface.Label(650, 350, 300, 100, None, self.color['background'])
        score_text.add_text("ҰПАЙ: " + str(self.score), 55, "Fonts/Capture_it.ttf", (236, 240, 241))

        replay = interface.Button(250, 500, 500, 100, self.draw_map, (0, 255, 127), (144, 220, 144))
        replay.add_text("Қайтадан", 60, "Fonts/Capture_it.ttf", self.color['background'])

        exit = interface.Button(900, 500, 500, 100, close, (220, 20, 60), (245, 183, 177))
        exit.add_text("Шығу", 60, "Fonts/Capture_it.ttf", self.color['background'])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if replay.isActive():
                        replay.action()
                    if exit.isActive():
                        exit.action()

            replay.draw()
            exit.draw()
            level_failed_text.draw()
            score_text.draw()

            pygame.display.update()
            clock.tick(60)

    def start_level(self, apples, windows, blocks, walls):
        slingshot = physics_engine.Slingshot(250, height - 200, 30, 200)

        apples[0].load(slingshot)

        mouse_click = False
        flag = 1

        windows_to_remove = []
        blocks_to_remove = []

        score_text = interface.Label(283, 50, 200, 50, None, self.color['background'])
        score_text.add_text("ҰПАЙ : " + str(self.score), 40, "Fonts/Capture_it.ttf", (236, 240, 241))

        apples_remaining = interface.Label(201, 110, 100, 50, None, self.color['background'])
        apples_remaining.add_text("Қалған алмалар : " + str(len(apples)), 40, "Fonts/Capture_it.ttf", (236, 240, 241))

        windows_remaining = interface.Label(199, 170, 100, 50, None, self.color['background'])
        windows_remaining.add_text("Қалған терезелер : " + str(len(windows)), 40, "Fonts/Capture_it.ttf",
                                   (236, 240, 241))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if apples[0].mouse_selected():
                        mouse_click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click = False
                    if apples[0].mouse_selected():
                        flag = 0

            if (not apples[0].loaded) and all_rest(windows, apples, blocks):
                apples.pop(0)
                if self.check_win(windows, apples) == 1:
                    self.score += len(apples) * 100
                    self.level_cleared()
                elif self.check_win(windows, apples) == 0:
                    self.level_failed()

                if not apples == []:
                    apples[0].load(slingshot)
                flag = 1

            if mouse_click:
                apples[0].reposition(slingshot, mouse_click)

            if not flag:
                apples[0].unload()

            # display.fill(self.color['background'])
            color = self.color['background']
            for i in range(3):
                color = (color[0] + 5, color[1] + 5, color[2] + 5)
                pygame.draw.rect(display, color, (0, i * 300, width, 300))

            pygame.draw.rect(display, (77, 86, 86), (0, height, width, 50))

            slingshot.draw(apples[0])

            for i in range(len(windows)):
                for j in range(len(blocks)):
                    pig_v, block_v = windows[i].velocity.magnitude, blocks[j].velocity.magnitude
                    windows[i], blocks[j], result_block_pig = physics_engine.collision_handler(windows[i], blocks[j],
                                                                                               "BALL_N_BLOCK")
                    pig_v1, block_v1 = windows[i].velocity.magnitude, blocks[j].velocity.magnitude

                    if result_block_pig:
                        if abs(pig_v - pig_v1) > d_velocity:
                            blocks_to_remove.append(blocks[j])
                            blocks[j].destroy()
                        if abs(block_v - block_v1) > d_velocity:
                            windows_to_remove.append(windows[i])
                            windows[i].dead()

            for i in range(len(apples)):
                if not (apples[i].loaded or apples[i].velocity.magnitude == 0):
                    for j in range(len(blocks)):
                        apples_v, block_v = apples[i].velocity.magnitude, blocks[j].velocity.magnitude
                        apples[i], blocks[j], result_bird_block = physics_engine.collision_handler(apples[i], blocks[j],
                                                                                                   "BALL_N_BLOCK")
                        apples_v1, block_v1 = apples[i].velocity.magnitude, blocks[j].velocity.magnitude

                        if result_bird_block:
                            if abs(apples_v - apples_v1) > d_velocity:
                                if not blocks[j] in blocks_to_remove:
                                    blocks_to_remove.append(blocks[j])
                                    blocks[j].destroy()

            for i in range(len(windows)):
                windows[i].move()
                for j in range(i + 1, len(windows)):
                    pig1_v, pig2_v = windows[i].velocity.magnitude, windows[j].velocity.magnitude
                    windows[i], windows[j], result = physics_engine.collision_handler(windows[i], windows[j], "BALL")
                    pig1_v1, pig2_v1 = windows[i].velocity.magnitude, windows[j].velocity.magnitude
                    result = True
                    if result:
                        if abs(pig1_v - pig1_v1) > d_velocity:
                            if not windows[j] in windows_to_remove:
                                windows_to_remove.append(windows[j])
                                windows[j].dead()
                        if abs(pig2_v - pig2_v1) > d_velocity:
                            if not windows[i] in windows_to_remove:
                                windows_to_remove.append(windows[i])
                                windows[i].dead()

                for wall in walls:
                    windows[i] = wall.collision_manager(windows[i])

                windows[i].draw()

            for i in range(len(apples)):
                if (not apples[i].loaded) and apples[i].velocity.magnitude:
                    apples[0].move()
                    for j in range(len(windows)):
                        bird_v, pig_v = apples[i].velocity.magnitude, windows[j].velocity.magnitude
                        apples[i], windows[j], result_bird_pig = physics_engine.collision_handler(apples[i], windows[j],
                                                                                                  "BALL")
                        bird_v1, pig_v1 = apples[i].velocity.magnitude, windows[j].velocity.magnitude
                        result = True
                        if result_bird_pig:
                            if abs(bird_v - bird_v1) > d_velocity:
                                if not windows[j] in windows_to_remove:
                                    windows_to_remove.append(windows[j])
                                    windows[j].dead()

                if apples[i].loaded:
                    apples[i].project_path()

                for wall in walls:
                    apples[i] = wall.collision_manager(apples[i])

                apples[i].draw()

            for i in range(len(blocks)):
                for j in range(i + 1, len(blocks)):
                    block1_v, block2_v = blocks[i].velocity.magnitude, blocks[j].velocity.magnitude
                    blocks[i], blocks[j], result_block = physics_engine.block_collision_handler(blocks[i], blocks[j])
                    block1_v1, block2_v1 = blocks[i].velocity.magnitude, blocks[j].velocity.magnitude

                    if result_block:
                        if abs(block1_v - block1_v1) > d_velocity:
                            if not blocks[j] in blocks_to_remove:
                                blocks_to_remove.append(blocks[j])
                                blocks[j].destroy()
                        if abs(block2_v - block2_v1) > d_velocity:
                            if not blocks[i] in blocks_to_remove:
                                blocks_to_remove.append(blocks[i])
                                blocks[i].destroy()

                blocks[i].move()

                for wall in walls:
                    blocks[i] = wall.collision_manager(blocks[i], "BLOCK")

                blocks[i].draw()

            for wall in walls:
                wall.draw()

            score_text.add_text("ҰПАЙ : " + str(self.score), 40, "Fonts/Capture_it.ttf", (236, 240, 241))
            score_text.draw()

            apples_remaining.add_text("Қалған алмалар : " + str(len(apples)), 40, "Fonts/Capture_it.ttf",
                                      (236, 240, 241))
            apples_remaining.draw()

            windows_remaining.add_text("Қалған терезелер : " + str(len(windows)), 40, "Fonts/Capture_it.ttf",
                                       (236, 240, 241))
            windows_remaining.draw()

            pygame.display.update()

            if all_rest(windows, apples, blocks):
                for pig in windows_to_remove:
                    if pig in windows:
                        windows.remove(pig)
                        self.score += 100

                for block in blocks_to_remove:
                    if block in blocks:
                        blocks.remove(block)
                        self.score += 50

                windows_to_remove = []
                blocks_to_remove = []

            clock.tick(60)
