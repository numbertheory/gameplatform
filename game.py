import pyglet
from tickytacky.screen.screen import Screen
import json

main_screen = Screen(title="game", fixed=True)


def on_draw():
    main_screen.clear()
    main_screen.batch.draw()


def init():
    load_sprite([10, 10])


def load_sprite(location):
    with open("snail_sprite.json", "r") as json_file:
        snail = json.load(json_file)
    main_screen.add_sprite(data=snail, location=location)


def update(dt):
    load_sprite([200, 200])
    on_draw()


if __name__ == "__main__":
    # Start it up!
    init()

    pyglet.clock.schedule_interval(update, 5)

    pyglet.app.run()
