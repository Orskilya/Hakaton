import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, image, coord, key=0, *group):
        super().__init__(*group)
