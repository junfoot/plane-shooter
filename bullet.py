import pygame, globalvar
scene = globalvar.get_value('scene')
if scene == 1:
    from scene_banana import *
elif scene == 2:
    from scene_chicken import *
elif scene == 3:
    from scene_oldeight import *

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet1.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 10
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.count = 0

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left, self.rect.top = position
        self.active = True
        self.count = 0

class Bullet2(Bullet1):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet2.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.count = 0


class Bullet3(Bullet1):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet3.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.count = 0
