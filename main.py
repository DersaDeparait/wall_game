import pygame as pg
from game_object.base import Wall, Life

surface = pg.display.set_mode((1920, 1080))
b = []
for i in range(3):
    b.append(Wall(position=[100, i*100+100]))
    b.append(Life(position=[300, i*100+100]))

def control():
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()

def update():
    for bb in b:
        bb.update()

def draw():
    surface.fill([0, 150, 225])
    for bb in b:
        bb.draw(surface)
    pg.display.flip()

while True:
    control()
    update()
    draw()
