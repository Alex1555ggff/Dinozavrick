import pygame as pg

pg.init()

stone_img = [pg.image.load("objeckt/Stone0.png"), pg.image.load("objeckt/Stone1.png")]

cloud_img = [pg.image.load("objeckt/Cloud0.png"), pg.image.load("objeckt/Cloud1.png")]

danger_img = [pg.image.load("objeckt/Cactus0.png"), pg.image.load("objeckt/Cactus1.png"),
                  pg.image.load("objeckt/Cactus2.png")]

shot_img = pg.image.load('objeckt/shot.png')
shot_img = pg.transform.scale(shot_img, (30, 9))

pop_img = [pg.image.load("objeckt/Light0.png"), pg.image.load("objeckt/Light1.png"), pg.image.load("objeckt/Light2.png"), pg.image.load("objeckt/Light3.png"), pg.image.load("objeckt/Light4.png"), pg.image.load("objeckt/Light5.png"), pg.image.load("objeckt/Light6.png"), pg.image.load("objeckt/Light7.png"), pg.image.load("objeckt/Light8.png"), pg.image.load("objeckt/Light9.png"), pg.image.load("objeckt/Light10.png")]

dino_img = [pg.image.load("skins/Dino0.png"), pg.image.load("skins/Dino1.png"), pg.image.load("skins/Dino2.png"),
            pg.image.load("skins/Dino3.png"), pg.image.load("skins/Dino4.png")]

dino2_img = [pg.image.load("skins/Dino2_0.png"), pg.image.load("skins/Dino2_1.png"), pg.image.load("skins/Dino2_2.png"),
            pg.image.load("skins/Dino2_3.png"), pg.image.load("skins/Dino2_4.png")]

bird_img = [pg.image.load("skins/Bird0.png"), pg.image.load("skins/Bird1.png"), pg.image.load("skins/Bird2.png"),
            pg.image.load("skins/Bird3.png"), pg.image.load("skins/Bird4.png"), pg.image.load("skins/Bird5.png")]

health_img = pg.image.load("imege/heart.png")
health_img = pg.transform.scale(health_img, (40, 40))

game_img = pg.image.load("imege/zanovo.png")
game_img = pg.transform.scale(game_img, (80, 80))

game_img1 = pg.image.load("imege/pause.png")
game_img1 = pg.transform.scale(game_img1, (80, 80))

game_img2 = pg.image.load("imege/menu.png")
game_img2 = pg.transform.scale(game_img2, (80, 80))

land_n = pg.image.load('imege/night.png')

land = pg.image.load("imege/Land.jpg")

dino_btn = pg.image.load('skins/Dino_s.png')

dino_skins = pg.image.load('skins/Dino_s.png')

dino_skins2 = pg.image.load('skins/Dino_n.png')

jamp_sound = pg.mixer.Sound('Sound/Rrr.wav')
jamp_sound.set_volume(0.1)

foll_sound = pg.mixer.Sound('Sound/Bdish.wav')
foll_sound.set_volume(0.05)

health_sound = pg.mixer.Sound('Sound/hp+.wav')
health_sound.set_volume(0.02)

loss_sound = pg.mixer.Sound('Sound/loss.wav')
loss_sound.set_volume(0.05)

shot_sound = pg.mixer.Sound('Sound/shot.wav')
shot_sound.set_volume(0.1)

pg.mixer.music.load("Sound/Big_Slinker.mp3")
pg.mixer.music.set_volume(0.05)
pg.mixer.music.play(-1)

font_tape = "imege/PingPong.ttf"

icon = pg.image.load("imege/Dino_i.png")
icon = pg.transform.scale(icon, (32, 32))
pg.display.set_icon(icon)

danger_img = [pg.image.load("objeckt/Cactus0.png"), pg.image.load("objeckt/Cactus1.png"),
                  pg.image.load("objeckt/Cactus2.png")]