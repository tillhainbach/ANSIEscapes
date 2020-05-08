from .pyansiescapesenums import ANSICommands, TextAttributes, ColorDrawingLevel, Colors, Colors256
from . import utils
from collections.abc import Iterable
from itertools import chain
import logging
import inspect

_logger = logging.getLogger(__file__)
# Curser controls:


def cursor_up(numberOfLines=1):
    return ANSICommands.start + "{:d}A".format(numberOfLines)


def cursor_down(numberOfLines=1):
    return ANSICommands.start + "{:d}B".format(numberOfLines)

# Clearers:


def clear_to_end_of_line():
    return ANSICommands.start + "0K"


def clear_to_start_of_line():
    return ANSICommands.start + "1K"


def clear_line():
    return ANSICommands.start + "2K"


def clear_lines(numberOfLines=1):
    return ((clear_line() + cursor_up()) * numberOfLines)


def clear_screen_until_end():
    return ANSICommands.start + "0J"


def clear_screen_to_beginning():
    return ANSICommands.start + "1J"


def clear_screen():
    return ANSICommands.start + "2J"


# Rich Text formatting:
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
    # Format text to bold and underlined using postional arguments
    >>> format('Hello ANSI!', 'bold', 'underline')
    \'\\x1b[1;4mHello ANSI!\\x1b[0m\'

    # It's also possible to use keyword arguments with True, False
    >>> format('Hello ANSI!', bold=True, underline=True)
    \'\\x1b[1;4mHello ANSI!\\x1b[0m\'

    # You can also set and color and background color
    >>> format('Hello ANSI!', color = 'blue', background = 'white')
    \'\\x1b[34;47mHello ANSI!\\x1b[0m\'

    >>> format('Hello ANSI!', color = {'name':'blue', 'colormode':256}, background = 'white')
    \'\\x1b[38;5;12;47mHello ANSI!\\x1b[0m\'
    """
    # parse positional text attributes
    text_attribute_arguments = (
        arg for arg in args if arg in TextAttributes.__members__.keys())
    # parse keyword text attribute arguments:
    text_attribute_keywords = (
        kwarg for kwarg in kwargs.keys() if kwarg and kwarg in TextAttributes.__members__.keys()
    )
    text_attributes = (
        TextAttributes[key] for key in chain(
            text_attribute_arguments,
            text_attribute_keywords))
    # parse positional
    color_attributes = []
    for i, key in enumerate(["color", "background"]):
        try:
            value = kwargs[key]
        except KeyError:
            continue
        if isinstance(value, tuple) or isinstance(value, list):
            attribute = _color(*value, drawing_level=i)
        elif isinstance(value, dict):
            attribute = _color(**value, drawing_level=i)
        else:
            attribute = _color(value, drawing_level=i)

        color_attributes.append(attribute)

    return _format_rich_text(
        *text_attributes, *color_attributes) + text + reset()

# TextAttributes:


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


# Colors:
def color(*args, **kwargs):
    """Return ANSI Escape Sequence for specified color.

    Color value argument get parsed in this order:
    colorid, name, hex, rgb, hsl.

    Colormode gets toggled in this order:
    Conditions for 256-bit colormode are checked first:
        color_id is not None and color_id > 8 --> 256-bit colormode
        name not in Colors or name is hex or rgb or hsl --> 256-bit colormode
        any(hex, rgb, hsl) --> 256-bit colormode
        bright or blink or colormode == 256 --> 256-bit colormode

    Next the condition for 16-bit colormode are checked:
        ((color_id < 8 or name in Colors) and bold) or colormode == 16 --> 16-bit colormode

    If none of the above conditions are true, fallback to default 8-bit colormode.

    Parameters:
    name: Colors-Obj, Colors256-Obj, integer, str, tuple, list, array-like
        A color name. Any name in Colors or Colors256.
        Integers or Integer-strings will tripper color id parsing.
        Strings with leading "#" will trigger hex value parsing.
        Tuple, list or array-like will trigger parsing as either rgb- or
        hsl-values based on the input values.
        See "_parse_rgb_or_hsl" for details on parsing logic.
    color_id: int
        The color id as integer or integer-string.
        Default: None
    hex: str
        A hexadecimal color value as str. Must start with a leading "#".
        See "_parse_hex" for details on parsing logic.
        Default: None
    rgb: tuple, list, array-like
        Color values in rgb color space. Must be iterable and of length 3.
        See "_parse_rgb_or_hsl" for details on parsing logic.
        Default: None
    hsl: tuple, list, array-like
        Color values in hsl color space. Must be iterable and of lenght 3.
        See "_parse_rgb_or_hsl" for detail on parsing logic.
        Default: None
    drawing_level: str or ColorDrawingLevel-Obj
        The color drawing level.
        Valid foreground values are:
            "foreground", ColorDrawingLevel.foreground, 0, "3"
        Valid background values are:
            "background", ColorDrawingLevel.background, 1, "4"
        Default: "foreground"
    bold: boolean, or parseable to boolean
        Triggers bold colors (16-bit).
        Default: False
    blink: boolean, or parseable to boolean
        Triggers "blink/birght" colors (256-bit).
        Deafault: False
    bright: boolean, or parseable to boolean
        Triggers "blink/birght" colors (256-bit).
        Default: False
    colormode: integer or integer-string.
        Triggers 8-, 16-, or 256-bit colors. Any in (8, 16, 256).
        Default: 8

    Raises:
    -------
    TypeError:
        If all color arguments are None.

    Returns:
    str
        ANSI Escape Sequences for the specified color

    Examples:
    ---------
    # Get string for 8-bit red text coloring (e.g. foreground).
    >>> color(name="red")
    \'\\x1b[31m\'

    # Get string for bold red background.
    >>> color(name="red", bold=True, drawing_level="background")
    \'\\x1b[41;1m\'

    # Get string for 256-bit red background.
    >>> color(name="red", bold=True, blink=True, drawing_level="background")
    \'\\x1b[48;5;9m\'

    # Get string for mediumspringgreen foreground 256-bit color.
    >>> color(name="mediumspringgreen")
    \'\\x1b[38;5;49m\'

    """
    return _format_rich_text(_color(*args, **kwargs))


def _color(name=None,  # color name as sting, hex string, rgb tuple/list
           color_id=None,
           hex=None,
           rgb=None,
           hsl=None,
           drawing_level=ColorDrawingLevel.foreground,  # color foreground or background
           bold=False,  # toggle bold colors (16bit support needed)
           # toggle blink or bright mode (both are provided for convenience)
           # 256 bit color support needed
           blink=False, bright=False,
           colormode=8):  # gets overwritten by bold or bright/blink, provided for convenience
    # Parse drawing level
    drawing_level = utils.parse_drawing_level(drawing_level)
    colormode = utils.parse_colormode(colormode, blink, bright, bold)
    _logger.debug("{}".format(colormode))
    # Check if a valid color was provided
    argc, arg = utils.get_first_color_argument(color_id, name, hex, rgb, hsl)
    # Look-up correct get color id function
    get_color_id = utils.parsing_switcher(argc, arg)
    color_id, colormode = get_color_id(arg, colormode)
    _logger.debug("{}, {}".format(color_id, colormode))
    color_string = utils.get_color_string(color_id, colormode)

    return drawing_level + color_string

# convenience functions:


def color_8bit(name, drawing_level=ColorDrawingLevel.foreground):
    if utils.is_8bit_color(name):
        return _format_rich_text(drawing_level + Colors[name])
    else:
        return ""


def background(name):
    return color(name, drawing_level=ColorDrawingLevel.background)


def black(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("black")


def red(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("red")


def green(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("green")


def yellow(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("yellow")


def blue(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("blue")


def magenta(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("magenta")


def cyan(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("cyan")


def white(drawing_level=ColorDrawingLevel.foreground):
    return color_8bit("white")


def _format_rich_text(*formatting_commands):
    outString = ANSICommands.start
    logging.debug(
        "_format_rich_text received: {}".format(
            ", ".join(formatting_commands)))
    outString += ANSICommands.separator.join(formatting_commands)
    outString += ANSICommands.stop
    logging.debug(ANSICommands._debug_esc + outString[1:])
    return outString


if __name__ == '__main__':
    import doctest
    doctest.testmod()
