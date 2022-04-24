import pyglet


class Screen(pyglet.window.Window):
    def __init__(self, width=1680, height=1120, title="NoName", fixed=False):
        super().__init__(width, height, title)
        if fixed:
            super().set_minimum_size(1680, 1120)
            super().set_maximum_size(1024, 768)

    def set_pixel(self, color):
        pass
