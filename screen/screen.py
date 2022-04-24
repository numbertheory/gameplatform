import pyglet


class Screen(pyglet.window.Window):
    def __init__(self, width=240, height=160, title="NoName", fixed=False):
        super().__init__(width*7, height*7, title)
        if fixed:
            super().set_maximum_size(width*7, height*7)
            super().set_minimum_size(width*7, height*7)

    def set_pixel(self, color):
        pass
