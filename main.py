import pygame as pg
import random

from itom import *
from object import *
from kanstant import *

pg.init()

dino_hero = dino_img
danger_options = [69, 449, 37, 410, 40, 420]

class object:
    def __init__(self, x, y, w, image, speed):
        self.x = x
        self.y = y
        self.w = w
        self.image = image
        self.speed = speed
    def move(self):
        if self.x >= -self.w:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_radius(self, radius, y, w, image):
        self.x = radius
        self.y = y
        self.w = w
        self.image = image
        display.blit(self.image, (self.x, self.y))


class Button:
    def __init__(self, w=0, h=0, img=None, action=None, x=0, y=0, xy=0, wh=0, inactive_color=(13, 142, 58), active_color=(23, 204, 58)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.xy = xy
        self.wh = wh
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.img = img
        self.action = action

    def draw(self, messege=None, font_size=30):
        global game

        button_sound = pg.mixer.Sound('Sound/button.wav')
        button_sound.set_volume(0.05)

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if self.img is not None:
            display.blit(self.img, (self.x, self.y))

        if self.x <= mouse[0] < self.x + self.w and self.y <= mouse[1] < self.y + self.h:
            if messege is not None:
                pg.draw.rect(display, self.active_color, (self.x-self.xy, self.y-self.xy, self.w+self.wh, self.h+self.wh))

            if click[0] == 1:
                button_sound.play()
                if self.action is not None:
                    self.action()

        elif messege is not None:
            pg.draw.rect(display, self.inactive_color, (self.x+self.xy, self.y+self.xy, self.w-self.wh, self.h-self.wh))

        print_text(messeg=messege, x=self.x + 10, y=self.y + 10, font_size=font_size)

class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 8
        self.speed_y = 0
        self.dest_x = 0
        self.dest_y = 0

    def move(self):
        self.x += self.speed_x
        if self.x <= wind_w:
            display.blit(shot_img, (self.x, self.y))
            return True
        else:
            return False

    def find_path(self, dest_x, dest_y):
        self.dest_y = dest_y
        self.dest_x = dest_x

        delta_x = dest_x - self.x
        count_up = delta_x // self.speed_x

        if self.y >= dest_y:
            delta_y = self.y - dest_y
            self.speed_y = delta_y / count_up
        else:
            delta_y = dest_y - self.y
            self.speed_y = -(delta_y / count_up)

    def move_to(self, reverse=False):
        if not reverse:
            self.x += self.speed_x
            self.y -= self.speed_y
        else:
            self.x -= self.speed_x
            self.y += self.speed_y

        if self.x <= wind_w and not reverse:
            display.blit(shot_img, (self.x, self.y))
            return True
        elif self.x >= 0 and reverse:
            display.blit(shot_img, (self.x, self.y))
            return True
        else:
            return False

class Bird:
    def __init__(self, away_y):
        self.x = random.randrange(550, 750)
        self.y = away_y
        self.w = 105
        self.h = 55
        self.ay = away_y
        self.speed = 3
        self.dest_y = self.speed * random.randrange(20, 100)
        self.img_cnt = 0
        self.cd_hide = 0
        self.come = True
        self.go_aw = False
        self.cd_shoot = 0
        self.all_shoot = []

    def draw(self):
        if self.img_cnt == 48:
            self.img_cnt = 0

        display.blit(bird_img[self.img_cnt // 8], (self.x, self.y))
        self.img_cnt += 1

        if self.come and self.cd_hide == 0:
            return 1
        elif self.go_aw:
            return 2
        elif self.cd_hide > 0:
                self.cd_hide -= 1
        return 0

    def show(self):
        if self.y < self.dest_y:
            self.y += self.speed
        else:
            self.come = False
            self.dest_y = self.ay

    def hide(self):
        if self.y > self.dest_y:
            self.y -= self.speed
        else:
            self.come = True
            self.go_aw = False
            self.x = random.randrange(650, 750)
            self.dest_y = self.speed * random.randrange(20, 70)
            self.cd_hide = 240

    def check_demeg(self, bullet):
        if self.x <= bullet.x <= self.x + self.w:
            if self.y <= bullet.y <= self.y + self.h:
                self.go_aw = True
                self.cd_shoot = 500
                health_sound.play()
                all_ms_shot.remove(bullet)

    def shoot(self):
        if not self.cd_shoot:
            r_shoot = random.randrange(-100, 100)
            new_shoot = Shot(self.x, self.y)
            new_shoot.find_path(usr_x + usr_w // 2 + r_shoot, usr_y + usr_h // 2 + r_shoot)
            shot_sound.play()

            self.all_shoot.append(new_shoot)
            self.cd_shoot = 300
        else:
            self.cd_shoot -= 1

        for shoot in self.all_shoot:
            if not shoot.move_to(reverse=True):
                self.all_shoot.remove(shoot)

            if usr_x + 10 <= shoot.x <= usr_x + usr_w - 25:
                if usr_y + 10 <= shoot.y <= usr_y + usr_h - 15:

                    check_health()
                    jamp_sound.play()
                    self.all_shoot.remove(shoot)





mace_jamp = False

jamp_caunter = 30

def menu():
    global dino_btn

    cooldawn1 = 10

    start_btn = Button(288, 70, None, start_game_menu, 270, 200, 3, 6)
    quit_btn = Button(120, 70, None, pg.quit, 358, 290, 3, 6)
    skins_btn = Button(80, 80, dino_btn, skins, 367, 400, 0, 0)

    show = True

    while show:
        for even in pg.event.get():
            if even.type == pg.QUIT:
                pg.quit()
                quit()

        menu_img = pg.image.load('imege/Menu.jpg')
        display.blit(menu_img, (0, 0))

        if cooldawn1 == 0:
            start_btn.draw('Start game', 50)
            quit_btn.draw('Quit', 50)
            skins_btn.draw()
        else:
            cooldawn1 -= 1

        draw_mouse()
        pg.display.update()
        clock.tick(60)
        draw_mouse()

def skins():
    skin = True

    cooldawn1 = 10

    skins_s_btn = Button(100, 100, dino_skins, skin_show_s, 280, 250, 0, 0)
    skins_n_btn = Button(100, 100, dino_skins2, skin_show_n, 420, 250, 0, 0)

    while skin:
        for even in pg.event.get():
            if even.type == pg.QUIT:
                pg.quit()
                quit()

        menu_img = pg.image.load('imege/Menu.jpg')
        display.blit(menu_img, (0, 0))

        if cooldawn1 == 0:
            skins_n_btn.draw()
            skins_s_btn.draw()
        else:
            cooldawn1 -= 1

        pg.display.update()
        clock.tick(80)

def start_game_menu():
    pg.mixer.music.set_volume(0.03)
    pg.mixer.music.play(-1)

    while run_game():
        pass


def run_game():
    global mace_jamp, cooldawn, cooldawn_p, all_ms_shot
    game = True

    pg.mixer.music.load("Sound/background.mp3")
    pg.mixer.music.set_volume(0.1)

    pg.mixer.music.unpause()

    danger_arr = []
    create_dabger_arr(danger_arr)

    pg.mixer.music.play(-1)

    pause_btn = Button(80, 80, game_img1, pause, 360, 10, 0, 0)

    health = 2
    cooldawn = 10
    cooldawn_p = 0
    scores = -1
    scores_s = -1

    stone, cloud = random_objects()

    heart = object(800, 280, 30, health_img, 4)
    bird1 = Bird(-120)
    bird2 = Bird(-160)
    bird3 = Bird(-80)

    all_btn_shot = []
    all_ms_shot = []
    all_bird = [bird1, bird2, bird3]


    while game:
        global scores1, paused
        for even in pg.event.get():
            if even.type == pg.QUIT:
                pg.quit()
                quit()

        key = pg.key.get_pressed()
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if key[pg.K_SPACE]:
            mace_jamp = True
        if key[pg.K_ESCAPE]:
            pause()

        if mace_jamp:
            jamp()

        scores += 1
        scores1 = int(scores)

        scores_s += 1

        if scores_s <= 3600:
            display.blit(land, (0, 0))

        elif scores_s < 6440:
            display.blit(land_n, (0, 0))

        elif scores_s < 8560:
            display.blit(land, (0, 0))

        else:
            scores_s = 0

        print_text('Scores: ' + str(scores1 // 80), 10, 10, (0, 255, 0), "PingPong.ttf", 50)

        draw_arrey(danger_arr)

        move_object(stone, cloud)
        heart.move()

        if cooldawn_p == 0:
            pause_btn.draw()

            if key[pg.K_ESCAPE]:
                pause()

        else:
            cooldawn_p -= 1

        draw_dino()
        show_health()
        draw_mouse()

        if cooldawn == 0:
            if key[pg.K_x]:
                shot_sound.play()
                all_btn_shot.append(Shot(usr_x + usr_w - 10, usr_y + 57))
                cooldawn += 100

            elif click[0]:
                shot_sound.play()
                add_shot = Shot(usr_x + usr_w - 10, usr_y + 27)
                add_shot.find_path(mouse[0], mouse[1])
                all_ms_shot.append(add_shot)
                cooldawn += 100

        else:
            print_text(str(cooldawn // 20), 250, usr_y - 20)
            cooldawn -= 1

        for shot in all_btn_shot:
            if not shot.move():
                all_btn_shot.remove(shot)

        for shot in all_ms_shot:
            if not shot.move_to():
                all_ms_shot.remove(shot)

        for barier in danger_arr:
            for shot in all_ms_shot:
                if barier.x <= shot.x <= barier.x + barier.w and barier.y <= shot.y <= barier.y + 70:
                    objects_retern(danger_arr, barier)

        for barier in danger_arr:
            for shot in all_btn_shot:
                if barier.x <= shot.x <= barier.x + barier.w and barier.y <= shot.y <= barier.y + 70:
                    objects_retern(danger_arr, barier)


        hearts_plus(heart)

        draw_birds(all_bird)
        check_bird_demeg(all_bird, all_ms_shot)

        if check_collision(danger_arr):
            check_health()

        pg.display.update()
        clock.tick(80)

    return game_over()

def jamp():
    global usr_y, mace_jamp, jamp_caunter
    if jamp_caunter >= -30:
        if jamp_caunter == 30:
            pass
        if jamp_caunter == -30:
            foll_sound.play()
        usr_y -= jamp_caunter / 2.5
        jamp_caunter -= 1
    else:
        jamp_caunter = 30
        mace_jamp = False

def create_dabger_arr(arrey):
    choice = random.randrange(0, 3)
    img = danger_img[choice]
    width = danger_options[choice * 2]
    height = danger_options[choice * 2 + 1]
    arrey.append(object(wind_w + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = danger_img[choice]
    width = danger_options[choice * 2]
    height = danger_options[choice * 2 + 1]
    arrey.append(object(wind_w + 300, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = danger_img[choice]
    width = danger_options[choice * 2]
    height = danger_options[choice * 2 + 1]
    arrey.append(object(wind_w + 600, height, width, img, 4))

def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < wind_w:
        radius = wind_w
        if radius - maximum < 30:
            radius += 200
    else:
        radius = maximum


    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)

    return radius

def draw_arrey(arrey):
    for danger in arrey:
        check = danger.move()
        if not check:
            objects_retern(arrey, danger)

def objects_retern(objects, obj):
    radius = find_radius(objects)

    choice = random.randrange(0, 3)
    img = danger_img[choice]
    width = danger_options[choice * 2]
    height = danger_options[choice * 2 + 1]

    obj.return_radius(radius, height, width, img)

def random_objects():
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = object(wind_w, wind_h - 80, 10, img_of_stone, 4)
    cloud = object(wind_w, 80, 70, img_of_cloud, 2)

    return stone, cloud

def move_object(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]
        stone.return_radius(wind_w, 500 + random.randrange(30, 80), stone.w, img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_radius(wind_w, random.randrange(10, 200), stone.w, img_of_cloud)

def draw_dino():
    global img_caunter, dino_hero
    if img_caunter == 30:
        img_caunter = 0

    display.blit(dino_hero[img_caunter // 6], (usr_x, usr_y))
    img_caunter += 1

def print_text (messeg, x, y, font_color=(0, 0, 0), font_tape = "imege/PingPong.ttf", font_size = 30):
    font_tape = "imege/PingPong.ttf"
    font_tape = pg.font.Font(font_tape, font_size)
    text = font_tape.render(messeg, True, font_color)
    display.blit(text, (x, y))

def unpauset():
    global paused, cooldawn_p, cooldawn
    paused = False
    cooldawn_p = 20
    cooldawn = 20

def pause():
    global paused
    pg.mixer.music.pause()

    paused = True

    cooldawn1 = 20

    pause_btn3 = Button(80, 80, game_img1, unpauset, 360, 10, 0, 0)
    pause_btn1 = Button(80, 80, game_img, run_game, 360, 110, 0, 0)
    pause_btn2 = Button(80, 80, game_img2, menu, 360, 210, 0, 0)

    while paused:
        for even in pg.event.get():
            if even.type == pg.QUIT:
                pg.quit()
                quit()

        if cooldawn1 == 0:
            print_text("Pauset", 160, 150, (0, 0, 0), "imege/PingPong.ttf", 50)
            pause_btn3.draw()
            pause_btn1.draw()
            pause_btn2.draw()
            key = pg.key.get_pressed()
            if key[pg.K_RETURN]:
                paused = False

        else:
            cooldawn1 -= 1

        pg.display.update()
        clock.tick(60)

    pg.mixer.music.unpause()

def check_collision(barriers):
    for barrier in barriers:
        if barrier.y == 449:
            if not mace_jamp:
                if barrier.x <= usr_x + usr_w - 35 <= barrier.x + barrier.w:
                    if check_health():
                        objects_retern(barriers, barrier)
                    else:
                        return True
            elif jamp_caunter >= 0:
                if usr_y + usr_h - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_w - 35 <= barrier.x + barrier.w:
                        if check_health():
                            objects_retern(barriers, barrier)
                        else:
                            return True
            else:
                if usr_y + usr_h - 10 >= barrier.y:
                    if barrier.x <= usr_x <= barrier.x + barrier.w:
                        if check_health():
                            objects_retern(barriers, barrier)
                        else:
                            return True
        else:
            if jamp_caunter <= 0:
                if usr_y + usr_h - 15 >= barrier.y:
                    if barrier.x <= usr_x + usr_w - 35 <= barrier.x + barrier.w:
                        if check_health():
                            objects_retern(barriers, barrier)
                        else:
                            return True
                    elif usr_x <= barrier.x + barrier.w <= usr_x + usr_w - 18:
                        if check_health():
                            objects_retern(barriers, barrier)
                        else:
                            return True
            if not mace_jamp:
                if barrier.x <= usr_x + usr_w - 5 <= barrier.x + barrier.w:
                    if check_health():
                        objects_retern(barriers, barrier)
                    else:
                        return True
            if jamp_caunter >= -1:
                if usr_y + usr_h - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_w - 35 <= barrier.x + barrier.w:
                        if check_health():
                            objects_retern(barriers, barrier)
                        else:
                            return True

    return False

def game_over():
    stopped = True

    global health

    pg.mixer.music.pause()

    health = 2

    menu_btn = Button(80, 80, game_img, run_game, 300, 280)
    menu_btn1 = Button(80, 80, game_img2, menu, 400, 280)

    while stopped:
        for even in pg.event.get():
            if even.type == pg.QUIT:
                pg.quit()
                quit()

        print_text("Game Over",200, 120, (255, 0, 0), "imege/PingPong.ttf", 80)
        print_text('you Scores: ' + str(scores1 // 80), 220, 200, (255, 0, 0), "PingPong.ttf", 50)
        menu_btn.draw()
        menu_btn1.draw()

        pg.display.update()
        clock.tick(60)

def show_health():
    global health
    show = 0
    x = 10
    while show != health:
        display.blit(health_img, (x, 60))
        x += 44
        show += 1

def check_health():
    global health
    health -= 1
    if health <= 0:
        loss_sound.play()
        game_over()
    else:
        jamp_sound.play()
        return True

def hearts_plus(heart):
    global health, usr_x, usr_y, usr_h, usr_w
    if usr_x <= heart.x <= usr_x + usr_w:
        if usr_y <= heart.y <= usr_y + usr_h:
            health_sound.play()
            if health < 5:
                health += 1
            heart.y = random.randrange(200, 350)
            radius = wind_w + random.randrange(2000, 7000)
            heart.return_radius(radius, heart.y, heart.w, heart.image)
    if heart.x <= 0:
        heart.y = random.randrange(200, 250)
        radius = wind_w + random.randrange(2000, 7000)
        heart.return_radius(radius, heart.y, heart.w, heart.image)

def draw_birds(birds):
    for bird in birds:
        action = bird.draw()
        if action == 1:
            bird.show()
        elif action == 2:
            bird.hide()
        else:
            bird.shoot()

def check_bird_demeg(birds, bullets):
    for bird in birds:
        for bullet in bullets:
            bird.check_demeg(bullet)

def draw_mouse():
    global mouse_caunter, need_draw_click
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    mouse_size = [10, 12, 16, 20, 28, 34, 40, 45, 48, 54, 58]

    if click[0] or click[1]:
        need_draw_click = True

    if need_draw_click:
        draw_x = mouse[0] - mouse_size[mouse_caunter] // 2
        draw_y = mouse[1] - mouse_size[mouse_caunter] // 2

        display.blit(pop_img[mouse_caunter], (draw_x, draw_y))
        mouse_caunter += 1

        if mouse_caunter == 10:
            need_draw_click = False
            mouse_caunter = 0

def skin_show_n():
    global dino_hero, dino_btn, dino2_img
    dino_hero = dino2_img
    dino_btn = dino_skins2
    menu()

def skin_show_s():
    global dino_hero, dino_btn
    dino_hero = dino_img
    dino_btn = dino_skins
    menu()


if __name__ == '__main__':
    menu()

while run_game():
    health = 2
