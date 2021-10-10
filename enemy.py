import pygame,globalvar
from random import *
scene = globalvar.get_value('scene')
if scene == 1:
    from scene_banana import *
elif scene == 2:
    from scene_chicken import *
elif scene == 3:
    from scene_oldeight import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy1.convert_alpha()
        self.destroy_images = [enemy1_down1.convert_alpha(),
                               enemy1_down2.convert_alpha(),
                               enemy1_down3.convert_alpha()]
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.score_once = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.score_once = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)

class MidEnemy(SmallEnemy):
    energy = 8

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = enemy2_1.convert_alpha()
        self.image2 = enemy2_2.convert_alpha()
        self.image_hit = enemy2_hit.convert_alpha()
        self.destroy_images = [enemy2_down1.convert_alpha(),
                               enemy2_down2.convert_alpha(),
                               enemy2_down3.convert_alpha()]
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1.5
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = MidEnemy.energy
        self.hit = False
        self.score_once = True

    def reset(self):
        self.active = True
        self.score_once = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)

class BigEnemy(SmallEnemy):
    energy = 20

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = enemy3_1.convert_alpha()
        self.image2 = enemy3_2.convert_alpha()
        self.image_hit = enemy3_hit.convert_alpha()
        self.destroy_images = [enemy3_down1.convert_alpha(),
                               enemy3_down2.convert_alpha(),
                               enemy3_down2.convert_alpha()]
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -2 * self.height)
        self.mask = pygame.mask.from_surface(self.image2)
        self.energy = BigEnemy.energy
        self.hit = False
        self.score_once = True

    def reset(self):
        self.active = True
        self.score_once = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)
