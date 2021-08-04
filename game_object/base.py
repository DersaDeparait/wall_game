import pygame as pg
import math


class BaseObject:
    def __init__(self, health=1000, position=[0,0], velocity=[0,0], acceleration=[0,0], control=None):
        self.health = health
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.control = control

    def control(self):
        if self.control != None:
            self.control()

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
                 acceleration=[0,0], small_size=0.5, size=[100, 100], width=4, control=None,
                 color_left=[70, 150, 250, 0], color_down=[0, 0, 0, 0], color_right=[0, 0, 0, 0],
                 color_up=[70, 150, 250, 0], color_center=[0, 80, 150, 0]):
        super().__init__(health, position, velocity, acceleration, control=control)
        self.small_size = small_size
        self.size = size
        self.width = width
        self.color_left = color_left
        self.color_down = color_down
        self.color_right = color_right
        self.color_up = color_up
        self.color_center = color_center

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
                [self.position[0] - self.size[0] * self.small_size / 2, self.position[1] - self.size[1] * self.small_size / 2],
                [self.position[0] - self.size[0] * self.small_size / 2, self.position[1] + self.size[1] * self.small_size / 2],
                [self.position[0] + self.size[0] * self.small_size / 2, self.position[1] + self.size[1] * self.small_size / 2],
                [self.position[0] + self.size[0] * self.small_size / 2, self.position[1] - self.size[1] * self.small_size / 2]
            ]
        ]
        colors = [
            self.color_left,  # left
            self.color_down,  # down
            self.color_right,  # right
            self.color_up,  # up
            self.color_center  # central
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

class Life(BaseObject):
    def __init__(self, health=1000, position=[0, 0], velocity=[0, 0], acceleration=[0, 0], size=44, small_size=0.84,
                 control=None, spin=0, spin_velocity=0, spin_acceleration=0,
                 color_frame=[0,0,0,0], color_body=[70, 70, 150,0], color_eye=[100, 100, 250,0]):
        super().__init__(health, position, velocity, acceleration, control)
        self.size = size
        self.small_size = small_size
        self.spin = spin
        self.spin_velocity = spin_velocity
        self.spin_acceleration = spin_acceleration
        self.color_frame = color_frame
        self.color_body = color_body
        self.color_eye = color_eye

    def update(self):
        super().update()
        self.update_spin()

    def update_spin(self):
        self.spin_velocity += self.spin_acceleration
        self.spin_acceleration = 0
        self.spin += self.spin_velocity

    def draw(self, surface):
        super().draw(surface)
        position = [self.position[0] + math.cos(self.spin) * self.size / 2,
                    self.position[1] - math.sin(self.spin) * self.size / 2]

        pg.draw.circle(surface=surface, color=self.color_frame, center=self.position, radius=self.size)
        pg.draw.circle(surface=surface, color=self.color_body, center=self.position, radius=self.size * self.small_size)

        pg.draw.circle(surface=surface, color=self.color_frame,
                       center=position, radius=self.size / 2)
        pg.draw.circle(surface=surface, color=self.color_eye,
                       center=position, radius=self.size * (1 - (1 - self.small_size) * 2) / 2)
