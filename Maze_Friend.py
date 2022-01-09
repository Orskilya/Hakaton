import pygame


class Oleg(pygame.sprite.Sprite):
    def __init__(self, image, coord, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]
        self.mask = pygame.mask.from_surface(self.image)