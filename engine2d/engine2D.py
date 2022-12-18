from enum import Enum

from engine2d.figures.figure import Figure


class Color(Enum):
    BLACK = "black"
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Engine2D:
    color = "black"
    canvas = list()

    def add_figure(self, figure):
        if isinstance(figure, Figure):
            self.canvas.append([self.color, figure])
        else:
            raise Exception("Sorry, argument must be a Figure")

    def change_color(self, color):
        local_color = color.lower()
        if local_color == Color.BLACK.value \
                or local_color == Color.RED.value \
                or local_color == Color.BLUE.value \
                or local_color == Color.GREEN.value:
            self.color = local_color
        else:
            raise Exception(f"Sorry, color must be in {[c.value for c in Color]}")

    def reset_color(self):
        self.color = "black"

    def draw(self):
        for fig in self.canvas:
            fig[1].draw()
            print(f"Color is: {fig[0]}")
        self.canvas.clear()
        
