import pyglet
from tickytacky.screen.screen import Screen
import json


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    with open("snail_sprite.json", "r") as json_file:
        data = json.load(json_file)
    main_screen.add_sprite(data, 1)
    pyglet.app.run()
