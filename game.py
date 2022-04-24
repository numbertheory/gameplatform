import pyglet
from screen.screen import Screen


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    for y in range(1, 159):
        for x in range(1, 239):
            main_screen.set_pixel(pixel=(x, y*-1), color=(255, y, x))
    pyglet.app.run()
