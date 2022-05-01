from screen import Screen
from sprite import Sprites


class Scene():
    def __init__(self, **kwargs):
        self.sprites = Sprites(kwargs.get("sprites"))
        self.pixel_sprites = []
        self.window = Screen(
            title=kwargs.get("title"),
            fixed=kwargs.get("fixed", False),
            height=kwargs.get("height"),
            width=kwargs.get("width"),
            pixel_sprites=self.pixel_sprites)

    def load_scene(self):
        pass
