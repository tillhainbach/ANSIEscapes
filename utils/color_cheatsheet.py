import json
import pyansiescapes as ansi
from pyansiescapes.pyansiescapesenums import Colors256

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

def _break_line(counter, after):
    if (counter + 1) % after == 0:
        print()

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

def color256_cheatsheet(display_colorid=True, display_colorname=False,
                        display_hex=True, display_rgb=True, display_hsl=True,
                        drawing_level='foreground'):

    max_characters_per_line = 72
    display_arguments = [display_colorid, display_colorname, display_hex,
                         display_rgb, display_hsl]

    display_string_length = _get_display_string_legth(*display_arguments)
    break_line_after = int(max_characters_per_line / display_string_length)
    for color in color_data:
        color_id = color['colorId']
        ansi_code = ansi.color(color_id=color_id, drawing_level=drawing_level)
        display_name = _make_display_name(color, *display_arguments)
        _print_color(ansi_code, display_name)
        _break_line(int(color))



if __name__ == '__main__':
    with open("../Resources/color_data.json", 'r') as fh:
        json_input = fh.read()

    color_data = json.loads(json_input)

    color256_cheatsheet(json)
