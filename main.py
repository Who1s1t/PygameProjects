import os
import pygame

pygame.init()
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


class Mountain(pygame.sprite.Sprite):
    image = load_image("fon..png", color_key=-1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
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

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)

class Enemy(pygame.sprite.Sprite):
    image = load_image("enemy.png", color_key="black")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 270
        self.rect.y = 436

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)

class Pistol(pygame.sprite.Sprite):
    image = load_image("Pistol.png", color_key="black")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Pistol.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)

all_sprites = pygame.sprite.Group()
mountain = Mountain()
player = Player()
enemy = Enemy()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
