from .pyansiescapesenums import ANSICommands, TextAttributes, ColorDrawingLevel, Colors, Colors256
from collections.abc import Iterable
from itertools import chain
import logging




def _unify_color_name_string(colorname):
    """ Converts the input color name string into the appropiate format."""
    return colorname[0].upper() + colorname[1:].lower()

def _get_color_id_256(colorname=None, colorcode=None, rgb=None, hsl=None):
    """
    Trys to find the corresponding color id string from the 256 bit color palette.
    Returns None on failure.
    Accepts colorname as strings (e.g 'red'), any colorcode (as str or int '1' or 1)
    or rgb-values as anything that can be used with a *-expression.
    Uses the first argument and ignores the rest.
    """
    if colorname is not None:
        arg = _unify_color_name_string(colorname)
    elif colorcode is not None:
        arg = colorcode
    elif rgb is not None:
        arg = 'rgb_' + '_'.join((str(val) for val in rgb))
    elif hsl is not None:
        arg = 'hsl_' + "_".join((str(val) for val in hsl))
    elif hex is not None:
        arg = 'hex_' + hex[1:]

    try:
        color_id = Colors256[arg]
    except IndexError:
        color_id = None

    return color_id


def cursor_up(numberOfLines=1):
    return ANSICommands.start + "{:d}A".format(numberOfLines)


def cursor_down(numberOfLines=1):
    return ANSICommands.start + "{:d}B".format(numberOfLines)


def clear_to_end_of_line():
    return ANSICommands.start + "0K"


def clear_to_start_of_line():
    return ANSICommands.start + "1K"


def clear_line():
    return ANSICommands.start + "2K"


def erase_lines(numberOfLines=1):
    return ((clearLine() + cursor_up()) * numberOfLines)


def erase_display():
    return ANSICommands.start + "2J"


def clear_screen_until_end():
    return ANSICommands.start + "0J"


def clear_screen_to_beginning():
    return ANSICommands.start + "1J"


def bold():
    return ANSICommands.start + "1"

def _parse_drawing_level(drawing_level):
    if not isinstance(drawing_level, ColorDrawingLevel):
        try:
            drawing_level = ColorDrawingLevel[drawing_level]
        except IndexError as E:
            raise E("Cannot parse {} into type ColorDrawingLevel".format(drawing_level))

    return drawing_level

def _parse_color_name(name, hex, rgb, hsl):
    print(name, hex, rgb, hsl)
    if not any((name, hex, rgb, hsl)):
        # do nothing
        return
    if not isinstance(name, str) and name is not None:
        # user provide rgb value
        if isinstance(name, Iterable):
            rgb = name
            name = None
        else:
            # cannot understand input argument type
            raise TypeError

    if name.startswith('#'):
        # user input name is a hex colorvalue
        hex = name
        name = None

    return (name, hex, rgb, hsl)

def _parse_color_arguments(name, color_id, hex, rgb, hsl):
    if all((name, color_id, hex, rgb, hsl)) is None:
        raise TypeError("Cannot parse 'None' into a color. Please provide a color!")
    if any((hex, rgb, hsl)) is not None:
        blink = bright = bold = True
        return (bold, blink, bright)
    if name is not None and name not in Colors.__members__.keys():
        blink = bright = bold = True
        return (bold, blink, bright)
    if color_id > 8 and colorid < 16:
        bold = True
    elif color_id >= 16:
        blink = bright = True


    return (bold, blink, bright)

def _parse_colormode(colormode, bold, blink, bright):
    """Parse colormode setters into colormode

    Returns the colormode in int. Bold, blink and bright will override colormode
    setting.
    """
    if blink or bright:
        colormode = 256
        return colormode
    elif bold and not any((blink, bright)):
        colormode = 16
        return colormode
    elif not any((bold, blink, bright)):
        colormode = 8
        return colormode
    else:
        return colormode

def _get_color_string(name, color_id, hex, rgb, hsl, colormode):
    if colormode == 256:
        color_id = _get_color_id_256(name, hex, rgb, hsl)
        color_string = Colors._blink + ANSICommands.separator + \
            TextAttributes.blink + ANSICommands.separator + color_id
    elif colormode == 16:
        color_id = Colors[name]
        color_string = color_id + ANSICommands.separator + TextAttributes.bold
    else:
        color_string = Colors[name]
    return color_string


