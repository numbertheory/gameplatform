import pyglet


class Screen(pyglet.window.Window):
    def __init__(self, width=240, height=160,
                 factor=7, title="NoName", fixed=False):
        super().__init__(width*factor, height*factor, title)
        if fixed:
            super().set_maximum_size(width*factor, height*factor)
            super().set_minimum_size(width*factor, height*factor)

    def set_pixel(self, color):
        pass
