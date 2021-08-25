class CommonFunctionality:

    id_counter = -1

    @staticmethod
    def __add_id_counter():
        CommonFunctionality.id_counter += 1
        return CommonFunctionality.id_counter

    default_surface = None

    @staticmethod
    def __get_default_surface():
        if CommonFunctionality.default_surface == None:
            from main2 import surface
            CommonFunctionality.default_surface = surface
        return CommonFunctionality.default_surface


    def __init__(self, surface=None):
        self.surface = surface or CommonFunctionality.__get_default_surface()
        self.id = CommonFunctionality.__add_id_counter()

    def get_surface(self):
        return self.surface

    def set_surface(self, value):
        self.surface = value


    def control(self):
        pass


    def update(self):
        pass


    def draw(self):
        pass



class Background(CommonFunctionality):
    def __init__(self, color=(0, 0, 0)):
        super().__init__()
        self.color = color

    def draw(self):
        super().draw()
        self.surface.fill(self.color)