def color(name = None,  # color name as sting, hex string, rgb tuple/list
          drawing_level = ColorDrawingLevel.foreground,  # color foreground or background
          bold=False,  # toggle bold colors (16bit support needed)
          # toggle blink or bright mode (both are provided for convenience)
          # 256 bit color support needed
          blink=False, bright=False,
          colormode=None,  # gets overwritten by bold or bright/blink, provided for convenience
          color_id=None, rgb=None, hex=None, hsl=None):


    drawing_level = _parse_drawing_level(drawing_level)
    name, hex, rgb, hsl = _parse_color_name(name, hex, rgb, hsl)
    bold, blink, bright = _parse_color_arguments(name, color_id, hex, rgb, hsl)
    colormode = _parse_colormode(colormode, bold, blink, bright)
    color_string = _get_color_string(name, color_id, hex, rgb, hsl, colormode)

    return _format_rich_text(drawing_level + color_string)

def _format_rich_text(*formatting_commands):
    outString = ANSICommands.start
    logging.debug("_format_rich_text received: {}".format(", ".join(formatting_commands)))
    outString += ANSICommands.separator.join(formatting_commands)
    outString += ANSICommands.stop
    logging.debug(debug_ANSICommands.start + outString[1:])
    return outString

def _is_8bit_color(name):
    return name in Colors.__members__.keys()


def format(text="", *args, **kwargs) -> str:
    """Return formatted text as str.

    Uses the formatting attributes given in *args or **kwargs.
    Postional arguments or keywordarguments that are not supported
    will be ignored.
    Parameters
    -----------
        text : str
            The text/string that should be formatted.
        args : any
            Any number of postional arguments. Unsupported arguments will be
            ignored. See "supported arguments" section for futher details.
        **kwargs : any
            Any number of keyword arguments. Unsupported keyword arguments
            will be ignored. See "supported keywords" section for further
            details.

    Returns
    -------
    string
        The text with leading ANSI ANSICommands.startape sequences "rich text" commands and
        a trailing ANSI ANSICommands.startape sequences "reset" command.

    Example
    -------
    >>> format('Hello ANSI!', color = 'blue', background = 'white'))
    \u001b[38;5;12;48;5;15mHello ANSI!\u001b[0m
    """
    text_attribute_arguments = (
        arg for arg in args if arg in TextAttributes.__members__.keys())
    color_keys = (
        key for key in chain(
            Colors.__members__.keys(),
            Colors256.__members__.keys()))
    color_arguments = (arg for arg in args if arg in color_keys)

    return _format_rich_text(*args, **kwargs) + text + resetFormatting()


def color8(name, drawing_level=ColorDrawingLevel.foreground):
    if _is_8bit_color(name):
        return _format_rich_text(drawing_level + Colors[name])
    else:
        return ""


def background(colorName):
    return color8(colorName, drawing_level=ColorDrawingLevel.background)


def black(drawing_level=ColorDrawingLevel.foreground):
    return color8("black")


def red(drawing_level=ColorDrawingLevel.foreground):
    return color8("red")


def green(drawing_level=ColorDrawingLevel.foreground):
    return color8("green")


def yellow(drawing_level=ColorDrawingLevel.foreground):
    return color8("yellow")


def blue(drawing_level=ColorDrawingLevel.foreground):
    return color8("blue")


def magenta(drawing_level=ColorDrawingLevel.foreground):
    return color8("magenta")


def cyan(drawing_level=ColorDrawingLevel.foreground):
    return color8("cyan")


def white(drawing_level=ColorDrawingLevel.foreground):
    return color8("white")


def reset():
    return _format_rich_text(TextAttributes.reset)


def bold():
    return _format_rich_text(TextAttributes.bold)


def underscore():
    return _format_rich_text(TextAttributes.underscore)


def underline():
    return _format_rich_text(TextAttributes.underline)


def bright():
    return _format_rich_text(TextAttributes.bright)


def blink():
    return _format_rich_text(TextAttributes.blink)


def reversed():
    return _format_rich_text(TextAttributes.reversed)


def concealed():
    return _format_rich_text(TextAttributes.concealed)
