import pygame as pg
from os.path import join

from utils.utils import join_assets

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
