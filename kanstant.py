import pygame as pg

pg.mixer.pre_init(44100, -16, 1, 512)

wind_w = 800
wind_h = 600

usr_w = 60
usr_h = 100
usr_x = wind_w // 3
usr_y = wind_h - usr_h - 100

danger_w = 20
danger_h = 70
danger_x = wind_w - 50
danger_y = wind_h - danger_h - 100

cooldawn = 0

img_caunter = 5
health = 2

mouse_caunter = 0
need_draw_click = False

clock = pg.time.Clock()

display = pg.display.set_mode((wind_w, wind_h))
pg.display.set_caption("Run, Dino! Run!")