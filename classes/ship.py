from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from utils.utils import join_assets
import pygame as pg


class Ship(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pg.image.load(
            join_assets("images", "ship.png")).convert_alpha()
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        # self.mask = pg.mask.from_surface(self.image)
        self.direction = pg.Vector2(0, 0)
        self.speed = 1000

    def update(self, dt):
        # Input mapping
        keys = pg.key.get_pressed()

        # Movement:
        self.direction.x = int(keys[pg.K_RIGHT]) - int(keys[pg.K_LEFT])
        self.direction.y = int(keys[pg.K_DOWN]) - int(keys[pg.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
