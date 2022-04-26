import pyglet
from tickytacky.screen import Screen
import json

with open("snail_sprite.json", "r") as json_file:
    snail = json.load(json_file)

main_screen = Screen(title="game",
                     fixed=True,
                     pixel_sprites=[{"name": "snail",
                                     "data": snail,
                                     "location": [10, 10]}])


def init():
    main_screen.add_sprite("snail", [10, 10])


def update(dt):
    old_loc = main_screen.sprites["snail"]["location"]
    new_loc = [old_loc[0] + 1, old_loc[1]]
    main_screen.add_sprite("snail", new_loc)
    pass


if __name__ == "__main__":
    # Start it up!
    init()

    pyglet.clock.schedule_interval(update, 1/12)

    pyglet.app.run()
