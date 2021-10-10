import pygame, sys, os, time
from pygame.locals import *
import globalvar, random
from importlib import reload

globalvar.init()
globalvar.set_value('scene', 1)
import plane, bullet, enemy, supply, music
globalvar.set_value('scene', 0)

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

bg_size = width, height = 400, 600
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("WELCOME TO 欢乐打飞机")

background_menu = pygame.image.load("images/background-2.0.png").convert()
silent = False
single = True

def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def inc_speed(target, inc):
    for each in target:
        each.speed += inc

def main():
    global silent
    global single
    bullets = []
    bullets_you = []
    delay = 100
    level = 1
    invici_time_start = 0
    recorded = False
    # 用于切换图片
    switch_image = True
    switch_image1 = True
    switch_image2 = True
    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0
    you_destroy_index = 0
    # 控制声音次数
    music_once1 = True
    music_once2 = True
    music_once3 = True
    music_once4 = True
    music_once5 = False
    music_once6 = True
    music_once7 = True
    # 补给定时器
    DOUBLE_BULLET_TIME = USEREVENT + 4
    DOUBLE_BULLET_TIME_Y = USEREVENT + 6
    PENETRATE_BULLET_TIME = USEREVENT + 2
    PENETRATE_BULLET_TIME_Y = USEREVENT + 7
    SPEED_TIME = USEREVENT + 5
    is_double_bullet = False
    is_penetrate_bullet = False
    is_speed = False
    you_is_double_bullet = False
    you_is_penetrate_bullet = False
    # 无敌时间计时器
    INVICIBLE_TIME = USEREVENT + 3

    # 生成双方飞机
    me = plane.MyPlane(bg_size)
    you = plane.YourPlane(bg_size)

    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 5
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1((me.rect.centerx - 5, me.rect.centery - 30)))
    # 生成双枪子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 10
    for i in range(BULLET2_NUM // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 23, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 17, me.rect.centery)))
    # 生成贯穿子弹
    bullet3 = []
    bullet3_index = 0
    BULLET3_NUM = 7
    for i in range(BULLET3_NUM):
        bullet3.append(bullet.Bullet3((me.rect.centerx - 9, me.rect.centery - 40)))
    # 生成超级子弹
    bullet4 = []
    bullet4_index = 0
    BULLET4_NUM = 15
    for i in range(BULLET4_NUM):
        bullet4.append(bullet.Bullet1((me.rect.centerx - 5, me.rect.centery - 30)))

    # 你方子弹
    bullet5 = []
    bullet5_index = 0
    BULLET5_NUM = 5
    for i in range(BULLET5_NUM):
        bullet5.append(bullet.Bullet1((you.rect.centerx - 5, you.rect.centery - 30)))
    bullet6 = []
    bullet6_index = 0
    BULLET6_NUM = 10
    for i in range(BULLET6_NUM // 2):
        bullet6.append(bullet.Bullet2((you.rect.centerx - 23, you.rect.centery)))
        bullet6.append(bullet.Bullet2((you.rect.centerx + 17, you.rect.centery)))
    bullet7 = []
    bullet7_index = 0
    BULLET7_NUM = 7
    for i in range(BULLET7_NUM):
        bullet7.append(bullet.Bullet3((you.rect.centerx - 9, you.rect.centery - 40)))
    bullet8 = []
    bullet8_index = 0
    BULLET8_NUM = 15
    for i in range(BULLET8_NUM):
        bullet8.append(bullet.Bullet1((you.rect.centerx - 5, you.rect.centery - 30)))

    # 生成敌方飞机组
    enemies = pygame.sprite.Group()
    # 生成敌方小飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 10)
    # 生成敌方中飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 5)
    # 生成敌方大飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 1)

    # 每30s一个武器补给
    bullet_supply1 = supply.Bullet_Supply1(bg_size)
    bullet_supply2 = supply.Bullet_Supply2(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, random.randint(20, 40) * 1000)
    # 30s-60s随机给出一个自身增益补给
    life_supply = supply.Life_Supply(bg_size)
    speed_supply = supply.Speed_Supply(bg_size)
    SELF_SUPPLY_TIME = USEREVENT + 1
    pygame.time.set_timer(SELF_SUPPLY_TIME, random.randint(30, 60) * 1000)

    # 全屏炸弹
    bomb_image = supply.bomb_image.convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_num = 3
    # 生命值
    life_num = 3
    life_font = pygame.font.Font("font/allgemeine.ttf", 24)
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    # 统计得分
    score = 0
    score_you = 0
    score_font = pygame.font.Font("font/allgemeine.ttf", 36)
    # background
    background = supply.background_image.convert()

    # 游戏开始界面
    scene1_image_un = pygame.image.load("images/scene1.png").convert_alpha()
    scene1_image_p = pygame.image.load("images/scene1_pressed.png").convert_alpha()
    scene1_rect = scene1_image_un.get_rect()
    scene2_image_un = pygame.image.load("images/scene2.png").convert_alpha()
    scene2_image_p = pygame.image.load("images/scene2_pressed.png").convert_alpha()
    scene2_rect = scene2_image_un.get_rect()
    scene3_image_un = pygame.image.load("images/scene3.png").convert_alpha()
    scene3_image_p = pygame.image.load("images/scene3_pressed.png").convert_alpha()
    scene3_rect = scene3_image_un.get_rect()
    start_instruction_un = pygame.image.load("images/instruction.png").convert_alpha()
    start_instruction_p = pygame.image.load("images/instruction_p.png").convert_alpha()
    start_instrution_rect = start_instruction_un.get_rect()
    scene1_image = scene1_image_un
    scene2_image = scene2_image_un
    scene3_image = scene3_image_un
    start_instruction_image = start_instruction_un

    # 模式界面
    menu_person = False
    single_un = pygame.image.load('images/single.png').convert_alpha()
    single_p = pygame.image.load('images/single_pressed.png').convert_alpha()
    single_rect = single_un.get_rect()
    double_un = pygame.image.load("images/double.png").convert_alpha()
    double_p = pygame.image.load("images/double_pressed.png").convert_alpha()
    double_rect = double_un.get_rect()
    back_un = pygame.image.load("images/back.png").convert_alpha()
    back_p = pygame.image.load("images/back_pressed.png").convert_alpha()
    back_rect = back_un.get_rect()
    single_image = single_un
    double_image = double_un
    back_image = back_un

    # 游戏结束画面
    gameover_font = pygame.font.Font("font/oldschool.ttf", 36)
    restart_image_un = pygame.image.load("images/restart_unpressed.png").convert_alpha()
    restart_image_p = pygame.image.load("images/restart.png").convert_alpha()
    restart_rect = restart_image_un.get_rect()
    menu_image_un = pygame.image.load("images/menu_unpressed.png").convert_alpha()
    menu_image_p = pygame.image.load("images/menu.png").convert_alpha()
    menu_rect = menu_image_un.get_rect()
    quit_image_un = pygame.image.load("images/quit_unpressed.png").convert_alpha()
    quit_image_p = pygame.image.load("images/quit.png").convert_alpha()
    quit_rect = quit_image_un.get_rect()
    restart_image = restart_image_un
    menu_image = menu_image_un
    quit_image = quit_image_un

    # 游戏暂停标志
    pause = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    pause_rect = pause_nor_image.get_rect()
    pause_rect.left, pause_rect.top = width - pause_rect.width - 50, 10
    pause_image = pause_nor_image

    # 静音标志
    silent_nor_image = pygame.image.load("images/sound_on_un.png").convert_alpha()
    silent_pressed_image = pygame.image.load("images/sound_on_p.png").convert_alpha()
    sound_nor_image = pygame.image.load("images/sound_off_un.png").convert_alpha()
    sound_pressed_image = pygame.image.load("images/sound_off_p.png").convert_alpha()
    silent_rect = silent_nor_image.get_rect()
    silent_rect.left, silent_rect.top = width - silent_rect.width - 10, 10
    silent_image = silent_nor_image

    # 开始运行
    scene = globalvar.get_value('scene')
    if scene == 0:
        pygame.mixer.music.load("sound/斗♂地主.mp3")
    else:
        pygame.mixer.music.load(supply.bgm)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    running = True

    while running:
        if silent:
            pygame.mixer.music.pause()
            pygame.mixer.pause()
        else:
            if me.speed ==6:
                pygame.mixer.music.unpause()
            pygame.mixer.unpause()
        pos = pygame.mouse.get_pos()
        if silent_rect.collidepoint(pos):
            if silent:
                silent_image = sound_pressed_image
            else:
                silent_image = silent_pressed_image
        else:
            if silent:
                silent_image = sound_nor_image
            else:
                silent_image = silent_nor_image
        if pygame.mouse.get_pressed()[0]:
            if silent_rect.collidepoint(pos):
                silent = not silent
                time.sleep(0.1)

        # 菜单
        if scene == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    pygame.mixer.quit()
                    sys.exit()

            screen.blit(background_menu, (0, 0))

            # 选场景
            if not menu_person:
                scene1_rect.left, scene1_rect.top = 15, 350
                screen.blit(scene1_image, scene1_rect)
                scene2_rect.left, scene2_rect.top = 150, 350
                screen.blit(scene2_image, scene2_rect)
                scene3_rect.left, scene3_rect.top = 285, 350
                screen.blit(scene3_image, scene3_rect)
                start_instrution_rect.left, start_instrution_rect.top = 0, 172
                screen.blit(start_instruction_image, start_instrution_rect)

                pos = pygame.mouse.get_pos()
                if start_instrution_rect.collidepoint(pos):
                    start_instruction_image = start_instruction_p
                else:
                    start_instruction_image = start_instruction_un
                if scene1_rect.collidepoint(pos):
                    scene1_image = scene1_image_p
                else:
                    scene1_image = scene1_image_un
                if scene2_rect.collidepoint(pos):
                    scene2_image = scene2_image_p
                else:
                    scene2_image = scene2_image_un
                if scene3_rect.collidepoint(pos):
                    scene3_image = scene3_image_p
                else:
                    scene3_image = scene3_image_un

                if pygame.mouse.get_pressed()[0]:
                    if start_instrution_rect.collidepoint(pos):
                        os.system('instruction.txt')
                    elif scene1_rect.collidepoint(pos):
                        globalvar.set_value('scene', 1)
                        reload(plane), reload(bullet), reload(enemy), reload(supply), reload(music)
                        time.sleep(0.2)
                        menu_person = True
                    elif scene2_rect.collidepoint(pos):
                        globalvar.set_value('scene', 2)
                        reload(plane), reload(bullet), reload(enemy), reload(supply), reload(music)
                        time.sleep(0.2)
                        menu_person = True
                    elif scene3_rect.collidepoint(pos):
                        globalvar.set_value('scene', 3)
                        reload(plane), reload(bullet), reload(enemy), reload(supply), reload(music)
                        time.sleep(0.2)
                        menu_person = True

            # 选模式
            else:
                single_rect.left, single_rect.top = 10, 350
                screen.blit(single_image, single_rect)
                double_rect.left, double_rect.top = 200, 430
                screen.blit(double_image, double_rect)
                back_rect.left, back_rect.top = 10, 10
                screen.blit(back_image, back_rect)

                pos = pygame.mouse.get_pos()
                if single_rect.collidepoint(pos):
                    single_image = single_p
                else:
                    single_image = single_un

                if double_rect.collidepoint(pos):
                    double_image = double_p
                else:
                    double_image = double_un

                if back_rect.collidepoint(pos):
                    back_image = back_p
                else:
                    back_image = back_un

                if pygame.mouse.get_pressed()[0]:
                    if single_rect.collidepoint(pos):
                        single = True
                        running = not running
                    elif double_rect.collidepoint(pos):
                        single = False
                        running = not running
                    elif back_rect.collidepoint(pos):
                        menu_person = not menu_person

        # 游戏开始
        else:
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    pygame.mixer.quit()
                    sys.exit()

                elif event.type == SUPPLY_TIME:
                    random_num = random.choice([1, 2, 3])
                    if random_num == 1:
                        bullet_supply1.reset()
                    elif random_num == 2:
                        bullet_supply2.reset()
                    else:
                        bomb_supply.reset()

                elif event.type == SELF_SUPPLY_TIME:
                    if random.choice([True, False]):
                        life_supply.reset()
                    else:
                        speed_supply.reset()

                elif event.type == INVICIBLE_TIME:
                    me.invicible = False
                    pygame.time.set_timer(INVICIBLE_TIME, 0)

                elif event.type == DOUBLE_BULLET_TIME:
                    is_double_bullet = False
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)

                elif event.type == DOUBLE_BULLET_TIME_Y:
                    you_is_double_bullet = False
                    pygame.time.set_timer(DOUBLE_BULLET_TIME_Y, 0)

                elif event.type == PENETRATE_BULLET_TIME:
                    is_penetrate_bullet = False
                    pygame.time.set_timer(PENETRATE_BULLET_TIME, 0)

                elif event.type == PENETRATE_BULLET_TIME_Y:
                    you_is_penetrate_bullet = False
                    pygame.time.set_timer(PENETRATE_BULLET_TIME_Y, 0)

                elif event.type == SPEED_TIME:
                    if not silent:
                        pygame.mixer.music.unpause()
                    music.speed_music.stop()
                    is_speed = False
                    me.speed = 6
                    you.speed = 6
                    pygame.time.set_timer(SPEED_TIME, 0)

                elif event.type == KEYDOWN and event.key == K_SPACE and bomb_num:
                    music.bili_bomb_music.play()
                    bomb_num -= 1
                    for each in enemies:
                        if each.rect.bottom > 0:
                            each.active = False
                            if each in small_enemies:
                                score += 50
                                score_you += 50
                            elif each in mid_enemies:
                                score += 250
                                score_you += 250
                            else:
                                score += 1000
                                score += 1000
            # playing
            if life_num:
                # 难度提升
                score_total = score + score_you
                if level == 1 and score_total > 5000:
                    level = 2
                    add_small_enemies(small_enemies, enemies, 10)
                    add_mid_enemies(mid_enemies, enemies, 5)
                if level == 2 and score_total > 10000:
                    level = 3
                    add_small_enemies(small_enemies, enemies, 10)
                    add_mid_enemies(mid_enemies, enemies, 5)
                    add_big_enemies(big_enemies, enemies, 1)
                    inc_speed(small_enemies, 1)
                if level == 3 and score_total > 20000:
                    level = 4
                    add_small_enemies(small_enemies, enemies, 5)
                    add_mid_enemies(mid_enemies, enemies, 2)
                    add_big_enemies(big_enemies, enemies, 1)
                    inc_speed(small_enemies,1)
                if level == 4 and score_total > 30000:
                    level = 5
                    add_small_enemies(small_enemies, enemies, 5)
                    add_mid_enemies(mid_enemies, enemies, 2)
                    add_big_enemies(big_enemies, enemies, 1)
                    inc_speed(small_enemies, 1)
                if score_total > level * 10000 and int(score_total / 10000) == level:
                    level += 1
                    add_small_enemies(small_enemies, enemies, 2)
                    add_mid_enemies(mid_enemies, enemies, 1)
                    add_big_enemies(big_enemies, enemies, 1)
                    inc_speed(small_enemies, 1)

                pos = pygame.mouse.get_pos()
                if pause_rect.collidepoint(pos):
                    if pause:
                        pause_image = resume_pressed_image
                    else:
                        pause_image = pause_pressed_image
                else:
                    if pause:
                        pause_image = resume_nor_image
                    else:
                        pause_image = pause_nor_image
                if pygame.mouse.get_pressed()[0]:
                    if pause_rect.collidepoint(pos):
                        pause = not pause
                        time.sleep(0.2)

                # pause:
                if pause:
                    # 绘制分数
                    if single:
                        score_text = score_font.render("Score : %s" % str(score), True, (255, 150, 0))
                        screen.blit(score_text, (10, 5))
                    else:
                        score_text = score_font.render("Score : %s" % str(score), True, (255, 150, 0))
                        screen.blit(score_text, (10, 5))
                        score_text2 = score_font.render("Score : %s" % str(score_you), True, (0, 255, 0))
                        screen.blit(score_text2, (10, 45))
                    # 绘制剩余生命值
                    if life_num:
                        life_text = life_font.render("Life", True, (255,0,0))
                        screen.blit(life_text, (350, 560))
                        for i in range(life_num):
                            screen.blit(life_image, (320 - i * 30, height - 10 - bomb_rect.height))
                    # 绘制比利炸弹数量
                    for i in range(bomb_num):
                        screen.blit(bomb_image, (10 + i * 30, height - 10 - bomb_rect.height))
                    # 绘制暂停键
                    screen.blit(pause_image, pause_rect)
                else:
                    key_pressed = pygame.key.get_pressed()
                    if key_pressed[K_UP]:
                        me.moveUp()
                    if key_pressed[K_DOWN]:
                        me.moveDown()
                    if key_pressed[K_LEFT]:
                        me.moveLeft()
                    if key_pressed[K_RIGHT]:
                        me.moveRight()
                    if key_pressed[K_w]:
                        you.moveUp()
                    if key_pressed[K_s]:
                        you.moveDown()
                    if key_pressed[K_a]:
                        you.moveLeft()
                    if key_pressed[K_d]:
                        you.moveRight()

                    # 绘制我方飞机，并检测是否被撞
                    if me.active:
                        if me.invicible:
                            if switch_image:
                                screen.blit(me.image5, me.rect)
                            else:
                                screen.blit(me.image6, me.rect)
                        elif is_speed:
                            if switch_image:
                                screen.blit(me.image3, me.rect)
                            else:
                                screen.blit(me.image4, me.rect)
                        else:
                            if switch_image:
                                screen.blit(me.image1, me.rect)
                            else:
                                screen.blit(me.image2, me.rect)
                        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
                        if enemies_down and not me.invicible:
                            me.active = False
                    else:
                        if music_once4:
                            music.me_down_music.play()
                        music_once4 = False
                        if not (delay % 5):
                            screen.blit(me.destroy_images[me_destroy_index], me.rect)
                            me_destroy_index = (me_destroy_index + 1) % 3
                            if me_destroy_index == 0:
                                music_once4 = True
                                life_num -= 1
                                me.reset()
                                pygame.time.set_timer(INVICIBLE_TIME, 3 * 1000)

                    # 绘制你方飞机
                    if not single:
                        if you.active:
                            if you.invicible:
                                if time.time() - invici_time_start > 3:
                                    you.invicible = False
                                if switch_image:
                                    screen.blit(you.image5, you.rect)
                                else:
                                    screen.blit(you.image6, you.rect)
                            elif is_speed:
                                if switch_image:
                                    screen.blit(you.image3, you.rect)
                                else:
                                    screen.blit(you.image4, you.rect)
                            else:
                                if switch_image:
                                    screen.blit(you.image1, you.rect)
                                else:
                                    screen.blit(you.image2, you.rect)
                            enemies_down = pygame.sprite.spritecollide(you, enemies, False, pygame.sprite.collide_mask)
                            if enemies_down and not you.invicible:
                                you.active = False
                        else:
                            if music_once4:
                                music.me_down_music.play()
                            music_once4 = False
                            if not (delay % 5):
                                screen.blit(you.destroy_images[you_destroy_index], you.rect)
                                you_destroy_index = (you_destroy_index + 1) % 3
                                if you_destroy_index == 0:
                                    music_once4 = True
                                    life_num -= 1
                                    you.reset()
                                    invici_time_start = time.time()

                    # 绘制我方子弹,检测子弹是否击中敌机
                    if not (delay % 10) and not is_penetrate_bullet:
                        if is_double_bullet:
                            bullets = bullet2
                            bullets[bullet2_index].reset((me.rect.centerx - 23, me.rect.centery))
                            bullets[bullet2_index + 1].reset((me.rect.centerx + 17, me.rect.centery))
                            bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                        else:
                            bullets = bullet1
                            bullets[bullet1_index].reset((me.rect.centerx - 5, me.rect.centery - 30))
                            bullet1_index = (bullet1_index + 1) % BULLET1_NUM
                    if not (delay % 20) and is_penetrate_bullet:
                        bullets = bullet3
                        bullets[bullet3_index].reset((me.rect.centerx - 9, me.rect.centery - 40))
                        bullet3_index = (bullet3_index + 1) % BULLET3_NUM
                    if not (delay % 5) and is_speed:
                        bullets = bullet4
                        bullets[bullet4_index].reset((me.rect.centerx - 5, me.rect.centery - 30))
                        bullet4_index = (bullet4_index + 1) % BULLET4_NUM

                    # 绘制你方子弹
                    if not single:
                        if not (delay % 10) and not you_is_penetrate_bullet:
                            if you_is_double_bullet:
                                bullets_you = bullet6
                                bullets_you[bullet6_index].reset((you.rect.centerx - 23, you.rect.centery))
                                bullets_you[bullet6_index + 1].reset((you.rect.centerx + 17, you.rect.centery))
                                bullet6_index = (bullet6_index + 2) % BULLET6_NUM
                            else:
                                bullets_you = bullet5
                                bullets_you[bullet5_index].reset((you.rect.centerx - 5, you.rect.centery - 30))
                                bullet5_index = (bullet5_index + 1) % BULLET5_NUM
                        if not (delay % 20) and you_is_penetrate_bullet:
                            bullets_you = bullet7
                            bullets_you[bullet7_index].reset((you.rect.centerx - 9, you.rect.centery - 40))
                            bullet7_index = (bullet7_index + 1) % BULLET7_NUM
                        if not (delay % 5) and is_speed:
                            bullets_you = bullet8
                            bullets_you[bullet8_index].reset((you.rect.centerx - 5, you.rect.centery - 30))
                            bullet8_index = (bullet8_index + 1) % BULLET8_NUM

                    # 碰撞检测
                    for b in bullets:
                        if b.active:
                            b.move()
                            screen.blit(b.image, b.rect)
                            enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                            if enemy_hit:
                                if is_penetrate_bullet:
                                    if b.count < 7:
                                        for e in enemy_hit:
                                            if e in mid_enemies or e in big_enemies:
                                                b.count += 1
                                                e.hit = True
                                                e.energy -= 1
                                                if e.energy == 0:
                                                    e.active = False
                                                    if e.score_once:
                                                        e.score_once = False
                                                        if e in mid_enemies:
                                                            score += 500
                                                        else:
                                                            score += 2000
                                            else:
                                                e.active = False
                                                if e.score_once:
                                                    e.score_once = False
                                                    score += 100
                                    else:
                                        b.active = False
                                else:
                                    b.active = False
                                    for e in enemy_hit:
                                        if e in mid_enemies or e in big_enemies:
                                            e.hit = True
                                            e.energy -= 1
                                            if e.energy == 0:
                                                e.active = False
                                                if e.score_once:
                                                    e.score_once = False
                                                    if e in mid_enemies:
                                                        score += 500
                                                    else:
                                                        score += 2000
                                        else:
                                            e.active = False
                                            if e.score_once:
                                                e.score_once = False
                                                score += 100

                    if not single:
                        for b in bullets_you:
                            if b.active:
                                b.move()
                                screen.blit(b.image, b.rect)
                                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                                if enemy_hit:
                                    if you_is_penetrate_bullet:
                                        if b.count < 7:
                                            for e in enemy_hit:
                                                if e in mid_enemies or e in big_enemies:
                                                    b.count += 1
                                                    e.hit = True
                                                    e.energy -= 1
                                                    if e.energy == 0:
                                                        e.active = False
                                                        if e.score_once:
                                                            e.score_once = False
                                                            if e in mid_enemies:
                                                                score_you += 500
                                                            else:
                                                                score_you += 2000
                                                else:
                                                    e.active = False
                                                    if e.score_once:
                                                        e.score_once = False
                                                        score_you += 100
                                        else:
                                            b.active = False
                                    else:
                                        b.active = False
                                        for e in enemy_hit:
                                            if e in mid_enemies or e in big_enemies:
                                                e.hit = True
                                                e.energy -= 1
                                                if e.energy == 0:
                                                    e.active = False
                                                    if e.score_once:
                                                        e.score_once = False
                                                        if e in mid_enemies:
                                                            score_you += 500
                                                        else:
                                                            score_you += 2000
                                            else:
                                                e.active = False
                                                if e.score_once:
                                                    e.score_once = False
                                                    score_you += 100

                    # 绘制敌方大飞机
                    for each in big_enemies:
                        if each.active:
                            each.move()
                            if each.hit:
                                music.enemy3_hit_music.play()
                                screen.blit(each.image_hit, each.rect)
                                each.hit = False
                            else:
                                if switch_image2:
                                    screen.blit(each.image1, each.rect)
                                else:
                                    screen.blit(each.image2, each.rect)
                            if each.rect.bottom == -50:
                                music.enemy3_emerge_music.play(10)
                            # 血槽
                            pygame.draw.line(screen, (0,0,0), (each.rect.left, each.rect.top - 5),
                                             (each.rect.right, each.rect.top - 5), 2)
                            energy_remain = each.energy / enemy.BigEnemy.energy
                            if energy_remain > 0.2:
                                energy_color = (0, 255, 0)
                            else:
                                energy_color = (255, 0, 0)
                            pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                                             (each.rect.left + each.rect.width * energy_remain,
                                              each.rect.top - 5), 2)
                        else:
                            music.enemy3_emerge_music.stop()
                            if music_once3:
                                music.enemy3_down_music.play()
                            music_once3 = False
                            if not (delay % 5):
                                screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                                e3_destroy_index = (e3_destroy_index + 1) % 3
                                if e3_destroy_index == 0:
                                    music_once3 = True
                                    each.reset()

                    # 绘制敌方中飞机
                    for each in mid_enemies:
                        if each.active:
                            each.move()
                            if each.hit:
                                music.enemy2_hit_music.play()
                                screen.blit(each.image_hit, each.rect)
                                each.hit = False
                            else:
                                if switch_image1:
                                    screen.blit(each.image1, each.rect)
                                else:
                                    screen.blit(each.image2, each.rect)
                            # 血槽
                            pygame.draw.line(screen, (0,0,0), (each.rect.left, each.rect.top - 5),
                                             (each.rect.right, each.rect.top - 5), 2)
                            energy_remain = each.energy / enemy.MidEnemy.energy
                            if energy_remain > 0.2:
                                energy_color = (0,255,0)
                            else:
                                energy_color = (255,0,0)
                            pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                                             (each.rect.left + each.rect.width * energy_remain,
                                              each.rect.top - 5), 2)
                        else:
                            if music_once2:
                                music.enemy2_down_music.play()
                            music_once2 = False
                            if not (delay % 5):
                                screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                                e2_destroy_index = (e2_destroy_index + 1) % 3
                                if e2_destroy_index == 0:
                                    music_once2 = True
                                    each.reset()

                    # 绘制敌方小飞机
                    for each in small_enemies:
                        if each.active:
                            each.move()
                            screen.blit(each.image, each.rect)
                        else:
                            if music_once1:
                                music.enemy1_hit_music.play()
                                music_once1 = False
                            if not (delay % 5):
                                screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                                e1_destroy_index = (e1_destroy_index + 1) % 3
                                if e1_destroy_index == 0:
                                    music_once1 = True
                                    each.reset()

                    # 绘制双枪补给
                    if bullet_supply1.active:
                        bullet_supply1.move()
                        screen.blit(bullet_supply1.image, bullet_supply1.rect)
                        if pygame.sprite.collide_mask(bullet_supply1, me):
                            music.supply_get_music.play()
                            is_double_bullet = True
                            pygame.time.set_timer(DOUBLE_BULLET_TIME, 15 * 1000)
                            bullet_supply1.active = False
                        if not single:
                            if pygame.sprite.collide_mask(bullet_supply1, you):
                                music.supply_get_music.play()
                                you_is_double_bullet = True
                                pygame.time.set_timer(DOUBLE_BULLET_TIME_Y, 15 * 1000)
                                bullet_supply1.active = False
                    # 绘制穿甲补给
                    if bullet_supply2.active:
                        bullet_supply2.move()
                        screen.blit(bullet_supply2.image, bullet_supply2.rect)
                        if pygame.sprite.collide_mask(bullet_supply2, me):
                            music.supply_get_music.play()
                            is_penetrate_bullet = True
                            pygame.time.set_timer(PENETRATE_BULLET_TIME, 15 * 1000)
                            bullet_supply2.active = False
                        if not single:
                            if pygame.sprite.collide_mask(bullet_supply2, you):
                                music.supply_get_music.play()
                                you_is_penetrate_bullet = True
                                pygame.time.set_timer(PENETRATE_BULLET_TIME_Y, 15 * 1000)
                                bullet_supply2.active = False
                    # 绘制比利炸弹补给
                    if bomb_supply.active:
                        bomb_supply.move()
                        screen.blit(bomb_supply.image, bomb_supply.rect)
                        if pygame.sprite.collide_mask(bomb_supply, me) or pygame.sprite.collide_mask(bomb_supply, you):
                            music.supply_get_music.play()
                            if bomb_num < 3:
                                bomb_num += 1
                            bomb_supply.active = False
                    # 绘制生命值补给
                    if life_supply.active:
                        life_supply.move()
                        screen.blit(life_supply.image, life_supply.rect)
                        if pygame.sprite.collide_mask(life_supply, me) or pygame.sprite.collide_mask(life_supply, you):
                            music.supply_get_music.play()
                            life_num += 1
                            life_supply.active = False
                    # 绘制加速补给
                    if speed_supply.active:
                        speed_supply.move()
                        screen.blit(speed_supply.image, speed_supply.rect)
                        if pygame.sprite.collide_mask(speed_supply, me) or pygame.sprite.collide_mask(life_supply, you):
                            pygame.mixer.music.pause()
                            music.speed_music.play()
                            me.speed = 12
                            you.speed = 12
                            is_speed = True
                            pygame.time.set_timer(SPEED_TIME, 15 * 1000)
                            speed_supply.active = False

                    # 绘制分数
                    if single:
                        score_text = score_font.render("Score : %s" % str(score), True, (255,150,0))
                        screen.blit(score_text, (10, 5))
                    else:
                        score_text = score_font.render("Score : %s" % str(score), True, (255,150,0))
                        screen.blit(score_text, (10, 5))
                        score_text2 = score_font.render("Score : %s" % str(score_you), True, (0, 255, 0))
                        screen.blit(score_text2, (10, 45))
                    # 绘制剩余生命值
                    if life_num:
                        life_text = life_font.render("Life", True, (255,0,0))
                        screen.blit(life_text, (350, 560))
                        for i in range(life_num):
                            screen.blit(life_image, (320 - i * 30, height - 10 - bomb_rect.height))
                    # 绘制比利炸弹数量
                    for i in range(bomb_num):
                        screen.blit(bomb_image, (10 + i * 30, height - 10 - bomb_rect.height))
                    # 绘制暂停键
                    screen.blit(pause_image, pause_rect)
                    # 切换图片
                    if not (delay % 5):
                        switch_image = not switch_image
                    if not (delay % 20):
                        switch_image1 = not switch_image1
                        switch_image2 = not switch_image2
                    # 延迟变量递减设置
                    delay -= 1
                    if not delay:
                        delay = 100
            # end
            else:
                pygame.time.set_timer(SUPPLY_TIME, 0)
                pygame.time.set_timer(SELF_SUPPLY_TIME, 0)
                if single and not recorded:
                    recorded = True
                    with open("record.txt", "r") as f:
                        record_score = int(f.read())
                    if score > record_score:
                        with open("record.txt", "w") as f:
                            f.write(str(score))
                    recorded = False

                # 绘制结束界面
                if single:
                    gameover_text1 = gameover_font.render("Best Score: %d" % record_score, True, (0,0,0))
                    gameover_text1_rect = gameover_text1.get_rect()
                    gameover_text1_rect.left, gameover_text1_rect.top = \
                        (width - gameover_text1_rect.width) // 2, height - 500
                    screen.blit(gameover_text1, gameover_text1_rect)

                    gameover_text2 = gameover_font.render("Your Score : %s" % str(score), True, (0,0,0))
                    gameover_text2_rect = gameover_text2.get_rect()
                    gameover_text2_rect.left, gameover_text2_rect.top = \
                        (width - gameover_text2_rect.width) // 2, gameover_text1_rect.bottom + 20
                    screen.blit(gameover_text2, gameover_text2_rect)

                else:
                    gameover_text1 = gameover_font.render("Score_orange : %s" % str(score), True, (0, 0, 0))
                    gameover_text1_rect = gameover_text1.get_rect()
                    gameover_text1_rect.left, gameover_text1_rect.top = \
                        (width - gameover_text1_rect.width) // 2, height - 500
                    screen.blit(gameover_text1, gameover_text1_rect)

                    gameover_text2 = gameover_font.render("Score_green : %s" % str(score_you), True, (0, 0, 0))
                    gameover_text2_rect = gameover_text2.get_rect()
                    gameover_text2_rect.left, gameover_text2_rect.top = \
                        (width - gameover_text2_rect.width) // 2, gameover_text1_rect.bottom + 20
                    screen.blit(gameover_text2, gameover_text2_rect)

                restart_rect.left, restart_rect.top = (width - restart_rect.width) // 4 - 10,\
                                                      gameover_text2_rect.bottom + 135
                screen.blit(restart_image, restart_rect)

                menu_rect.left, menu_rect.top = (width - menu_rect.width) - 20, restart_rect.top
                screen.blit(menu_image, menu_rect)

                quit_rect.left, quit_rect.top = (width - quit_rect.width) // 2, menu_rect.bottom + 35
                screen.blit(quit_image, quit_rect)

                # 检测鼠标操作
                pos = pygame.mouse.get_pos()
                if restart_rect.collidepoint(pos):
                    restart_image = restart_image_p
                else:
                    restart_image = restart_image_un

                if menu_rect.collidepoint(pos):
                    menu_image = menu_image_p
                else:
                    menu_image = menu_image_un

                if quit_rect.collidepoint(pos):
                    quit_image = quit_image_p
                else:
                    quit_image = quit_image_un

                if pygame.mouse.get_pressed()[0]:
                    if menu_rect.collidepoint(pos):
                        running = not running
                        globalvar.set_value('scene', 0)
                        time.sleep(0.1)
                    elif quit_rect.left < pos[0] < quit_rect.right and quit_rect.top < pos[1] < quit_rect.bottom:
                        pygame.quit()
                        pygame.mixer.quit()
                        sys.exit()
                    elif restart_rect.collidepoint(pos):
                        running = False

        # 绘制静音键
        screen.blit(silent_image, silent_rect)
        if silent:
            pygame.mixer.pause()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    while True:
        main()
