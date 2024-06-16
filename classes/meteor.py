from random import randint, uniform
import pygame as pg

from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class Meteor(pg.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_frect(
            center=(randint(0, WINDOW_WIDTH), 0))
        self.speed = randint(600, 800)
        self.direction = pg.Vector2(uniform(-0.5, 0.5), 1)
        self.original_image = img
        self.rotation = 0
        self.rotation_speed = randint(40, 60)

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

        self.rotation += self.rotation_speed * dt
        self.image = pg.transform.rotozoom(
            self.original_image, self.rotation, 1)
        self.rect = self.image.get_frect(center=self.rect.center)
