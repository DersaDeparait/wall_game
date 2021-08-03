import pygame as pg


class BaseObject:
    def __init__(self, health=1000, position=[0,0], velocity=[0,0], acceleration=[0,0]):
        self.health = health
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self):
        self.update_position()

    def update_position(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.acceleration[0] = 0
        self.acceleration[1] = 0

    def draw(self, surface):
        pass


class Wall(BaseObject):
    def __init__(self, health=1000, position=[110,110], velocity=[0,0],
                 acceleration=[0,0], small_rectangle=0.5, size=[100, 100], width=4):
        super().__init__(health, position, velocity, acceleration)
        self.small_rectangle = small_rectangle
        self.size = size
        self.width = width

    def update(self):
        super().update()

    def draw(self, surface):
        super().draw(surface)

        points = [
            [
                [self.position[0] - self.size[0] / 2, self.position[1] - self.size[1] / 2],
                [self.position[0] - self.size[0] / 2, self.position[1] + self.size[1] / 2],
                [self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2],
                [self.position[0] + self.size[0] / 2, self.position[1] - self.size[1] / 2]
            ],
            [
                [self.position[0] - self.size[0] * self.small_rectangle / 2, self.position[1] - self.size[1] * self.small_rectangle / 2],
                [self.position[0] - self.size[0] * self.small_rectangle / 2, self.position[1] + self.size[1] * self.small_rectangle / 2],
                [self.position[0] + self.size[0] * self.small_rectangle / 2, self.position[1] + self.size[1] * self.small_rectangle / 2],
                [self.position[0] + self.size[0] * self.small_rectangle / 2, self.position[1] - self.size[1] * self.small_rectangle / 2]
            ]
        ]
        colors = [
            [70, 150, 250, 0],  # left
            [0, 0, 0, 0],  # down
            [0, 0, 0, 0],  # right
            [70, 150, 250, 0],  # up
            [0, 80, 150, 0]  # central
        ]

        pg.draw.polygon(surface, color=colors[0], points=[points[0][0], points[1][1], points[0][1]])
        pg.draw.polygon(surface, color=colors[0], points=[points[0][0], points[1][1], points[1][0]])

        pg.draw.polygon(surface, color=colors[1], points=[points[0][1], points[1][2], points[1][1]])
        pg.draw.polygon(surface, color=colors[1], points=[points[0][1], points[1][2], points[0][2]])

        pg.draw.polygon(surface, color=colors[2], points=[points[0][2], points[1][3], points[1][2]])
        pg.draw.polygon(surface, color=colors[2], points=[points[0][2], points[1][3], points[0][3]])

        pg.draw.polygon(surface, color=colors[3], points=[points[0][3], points[1][0], points[1][3]])
        pg.draw.polygon(surface, color=colors[3], points=[points[0][3], points[1][0], points[0][0]])

        pg.draw.polygon(surface, color=colors[-1], points=[points[1][0], points[1][1], points[1][2]])
        pg.draw.polygon(surface, color=colors[-1], points=[points[1][0], points[1][3], points[1][2]])

        pg.draw.lines(surface,
                      color=colors[4],
                      closed=True,
                      points=[points[0][0], points[1][0], points[1][1], points[0][1]],
                      width=self.width)

        pg.draw.lines(surface,
                      color=colors[4],
                      closed=True,
                      points=[points[0][1], points[1][1], points[1][2], points[0][2]],
                      width=self.width)

        pg.draw.lines(surface,
                      color=colors[4],
                      closed=True,
                      points=[points[0][2], points[1][2], points[1][3], points[0][3]],
                      width=self.width)

        pg.draw.lines(surface,
                      color=colors[4],
                      closed=True,
                      points=[points[0][3], points[1][3], points[1][0], points[0][0]],
                      width=self.width)
