from random import randint
import pygame as pg
import sys

W = 400
H = 400
WHITE = (255, 255, 255)


class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

sc = pg.display.set_mode((W, H))

# координата x будет случайна
car1 = Car(randint(1, W), "content/sprite/Byakuya.png")

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pg.display.update()
    pg.time.delay(20)

    # машинка ездит сверху вниз
    if car1.rect.y < H:
        car1.rect.y += 2
    else:
        car1.rect.y = 0
