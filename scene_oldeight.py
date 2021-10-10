import pygame
background = pygame.image.load("scene_oldeight/background1.png")

# bullet
bullet1 = pygame.image.load("scene_oldeight/bullet1.png")
bullet2 = pygame.image.load("scene_oldeight/bullet2.png")
bullet3 = pygame.image.load("scene_oldeight/bullet3.png")

# enemy
enemy1 = pygame.image.load("scene_oldeight/enemy1.png")
enemy1_down1 = pygame.image.load("scene_oldeight/enemy1_down1.png")
enemy1_down2 = pygame.image.load("scene_oldeight/enemy1_down2.png")
enemy1_down3 = pygame.image.load("scene_oldeight/enemy1_down3.png")

enemy2_1 = pygame.image.load("scene_oldeight/enemy2_1.png")
enemy2_2 = enemy2_1
enemy2_hit = pygame.image.load("scene_oldeight/enemy2_hit.png")
enemy2_down1 = pygame.image.load("scene_oldeight/enemy2_down1.png")
enemy2_down2 = pygame.image.load("scene_oldeight/enemy2_down2.png")
enemy2_down3 = pygame.image.load("scene_oldeight/enemy2_down3.png")

enemy3_1 = pygame.image.load("scene_oldeight/enemy3_1.png")
enemy3_2 = pygame.image.load("scene_oldeight/enemy3_2.png")
enemy3_hit = pygame.image.load("scene_oldeight/enemy3_hit.png")
enemy3_down1 = pygame.image.load("scene_oldeight/enemy3_down1.png")
enemy3_down2 = pygame.image.load("scene_oldeight/enemy3_down2.png")
enemy3_down3 = pygame.image.load("scene_oldeight/enemy3_down3.png")

# supply
bullet_supply = pygame.image.load("scene_oldeight/bullet_supply.png")
bullet_supply2 = pygame.image.load("scene_oldeight/bullet_supply2.png")
bomb_supply = pygame.image.load("scene_oldeight/mask_supply.png")
bomb = pygame.image.load("scene_oldeight/mask.png")

# music
enemy1_hit_music = pygame.mixer.Sound("sound3/Ah.wav")
enemy1_hit_music.set_volume(1)

enemy2_hit_music = pygame.mixer.Sound("sound3/chou.wav")
enemy2_hit_music.set_volume(0.6)
enemy2_down_music = pygame.mixer.Sound("sound3/cdf.wav")
enemy2_down_music.set_volume(1)

enemy3_emerge_music = pygame.mixer.Sound("sound3/mei_fannao.wav")
enemy3_emerge_music.set_volume(1)
enemy3_hit_music = pygame.mixer.Sound("sound3/ao.wav")
enemy3_hit_music.set_volume(1)
enemy3_down_music = pygame.mixer.Sound("sound3/alg_zjwl.wav")
enemy3_down_music.set_volume(1)

me_down_music = pygame.mixer.Sound("sound3/gan_xdm.wav")
me_down_music.set_volume(1)

supply_get_music = pygame.mixer.Sound("sound3/mei_zher_zher.wav")
supply_get_music.set_volume(1)

bili_bomb_music = pygame.mixer.Sound("sound3/alg_gan.wav")
bili_bomb_music.set_volume(1)

speed_music = pygame.mixer.Sound("sound3/xin_ba_dao.wav")
speed_music.set_volume(1)

background_music = "sound3/Lopu$ - So Cute~.mp3"
