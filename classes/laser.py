import pygame as pg


class Laser(pg.sprite.Sprite):
    def __init__(self, groups, img, ship_pos):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_frect(
            center=ship_pos)
        self.speed = 1000
        self.direction = pg.Vector2(0, -1)

    def update(self, dt):
        self.rect.centery -= self.speed * dt
        if self.rect.bottom < 0:
            self.kill()
