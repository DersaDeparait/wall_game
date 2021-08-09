import pygame as pg
from scene.scene import Scene

surface = pg.display.set_mode((1920, 1080))

scene = Scene()

def control():
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()


while True:
    control()
    scene.update()
    scene.draw(surface=surface, display=pg.display)
