import pyglet
from screen.screen import Screen


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    pyglet.app.run()
