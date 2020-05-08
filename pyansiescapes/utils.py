from .pyansiescapesenums import ANSICommands, TextAttributes, ColorDrawingLevel, Colors, Colors256
from collections.abc import Iterable
from itertools import chain
import logging
import inspect

_logger = logging.getLogger(__file__)

# Little helpers:
def any_is_not_none(*args):
    return any(arg is not None for arg in args)

def all_are_none(*args):
    return all(arg is None for arg in args)

def any_is_none(*args):
    return any(arg is None for arg in args)

def all_are_not_none(*args):
    return all(arg is not None for arg in args)

# Checkers:
def is_8bit_color(name):
    return name in Colors.__members__.keys()

def is_valid_hex_string(hex):
    return (hex.startswith("#") and len(hex) == 7 and has_only_valid_characters(hex))

_valid_hex_characters = set("#abcdef0123456789")
def has_only_valid_characters(hex):
    return set(hex) <= _valid_hex_characters

# Parses:
def parsing_switcher(argc, arg):
    switcher = {0 : get_color_id_from_id,
                1 : get_color_id_from_name,
                2 : get_color_id_from_hex,
                3 : lambda x,y: get_color_id_from_iterable(x,y, "rgb"),
                4 : lambda x,y: get_color_id_from_iterable(x,y, "hsl")
            }
    if argc == 1:
        # parse color name and then check again
        argc, arg = parse_color_name(arg)

    return switcher[argc]

def parse_drawing_level(drawing_level):
    """Parse drawing level in to legal ANSI drawing level Sequence."""
    if isinstance(drawing_level, int):
        try:
            drawing_level = list(ColorDrawingLevel)[drawing_level]
        except IndexError as E:
            raise E("Cannot parse {} into type ColorDrawingLevel".format(drawing_level))

    elif not isinstance(drawing_level, ColorDrawingLevel):
        if drawing_level in ["3", "4"]:
            drawing_level = drawing_level
        else:
            try:
                drawing_level = ColorDrawingLevel[drawing_level]
            except KeyError as E:
                raise E("Cannot parse {} into type ColorDrawingLevel".format(drawing_level))

    return drawing_level

def parse_color_arguments_into_colormode(name, color_id, hex, rgb, hsl, colormode):
    """Sets colormode based on the color arguments."""
    if any_is_not_none(hex, rgb, hsl):
        colormode = 256
    elif name is not None and name not in Colors.__members__.keys():
        colormode = 256
    elif color_id >= 16:
        colormode = 256
    return colormode

def parse_colormode(colormode, blink, bright, bold):
    """Parse colormode setters into colormode.

    Returns the colormode in int. Blink and Bright will override colormode.
    Bold overrides colormode if colormode == 8.
    setting.
    """
    if blink or bright or colormode == 256:
        colormode = 256
        return colormode
    elif bold or colormode == 16:
        colormode = 16
        return colormode
    else:
        return colormode

def parse_color_name(name):
    """Parses the color name.

    Parameters
    ----------
    name: Colors-Obj, Colors256-Obj, str, tuple, list, array-like
        A color name. Any name in Colors or Colors256. Strings with leading "#"
        will trigger hex value parsing. Tuple, list or array-like will trigger
        parsing as either rgb- or hsl-values based on the input values.
        See "_parse_rgb_or_hsl" for details on parsing logic.

    Raises
    ------
    TypeError:
        If name is not of type str, Iterable or integer it cannot be parsed and
        will raise TypeError.

    Returns
    -------
    tuple: (int, (int or tuple or list or str))
        Returns the input arguments parsed input the correct arguments.

    Examples
    --------
    # Color name string as name argument
    >>>parse_color_name(name="blue")
    (1, 'blue')

    # Hexadecimal color value as "name" argument
    >>> parse_color_name(name="#ffffff")
    (2, #ffffff)

    # Rgb-values as "name" argument
    >>> parse_color_name((255, 0, 0))
    (3, (255,0,0))

    # Color-id as "name" argument
    >>> parse_color_name(name=1)
    (0, 1)

    # Color-id string as "name" argument
    >>> parse_color_name(name="1")
    (0, 1)

    # Received incorrect argument for "name". Raise TypeError.
    >>> parse_color_name(name={k:l})
    TypeError Cannot understand "name={k:l}" input argument type

    """
    try:
        name = int(name)
    except (ValueError, TypeError):
        pass
    # if name is and interger, its a color_id
    if isinstance(name, int):
        return 0, name
    elif name.startswith('#'):
        # user input name is a hex colorvalue
        return 2, name
    elif not isinstance(name, str):
        # user provided rgb or hsl value
        if isinstance(name, Iterable):
            return 3, name
        else:
            # cannot understand input argument type
            raise TypeError("Cannot understand \"name={}\" input argument type".format(name))

    return 1, name

