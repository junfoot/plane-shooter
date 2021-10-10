import pygame
background = pygame.image.load("scene_chicken/background2.png")

# bullet
bullet1 = pygame.image.load("scene_chicken/bullet4.png")
bullet2 = bullet1
bullet3 = pygame.image.load("scene_chicken/bullet5.png")

# enemy
enemy1 = pygame.image.load("scene_chicken/enemy4.png")
enemy1_down1 = pygame.image.load("scene_chicken/enemy4_down1.png")
enemy1_down2 = pygame.image.load("scene_chicken/enemy4_down2.png")
enemy1_down3 = pygame.image.load("scene_chicken/enemy4_down3.png")

enemy2_1 = pygame.image.load("scene_chicken/enemy5_1.png")
enemy2_2 = pygame.image.load("scene_chicken/enemy5_2.png")
enemy2_hit = pygame.image.load("scene_chicken/enemy5_hit.png")
enemy2_down1 = pygame.image.load("scene_chicken/enemy5_down1.png")
enemy2_down2 = pygame.image.load("scene_chicken/enemy5_down2.png")
enemy2_down3 = pygame.image.load("scene_chicken/enemy5_down3.png")

enemy3_1 = pygame.image.load("scene_chicken/enemy6_1.png")
enemy3_2 = pygame.image.load("scene_chicken/enemy6_2.png")
enemy3_hit = pygame.image.load("scene_chicken/enemy6_hit.png")
enemy3_down1 = pygame.image.load("scene_chicken/enemy6_down1.png")
enemy3_down2 = pygame.image.load("scene_chicken/enemy6_down2.png")
enemy3_down3 = pygame.image.load("scene_chicken/enemy6_down3.png")

# supply
bullet_supply = pygame.image.load("scene_chicken/bullet_supply3.png")
bullet_supply2 = pygame.image.load("scene_chicken/bullet_supply4.png")
bomb_supply = pygame.image.load("scene_chicken/lawyer_supply.png")
bomb = pygame.image.load("scene_chicken/lawyer.png")

# music
enemy1_hit_music = pygame.mixer.Sound("sound2/ji.wav")
enemy1_hit_music.set_volume(0.4)

enemy2_hit_music = pygame.mixer.Sound("sound2/gan.wav")
enemy2_hit_music.set_volume(0.6)
enemy2_down_music = pygame.mixer.Sound("sound2/ni_gan_ma.wav")
enemy2_down_music.set_volume(1)

enemy3_emerge_music = pygame.mixer.Sound("sound2/ctrl.wav")
enemy3_emerge_music.set_volume(1)
enemy3_hit_music = pygame.mixer.Sound("sound2/O.wav")
enemy3_hit_music.set_volume(1)
enemy3_down_music = pygame.mixer.Sound("sound2/O_FingCing.wav")
enemy3_down_music.set_volume(1)

me_down_music = pygame.mixer.Sound("sound2/Aaaa.wav")
me_down_music.set_volume(1)

supply_get_music = pygame.mixer.Sound("sound2/cappuccino.wav")
supply_get_music.set_volume(0.6)

bili_bomb_music = pygame.mixer.Sound("sound2/duang.wav")
bili_bomb_music.set_volume(1)

speed_music = pygame.mixer.Sound("sound2/ji_ni_tai_mei.wav")
speed_music.set_volume(1)

background_music = "sound2/我是女生.mp3"
