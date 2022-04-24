import pyglet

class Screen(pyglet.window.Window):
    def __init__(self, width=1680, height=1120, title="NoName"):
        super().__init__(width, height, title)
