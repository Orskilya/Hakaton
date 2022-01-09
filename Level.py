import pygame


class Level(pygame.sprite.Sprite):
    def __init__(self, images, chests, *group):
        super().__init__(*group)
        self.n = 0
        self.images = images
        self.image = images[self.n]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.chests = chests

    def update(self, hero):
        if self.n == 0:
            self.chests[0].rect.x = 10
            self.chests[0].rect.y = 275
            self.chests[1].rect.x = 100
            self.chests[1].rect.y = 650
            self.chests[2].rect.x = 275
            self.chests[2].rect.y = 500
            self.chests[3].rect.x = 975
            self.chests[3].rect.y = 450
        elif self.n == 1:
            self.chests[0].rect.x = 125
            self.chests[0].rect.y = 275
            self.chests[1].rect.x = 100
            self.chests[1].rect.y = 650
            self.chests[2].rect.x = 275
            self.chests[2].rect.y = 500
            self.chests[3].rect.x = 975
            self.chests[3].rect.y = 450
        if hero.rect.x >= 1150 and hero.rect.y >= 500 and hero.key and self.n == 0:
            self.n += 1
            self.image = self.images[self.n]
            self.mask = pygame.mask.from_surface(self.image)
            hero.coord = [50, 40]