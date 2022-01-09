import pygame
import os
import Hero
import Level
import Background
import sys
import Chest
import Door


def load_image(name, size_of_sprite=None, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if size_of_sprite:
        image = pygame.transform.scale(image, (size_of_sprite[0], size_of_sprite[1]))
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((2, 2))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def shadow():
    pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect((0, 0), (hero.rect.x - 75, 720)))
    pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect((0, 0), (1280, hero.rect.y - 75)))
    pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect((hero.rect.x + hero.rect.w + 25, 0), (1280, 720)))
    pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect((0, hero.rect.y + hero.rect.h + 75), (1280, 720)))


class Lobby:
    global HEIGHT, SIZE, FPS

    def __init__(self):
        self.bg = load_image('lobby_bg.png', SIZE)
        self.logo = load_image('Logo.png')
        self.current_button = None
        self.disclaimer_update()
        self.cycle()

    def cycle(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # button push
                    pos = event.pos
                    if 40 <= pos[0] <= 330:
                        if HEIGHT * 0.35 <= pos[1] <= HEIGHT * 0.35 + 55:
                            self.ent_update()
                            return
                        elif HEIGHT * 0.35 + 55 + 20 <= pos[1] <= HEIGHT * 0.35 + 2 * 55 + 2 * 20:
                            quit()
                elif event.type == pygame.MOUSEMOTION:
                    pos = event.pos
                    if 40 <= pos[0] <= 330:
                        if HEIGHT * 0.35 <= pos[1] <= HEIGHT * 0.35 + 55:
                            self.current_button = 1
                        elif HEIGHT * 0.35 + 55 + 20 <= pos[1] <= HEIGHT * 0.35 + 2 * 55 + 2 * 20:
                            self.current_button = 2
                        else:
                            self.current_button = None
                    else:
                        self.current_button = None

            self.update_window(self.current_button)
            pygame.display.flip()
            clock.tick(FPS)

    def update_window(self, current_button=None):  # rendering
        screen.blit(self.bg, (0, 0))
        screen.blit(self.logo, (WIDTH * 0.35, HEIGHT * 0.45))
        font = pygame.font.SysFont('Arialms', 80)

        with open(f'data/buttons.txt', 'r', encoding='utf-8') as f:
            self.buttons = map(lambda x: x.rstrip(), f.readlines())

        self.text_coord = HEIGHT * 0.35
        button = 1
        for line in self.buttons:
            if current_button == button:
                string_rendered = font.render(line, True, pygame.Color('#fe0002'))
                current_button = None
            else:
                string_rendered = font.render(line, True, pygame.Color('#980002'))
            self.buttons = string_rendered.get_rect()
            self.text_coord += 20
            self.buttons.top = self.text_coord
            self.buttons.x = 40
            self.text_coord += self.buttons.height
            screen.blit(string_rendered, self.buttons)
            button += 1

    def disclaimer_update(self):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Arialms', 40)
        font1 = pygame.font.SysFont('Arialms', 60)

        with open('data/disclaimer.txt', 'r', encoding='utf-8') as f:
            text = map(lambda x: x.rstrip(), f.readlines())

        screen.blit(font1.render('Дисклеймер', True, pygame.Color('#980002')), (WIDTH * 0.4, HEIGHT * 0.2))

        self.text_coord = HEIGHT * 0.3
        for line in text:
            string_rendered = font.render(line, True, pygame.Color('#980002'))
            text = string_rendered.get_rect()
            self.text_coord += 10
            text.top = self.text_coord
            text.x = WIDTH * 0.2
            self.text_coord += text.height
            screen.blit(string_rendered, text)

        screen.blit(font.render('Нажмите "Пробел", чтобы продолжить', True, pygame.Color('#980002')),
                    (WIDTH * 0.3, HEIGHT * 0.6))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            pygame.display.flip()
            clock.tick(FPS)

    def ent_update(self):
        font = pygame.font.SysFont('Arialms', 40)
        screen.fill((0, 0, 0))
        photo = load_image('strange.png')
        screen.blit(photo, (30, HEIGHT * 0.1))

        with open('data/strange_text.txt', 'r', encoding='utf-8') as f:
            text = map(lambda x: x.rstrip(), f.readlines())

        self.text_coord = HEIGHT * 0.3
        for line in text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            text = string_rendered.get_rect()
            self.text_coord += 10
            text.top = self.text_coord
            text.x = WIDTH * 0.35
            self.text_coord += text.height
            screen.blit(string_rendered, text)

        screen.blit(font.render('Продолжить', True, pygame.Color('#980002')),
                    (WIDTH * 0.8, HEIGHT * 0.9))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # button push
                    pos = event.pos
                    if HEIGHT * 0.9 <= pos[1] <= HEIGHT and WIDTH * 0.8 <= pos[0] <= WIDTH * 0.95:
                        return
            pygame.display.flip()
            clock.tick(FPS)

    def quit(self):
        pygame.quit()
        sys.exit()


FPS = 60
running = True
pygame.init()
SIZE = WIDTH, HEIGHT = 1280, 720
bg = []
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
lobby = Lobby()
font = pygame.font.SysFont('Arialms', 30)
text = font.render('У вас есть ключ', True, pygame.Color('Yellow'))
all_sprites = pygame.sprite.Group()
collision = pygame.sprite.Group()
chests = pygame.sprite.Group()
door_sg = pygame.sprite.Group()
chests_list = []
bg.append(Background.Bg(load_image('Background.png'), (0, 0), all_sprites))
bg.append(Background.Bg(load_image('Background.png'), (677, 0), all_sprites))
bg.append(Background.Bg(load_image('Background.png'), (0, 320), all_sprites))
bg.append(Background.Bg(load_image('Background.png'), (677, 320), all_sprites))
bg.append(Background.Bg(load_image('Background.png'), (0, 640), all_sprites))
bg.append(Background.Bg(load_image('Background.png'), (677, 640), all_sprites))
chests_list.append(Chest.Chest([load_image('Chest.png', (80, 65)), load_image('Chest_open.png', (50, 40))], [530, 430], 0, all_sprites, chests))
chests_list.append(Chest.Chest([load_image('Chest.png', (80, 65)), load_image('Chest_open.png', (50, 40))], [850, 410], 0, all_sprites, chests))
chests_list.append(Chest.Chest([load_image('Chest.png', (80, 65)), load_image('Chest_open.png', (50, 40))], [930, 50], 1, all_sprites, chests))
chests_list.append(Chest.Chest([load_image('Chest.png', (80, 65)), load_image('Chest_open.png', (50, 40))], [200, 380], 0, all_sprites, chests))
door = Door.Door(load_image('door.png', (64, 45)), [950, 600], all_sprites, door_sg)
lvl = Level.Level(
    [load_image('lab2.png', (1280, 720), -1), load_image('lab1.png', (1280, 720)), load_image('lab3.png', (1280, 720), -1)],
    chests_list, door, all_sprites, collision)
hero = Hero.Hero(load_image('Hero_sheet.png'), [85, 85], 10, 8, collision, chests, door, lvl, all_sprites)
lvl.next_level()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or \
                    event.key == pygame.K_d:
                hero.update(event, 'move')
    screen.fill(pygame.Color('white'))
    all_sprites.update()
    all_sprites.draw(screen)
    # shadow()
    if hero.key:
        screen.blit(text, (30, 30))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
