import pygame as pg
from os.path import join

from classes.explosion import Explosion
from classes.laser import Laser
from classes.meteor import Meteor
from classes.ship import Ship
from classes.star import Star
from utils.utils import join_assets
from utils.constants import DISPLAY, WINDOW_WIDTH


def execute_collisions():
    global running
    global destroyed_meteors

    ship_collided = pg.sprite.spritecollide(
        ship, meteor_sprites, True, pg.sprite.collide_mask)
    if ship_collided:
        damage_sound.play()
        destroyed_meteors = 0
        # running = False

    for laser in laser_sprites:
        collided = pg.sprite.spritecollide(
            laser, meteor_sprites, True)
        if collided:
            explosion_sound.play()
            destroyed_meteors += len(collided)
            laser.kill()
            Explosion(sprites, explosion_frames, laser.rect.midtop)


def display_score():
    score = font.render(f"Score: {destroyed_meteors}", True, 'white')
    score_rect = score.get_frect(midbottom=(
        WINDOW_WIDTH / 2, 75))
    DISPLAY.blit(score, score_rect)


# Setup pygame
pg.init()


pg.display.set_caption("SPACE_SHOOTER")

# Imports
star_img = pg.image.load(join_assets("images", "star.png")).convert_alpha()
meteor_img = pg.image.load(join_assets("images", "meteor.png")).convert_alpha()
laser_img = pg.image.load(join_assets("images", "laser.png")).convert_alpha()
explosion_frames = [pg.image.load(join('assets', 'images', 'explosion', f'{
    i}.png')).convert_alpha() for i in range(21)]
laser_sound = pg.mixer.Sound(join_assets("audio", "laser.wav"))
explosion_sound = pg.mixer.Sound(join_assets("audio", "explosion.wav"))
damage_sound = pg.mixer.Sound(join_assets("audio", "damage.ogg"))
game_music = pg.mixer.Sound(join_assets("audio", "game_music.wav"))
font = pg.font.Font(join('assets', 'Oxanium-Bold.ttf'), 30)
font_surface = font.render('TEST', True, 'red')

laser_sound.set_volume(0.5)
explosion_sound.set_volume(0.6)
game_music.set_volume(0.4)
game_music.play(-1)

# Groups
sprites = pg.sprite.Group()
meteor_sprites = pg.sprite.Group()
laser_sprites = pg.sprite.Group()


# Stars
for _ in range(35):
    Star(sprites, star_img)

# Meteor
METEOR_EVENT = pg.event.custom_type()
pg.time.set_timer(METEOR_EVENT, 250)

# Ship
ship = Ship(sprites)

# Laser
LASER_EVENT = pg.event.custom_type()
pg.time.set_timer(LASER_EVENT, 250)

destroyed_meteors = 0

clock = pg.time.Clock()
FPS = 60
running = True

while running:
    # limits FPS to 60
    clock.tick(FPS)

    dt = clock.tick(FPS) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == LASER_EVENT:
            Laser((laser_sprites, sprites), laser_img, ship.rect.midtop)
            laser_sound.play()
        if event.type == METEOR_EVENT:
            Meteor((meteor_sprites, sprites), meteor_img)

    sprites.update(dt)

    execute_collisions()

    # Fill the screen with a color to wipe away anything from last frame
    DISPLAY.fill("black")

    sprites.draw(DISPLAY)

    display_score()

    # Update the display to put your work on screen
    pg.display.update()


pg.quit()
