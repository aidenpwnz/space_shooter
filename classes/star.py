from random import randint
import pygame as pg
from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class Star(pg.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_frect(
            center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
