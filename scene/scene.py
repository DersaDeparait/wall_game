from game_object.factory import WallFactory, LifeFactory

class Scene:
    def __init__(self, background_color=None):
        self.background_color = background_color or [20, 220, 190]
        self.objects = []

        factory_wall = WallFactory(health=1000, position=[100, 100], size=100)
        for i in range(23):
            self.objects.append(factory_wall.create_object())

        factory_life = LifeFactory(health=1000, position=None, size=30)
        for i in range(8):
            self.objects.append(factory_life.create_object())

    def control(self):
        pass

    def update(self):
        for object in self.objects:
            object.update()

    def draw(self, surface, display):
        surface.fill(self.background_color)
        for object in self.objects:
            object.draw(surface=surface)
        display.flip()
