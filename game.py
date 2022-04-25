import pyglet
from tickytacky.screen.screen import Screen


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    data = {"palette":
            {"red": (255, 0, 0),
             "bg": None},
            "location": [100, 100],
            "shape": [["red", "bg", "red", "bg"]]}
    main_screen.add_sprite(data, 1)
    pyglet.app.run()
