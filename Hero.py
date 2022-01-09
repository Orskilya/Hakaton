import pygame
fps = 60


class Hero(pygame.sprite.Sprite):
    def __init__(self, sheet, coord, columns, rows, collision_objects, chests, door, level, *group):
        super().__init__(*group)
        self.coord = coord  # list
        self.keys = []
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.cur_row = 0
        self.image = self.frames[0][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.coord
        self.count = 0
        self.images_speed = 10
        self.speed = 150
        self.size = (self.rect.w * 0.6, self.rect.h * 0.6)
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.mask = pygame.mask.from_surface(self.image)
        self.collision_objects = collision_objects
        self.move = (0, 0)
        self.key = False
        self.collision_chests = chests
        self.door = door
        self.level = level

    def fly(self, key=None, par=None):
        if par == 'go':
            if key in [pygame.K_s, pygame.K_w, pygame.K_a, pygame.K_d]:
                self.keys.append(key)
        elif par == 'stop':
            del self.keys[self.keys.index(key)]
        if pygame.K_s in self.keys:
            self.coord[1] += self.speed // fps
            self.move = (-(self.speed // fps), 1)
        elif pygame.K_w in self.keys:
            self.coord[1] -= self.speed // fps
            self.move = (self.speed // fps, 1)
        elif pygame.K_a in self.keys:
            self.coord[0] -= self.speed // fps
            self.move = (self.speed // fps, 0)
        elif pygame.K_d in self.keys:
            self.coord[0] += self.speed // fps
            self.move = (-(self.speed // fps), 0)
        for sprite in self.collision_objects:
            if pygame.sprite.collide_mask(sprite, self):
                self.coord[self.move[1]] += self.move[0]
        for chest in self.collision_chests:
            if self.key:
                break
            if pygame.sprite.collide_mask(chest, self):
                if chest.key == 1:
                    self.key = True
        if pygame.sprite.collide_mask(self, self.door):
            if self.key:
                self.key = False
                self.level.next_level()
                if self.level.n == 1:
                    self.coord = [60, 60]
                elif self.level.n == 2:
                    self.coord = [60, 80]
        self.move = (0, 0)
        self.rect.center = self.coord
        self.update_frame()

    def update(self, event=None, par=None, **kwargs):
        if par == 'move' or self.keys:
            if not event:
                self.fly()
            elif event.type == pygame.KEYDOWN:
                self.fly(event.key, 'go')
            else:
                self.fly(event.key, 'stop')

    def update_frame(self):
        if self.count == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            if pygame.K_s in self.keys:
                self.cur_row = 4
            elif pygame.K_w in self.keys:
                self.cur_row = 0
            elif pygame.K_a in self.keys:
                self.cur_row = 6
            elif pygame.K_d in self.keys:
                self.cur_row = 2
            self.image = self.frames[self.cur_row][self.cur_frame]
            self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
            self.mask = pygame.mask.from_surface(self.image)
        self.count = (self.count + 1) % self.images_speed

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, (sheet.get_width() // columns),
                                (sheet.get_height() - 20) // rows)
        for j in range(rows):
            local_frames = []
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j + 20)
                local_frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
            self.frames.append(local_frames.copy())
            local_frames.clear()


