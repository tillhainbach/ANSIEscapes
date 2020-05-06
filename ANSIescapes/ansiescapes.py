from enum import Enum
from ansiEscapesEnums import *
from collections.abc import Iterable
from itertools import chain


class ANSIEscapes:
    ESC = "\u001b["
    commandStop = "m"
    commandSeparator = ";"

    def __init(self):
        pass

    def _unifyColorNameString(colorname):
        """ Converts the input color name string into the appropiate format."""
        return colorname[0].upper() + colorname[1:].lower()

    def _getColorId256(colorname = None, colorcode = None, rgb = None, hsl = None):
        """
        Trys to find the corresponding color id string from the 256 bit color palette.
        Returns None on failure.
        Accepts colorname as strings (e.g 'red'), any colorcode (as str or int '1' or 1)
        or rgb-values as anything that can be used with a *-expression.
        Uses the first argument and ignores the rest.
        """
        if colorname is not None:
            arg = _unifyColorNameString(colorname)
        elif colorcode is not None:
            arg = colorcode
        elif rgb is not None:
            arg = 'rgb_' + '_'.join((str(val) for val in rgb))
        elif hsl is not None:
            arg = 'hsl_' + "_".join((str(val) for val in hsl))
        elif hex is not None:
            arg = 'hex_' + hex[1:]

        try:
            colorId = Colors256[arg]
        except IndexError:
            colorId = None

        return ColorsId

    @staticmethod
    def cursorUp(numberOfLines = 1):
        return ANSIEscapes.ESC + "{:d}A".format(numberOfLines)

    @staticmethod
    def cursorDown(numberOfLines = 1):
        return ANSIEscapes.ESC + "{:d}B".format(numberOfLines)

    @staticmethod
    def clearToEndOfLine():
        return ANSIEscapes.ESC + "0K"

    @staticmethod
    def clearToStartOfLine():
        return ANSIEscapes.ESC + "1K"

    @staticmethod
    def clearLine():
        return ANSIEscapes.ESC + "2K"

    @staticmethod
    def eraseLines(numberOfLines = 1):
        return ((ANSIEscapes.clearLine() + ANSIEscapes.cursorUp()) * numberOfLines)

    @staticmethod
    def eraseDisplay():
        return ANSIEscapes.ESC + "2J"

    @staticmethod
    def clearScreenUntilEnd():
        return ANSIEscapes.ESC + "0J"

    @staticmethod
    def clearScreenToBeginning():
        return ANSIEscapes.ESC + "1J"

    @staticmethod
    def bold():
        return ANSIEscapes.ESC + "1"

    @staticmethod
    def color(name = None, # color name as sting, hex string, rgb tuple/list
              drawingLevel = ColorDrawingLevel.foreground, # color foreground or background
              bold = false, # toggle bold colors (16bit support needed)
              blink = false, bright = false, # toggle blink or bright mode (both are provided for convenience) 256 bit color support needed
              colormode = None, # gets overwritten by bold or bright/blink, provided for convenience
              colorId = None, rgb = None, hex = None, hsl = None):

        if not isinstance(name, str):
            # user provide rgb value
            if isinstance(name, Iterable):
                rgb = name
                name = None
            else:
                # cannot understand input argument type
                raise TypeError

        if name.startswith('#')
            # user input name is a hex colorvalue
            hex = name
            name = None

        # providing rgb, hsl or hex values toggles blink/256bit mode automatically
        if any(rgb, hsl, hex) is not None or bright:
            blink = bold = True

        if name not in Colors.__members__.keys():
            # user did not provide an 8 bit color name
            blink = bold = True

        colormode = (8 * 2**bold)**(2**blink)

        if colormode == 256:
            colorId = _getColorId256(name, hex, rgb, hsl)
            colorString = Colors._blink + ANSIEscapes.commandSeparator + TextAttributes.blink + ANSIEscapes.commandSeparator + colorId
        elif colormode == 16:
            colorId = Colors[name]
            colorString = colorId + ANSIEscapes.commandSeparator + TextAttributes.bold
        else:
            colorString = Colors[name]

        return _formatRichText("", drawingLevel + colorString)

    def _formatRichText(*formattingCommands):
        outString = ANSIEscapes.ESC
        outString += ANSIEscapes.commandSeparator.join(formattingCommands)
        return outString + ANSIEscapes.commandStop

    def _is8bitColor(name):
        return name in Colors.__members__.keys()

    @staticmethod
    def formatText(text = "", *args, **kwargs):
        textAttributeArguments = (arg for arg in args if arg in TextAttributes.__members__.keys())
        colorKeys = (key for key in chain(Colors.__members__.keys(), Colors256.__members__.keys()))
        colorArguments = (arg for arg in args if arg in in colorKeys)

        return _formatRichText(*args, **kwargs) + text + resetFormatting()

    @staticmethod
    def color8(name, drawingLevel = ColorDrawingLevel.foreground):
        if _is8bitColor(name):
            return _formatRichText("", drawingLevel + Colors[name])
        else:
            return ""

    @staticmethod
    def background(colorName):
        return color8(colorName, drawingLevel = ColorDrawingLevel.background)

    @staticmethod
    def black(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Black")

    @staticmethod
    def red(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Red")

    @staticmethod
    def green(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Green")

    @staticmethod
    def yellow(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Yellow")

    @staticmethod
    def blue(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Blue")

    @staticmethod
    def magenta(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Magenta")

    @staticmethod
    def cyan(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("Cyan")

    @staticmethod
    def white(drawingLevel = ColorDrawingLevel.foreground):
    	return color8("White")

    @staticmethod
    def reset():
    	return _formatRichText(TextAttributes.reset)

    @staticmethod
    def bold():
    	return _formatRichText(TextAttributes.bold)

    @staticmethod
    def underscore():
    	return _formatRichText(TextAttributes.underscore)

    @staticmethod
    def underline():
    	return _formatRichText(TextAttributes.underline)

    @staticmethod
    def bright():
    	return _formatRichText(TextAttributes.bright)

    @staticmethod
    def blink():
    	return _formatRichText(TextAttributes.blink)

    @staticmethod
    def reversed():
    	return _formatRichText(TextAttributes.reversed)

    @staticmethod
    def concealed():
    	return _formatRichText(TextAttributes.concealed)
