import pygame as pg

WIDTH = 1920  # ширина игрового окна
HEIGHT = 1080  # высота игрового окна
FPS = 60  #  частота кадров в секунду

pg.init()

surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Wall game")
clock = pg.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


from CommonFunctionality import Background
b = Background(color=(150, 150, 0))



run = True
while run:
    b.draw()
    pg.display.flip()

