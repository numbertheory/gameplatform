from tickytacky.screen import Screen
from tickytacky.sprite import Sprites, Tiles
from pyglet.sprite import Sprite
import json


class Scene():
    def __init__(self, **kwargs):
        self.sprites = Sprites(kwargs.get("sprites"))
        self.window = Screen(
            title=kwargs.get("title"),
            fixed=kwargs.get("fixed", False),
            height=kwargs.get("height"),
            width=kwargs.get("width"),
            pixel_sprites=self.sprites.pixel_sprites)
        self.tiles = Tiles(tile_files=kwargs.get("tile_files", []))
        self.scenes = self.scene_data(scene_data=kwargs.get("scene_data"))
        self.current_scene = "scene1"

    def load_scene(self, new_scene):
        self.current_scene = new_scene
        self.scene = []
        for tile in self.scenes[new_scene]:
            x = tile[1]
            y = tile[2]
            self.scene.append(
                Sprite(self.tiles.tile_data[tile[0]],
                       x=x, y=y, batch=self.window.batch)
            )
        self.window.batch.draw()

    def scene_data(self, scene_data):
        if scene_data:
            with open(scene_data, "r") as json_file:
                scenes = json.load(json_file)
            return scenes
