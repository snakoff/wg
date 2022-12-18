from engine2d.figures.figure import Figure


class Circle(Figure):
    x, y = 0, 0

    def __init__(self, x, y, radius):
        super().__init__("Circle")
        self.__x = x
        self.__y = y
        self.__radius = radius

    def draw(self):
        print_string = f"Drawing {self.f_type}: {self.__x, self.__y} with radius {self.__radius}"
        print(print_string)
