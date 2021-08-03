import pygame as pg
import game_object.base

surface = pg.display.set_mode((1920, 1080))
print(surface)
b = []
for i in range(3):
    b.append(game_object.base.Wall(position=[100, i*100+100]))


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()

    surface.fill([0, 150, 225])
    for bb in b:
        bb.draw(surface)
    pg.display.flip()
