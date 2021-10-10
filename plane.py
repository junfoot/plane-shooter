import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/plane1_1.png").convert_alpha()
        self.image2 = pygame.image.load("images/plane1_2.png").convert_alpha()
        self.image3 = pygame.image.load("images/plane1_1_speed.png").convert_alpha()
        self.image4 = pygame.image.load("images/plane1_2_speed.png").convert_alpha()
        self.image5 = pygame.image.load("images/plane1_1_invicible.png").convert_alpha()
        self.image6 = pygame.image.load("images/plane1_2_invicible.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/plane1_down1.png").convert_alpha(),
            pygame.image.load("images/plane1_down2.png").convert_alpha(),
            pygame.image.load("images/plane1_down3.png").convert_alpha()
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 50
        self.speed = 6
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.invicible = False

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 50:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 50

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 50
        self.active = True
        self.invicible = True

class YourPlane(MyPlane):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/plane2_1.png").convert_alpha()
        self.image2 = pygame.image.load("images/plane2_2.png").convert_alpha()
        self.image3 = pygame.image.load("images/plane2_1_speed.png").convert_alpha()
        self.image4 = pygame.image.load("images/plane2_2_speed.png").convert_alpha()
        self.image5 = pygame.image.load("images/plane2_1_invicible.png").convert_alpha()
        self.image6 = pygame.image.load("images/plane2_2_invicible.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/plane2_down1.png").convert_alpha(),
            pygame.image.load("images/plane2_down2.png").convert_alpha(),
            pygame.image.load("images/plane2_down3.png").convert_alpha()
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 3, self.height - self.rect.height - 50
        self.speed = 6
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.invicible = False

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 3, self.height - self.rect.height - 50
        self.active = True
        self.invicible = True

