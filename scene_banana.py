import pygame
pygame.mixer.init()
background = pygame.image.load("scene_banana/background1.png")

# bullet
bullet1 = pygame.image.load("scene_banana/bullet1.png")
bullet2 = pygame.image.load("scene_banana/bullet2.png")
bullet3 = pygame.image.load("scene_banana/bullet3.png")

# enemy
enemy1 = pygame.image.load("scene_banana/enemy1.png")
enemy1_down1 = pygame.image.load("scene_banana/enemy1_down1.png")
enemy1_down2 = pygame.image.load("scene_banana/enemy1_down2.png")
enemy1_down3 = pygame.image.load("scene_banana/enemy1_down3.png")

enemy2_1 = pygame.image.load("scene_banana/enemy2_1.png")
enemy2_2 = pygame.image.load("scene_banana/enemy2_2.png")
enemy2_hit = pygame.image.load("scene_banana/enemy2_hit.png")
enemy2_down1 = pygame.image.load("scene_banana/enemy2_down1.png")
enemy2_down2 = pygame.image.load("scene_banana/enemy2_down2.png")
enemy2_down3 = pygame.image.load("scene_banana/enemy2_down3.png")

enemy3_1 = pygame.image.load("scene_banana/enemy3_1.png")
enemy3_2 = pygame.image.load("scene_banana/enemy3_2.png")
enemy3_hit = pygame.image.load("scene_banana/enemy3_hit.png")
enemy3_down1 = pygame.image.load("scene_banana/enemy3_down1.png")
enemy3_down2 = pygame.image.load("scene_banana/enemy3_down2.png")
enemy3_down3 = pygame.image.load("scene_banana/enemy3_down3.png")

# supply
bullet_supply = pygame.image.load("scene_banana/bullet_supply.png")
bullet_supply2 = pygame.image.load("scene_banana/bullet_supply2.png")
bomb_supply = pygame.image.load("scene_banana/bili_supply.png")
bomb = pygame.image.load("scene_banana/bili.png")

# music
enemy1_hit_music = pygame.mixer.Sound("sound/ya.wav")
enemy1_hit_music.set_volume(0.4)

enemy2_hit_music = pygame.mixer.Sound("sound/fa.wav")
enemy2_hit_music.set_volume(0.6)
enemy2_down_music = pygame.mixer.Sound("sound/fck_you.wav")
enemy2_down_music.set_volume(1)

enemy3_emerge_music = pygame.mixer.Sound("sound/boy next door.wav")
enemy3_emerge_music.set_volume(1)
enemy3_hit_music = pygame.mixer.Sound("sound/ah.wav")
enemy3_hit_music.set_volume(1)
enemy3_down_music = pygame.mixer.Sound("sound/AH_That_Is_Good.wav")
enemy3_down_music.set_volume(1)

me_down_music = pygame.mixer.Sound("sound/Eeeee.wav")
me_down_music.set_volume(0.5)

supply_get_music = pygame.mixer.Sound("sound/BonusGet.wav")
supply_get_music.set_volume(0.6)

bili_bomb_music = pygame.mixer.Sound("sound/That_Is_Power.wav")
bili_bomb_music.set_volume(0.6)

speed_music = pygame.mixer.Sound("sound/Pump it.wav")
speed_music.set_volume(1)

background_music = "sound/粉红的回忆.mp3"
