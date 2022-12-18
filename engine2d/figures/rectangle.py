from engine2d.figures.figure import Figure


class Rectangle(Figure):
    x, y = 0, 0
    length, width = 0, 0

    def __init__(self, x, y, length, width):
        super().__init__("Rectangle")
        self.x, self.y = x, y
        self.length, self.width = length, width

    def draw(self):
        print_string = f"Drawing {self.f_type}: with start point {self.x, self.y}" \
                       f", length: {self.length}, width: {self.width}"
        print(print_string)
