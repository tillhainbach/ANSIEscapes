import json
import pyansiescapes as ansi
from pyansiescapes.pyansiescapesenums import Colors256
import logging
import sys

def _make_display_name(
        color,
        display_colorid=True,
        display_colorname=False,
        display_hex=False,
        display_rgb=False,
        display_hsl=False):
    name = ""
    info = []
    if display_colorid: name = str(color['colorId'])
    if display_colorname: info.append(color.name)
    if display_hex: info.append(color['hexString'])
    if display_rgb: info.append(_color_value_to_string(color['rgb'], 'rgb'))
    if display_hsl: info.append(_color_value_to_string(color['hsl'], 'hsl'))
    infos = ", ".join(info).rstrip(", ")
    if infos:
        name += ":"
    display_name = "{} [{}]".format(name.rjust(4), infos)

    return display_name

def _break_line(counter, after):
    if (counter + 1) % after == 0:
        print()

def _color_value_to_string(color_value, key):
    color_values = (round(val) for val in color_value.values())
    return key + "({},{},{})".format(*color_values)

def _print_color(ansi_code, display_name="", display_string_length=6):
    #print("{}{}{}m".format(drawing_level, color, additional_attributes), end="")
    return print(ansi_code + display_name.ljust(display_string_length) + ansi.reset(), end = "")

def _get_display_string_legth(display_colorid=True,
                            display_colorname=False,
                            display_hex=True,
                            display_rgb=True,
                            display_hsl=True):
    display_string_length = 6
    if display_colorname:
        name_keys = (key for key in Colors256.__members__.keys() if "_" not in key)
        display_string_length += len(max(chain(name_keys), key=len))
    if display_hex:
        display_string_length += 9
    if display_rgb:
        display_string_length += 20
    if display_hsl:
        display_string_length += 20

    return display_string_length

def color256_cheatsheet(color_data,
                        display_colorid=True, display_colorname=False,
                        display_hex=True, display_rgb=True, display_hsl=True,
                        drawing_level='foreground'):

    max_characters_per_line = 72
    display_arguments = [display_colorid, display_colorname, display_hex,
                         display_rgb, display_hsl]

    display_string_length = _get_display_string_legth(*display_arguments)
    break_line_after = int(max_characters_per_line / display_string_length)
    for color in color_data:
        color_id = color['colorId']
        ansi_code = ansi.color(color_id=color_id, drawing_level=drawing_level, colormode=256)
        display_name = _make_display_name(color, *display_arguments)
        _print_color(ansi_code, display_name, display_string_length)
        _break_line(color_id, break_line_after)

def _is_grey_tone(rgb):
    if isinstance(rgb, dict):
        rgb = rgb.values()
    r,g,b = rgb
    return r == g == b

def _is_red_tone(rgb):
    if isinstance(rgb, dict):
        rgb = rgb.values()
    r,g,b = rgb

    return r >=95 and g==0  and b <135

def filter_colors(color_data, filterkey):
    if filterkey == "greys":
        color_data = (color for color in color_data if _is_grey_tone(color['rgb']))
        color_data = sorted(color_data, key=lambda color: color['rgb']['r'])
    if filterkey == "reds":
        color_data = (color for color in color_data if _is_red_tone(color['rgb']))
        color_data = sorted(color_data, key=lambda color: color['rgb']['r'])

    return color_data

def get_unique_values(color_data, key):
    unqiues = [set(), set(), set()]
    for color in color_data:
        for i, value in enumerate(color[key].values()):
            unqiues[i].add(value)
    return unqiues

def get_unique_values_from_colors256(key):
    unqiues = [set(), set(), set()]
    color_data = (color[4:].split("_") for color in Colors256.__members__.keys() if color.startswith(key))
    for color in color_data:
        for i,value in enumerate(color):
            unqiues[i].add(int(value))
    return unqiues

if __name__ == '__main__':
    logger = logging.basicConfig(level=logging.WARN)
    with open("../Resources/color_data.json", 'r') as fh:
        json_input = fh.read()


    color_data = json.loads(json_input)
    greys = filter_colors(color_data, 'greys')
    not_greys = (color for color in color_data if color not in greys)
    val, _, _ = get_unique_values(not_greys, "rgb")
    val = sorted(val)
    print(val)

    #
    # color256_cheatsheet(color_data, drawing_level='background')
