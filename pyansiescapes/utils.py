from .pyansiescapesenums import ANSICommands, TextAttributes, ColorDrawingLevel, Colors, Colors256
from collections.abc import Iterable
from itertools import chain
import logging
import inspect

_logger = logging.getLogger(__file__)
#--------------------- Parsers ------------------------------
def parsing_switcher(argc, arg):
    """Return get color_id function for argument arg.

    If argument is 'name', parse name first to check if user did not
    provide a hexadecimal, rgb or hsl value.

    Parameters:
    argc: int
        The positional argument count [1-4] which specifies the argument type.

    arg: int, str, tuple, list.
        The color argument.

    Return:
    -------
    func-obj
        The get_color_id_from_{type} function obj.
    """
    switcher = {0: get_color_id_from_id,
                1: get_color_id_from_name,
                2: get_color_id_from_hex,
                3: lambda x, y: get_color_id_from_iterable(x, y, "rgb"),
                4: lambda x, y: get_color_id_from_iterable(x, y, "hsl")
                }
    if argc == 1:
        # parse color name and then check again
        argc, arg = parse_color_name(arg)

    return switcher[argc]


def parse_drawing_level(drawing_level):
    """Parse drawing level into legal ANSI drawing level Sequence."""
    if isinstance(drawing_level, int):
        try:
            drawing_level = list(ColorDrawingLevel)[drawing_level]
        except IndexError as E:
            raise E(
                "Cannot parse {} into type ColorDrawingLevel".format(drawing_level))

    elif not isinstance(drawing_level, ColorDrawingLevel):
        if drawing_level in ["3", "4"]:
            drawing_level = drawing_level
        else:
            try:
                drawing_level = ColorDrawingLevel[drawing_level]
            except KeyError as E:
                raise E(
                    "Cannot parse {} into type ColorDrawingLevel".format(drawing_level))

    return drawing_level


def parse_color_arguments_into_colormode(
        name, color_id, hex, rgb, hsl, colormode):
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
    >>> parse_color_name(name="blue")
    (1, 'blue')

    # Hexadecimal color value as "name" argument
    >>> parse_color_name(name="#ffffff")
    (2, '#ffffff')

    # Rgb-values as "name" argument
    >>> parse_color_name((255, 0, 0))
    (3, (255, 0, 0))

    # Color-id as "name" argument
    >>> parse_color_name(name=1)
    (0, 1)

    # Color-id string as "name" argument
    >>> parse_color_name(name="1")
    (0, 1)

    # Received incorrect argument for "name". Raise TypeError.
    >>> parse_color_name(name=None)
    Traceback (most recent call last):
        ...
    TypeError: Cannot understand \"name=None\" input argument type

    """
    try:
        name = int(name)
    except (ValueError, TypeError):
        pass
    # if name is and interger, its a color_id
    if isinstance(name, int):
        return 0, name
    elif not isinstance(name, str):
        # user provided rgb or hsl value
        if isinstance(name, Iterable):
            return 3, name
        else:
            # cannot understand input argument type
            raise TypeError(
                "Cannot understand \"name={}\" input argument type".format(name))
    elif name.startswith('#'):
        # user input name is a hex colorvalue
        return 2, name

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
    'hex_ffffff'

    # Raise TypeError with hexadecimal color value is wrong.
    >>> parse_hex("ffffff")
    Traceback (most recent call last):
        ...
    TypeError: \"ffffff\" is not a valid hexadecimal color value

    # Raise TypeError with hexadecimal color value is wrong.
    >>> parse_hex("#gfffff")
    Traceback (most recent call last):
        ...
    TypeError: \"#gfffff\" is not a valid hexadecimal color value
    """
    if is_valid_hex_string(hex):
        hex = 'hex_' + hex[1:]
    else:
        raise TypeError(
            "\"{}\" is not a valid hexadecimal color value".format(hex))

    return hex


def parse_iterable(iterable, key):
    """ Parse color value to color key

    RGB-values will be cliped to their respective closest bin.
    """
    if key == "rgb":
        iterable = clip_to_closes_color(color)
    return key + '_'.join((str(val) for val in rgb))


def parse_arguments(*args):
    """Return generator over arguments that are not None."""
    for argc, arg in enumerate(args):
        if arg is not None:
            yield (argc, arg)


def clip_to_closes_color(color):
    """Clips the rgb values to their respective closest bin."""
    assert isinstance(color, Iterable)

    bins = [0, 95, 135, 175, 215, 255]
    color = (_round_to_next_bin(x, bins) for x in color)
    return color


def _round_to_next_bin(val, bins):
    """Return the bin in bins closest to value."""
    right = bisect_right(bins, val)
    left = right - 1
    ret = _get_closest(val, *bins[left:right+ 1]
                       ) if right != len(bins) else bins[left]
    return ret


def _get_closest(val, left, right):
    """Return left or right depending on which is closer to val"""
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
        raise TypeError(
            "Cannot parse 'None' into a color. Please provide a color!")

    return argc, arg