def parse_hex(hex):
    """Checks if hex is valid and return it in Colors256-key format.

    Parameters:
    -----------
    hex: str
        Hexadecimal color value. Must start with "#", be of lenght 7 and must be
        a valid hexadecimal value (all characters must be in set("#abcdef0123456789")).

    Raises:
    ----------
    TypeError:
        Raise TypeError if the input hex string is not valid.

    Returns:
    ----------
    str:
        The hexadecimal color value in Colors256-key-format (eg. "hex_ffffff").

    Examples:
    # Parse white hexadecimal color value into Colors256-key.
    >>> parse_hex("#ffffff")
    (hex_ffffff)

    # Raise TypeError with hexadecimal color value is wrong.
    >>> parse_hex("ffffff")
    TypeError "ffffff" is not a valid hexadecimal color value

    # Raise TypeError with hexadecimal color value is wrong.
    >>> parse_hex("#gfffff")
    TypeError "#gfffff" is not a valid hexadecimal color value
    """
    if is_valid_hex_string(hex):
        hex = 'hex_' + hex[1:]
    else:
        raise TypeError("\"{}\" is not a valid hexadecimal color value".format(hex))

    return hex

def parse_iterable(iterable, key):
    """ Parse color value to color key

    RGB-values will be clipt to their respective closest bin.
    """
    if key == "rgb":
        iterable = clip_to_closes_color(color)
    return key + '_'.join((str(val) for val in rgb))

def parse_arguments(*args):
    for argc, arg in enumerate(args):
        if arg is not None:
            yield (argc, arg)

def clip_to_closes_color(color):
    """Clips the rgb values to their respective closest bin."""
    assert isinstance(color, Iterable)

    bins = [0, 95, 135, 175, 215, 255]
    color = (round_to_next_bin(x, bins) for x in color)
    return color

def round_to_next_bin(val, bins):
    left = bisect_right(bins, val)
    print(bins[left-1], left)
    ret = get_closest(val, *bins[left-1:left+1]) if left != len(bins) else bins[left-1]
    return ret

def get_closest(val, left, right):
    ret = left if val - left < right - val else right
    return ret

# Getters:
def get_first_color_argument(*args):
    """Return first argument in args which is not None.

    Raises:
    -------
    TypeError:
        If all arguments are None.
    """
    try:
        argc, arg = next(parse_arguments(*args))
    except StopIteration:
        raise TypeError("Cannot parse 'None' into a color. Please provide a color!")

    return argc, arg

def get_color_id_from_id(color_id, colormode):
    if color_id > 8:
        colormode = 256
    return str(color_id), colormode

def get_color_id_from_color_enum(key, color_enum):
    try:
        color_id = color_enum[key]
    except IndexError as E:
        raise E("{} is not a valid color key".format(key))
    return color_id

def get_color_id_from_name(name, colormode):
    if name not in Colors.__members__.keys():
        colormode = 256
    color_enum = Colors
    if colormode == 256:
        color_enum = Colors256
    return get_color_id_from_color_enum(name.lower(), color_enum), colormode

def get_color_id_from_hex(hex, colormode):
    key = parse_hex(hex)
    return get_color_id_from_color_enum(key, Colors256)

def get_color_id_from_iterable(iterable, colormode):
    key = parse_iterable(iterable)
    return get_color_id_from_color_enum(key, Colors256)


def get_color_string(color_id, colormode):
    switcher = {8   : get_color_string_8_bit,
                16  : get_color_string_16_bit,
                256 : get_color_string_256_bit
            }
    return switcher[colormode](color_id)

def get_color_string_256_bit(color_id):
    return Colors._blink + ANSICommands.separator + \
        TextAttributes.blink + ANSICommands.separator + color_id

def get_color_string_16_bit(color_id):
    return color_id + ANSICommands.separator + TextAttributes.bold

def get_color_string_8_bit(color_id):
    return color_id

def get_all_color_arguments(func):
    return inspect.getargspec(func)


# hex: str
#     A hexadecimal color value as str. Must start with a leading "#".
#     See "_parse_hex" for details on parsing logic.
# rgb: tuple, list, array-like
#     Color values in rgb color space. Must be iterable and of length 3.
#     See "_parse_rgb_or_hsl" for details on parsing logic.
# hsl: tuple, list, array-like
#     Color values in hsl color space. Must be iterable and of lenght 3.
#     See "_parse_rgb_or_hsl" for detail on parsing logic.
