import pyglet
from tickytacky.screen.screen import Screen


if __name__ == "__main__":
    main_screen = Screen(title="game", fixed=True)
    for y in range(50, 100):
        for x in range(50, 100):
            main_screen.set_pixel(pixel=(x, y), color=(0, 0, 255))
    # pyglet.clock.schedule_interval(main_screen.update, 10)
    pyglet.app.run()