def get_color_id_from_id(color_id, colormode):
    """Return color_id as str and toggle colormode 256 if necessary."""
    if color_id > 8:
        colormode = 256
    return str(color_id), colormode


def get_color_id_from_color_enum(key, color_enum):
    """Return color_id as str for key in color_enum

    Parameters:
    -----------
    key: str
        A Color key as str. Any of format:
            name: '^[a-z, A-z, 0-9]*' (e.g. "blue")
            hex: '^hex_[0-9,a-f]{6}$' (e.g. "hex_ffffff")
            rgb: '^rgb_[0-9]{1,3}_[0-9]{1,3}_[0-9]{1,3}$'(e.g. rbg_255_0_0)
            hsl: '^hsl_[0-9]{1,3}_[0-9]{1,3}_[0-9]{1,3}$'(e.g. hsl_255_0_0)

    color_enum: Colors or Colors256 Enum
        An enum-obj of type Colors or Colors256.

    Return:
    -------
    str
        Color id as str ('^[0-9]{1,3}$' e.g. '102').

    Raise:
    -------
    KeyError
        Raise KeyError if key is not a valid color key for Color Enum.
    """
    try:
        color_id = color_enum[key]
    except KeyError as E:
        raise E("{} is not a valid color key".format(key))
    return color_id


def get_color_id_from_name(name, colormode):
    """Return a call to get_color_id_from_color_enum.

    Parses name into all lower cases letters and toggles colormode 256 if
    name is not an 8-bit Color name.

    Parameters:
    -----------
    name: str
        A color name as str with format name: '^[a-z, A-z, 0-9]*' (e.g. "blue").

    colormode: int
        Any integer in [8, 16, 256].

    Return:
    -------
    A call to get_color_id_from_color_enum

    """
    if colormode == 256:
        color_enum = Colors256
    else: # colormode != 256
        color_enum = Colors
        if not is_8bit_color(name):
            colormode = 256
    return get_color_id_from_color_enum(name.lower(), color_enum), colormode


def get_color_id_from_hex(hex, colormode):
    """Return a call to get_color_id_from_color_enum.

    Parses hex str (e.g. "#ffffff")into valid key format (e.g. "hex_ffffff").

    Parameters:
    -----------
    hex: str
        A hexadecimal color value as str with format:
            '^hex_[0-9,a-f]{6}$' (e.g. "hex_ffffff")

    colormode: any
        Just provide for compatibility but is ignored since hexdecimal color
        value toogles colormode 256 automatically.

    Return:
    -------
    A call to get_color_id_from_color_enum

    """
    key = parse_hex(hex)
    return get_color_id_from_color_enum(key, Colors256)


def get_color_id_from_iterable(iterable, colormode):
    """Return a call to get_color_id_from_color_enum.

    Parses iterarble (eg. (255, 0, 0) into valid key format (eg. rgb_255_0_0).

    Parameters:
    -----------
    iterable: tuple, list
        A color value as list or tuple with len(3):

    colormode: any
        Just provide for compatibility but is ignored since rgb/hsl color
        values toogle colormode 256 automatically.

    Return:
    -------
    A call to get_color_id_from_color_enum

    """
    key = parse_iterable(iterable)
    return get_color_id_from_color_enum(key, Colors256)


def get_color_string(color_id, colormode):
    """Return get_color_string func for colormode."""
    switcher = {8: get_color_string_8_bit,
                16: get_color_string_16_bit,
                256: get_color_string_256_bit
                }
    return switcher[colormode](color_id)


def get_color_string_256_bit(color_id):
    """Return ANSI color command string for 256 bit colors"""
    return Colors._blink + ANSICommands.separator + \
        TextAttributes.blink + ANSICommands.separator + color_id


def get_color_string_16_bit(color_id):
    """Return ANSI color command string for 16 bit (bold) colors"""
    return color_id + ANSICommands.separator + TextAttributes.bold


def get_color_string_8_bit(color_id):
    """Return ANSI color command string for 8 bit colors"""
    return color_id


#--------------------- Checker ------------------------------
def any_is_not_none(*args) -> bool:
    return any(arg is not None for arg in args)


def all_are_none(*args) -> bool:
    return all(arg is None for arg in args)


def any_is_none(*args) -> bool:
    return any(arg is None for arg in args)


def all_are_not_none(*args) -> bool:
    return all(arg is not None for arg in args)


def is_8bit_color(name) -> bool:
    """Return True if name is a valid key of Colors-Enum."""
    return name in Colors.__members__.keys()


def is_valid_hex_string(hex) -> bool:
    """Return True if hex is a valid hexadecimal color value string."""
    return (hex.startswith("#") and len(hex) ==
            7 and has_only_valid_characters(hex))


def has_only_valid_characters(hex) -> bool:
    """Return True if hex has only valid hexadecimal characters."""
    _valid_hex_characters = set("#abcdef0123456789")
    return set(hex) <= _valid_hex_characters


if __name__ == '__main__':
    import doctest
    doctest.testmod()
