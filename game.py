import pyglet
from tickytacky.screen.screen import Screen
import json


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    with open("snail_sprite.json", "r") as json_file:
        snail = json.load(json_file)
    sprite = main_screen.add_sprite(data=snail, location=[0, 100], group=1)
    pyglet.app.run()
