# Tickytacky

[![tickytacky pypi shield](https://img.shields.io/pypi/v/tickytacky)](https://pypi.org/project/tickytacky/)

## Description

This library aims to make it easy to make retro-style games with Pyglet.

## Examples

Examples can be found here, in the examples, repo:

[Tickytacky Examples](https://github.com/numbertheory/tickytacky-examples)

## Sprite Maker

Open tools/sprite_maker.html in a web browser to use the sprite maker. It's a small
tool that allows you to draw sprites and copy the code as JSON.

Example:
```
firefox tools/sprite_maker16.html

or

firefox tools/sprite_maker32.html

```

1. Select colors from the large color button. It's an HTML5 color selector, so it will
use your system's color picker to select any color.

2. Click the "Create Color option" to add it to the palette.

3. Choose that color from the palette options and draw with it. Name the color something in the palette.

4. If you remove a color from the palette, all pixels with that color will also be removed.

5. When done drawing, name the sprite and click the "Copy JSON to Clipboard" button. This will put the sprite information into the clipboard in JSON format.

6. Copy that info into a JSON file in your game.
