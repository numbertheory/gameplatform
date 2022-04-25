import pyglet
from pyglet import shapes


class Screen(pyglet.window.Window):
    def __init__(self, width=240, height=160,
                 factor=6, title="NoName", fixed=False):
        super().__init__(width*factor, height*factor, title)
        self.time = 0
        self.batch = pyglet.graphics.Batch()
        self.height = height
        self.width = width
        self.factor = factor
        self.title = title
        self.pixel = []

        if fixed:
            super().set_maximum_size(width*factor, height*factor)
            super().set_minimum_size(width*factor, height*factor)

    def pixel_system(self, x, y):
        _width = self.width - 1
        _height = self.height - 1
        _x = x * self.factor
        _y = ((y*-1 + 159) * self.factor)
        f = self.factor
        return [(_width * f) - _width * f + _x,
                (_height * f) - _height * f + _y]

    def set_pixel(self, pixel, color):
        pixel = self.pixel_system(pixel[0], pixel[1])
        self.pixel.append(shapes.Rectangle(
                           pixel[0],
                           pixel[1],
                           self.factor, self.factor,
                           color=color, batch=self.batch))

    def update(self, delta_time):
        self.time += delta_time
        self.clear()
        self.batch.draw()

    def on_draw(self):
        """Clear the screen and draw shapes"""
        self.clear()
        self.batch.draw()
