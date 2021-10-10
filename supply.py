import pygame,globalvar
from random import *
scene = globalvar.get_value('scene')
if scene == 1:
    from scene_banana import *
elif scene == 2:
    from scene_chicken import *
elif scene == 3:
    from scene_oldeight import *

bomb_image = bomb
background_image = background
bgm = background_music

class Bullet_Supply1(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet_supply.convert_alpha()

        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100


class Bullet_Supply2(Bullet_Supply1):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet_supply2.convert_alpha()

        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

class Bomb_Supply(Bullet_Supply1):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = bomb_supply.convert_alpha()

        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

class Life_Supply(Bullet_Supply1):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/life_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

class Speed_Supply(Bullet_Supply1):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/speed_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 3
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
