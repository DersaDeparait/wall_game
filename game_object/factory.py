from game_object.base_object import BaseObject, Wall, Life
import random

class FactoryMethod:
    def __init__(self, health=1000, position=None, velocity=None, acceleration=None, size=None, control=None) -> None:
        self.health = health
        self.position = position or [0, 0]
        self.velocity = velocity or [0, 0]
        self.acceleration = acceleration or [0, 0]
        self.size = size or 100
        self.control = control
        super().__init__()

    def create_object(self):
        return BaseObject()


class WallFactory(FactoryMethod):
    def __init__(self, health=1000, position=[0, 0], velocity=[0, 0], acceleration=[0, 0], size=[100, 100],
                 control=None) -> None:
        super().__init__(health, position, velocity, acceleration, size, control)
        self.counter = 0

    def create_object(self):
        position = self.position.copy()
        max_val = 9
        if self.counter < max_val:
            position = [self.position[0], self.position[1] + self.size * self.counter]
        elif self.counter < max_val * 2:
            position = [self.position[0] + self.size * (self.counter - max_val), self.position[1] + self.size * max_val]
        elif self.counter < max_val * 3:
            position = [self.position[0] + self.size * max_val, self.position[1] + self.size * (max_val - (self.counter - 2 * max_val))]

        size = self.size # if self.counter % 4 != 0 else self.size / 1.5
        velocity = self.velocity # if self.counter % 4 != 0 else [0, -0.1]

        wall = Wall(health=self.health,
                    position=position,
                    velocity=velocity,
                    acceleration=self.acceleration,
                    size=size,
                    control=self.control)
        self.counter += 1
        return wall


class LifeFactory(FactoryMethod):
    def create_object(self):
        position = [random.randint(0, 1600), random.randint(0, 1000)] if self.position == [0, 0] else self.position
        return Life(health=self.health,
                    position=position,
                    velocity=self.velocity,
                    acceleration=self.acceleration,
                    size=self.size,
                    control=self.control)
