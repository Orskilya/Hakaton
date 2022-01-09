import pygame


class Level(pygame.sprite.Sprite):
    def __init__(self, images, chests, door, *group):
        super().__init__(*group)
        self.n = -1
        self.images = images
        self.image = images[self.n]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.chests = chests
        self.door = door

    def next_level(self):
        self.n += 1
        self.image = self.images[self.n]
        self.mask = pygame.mask.from_surface(self.image)
        if self.n == 0:
            self.chests[0].rect.x = 45
            self.chests[0].rect.y = 230
            self.chests[1].rect.x = 80
            self.chests[1].rect.y = 620
            self.chests[2].rect.x = 850
            self.chests[2].rect.y = 230
            self.chests[3].rect.x = 1175
            self.chests[3].rect.y = 450
            self.door.rect.x = 630
            self.door.rect.y = 300
        elif self.n == 1:
            self.chests[0].rect.x = 270
            self.chests[0].rect.y = 200
            self.chests[1].rect.x = 15
            self.chests[1].rect.y = 650
            self.chests[2].rect.x = 1190
            self.chests[2].rect.y = 10
            self.chests[3].rect.x = 760
            self.chests[3].rect.y = 395
            self.door.rect.x = 950
            self.door.rect.y = 600
        elif self.n == 2:
            self.chests[0].rect.x = 380
            self.chests[0].rect.y = 250
            self.chests[1].rect.x = 15
            self.chests[1].rect.y = 650
            self.chests[2].rect.x = 1190
            self.chests[2].rect.y = 555
            self.chests[3].rect.x = 745
            self.chests[3].rect.y = 115
            self.door.rect.x = 480
            self.door.rect.y = 10
