import os
import pygame

pygame.init()
# 4000, 7000
size = width, height = 400, 700
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Stairs(pygame.sprite.Sprite):
    image = load_image("fon..png", color_key=-1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Stairs.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Player(pygame.sprite.Sprite):
    image = load_image("player.png", color_key="black")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 40
        self.rect.y = 532
        self.pistol = Pistol(self.rect.x - 198, self.rect.y+20, 'player')


class Enemy(pygame.sprite.Sprite):
    image = load_image("enemy.png", color_key="black")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 270
        self.rect.y = 436
        self.pistol = Pistol(self.rect.x - 10, self.rect.y + 15)


class Pistol(pygame.sprite.Sprite):
    image = load_image("Pistol4.png", color_key=None)

    def __init__(self, x, y, parent='enemy'):
        super().__init__(all_sprites)
        self.parent = parent
        self.image = Pistol.image
        if self.parent == "player":
            self.image = pygame.transform.flip(self.image, True, False)
        self.image1 = self.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.gradus = 1
        self.flag = 0


    def shot(self):
        bullet = Bullet(self.rect.x, self.rect.y)

    def update(self):
        if self.parent == "player":
            self.image = pygame.transform.rotate(self.image1, self.gradus)
            if self.flag:
                self.gradus -= 1
            else:
                self.gradus += 1
            oldCenter = self.rect.center
            rotreact = self.image.get_rect()
            rotreact.center = oldCenter
            self.rect = rotreact
            if self.gradus > 45:
                self.flag = 1
            elif self.gradus < 1:
                self.flag = 0
            print(self.rect)


class Bullet(pygame.sprite.Sprite):
    image = load_image("Pistol.png", color_key=-1)

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x - 10
        self.rect.y = y + 15

    def update(self):
        pass


all_sprites = pygame.sprite.Group()
mountain = Stairs()
player = Player()
enemy = Enemy()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            enemy.pistol.shot()
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
