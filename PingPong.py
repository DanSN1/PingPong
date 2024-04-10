from pygame import *
from random import randint


win = display.set_mode((650,400))
display.set_caption('Ping Pong')
background = transform.scale(image.load('aboba.png'), (700,500))
clock = time.Clock()
FPS = 60

class godgod(sprite.Sprite):
    def __init__(self, image1, x, y, speed, weith, height):
        super().__init__()
        self.image = transform.scale(image.load(image1),(weith, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(godgod):
    def Move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 230:
            self.rect.y += self.speed

class Raceta(godgod):
    def Move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 230:
            self.rect.y += self.speed

player = Rocket(('aboba3.png'), 100, 100, 8, 40, 170)
player2 = Raceta(('aboba4.png'), 500, 100, 8, 40, 170)

game = True
while game:
    win.blit(background, (0,-50))
    player.reset()
    player.Move()
    player2.reset()
    player2.Move()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()