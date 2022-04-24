import pyglet
from screen.screen import Screen


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    for y in range(0, 160):
        for x in range(0, 240):
            main_screen.set_pixel(pixel=(x, y), color=(255, y, x))
    pyglet.app.run()
