from engine2d.figures.figure import Figure


class Triangle(Figure):
    x_0, y_0 = 0, 0
    x_1, y_1 = 0, 0
    x_2, y_2 = 0, 0

    def __init__(self, x_0, y_0, x_1, y_1, x_2, y_2):
        super().__init__("Triangle")
        self.x_0, self.y_0 = x_0, y_0
        self.x_1, self.y_1 = x_1, y_1
        self.x_2, self.y_2 = x_2, y_2

    def draw(self):
        print_string = f"Drawing {self.f_type}: with points ({self.x_0, self.y_0},{self.x_1, self.y_1},{self.x_2, self.y_2})"
        print(print_string)
