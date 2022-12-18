import sys
from contextlib import contextmanager
from io import StringIO

import allure
import pytest

from engine2d.engine2D import Engine2D, Color
from engine2d.figures.circle import Circle
from engine2d.figures.rectangle import Rectangle
from engine2d.figures.triangle import Triangle


class TestClass:
    engine = Engine2D()

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    @allure.title("Add and draw figures test")
    def test_add_and_draw_figures(self):
        self.engine = Engine2D()
        self.add_figure(Triangle(0, 0, 1, 1, 2, 0))
        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert output in 'Drawing Triangle: with points ((0, 0),(1, 1),(2, 0))\nColor is: black'

        self.add_figure(Circle(0, 0, 3))
        self.add_figure(Rectangle(2, 2, 4, 5))
        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert output in 'Drawing Circle: (0, 0) with radius 3\nColor is: black\nDrawing Rectangle: with start ' \
                         'point (2, 2), length: 4, width: 5\nColor is: black'

    @allure.title("Empty canvas after draw test")
    def test_empty_canvas_after_draw(self):
        self.engine = Engine2D()
        self.add_figure(Rectangle(2, 2, 4, 5))

        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert 'Drawing Rectangle: with start point (2, 2), length: 4, width: 5\nColor is: black' in str(output)

        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert '' in str(output)

    @allure.title("Change color test")
    def test_change_color(self):
        self.engine = Engine2D()
        self.add_figure(Triangle(0, 0, 1, 1, 2, 0))
        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert output in 'Drawing Triangle: with points ((0, 0),(1, 1),(2, 0))\nColor is: black'

        self.change_color("green")
        self.add_figure(Circle(0, 0, 3))

        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert output in 'Drawing Circle: (0, 0) with radius 3\nColor is: green'

        self.engine.reset_color()
        self.add_figure(Rectangle(2, 2, 4, 5))

        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert output in 'Drawing Rectangle: with start point (2, 2), length: 4, width: 5\nColor is: black'

    @allure.title("Right queue draw test")
    def test_right_queue_draw(self):
        self.engine = Engine2D()
        self.add_figure(Triangle(1, 1, 2, 2, 3, 1))
        self.change_color("Red")
        self.add_figure(Rectangle(2, 2, 4, 5))
        self.change_color("bluE")
        self.add_figure(Circle(0, 0, 3))
        self.change_color("gReEn")
        self.add_figure(Circle(2, 2, 6))
        self.change_color("BLACK")
        self.add_figure(Rectangle(5, 5, 2, 6))

        with self.captured_output() as (out, err):
            self.draw_figure()
        output = out.getvalue().strip()
        assert output in 'Drawing Triangle: with points ((1, 1),(2, 2),(3, 1))\nColor is: black\n' \
                         'Drawing Rectangle: with start point (2, 2), length: 4, width: 5\nColor is: red\n' \
                         'Drawing Circle: (0, 0) with radius 3\nColor is: blue\n' \
                         'Drawing Circle: (2, 2) with radius 6\nColor is: green\n' \
                         'Drawing Rectangle: with start point (5, 5), length: 2, width: 6\nColor is: black\n'

    @allure.title("Add not figure test")
    def test_add_not_figure(self):
        engine = Engine2D()
        with pytest.raises(Exception) as ex:
            self.add_figure("figure")
        assert str(ex.value) in "Sorry, argument must be a Figure"

    @allure.title("Wrong color test")
    def test_wrong_color(self):
        engine = Engine2D()
        with pytest.raises(Exception) as ex:
            self.change_color("yellow")
        assert str(ex.value) in f"Sorry, color must be in {[c.value for c in Color]}"

    @allure.step("Add figure")
    def add_figure(self, figure):
        self.engine.add_figure(figure)

    @allure.step("Draw")
    def draw_figure(self):
        self.engine.draw()

    @allure.step("Change color to {color}")
    def change_color(self, color):
        self.engine.change_color(color)
