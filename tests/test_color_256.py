from pyansiescapes.pyansiescapes import ColorDrawingLevel, Colors, Colors256
from itertools import chain
from collections.abc import Iterable
import sys

def _print_color(color = "0", colormode = "", color256 = "", drawing_level = "3", display_name = "",display_string_length=6):
    additional_attributes = (";" + ";".join((colormode, color256))).rstrip(";")
    ansi = "\u001b[{}{}{}m".format(drawing_level, color, additional_attributes)
    #print("{}{}{}m".format(drawing_level, color, additional_attributes), end="")
    return print(ansi + display_name.ljust(display_string_length) + "\u001b[0m", end = "")

def _break_line(counter, after):
    if (counter + 1) % after == 0:
        print()

def _make_display_name(
        color,
        display_colorid=True,
        display_colorname=False,
        display_hex=False,
        display_rgb=False,
        display_hsl=False):
    name = ""
    info = []
    if display_colorid: name = color + ":"
    if display_colorname: info.append(color.name)
    if display_hex: info.append(_find_value(color, "hex_"))
    if display_rgb: info.append(_find_value(color, "rgb_"))
    if display_hsl: info.append(_find_value(color, "hsl_"))
    infos = ", ".join(info).rstrip(", ")
    display_name = "{} [{}]".format(name, infos)

    return display_name


def _find_value(color, prefix):
    if not isinstance(color, Colors256):
        value = ""
    else:
        try:
            value = next((key for key, value in Colors256.__members__.items() if value == color.value and key.startswith(prefix)))[4:]
            if prefix == "hex_":
                value = "#" + value
            else:
                value = prefix[:-1] + "({},{},{})".format(*(val for val in value.split("_")))
        except StopIteration:
            value = ""
    return value

def print_colors(
        colormodes=[8],
        display_colorid=True,
        display_colorname=False,
        display_hex=True,
        display_rgb=True,
        display_hsl=True,
        drawing_level='foreground',
        ):

    if not isinstance(drawing_level, ColorDrawingLevel):
        drawing_level = ColorDrawingLevel[drawing_level]

    if any((display_hex, display_rgb, display_hsl)):
        # just display 256 bit colors
        colormodes = [256]

    display_string_length = 6
    max_characters_per_line = 72
    iter_dict = {8 : [Colors],
                16 : [Colors, Colors],
                256 : [Colors256]}
    iters = [_enum for colormode in colormodes for _enum in iter_dict[colormode]]
    if display_colorname:
        name_keys = (key for _enum in iters for key in _enum.__members__.keys() if "_" not in key)
        display_string_length += len(max(chain(name_keys), key=len))
    if display_hex:
        display_string_length += 9
    if display_rgb:
        display_string_length += 20
    if display_hsl:
        display_string_length += 20
    break_line_after = int(max_characters_per_line / display_string_length)

    for colormode in colormodes:
        colormode_string = ""
        color256 = ""
        for color in chain.from_iterable(iter_dict[colormode]):
            display_name = _make_display_name(color, display_colorid, display_colorname, display_hex, display_rgb, display_hsl)
            color_int = int(color)
            if color.name ==  "_blink":
                    colormode_string = "1"
                    print()
                    continue
            if isinstance(color, Colors256):
                color256 = color
                color = Colors._blink
                colormode_string = "5"
            _print_color(color, colormode_string, color256 = color256, drawing_level = drawing_level, display_name = display_name, display_string_length=display_string_length)
            _break_line(color_int, break_line_after)
        print("")

if __name__ == '__main__':
    print_colors([8, 16, 256], display_colorname=True, drawing_level = 'background')
