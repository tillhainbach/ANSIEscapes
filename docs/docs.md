# pyansiescapes package

## Submodules

## pyansiescapes.commands module

API for console manipulation using ANSI Escape sequences in Python.


### pyansiescapes.commands.background(\*args: Any, \*\*kwargs: Any)
Convenience function for colored backgrounds.

Returns a call to `color()` with drawing_level= `enums.ColorDrawingLevel.background`.
See color for further description of input arguments. Drawing_level keyword
argument should be omitted.


### pyansiescapes.commands.black(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit black color.

See `color_8bit()` for further details.


### pyansiescapes.commands.blink()
Returns ‘bright/blink text’ ANSI-command string.


### pyansiescapes.commands.blue(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit blue color.

See `color_8bit()` for further details.


### pyansiescapes.commands.bold()
Returns ‘bold text’ ANSI-command string.


### pyansiescapes.commands.bright()
Returns ‘bright/blink text’ ANSI-command string.


### pyansiescapes.commands.clear_line()
Clears the entire line from start to end.


### pyansiescapes.commands.clear_lines(number_of_lines: int = 1)
Clears number_of_lines lines.


### pyansiescapes.commands.clear_screen()
Clears the entire screen.


### pyansiescapes.commands.clear_screen_to_beginning()
Clears screen from current cursor position to the beginning.


### pyansiescapes.commands.clear_screen_until_end()
Clears screen from current cursor position to the end.


### pyansiescapes.commands.clear_to_end_of_line()
Clears line from current cursor position to the end.


### pyansiescapes.commands.clear_to_start_of_line()
Clears line from start to current cursor position.


### pyansiescapes.commands.color(\*args: Any, \*\*kwargs: Any)
Returns ANSI Escape Sequence for specified color.


* **Parameters**

    
    * **\*args** – any valid positional argument for `_color()`.


    * **\*\*kwargs** – any valid keyword argument for `color()`.


### Examples

```python
>>> # Get string for 8-bit red text coloring (e.g. foreground).
>>> color(name="red")
'\x1b[31m'
```

```python
>>> # Get string for bold red background.
>>> color(name="red", bold=True, drawing_level="background")
'\x1b[41;1m'
```

```python
>>> # Get string for 256-bit red background.
>>> color(name="red", bold=True, blink=True, drawing_level="background")
'\x1b[48;5;9m'
```

```python
>>> # Get string for mediumspringgreen foreground 256-bit color.
>>> color(name="mediumspringgreen")
'\x1b[38;5;49m'
```


### pyansiescapes.commands.color_8bit(name: str, drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit colors.

Trys to find the color_id for provided name. Returns an empty string if name
is not an 8-bit color.


* **Parameters**

    
    * **name** – A color name. Any color name in Colors.


    * **drawing_level** – The color drawing level.
    Valid foreground values are:
    - “foreground”, ColorDrawingLevel.foreground, 0, “3”
    Valid background values are:
    - “background”, ColorDrawingLevel.background, 1, “4”
    Default: “foreground”



### pyansiescapes.commands.concealed()
Returns ‘concealed text’ ANSI-command string.


### pyansiescapes.commands.cursor_down(number_of_lines: int = 1)
Moves cursor down number_of_lines lines.


### pyansiescapes.commands.cursor_up(number_of_lines: int = 1)
Moves cursor up number_of_lines lines.


### pyansiescapes.commands.cyan(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit cyan color.

See `color_8bit()` for further details.


### pyansiescapes.commands.format(text: str, \*args: Any, \*\*kwargs: Any)
Return formatted text as str.

Uses the formatting attributes given in \*args or \*\*kwargs.
Postional arguments or keywordarguments that are not supported
will be ignored.


* **Parameters**

    
    * **text** – The text/string that should be formatted.


    * **\*args** – Any number of postional arguments. Unsupported arguments will be
    ignored. See “supported arguments” section for futher details.


    * **\*\*kwargs** – Any number of keyword arguments. Unsupported keyword arguments
    will be ignored. See “supported keywords” section for further
    details.



* **Returns**

    The text with leading ANSI Escape sequence “rich text”
    commands and a trailing ANSI Escape sequence “reset”
    command.


### Examples

```python
>>> # Format text to bold and underlined using postional arguments
>>> format('Hello ANSI!', 'bold', 'underline')
'\x1b[1;4mHello ANSI!\x1b[0m'
```

```python
>>> # It's also possible to use keyword arguments with True, False
>>> format('Hello ANSI!', bold=True, underline=True)
'\x1b[1;4mHello ANSI!\x1b[0m'
```

```python
>>> # You can also set font and background color
>>> format('Hello ANSI!', color='blue', background='white')
'\x1b[34;47mHello ANSI!\x1b[0m'
```

```python
>>> # Or provide a keyword argument dict
>>> format('Hello ANSI!', color={'name':'blue', 'colormode':256}, background='white')
'\x1b[38;5;12;47mHello ANSI!\x1b[0m'
```


### pyansiescapes.commands.green(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit green color.

See `color_8bit()` for further details.


### pyansiescapes.commands.magenta(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit magenta color.

See `color_8bit()` for further details.


### pyansiescapes.commands.red(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit red color.

See `color_8bit()` for further details.


### pyansiescapes.commands.reset()
Returns ‘reset’ ANSI-command string.


### pyansiescapes.commands.reversed()
Returns ‘reversed text’ ANSI-command string.


### pyansiescapes.commands.underline()
Returns ‘underlined/underscored text’ ANSI-command string.


### pyansiescapes.commands.underscore()
Returns ‘underlined/underscored text’ ANSI-command string.


### pyansiescapes.commands.white(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit white color.

See `color_8bit()` for further details.


### pyansiescapes.commands.yellow(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel] = <ColorDrawingLevel.foreground: '3'>)
Convenience function for 8-bit yellow color.

See `color_8bit()` for further details.

## pyansiescapes.enums module

Enumerates for different types of ANSI Escape Sequences.


### class pyansiescapes.enums.ANSICommands()
Bases: `pyansiescapes.enums.StrEnum`

ANSI Escape Sequences defining a command.


#### separator( = ';')

#### start( = '\\x1b[')

#### stop( = 'm')

### class pyansiescapes.enums.ColorDrawingLevel()
Bases: `pyansiescapes.enums.StrEnum`

ANSI color drawing level id-strings.


#### background( = '4')

#### foreground( = '3')

### class pyansiescapes.enums.Colors()
Bases: `pyansiescapes.enums.StrEnum`

Enum for ANSI Colors


#### black( = '0')

#### blue( = '4')

#### cyan( = '6')

#### green( = '2')

#### magenta( = '5')

#### red( = '1')

#### white( = '7')

#### yellow( = '3')

### class pyansiescapes.enums.Colors256()
Bases: `pyansiescapes.enums.StrEnum`

Enum for 256bit colors. Uses Each colorId has a name and aliases corresponding to the hex, rgb or hsl value


#### aqua( = '14')

#### aquamarine1( = '86')

#### aquamarine2( = '122')

#### aquamarine3( = '79')

#### black( = '0')

#### blue( = '12')

#### blue1( = '21')

#### blue3( = '19')

#### blue4( = '20')

#### blueviolet( = '57')

#### cadetblue( = '72')

#### cadetblue0( = '73')

#### chartreuse1( = '118')

#### chartreuse2( = '82')

#### chartreuse3( = '70')

#### chartreuse4( = '64')

#### chartreuse5( = '76')

#### chartreuse6( = '112')

#### cornflowerblue( = '69')

#### cornsilk1( = '230')

#### cyan1( = '51')

#### cyan2( = '50')

#### cyan3( = '43')

#### darkblue( = '18')

#### darkcyan( = '36')

#### darkgoldenrod( = '136')

#### darkgreen( = '22')

#### darkkhaki( = '143')

#### darkmagenta( = '90')

#### darkmagenta0( = '91')

#### darkolivegreen1( = '191')

#### darkolivegreen2( = '155')

#### darkolivegreen3( = '107')

#### darkolivegreen4( = '113')

#### darkolivegreen5( = '149')

#### darkolivegreen6( = '192')

#### darkorange( = '208')

#### darkorange3( = '130')

#### darkorange4( = '166')

#### darkred( = '52')

#### darkred0( = '88')

#### darkseagreen( = '108')

#### darkseagreen1( = '158')

#### darkseagreen2( = '151')

#### darkseagreen3( = '115')

#### darkseagreen4( = '65')

#### darkseagreen5( = '71')

#### darkseagreen6( = '150')

#### darkseagreen7( = '157')

#### darkseagreen8( = '193')

#### darkslategray1( = '123')

#### darkslategray2( = '87')

#### darkslategray3( = '116')

#### darkturquoise( = '44')

#### darkviolet( = '92')

#### darkviolet0( = '128')

#### deeppink1( = '198')

#### deeppink2( = '197')

#### deeppink3( = '161')

#### deeppink4( = '53')

#### deeppink5( = '89')

#### deeppink6( = '125')

#### deeppink7( = '162')

#### deeppink8( = '199')

#### deepskyblue1( = '39')

#### deepskyblue2( = '38')

#### deepskyblue3( = '31')

#### deepskyblue4( = '23')

#### deepskyblue5( = '24')

#### deepskyblue6( = '25')

#### deepskyblue7( = '32')

#### dodgerblue1( = '33')

#### dodgerblue2( = '27')

#### dodgerblue3( = '26')

#### fuchsia( = '13')

#### gold1( = '220')

#### gold3( = '142')

#### gold4( = '178')

#### green( = '2')

#### green1( = '46')

#### green3( = '34')

#### green4( = '28')

#### green5( = '40')

#### greenyellow( = '154')

#### grey( = '8')

#### grey0( = '16')

#### grey100( = '231')

#### grey11( = '234')

#### grey15( = '235')

#### grey19( = '236')

#### grey23( = '237')

#### grey27( = '238')

#### grey3( = '232')

#### grey30( = '239')

#### grey35( = '240')

#### grey37( = '59')

#### grey39( = '241')

#### grey42( = '242')

#### grey46( = '243')

#### grey50( = '244')

#### grey53( = '102')

#### grey54( = '245')

#### grey58( = '246')

#### grey62( = '247')

#### grey63( = '139')

#### grey66( = '248')

#### grey69( = '145')

#### grey7( = '233')

#### grey70( = '249')

#### grey74( = '250')

#### grey78( = '251')

#### grey82( = '252')

#### grey84( = '188')

#### grey85( = '253')

#### grey89( = '254')

#### grey93( = '255')

#### hex_000000( = '0')

#### hex_00005f( = '17')

#### hex_000080( = '4')

#### hex_000087( = '18')

#### hex_0000af( = '19')

#### hex_0000d7( = '20')

#### hex_0000ff( = '12')

#### hex_005f00( = '22')

#### hex_005f5f( = '23')

#### hex_005f87( = '24')

#### hex_005faf( = '25')

#### hex_005fd7( = '26')

#### hex_005fff( = '27')

#### hex_008000( = '2')

#### hex_008080( = '6')

#### hex_008700( = '28')

#### hex_00875f( = '29')

#### hex_008787( = '30')

#### hex_0087af( = '31')

#### hex_0087d7( = '32')

#### hex_0087ff( = '33')

#### hex_00af00( = '34')

#### hex_00af5f( = '35')

#### hex_00af87( = '36')

#### hex_00afaf( = '37')

#### hex_00afd7( = '38')

#### hex_00afff( = '39')

#### hex_00d700( = '40')

#### hex_00d75f( = '41')

#### hex_00d787( = '42')

#### hex_00d7af( = '43')

#### hex_00d7d7( = '44')

#### hex_00d7ff( = '45')

#### hex_00ff00( = '10')

#### hex_00ff5f( = '47')

#### hex_00ff87( = '48')

#### hex_00ffaf( = '49')

#### hex_00ffd7( = '50')

#### hex_00ffff( = '14')

#### hex_080808( = '232')

#### hex_121212( = '233')

#### hex_1c1c1c( = '234')

#### hex_262626( = '235')

#### hex_303030( = '236')

#### hex_3a3a3a( = '237')

#### hex_444444( = '238')

#### hex_4e4e4e( = '239')

#### hex_585858( = '240')

#### hex_5f0000( = '52')

#### hex_5f005f( = '53')

#### hex_5f0087( = '54')

#### hex_5f00af( = '55')

#### hex_5f00d7( = '56')

#### hex_5f00ff( = '57')

#### hex_5f5f00( = '58')

#### hex_5f5f5f( = '59')

#### hex_5f5f87( = '60')

#### hex_5f5faf( = '61')

#### hex_5f5fd7( = '62')

#### hex_5f5fff( = '63')

#### hex_5f8700( = '64')

#### hex_5f875f( = '65')

#### hex_5f8787( = '66')

#### hex_5f87af( = '67')

#### hex_5f87d7( = '68')

#### hex_5f87ff( = '69')

#### hex_5faf00( = '70')

#### hex_5faf5f( = '71')

#### hex_5faf87( = '72')

#### hex_5fafaf( = '73')

#### hex_5fafd7( = '74')

#### hex_5fafff( = '75')

#### hex_5fd700( = '76')

#### hex_5fd75f( = '77')

#### hex_5fd787( = '78')

#### hex_5fd7af( = '79')

#### hex_5fd7d7( = '80')

#### hex_5fd7ff( = '81')

#### hex_5fff00( = '82')

#### hex_5fff5f( = '83')

#### hex_5fff87( = '84')

#### hex_5fffaf( = '85')

#### hex_5fffd7( = '86')

#### hex_5fffff( = '87')

#### hex_626262( = '241')

#### hex_6c6c6c( = '242')

#### hex_767676( = '243')

#### hex_800000( = '1')

#### hex_800080( = '5')

#### hex_808000( = '3')

#### hex_808080( = '8')

#### hex_870000( = '88')

#### hex_87005f( = '89')

#### hex_870087( = '90')

#### hex_8700af( = '91')

#### hex_8700d7( = '92')

#### hex_8700ff( = '93')

#### hex_875f00( = '94')

#### hex_875f5f( = '95')

#### hex_875f87( = '96')

#### hex_875faf( = '97')

#### hex_875fd7( = '98')

#### hex_875fff( = '99')

#### hex_878700( = '100')

#### hex_87875f( = '101')

#### hex_878787( = '102')

#### hex_8787af( = '103')

#### hex_8787d7( = '104')

#### hex_8787ff( = '105')

#### hex_87af00( = '106')

#### hex_87af5f( = '107')

#### hex_87af87( = '108')

#### hex_87afaf( = '109')

#### hex_87afd7( = '110')

#### hex_87afff( = '111')

#### hex_87d700( = '112')

#### hex_87d75f( = '113')

#### hex_87d787( = '114')

#### hex_87d7af( = '115')

#### hex_87d7d7( = '116')

#### hex_87d7ff( = '117')

#### hex_87ff00( = '118')

#### hex_87ff5f( = '119')

#### hex_87ff87( = '120')

#### hex_87ffaf( = '121')

#### hex_87ffd7( = '122')

#### hex_87ffff( = '123')

#### hex_8a8a8a( = '245')

#### hex_949494( = '246')

#### hex_9e9e9e( = '247')

#### hex_a8a8a8( = '248')

#### hex_af0000( = '124')

#### hex_af005f( = '125')

#### hex_af0087( = '126')

#### hex_af00af( = '127')

#### hex_af00d7( = '128')

#### hex_af00ff( = '129')

#### hex_af5f00( = '130')

#### hex_af5f5f( = '131')

#### hex_af5f87( = '132')

#### hex_af5faf( = '133')

#### hex_af5fd7( = '134')

#### hex_af5fff( = '135')

#### hex_af8700( = '136')

#### hex_af875f( = '137')

#### hex_af8787( = '138')

#### hex_af87af( = '139')

#### hex_af87d7( = '140')

#### hex_af87ff( = '141')

#### hex_afaf00( = '142')

#### hex_afaf5f( = '143')

#### hex_afaf87( = '144')

#### hex_afafaf( = '145')

#### hex_afafd7( = '146')

#### hex_afafff( = '147')

#### hex_afd700( = '148')

#### hex_afd75f( = '149')

#### hex_afd787( = '150')

#### hex_afd7af( = '151')

#### hex_afd7d7( = '152')

#### hex_afd7ff( = '153')

#### hex_afff00( = '154')

#### hex_afff5f( = '155')

#### hex_afff87( = '156')

#### hex_afffaf( = '157')

#### hex_afffd7( = '158')

#### hex_afffff( = '159')

#### hex_b2b2b2( = '249')

#### hex_bcbcbc( = '250')

#### hex_c0c0c0( = '7')

#### hex_c6c6c6( = '251')

#### hex_d0d0d0( = '252')

#### hex_d70000( = '160')

#### hex_d7005f( = '161')

#### hex_d70087( = '162')

#### hex_d700af( = '163')

#### hex_d700d7( = '164')

#### hex_d700ff( = '165')

#### hex_d75f00( = '166')

#### hex_d75f5f( = '167')

#### hex_d75f87( = '168')

#### hex_d75faf( = '169')

#### hex_d75fd7( = '170')

#### hex_d75fff( = '171')

#### hex_d78700( = '172')

#### hex_d7875f( = '173')

#### hex_d78787( = '174')

#### hex_d787af( = '175')

#### hex_d787d7( = '176')

#### hex_d787ff( = '177')

#### hex_d7af00( = '178')

#### hex_d7af5f( = '179')

#### hex_d7af87( = '180')

#### hex_d7afaf( = '181')

#### hex_d7afd7( = '182')

#### hex_d7afff( = '183')

#### hex_d7d700( = '184')

#### hex_d7d75f( = '185')

#### hex_d7d787( = '186')

#### hex_d7d7af( = '187')

#### hex_d7d7d7( = '188')

#### hex_d7d7ff( = '189')

#### hex_d7ff00( = '190')

#### hex_d7ff5f( = '191')

#### hex_d7ff87( = '192')

#### hex_d7ffaf( = '193')

#### hex_d7ffd7( = '194')

#### hex_d7ffff( = '195')

#### hex_dadada( = '253')

#### hex_e4e4e4( = '254')

#### hex_eeeeee( = '255')

#### hex_ff0000( = '9')

#### hex_ff005f( = '197')

#### hex_ff0087( = '198')

#### hex_ff00af( = '199')

#### hex_ff00d7( = '200')

#### hex_ff00ff( = '13')

#### hex_ff5f00( = '202')

#### hex_ff5f5f( = '203')

#### hex_ff5f87( = '204')

#### hex_ff5faf( = '205')

#### hex_ff5fd7( = '206')

#### hex_ff5fff( = '207')

#### hex_ff8700( = '208')

#### hex_ff875f( = '209')

#### hex_ff8787( = '210')

#### hex_ff87af( = '211')

#### hex_ff87d7( = '212')

#### hex_ff87ff( = '213')

#### hex_ffaf00( = '214')

#### hex_ffaf5f( = '215')

#### hex_ffaf87( = '216')

#### hex_ffafaf( = '217')

#### hex_ffafd7( = '218')

#### hex_ffafff( = '219')

#### hex_ffd700( = '220')

#### hex_ffd75f( = '221')

#### hex_ffd787( = '222')

#### hex_ffd7af( = '223')

#### hex_ffd7d7( = '224')

#### hex_ffd7ff( = '225')

#### hex_ffff00( = '11')

#### hex_ffff5f( = '227')

#### hex_ffff87( = '228')

#### hex_ffffaf( = '229')

#### hex_ffffd7( = '230')

#### hex_ffffff( = '15')

#### honeydew2( = '194')

#### hotpink( = '205')

#### hotpink0( = '206')

#### hotpink2( = '169')

#### hotpink3( = '132')

#### hotpink4( = '168')

#### hsl_0_0_0( = '0')

#### hsl_0_0_10( = '234')

#### hsl_0_0_100( = '15')

#### hsl_0_0_14( = '235')

#### hsl_0_0_18( = '236')

#### hsl_0_0_22( = '237')

#### hsl_0_0_26( = '238')

#### hsl_0_0_3( = '232')

#### hsl_0_0_30( = '239')

#### hsl_0_0_34( = '240')

#### hsl_0_0_37( = '59')

#### hsl_0_0_40( = '242')

#### hsl_0_0_46( = '243')

#### hsl_0_0_50( = '8')

#### hsl_0_0_52( = '102')

#### hsl_0_0_54( = '245')

#### hsl_0_0_58( = '246')

#### hsl_0_0_61( = '247')

#### hsl_0_0_65( = '248')

#### hsl_0_0_68( = '145')

#### hsl_0_0_69( = '249')

#### hsl_0_0_7( = '233')

#### hsl_0_0_73( = '250')

#### hsl_0_0_75( = '7')

#### hsl_0_0_77( = '251')

#### hsl_0_0_81( = '252')

#### hsl_0_0_84( = '188')

#### hsl_0_0_85( = '253')

#### hsl_0_0_89( = '254')

#### hsl_0_0_93( = '255')

#### hsl_0_100_18( = '52')

#### hsl_0_100_25( = '1')

#### hsl_0_100_26( = '88')

#### hsl_0_100_34( = '124')

#### hsl_0_100_42( = '160')

#### hsl_0_100_50( = '9')

#### hsl_0_100_68( = '203')

#### hsl_0_100_76( = '210')

#### hsl_0_100_84( = '217')

#### hsl_0_100_92( = '224')

#### hsl_0_17_45( = '95')

#### hsl_0_20_60( = '138')

#### hsl_0_33_52( = '131')

#### hsl_0_33_76( = '181')

#### hsl_0_50_68( = '174')

#### hsl_0_60_60( = '167')

#### hsl_100_100_76( = '156')

#### hsl_100_60_60( = '113')

#### hsl_105_100_68( = '119')

#### hsl_120_100_18( = '22')

#### hsl_120_100_25( = '2')

#### hsl_120_100_26( = '28')

#### hsl_120_100_34( = '34')

#### hsl_120_100_42( = '40')

#### hsl_120_100_50( = '10')

#### hsl_120_100_68( = '83')

#### hsl_120_100_76( = '120')

#### hsl_120_100_84( = '157')

#### hsl_120_100_92( = '194')

#### hsl_120_17_45( = '65')

#### hsl_120_20_60( = '108')

#### hsl_120_33_52( = '71')

#### hsl_120_33_76( = '151')

#### hsl_120_50_68( = '114')

#### hsl_120_60_60( = '77')

#### hsl_135_100_68( = '84')

#### hsl_140_100_76( = '121')

#### hsl_140_60_60( = '78')

#### hsl_142_100_50( = '47')

#### hsl_146_100_42( = '41')

#### hsl_150_100_68( = '85')

#### hsl_150_100_84( = '158')

#### hsl_150_33_52( = '72')

#### hsl_150_50_68( = '115')

#### hsl_151_100_50( = '48')

#### hsl_152_100_34( = '35')

#### hsl_157_100_42( = '42')

#### hsl_15_100_68( = '209')

#### hsl_160_100_76( = '122')

#### hsl_160_60_60( = '79')

#### hsl_161_100_50( = '49')

#### hsl_162_100_26( = '29')

#### hsl_165_100_68( = '86')

#### hsl_166_100_34( = '36')

#### hsl_168_100_42( = '43')

#### hsl_170_100_50( = '50')

#### hsl_180_100_18( = '23')

#### hsl_180_100_25( = '6')

#### hsl_180_100_26( = '30')

#### hsl_180_100_34( = '37')

#### hsl_180_100_42( = '44')

#### hsl_180_100_50( = '14')

#### hsl_180_100_68( = '87')

#### hsl_180_100_76( = '123')

#### hsl_180_100_84( = '159')

#### hsl_180_100_92( = '195')

#### hsl_180_17_45( = '66')

#### hsl_180_20_60( = '109')

#### hsl_180_33_52( = '73')

#### hsl_180_33_76( = '152')

#### hsl_180_50_68( = '116')

#### hsl_180_60_60( = '80')

#### hsl_189_100_50( = '45')

#### hsl_191_100_42( = '38')

#### hsl_193_100_34( = '31')

#### hsl_195_100_68( = '81')

#### hsl_197_100_26( = '24')

#### hsl_198_100_50( = '39')

#### hsl_200_100_76( = '117')

#### hsl_200_60_60( = '74')

#### hsl_202_100_42( = '32')

#### hsl_207_100_34( = '25')

#### hsl_208_100_50( = '33')

#### hsl_20_100_76( = '216')

#### hsl_20_60_60( = '173')

#### hsl_210_100_68( = '75')

#### hsl_210_100_84( = '153')

#### hsl_210_33_52( = '67')

#### hsl_210_50_68( = '110')

#### hsl_213_100_42( = '26')

#### hsl_217_100_50( = '27')

#### hsl_220_100_76( = '111')

#### hsl_220_60_60( = '68')

#### hsl_225_100_68( = '69')

#### hsl_22_100_50( = '202')

#### hsl_240_100_18( = '17')

#### hsl_240_100_25( = '4')

#### hsl_240_100_26( = '18')

#### hsl_240_100_34( = '19')

#### hsl_240_100_42( = '20')

#### hsl_240_100_50( = '12')

#### hsl_240_100_68( = '63')

#### hsl_240_100_76( = '105')

#### hsl_240_100_84( = '147')

#### hsl_240_100_92( = '189')

#### hsl_240_17_45( = '60')

#### hsl_240_20_60( = '103')

#### hsl_240_33_52( = '61')

#### hsl_240_33_76( = '146')

#### hsl_240_50_68( = '104')

#### hsl_240_60_60( = '62')

#### hsl_255_100_68( = '99')

#### hsl_260_100_76( = '141')

#### hsl_260_60_60( = '98')

#### hsl_262_100_50( = '57')

#### hsl_266_100_42( = '56')

#### hsl_26_100_42( = '166')

#### hsl_270_100_68( = '135')

#### hsl_270_100_84( = '183')

#### hsl_270_33_52( = '97')

#### hsl_270_50_68( = '140')

#### hsl_271_100_50( = '93')

#### hsl_272_100_34( = '55')

#### hsl_277_100_42( = '92')

#### hsl_280_100_76( = '177')

#### hsl_280_60_60( = '134')

#### hsl_281_100_50( = '129')

#### hsl_282_100_26( = '54')

#### hsl_285_100_68( = '171')

#### hsl_286_100_34( = '91')

#### hsl_288_100_42( = '128')

#### hsl_290_100_50( = '165')

#### hsl_300_100_18( = '53')

#### hsl_300_100_25( = '5')

#### hsl_300_100_26( = '90')

#### hsl_300_100_34( = '127')

#### hsl_300_100_42( = '164')

#### hsl_300_100_50( = '13')

#### hsl_300_100_68( = '207')

#### hsl_300_100_76( = '213')

#### hsl_300_100_84( = '219')

#### hsl_300_100_92( = '225')

#### hsl_300_17_45( = '96')

#### hsl_300_20_60( = '139')

#### hsl_300_33_52( = '133')

#### hsl_300_33_76( = '182')

#### hsl_300_50_68( = '176')

#### hsl_300_60_60( = '170')

#### hsl_309_100_50( = '200')

#### hsl_30_100_68( = '215')

#### hsl_30_100_84( = '223')

#### hsl_30_33_52( = '137')

#### hsl_30_50_68( = '180')

#### hsl_311_100_42( = '163')

#### hsl_313_100_34( = '126')

#### hsl_315_100_68( = '206')

#### hsl_317_100_26( = '89')

#### hsl_318_100_50( = '199')

#### hsl_31_100_50( = '208')

#### hsl_320_100_76( = '212')

#### hsl_320_60_60( = '169')

#### hsl_322_100_42( = '162')

#### hsl_327_100_34( = '125')

#### hsl_328_100_50( = '198')

#### hsl_32_100_34( = '130')

#### hsl_330_100_68( = '205')

#### hsl_330_100_84( = '218')

#### hsl_330_33_52( = '132')

#### hsl_330_50_68( = '175')

#### hsl_333_100_42( = '161')

#### hsl_337_100_50( = '197')

#### hsl_340_100_76( = '211')

#### hsl_340_60_60( = '168')

#### hsl_345_100_68( = '204')

#### hsl_37_100_42( = '172')

#### hsl_40_100_76( = '222')

#### hsl_40_60_60( = '179')

#### hsl_41_100_50( = '214')

#### hsl_42_100_26( = '94')

#### hsl_45_100_68( = '221')

#### hsl_46_100_34( = '136')

#### hsl_48_100_42( = '178')

#### hsl_50_100_50( = '220')

#### hsl_60_100_18( = '58')

#### hsl_60_100_25( = '3')

#### hsl_60_100_26( = '100')

#### hsl_60_100_34( = '142')

#### hsl_60_100_42( = '184')

#### hsl_60_100_50( = '11')

#### hsl_60_100_68( = '227')

#### hsl_60_100_76( = '228')

#### hsl_60_100_84( = '229')

#### hsl_60_100_92( = '230')

#### hsl_60_17_45( = '101')

#### hsl_60_20_60( = '144')

#### hsl_60_33_52( = '143')

#### hsl_60_33_76( = '187')

#### hsl_60_50_68( = '186')

#### hsl_60_60_60( = '185')

#### hsl_69_100_50( = '190')

#### hsl_71_100_42( = '148')

#### hsl_73_100_34( = '106')

#### hsl_75_100_68( = '191')

#### hsl_77_100_26( = '64')

#### hsl_78_100_50( = '154')

#### hsl_80_100_76( = '192')

#### hsl_80_60_60( = '149')

#### hsl_82_100_42( = '112')

#### hsl_87_100_34( = '70')

#### hsl_88_100_50( = '118')

#### hsl_90_100_68( = '155')

#### hsl_90_100_84( = '193')

#### hsl_90_33_52( = '107')

#### hsl_90_50_68( = '150')

#### hsl_93_100_42( = '76')

#### hsl_97_100_50( = '82')

#### indianred( = '131')

#### indianred0( = '167')

#### indianred1( = '203')

#### indianred2( = '204')

#### khaki1( = '228')

#### khaki3( = '185')

#### lightcoral( = '210')

#### lightcyan1( = '195')

#### lightcyan3( = '152')

#### lightgoldenrod1( = '227')

#### lightgoldenrod2( = '186')

#### lightgoldenrod3( = '179')

#### lightgoldenrod4( = '221')

#### lightgoldenrod5( = '222')

#### lightgreen( = '119')

#### lightgreen0( = '120')

#### lightpink1( = '217')

#### lightpink3( = '174')

#### lightpink4( = '95')

#### lightsalmon1( = '216')

#### lightsalmon3( = '137')

#### lightsalmon4( = '173')

#### lightseagreen( = '37')

#### lightskyblue1( = '153')

#### lightskyblue3( = '109')

#### lightskyblue4( = '110')

#### lightslateblue( = '105')

#### lightslategrey( = '103')

#### lightsteelblue( = '147')

#### lightsteelblue1( = '189')

#### lightsteelblue3( = '146')

#### lightyellow3( = '187')

#### lime( = '10')

#### magenta1( = '201')

#### magenta2( = '165')

#### magenta3( = '127')

#### magenta4( = '163')

#### magenta5( = '164')

#### magenta6( = '200')

#### maroon( = '1')

#### mediumorchid( = '134')

#### mediumorchid1( = '171')

#### mediumorchid2( = '207')

#### mediumorchid3( = '133')

#### mediumpurple( = '104')

#### mediumpurple1( = '141')

#### mediumpurple2( = '135')

#### mediumpurple3( = '97')

#### mediumpurple4( = '60')

#### mediumpurple5( = '98')

#### mediumpurple6( = '140')

#### mediumspringgreen( = '49')

#### mediumturquoise( = '80')

#### mediumvioletred( = '126')

#### mistyrose1( = '224')

#### mistyrose3( = '181')

#### navajowhite1( = '223')

#### navajowhite3( = '144')

#### navy( = '4')

#### navyblue( = '17')

#### olive( = '3')

#### orange1( = '214')

#### orange3( = '172')

#### orange4( = '58')

#### orange5( = '94')

#### orangered1( = '202')

#### orchid( = '170')

#### orchid1( = '213')

#### orchid2( = '212')

#### palegreen1( = '121')

#### palegreen2( = '156')

#### palegreen3( = '77')

#### palegreen4( = '114')

#### paleturquoise1( = '159')

#### paleturquoise4( = '66')

#### palevioletred1( = '211')

#### pink1( = '218')

#### pink3( = '175')

#### plum1( = '219')

#### plum2( = '183')

#### plum3( = '176')

#### plum4( = '96')

#### purple( = '5')

#### purple0( = '93')

#### purple1( = '129')

#### purple3( = '56')

#### purple4( = '54')

#### purple5( = '55')

#### red( = '9')

#### red1( = '196')

#### red3( = '124')

#### red4( = '160')

#### rgb_0_0_0( = '0')

#### rgb_0_0_128( = '4')

#### rgb_0_0_135( = '18')

#### rgb_0_0_175( = '19')

#### rgb_0_0_215( = '20')

#### rgb_0_0_255( = '12')

#### rgb_0_0_95( = '17')

#### rgb_0_128_0( = '2')

#### rgb_0_128_128( = '6')

#### rgb_0_135_0( = '28')

#### rgb_0_135_135( = '30')

#### rgb_0_135_175( = '31')

#### rgb_0_135_215( = '32')

#### rgb_0_135_255( = '33')

#### rgb_0_135_95( = '29')

#### rgb_0_175_0( = '34')

#### rgb_0_175_135( = '36')

#### rgb_0_175_175( = '37')

#### rgb_0_175_215( = '38')

#### rgb_0_175_255( = '39')

#### rgb_0_175_95( = '35')

#### rgb_0_215_0( = '40')

#### rgb_0_215_135( = '42')

#### rgb_0_215_175( = '43')

#### rgb_0_215_215( = '44')

#### rgb_0_215_255( = '45')

#### rgb_0_215_95( = '41')

#### rgb_0_255_0( = '10')

#### rgb_0_255_135( = '48')

#### rgb_0_255_175( = '49')

#### rgb_0_255_215( = '50')

#### rgb_0_255_255( = '14')

#### rgb_0_255_95( = '47')

#### rgb_0_95_0( = '22')

#### rgb_0_95_135( = '24')

#### rgb_0_95_175( = '25')

#### rgb_0_95_215( = '26')

#### rgb_0_95_255( = '27')

#### rgb_0_95_95( = '23')

#### rgb_108_108_108( = '242')

#### rgb_118_118_118( = '243')

#### rgb_128_0_0( = '1')

#### rgb_128_0_128( = '5')

#### rgb_128_128_0( = '3')

#### rgb_128_128_128( = '8')

#### rgb_135_0_0( = '88')

#### rgb_135_0_135( = '90')

#### rgb_135_0_175( = '91')

#### rgb_135_0_215( = '92')

#### rgb_135_0_255( = '93')

#### rgb_135_0_95( = '89')

#### rgb_135_135_0( = '100')

#### rgb_135_135_135( = '102')

#### rgb_135_135_175( = '103')

#### rgb_135_135_215( = '104')

#### rgb_135_135_255( = '105')

#### rgb_135_135_95( = '101')

#### rgb_135_175_0( = '106')

#### rgb_135_175_135( = '108')

#### rgb_135_175_175( = '109')

#### rgb_135_175_215( = '110')

#### rgb_135_175_255( = '111')

#### rgb_135_175_95( = '107')

#### rgb_135_215_0( = '112')

#### rgb_135_215_135( = '114')

#### rgb_135_215_175( = '115')

#### rgb_135_215_215( = '116')

#### rgb_135_215_255( = '117')

#### rgb_135_215_95( = '113')

#### rgb_135_255_0( = '118')

#### rgb_135_255_135( = '120')

#### rgb_135_255_175( = '121')

#### rgb_135_255_215( = '122')

#### rgb_135_255_255( = '123')

#### rgb_135_255_95( = '119')

#### rgb_135_95_0( = '94')

#### rgb_135_95_135( = '96')

#### rgb_135_95_175( = '97')

#### rgb_135_95_215( = '98')

#### rgb_135_95_255( = '99')

#### rgb_135_95_95( = '95')

#### rgb_138_138_138( = '245')

#### rgb_148_148_148( = '246')

#### rgb_158_158_158( = '247')

#### rgb_168_168_168( = '248')

#### rgb_175_0_0( = '124')

#### rgb_175_0_135( = '126')

#### rgb_175_0_175( = '127')

#### rgb_175_0_215( = '128')

#### rgb_175_0_255( = '129')

#### rgb_175_0_95( = '125')

#### rgb_175_135_0( = '136')

#### rgb_175_135_135( = '138')

#### rgb_175_135_175( = '139')

#### rgb_175_135_215( = '140')

#### rgb_175_135_255( = '141')

#### rgb_175_135_95( = '137')

#### rgb_175_175_0( = '142')

#### rgb_175_175_135( = '144')

#### rgb_175_175_175( = '145')

#### rgb_175_175_215( = '146')

#### rgb_175_175_255( = '147')

#### rgb_175_175_95( = '143')

#### rgb_175_215_0( = '148')

#### rgb_175_215_135( = '150')

#### rgb_175_215_175( = '151')

#### rgb_175_215_215( = '152')

#### rgb_175_215_255( = '153')

#### rgb_175_215_95( = '149')

#### rgb_175_255_0( = '154')

#### rgb_175_255_135( = '156')

#### rgb_175_255_175( = '157')

#### rgb_175_255_215( = '158')

#### rgb_175_255_255( = '159')

#### rgb_175_255_95( = '155')

#### rgb_175_95_0( = '130')

#### rgb_175_95_135( = '132')

#### rgb_175_95_175( = '133')

#### rgb_175_95_215( = '134')

#### rgb_175_95_255( = '135')

#### rgb_175_95_95( = '131')

#### rgb_178_178_178( = '249')

#### rgb_188_188_188( = '250')

#### rgb_18_18_18( = '233')

#### rgb_192_192_192( = '7')

#### rgb_198_198_198( = '251')

#### rgb_208_208_208( = '252')

#### rgb_215_0_0( = '160')

#### rgb_215_0_135( = '162')

#### rgb_215_0_175( = '163')

#### rgb_215_0_215( = '164')

#### rgb_215_0_255( = '165')

#### rgb_215_0_95( = '161')

#### rgb_215_135_0( = '172')

#### rgb_215_135_135( = '174')

#### rgb_215_135_175( = '175')

#### rgb_215_135_215( = '176')

#### rgb_215_135_255( = '177')

#### rgb_215_135_95( = '173')

#### rgb_215_175_0( = '178')

#### rgb_215_175_135( = '180')

#### rgb_215_175_175( = '181')

#### rgb_215_175_215( = '182')

#### rgb_215_175_255( = '183')

#### rgb_215_175_95( = '179')

#### rgb_215_215_0( = '184')

#### rgb_215_215_135( = '186')

#### rgb_215_215_175( = '187')

#### rgb_215_215_215( = '188')

#### rgb_215_215_255( = '189')

#### rgb_215_215_95( = '185')

#### rgb_215_255_0( = '190')

#### rgb_215_255_135( = '192')

#### rgb_215_255_175( = '193')

#### rgb_215_255_215( = '194')

#### rgb_215_255_255( = '195')

#### rgb_215_255_95( = '191')

#### rgb_215_95_0( = '166')

#### rgb_215_95_135( = '168')

#### rgb_215_95_175( = '169')

#### rgb_215_95_215( = '170')

#### rgb_215_95_255( = '171')

#### rgb_215_95_95( = '167')

#### rgb_218_218_218( = '253')

#### rgb_228_228_228( = '254')

#### rgb_238_238_238( = '255')

#### rgb_255_0_0( = '9')

#### rgb_255_0_135( = '198')

#### rgb_255_0_175( = '199')

#### rgb_255_0_215( = '200')

#### rgb_255_0_255( = '13')

#### rgb_255_0_95( = '197')

#### rgb_255_135_0( = '208')

#### rgb_255_135_135( = '210')

#### rgb_255_135_175( = '211')

#### rgb_255_135_215( = '212')

#### rgb_255_135_255( = '213')

#### rgb_255_135_95( = '209')

#### rgb_255_175_0( = '214')

#### rgb_255_175_135( = '216')

#### rgb_255_175_175( = '217')

#### rgb_255_175_215( = '218')

#### rgb_255_175_255( = '219')

#### rgb_255_175_95( = '215')

#### rgb_255_215_0( = '220')

#### rgb_255_215_135( = '222')

#### rgb_255_215_175( = '223')

#### rgb_255_215_215( = '224')

#### rgb_255_215_255( = '225')

#### rgb_255_215_95( = '221')

#### rgb_255_255_0( = '11')

#### rgb_255_255_135( = '228')

#### rgb_255_255_175( = '229')

#### rgb_255_255_215( = '230')

#### rgb_255_255_255( = '15')

#### rgb_255_255_95( = '227')

#### rgb_255_95_0( = '202')

#### rgb_255_95_135( = '204')

#### rgb_255_95_175( = '205')

#### rgb_255_95_215( = '206')

#### rgb_255_95_255( = '207')

#### rgb_255_95_95( = '203')

#### rgb_28_28_28( = '234')

#### rgb_38_38_38( = '235')

#### rgb_48_48_48( = '236')

#### rgb_58_58_58( = '237')

#### rgb_68_68_68( = '238')

#### rgb_78_78_78( = '239')

#### rgb_88_88_88( = '240')

#### rgb_8_8_8( = '232')

#### rgb_95_0_0( = '52')

#### rgb_95_0_135( = '54')

#### rgb_95_0_175( = '55')

#### rgb_95_0_215( = '56')

#### rgb_95_0_255( = '57')

#### rgb_95_0_95( = '53')

#### rgb_95_135_0( = '64')

#### rgb_95_135_135( = '66')

#### rgb_95_135_175( = '67')

#### rgb_95_135_215( = '68')

#### rgb_95_135_255( = '69')

#### rgb_95_135_95( = '65')

#### rgb_95_175_0( = '70')

#### rgb_95_175_135( = '72')

#### rgb_95_175_175( = '73')

#### rgb_95_175_215( = '74')

#### rgb_95_175_255( = '75')

#### rgb_95_175_95( = '71')

#### rgb_95_215_0( = '76')

#### rgb_95_215_135( = '78')

#### rgb_95_215_175( = '79')

#### rgb_95_215_215( = '80')

#### rgb_95_215_255( = '81')

#### rgb_95_215_95( = '77')

#### rgb_95_255_0( = '82')

#### rgb_95_255_135( = '84')

#### rgb_95_255_175( = '85')

#### rgb_95_255_215( = '86')

#### rgb_95_255_255( = '87')

#### rgb_95_255_95( = '83')

#### rgb_95_95_0( = '58')

#### rgb_95_95_135( = '60')

#### rgb_95_95_175( = '61')

#### rgb_95_95_215( = '62')

#### rgb_95_95_255( = '63')

#### rgb_95_95_95( = '59')

#### rgb_98_98_98( = '241')

#### rosybrown( = '138')

#### royalblue1( = '63')

#### salmon1( = '209')

#### sandybrown( = '215')

#### seagreen1( = '84')

#### seagreen2( = '83')

#### seagreen3( = '78')

#### seagreen4( = '85')

#### silver( = '7')

#### skyblue1( = '117')

#### skyblue2( = '111')

#### skyblue3( = '74')

#### slateblue1( = '99')

#### slateblue3( = '61')

#### slateblue4( = '62')

#### springgreen1( = '48')

#### springgreen2( = '42')

#### springgreen3( = '35')

#### springgreen4( = '29')

#### springgreen5( = '41')

#### springgreen6( = '47')

#### steelblue( = '67')

#### steelblue1( = '75')

#### steelblue2( = '81')

#### steelblue3( = '68')

#### tan( = '180')

#### teal( = '6')

#### thistle1( = '225')

#### thistle3( = '182')

#### turquoise2( = '45')

#### turquoise4( = '30')

#### violet( = '177')

#### wheat1( = '229')

#### wheat4( = '101')

#### white( = '15')

#### yellow( = '11')

#### yellow1( = '226')

#### yellow2( = '190')

#### yellow3( = '148')

#### yellow4( = '100')

#### yellow5( = '106')

#### yellow6( = '184')

### class pyansiescapes.enums.StrEnum()
Bases: `str`, `enum.Enum`

An enumeration.


### class pyansiescapes.enums.TextAttributes()
Bases: `pyansiescapes.enums.StrEnum`

ANSI Escape Sequences for rich text attributes.


#### blink( = '5')

#### bold( = '1')

#### bright( = '5')

#### concealed( = '8')

#### reset( = '0')

#### reversed( = '7')

#### underline( = '4')

#### underscore( = '4')
## pyansiescapes.types module

## pyansiescapes.utils module

Utility functions used by pyansiescapes.

Provides functions for either parsing arguments, getting correct ids from
ANSI-Enums, or checking for correct types, format etc.


### pyansiescapes.utils.all_are_none(\*args: Any)

### pyansiescapes.utils.all_are_not_none(\*args: Any)

### pyansiescapes.utils.any_is_none(\*args: Any)

### pyansiescapes.utils.any_is_not_none(\*args: Any)

### pyansiescapes.utils.clip_to_closes_color(color: Union[Tuple[int, int, int], List[int]])
Clips the rgb values to their respective closest bin.


### pyansiescapes.utils.get_color_id_from_color_enum(key: str, color_enum: Union[pyansiescapes.enums.Colors, pyansiescapes.enums.Colors256])
Return color_id as str for key in color_enum


* **Parameters**

    
    * **key** – A Color key as str. Any of format:
    name: ‘^[a-z, A-z, 0-9]\*’ (e.g. “blue”)
    hex: ‘^hex_[0-9,a-f]{6}$’ (e.g. “hex_ffffff”)
    rgb: ‘^rgb_[0-9]{1,3}_[0-9]{1,3}_[0-9]{1,3}$’(e.g. rbg_255_0_0)
    hsl: ‘^hsl_[0-9]{1,3}_[0-9]{1,3}_[0-9]{1,3}$’(e.g. hsl_255_0_0)


    * **color_enum** – An enum-obj of type Colors or Colors256.



* **Returns**

    A color id as str (‘^[0-9]{1,3}$’ e.g. ‘102’).



* **Raises**

    **KeyError** – {key} is not a valid color key!
        If key is not a valid color key for Color Enum.



### pyansiescapes.utils.get_color_id_from_color_value(color_value: Union[Tuple[int, int, int], List[int]], colormode: int)
Returns a color id and the correct colormode.

Parses iterarble (eg. (255, 0, 0) into valid key format (eg. rgb_255_0_0).


* **Parameters**

    
    * **color_value** – A color value as list or tuple with len(3):


    * **colormode** – Just provide for compatibility but is ignored since rgb/hsl
    color values toogle colormode 256 automatically.



### pyansiescapes.utils.get_color_id_from_hex(hex: str, colormode: int)
Returns a color id and the correct colormode.

Parses hex str (e.g. “#ffffff”)into valid key format (e.g. “hex_ffffff”).


* **Parameters**

    
    * **hex** – str


    * **hexadecimal color value as str with format** (*A*) – ‘^hex_[0-9,a-f]{6}$’ (e.g. “hex_ffffff”)


    * **colormode** – Just provide for compatibility but is ignored since
    hexdecimalcolor value toogles colormode 256 automatically.



### pyansiescapes.utils.get_color_id_from_id(color_id: int, colormode: int)
Return color_id as str and toggle colormode 256 if necessary.


### pyansiescapes.utils.get_color_id_from_name(name: str, colormode: int)
Returns a color id and the correct colormode.

Parses name into all lower cases letters and toggles colormode 256 if
name is not an 8-bit Color name.


* **Parameters**

    
    * **name** – A color name as str with format name: ‘^[a-z, A-z, 0-9]\*’ (e.g. “blue”).


    * **colormode** – Any integer in [8, 16, 256].



### pyansiescapes.utils.get_color_string(color_id: str, colormode: int)
Return get_color_string func for colormode.


### pyansiescapes.utils.get_color_string_16_bit(color_id: str)
Return ANSI color command string for 16 bit (bold) colors


### pyansiescapes.utils.get_color_string_256_bit(color_id: str)
Return ANSI color command string for 256 bit colors


### pyansiescapes.utils.get_color_string_8_bit(color_id: str)
Return ANSI color command string for 8 bit colors


### pyansiescapes.utils.get_first_color_argument(\*args: Any)
Return first argument in args which is not None.


* **Raises**

    **TypeError** – Cannot parse ‘None’ into a color. Please provide a color!
        If all arguments are None.



### pyansiescapes.utils.has_only_valid_characters(hex: str)
Return True if hex has only valid hexadecimal characters.


### pyansiescapes.utils.is_8bit_color(name: str)
Return True if name is a valid key of Colors-Enum.


### pyansiescapes.utils.is_valid_hex_string(hex: str)
Return True if hex is a valid hexadecimal color value string.


### pyansiescapes.utils.parse_arguments(\*args: Any)
Yields arguments that are not None.


### pyansiescapes.utils.parse_color_name(name: Union[int, pyansiescapes.enums.Colors, pyansiescapes.enums.Colors256, str, Tuple[int, int, int], List[int]])
Parses the color name.


* **Parameters**

    **name** – A color name. Can be any name in Colors or Colors256 as str.
    Strings with leading “#” will trigger hex value parsing.
    Tuple, list or array-like will trigger parsing as either rgb-
    or hsl-values based on the input values.
    See “_parse_rgb_or_hsl” for details on parsing logic.



* **Returns**

    A tuple where the first value defines the color argument category and
    the second value is the color argument parse into the correct type.


### Examples

# Color name string as name argument
>>> parse_color_name(name=”blue”)
(1, ‘blue’)

# Hexadecimal color value as “name” argument
>>> parse_color_name(name=”#ffffff”)
(2, ‘#ffffff’)

# Rgb-values as “name” argument
>>> parse_color_name((255, 0, 0))
(3, (255, 0, 0))

# Color-id as “name” argument
>>> parse_color_name(name=1)
(0, 1)

# Color-id string as “name” argument
>>> parse_color_name(name=”1”)
(0, 1)

# Received incorrect argument for “name”. Raise TypeError.
>>> parse_color_name(name=None)
Traceback (most recent call last):
…
TypeError: Cannot understand “name=None” input argument type


### pyansiescapes.utils.parse_color_value(color_value: Union[Tuple[int, int, int], List[int]], key: str)
Parses color value to color key

RGB-values will be cliped to their respective closest bin.


### pyansiescapes.utils.parse_colormode(colormode: int, blink: bool, bright: bool, bold: bool)
Parse colormode setters into colormode.

Returns the colormode in int. Blink and Bright will override colormode.
Bold overrides colormode if colormode == 8.
setting.


* **Parameters**

    
    * **colormode** – Colormode for colors. Any in [8, 16, 256].


    * **blink** – Toggle blink/bright/256 bit mode.


    * **bright** – Toggle blink/bright/256 bit mode.


    * **bold** – Toggle bold/16-bit mode.



* **Returns**

    Either 8, 16 or 256 (as integer) corresponding to the colormode.



### pyansiescapes.utils.parse_drawing_level(drawing_level: Union[int, bool, str, pyansiescapes.enums.ColorDrawingLevel])
Parse drawing level into legal ANSI drawing level Sequence.


### pyansiescapes.utils.parse_hex(hex: str)
Checks if hex is valid and return it in Colors256-key format.


* **Parameters**

    **hex** – Hexadecimal color value. Must start with “#”, be of lenght 7 and
    must be a valid hexadecimal value (all characters must be in
    set(“#abcdef0123456789”)).



* **Returns**

    The hexadecimal color value in Colors256-key-format (eg. “hex_ffffff”).



* **Raises**

    **TypeError** – {hex} is not a valid hexadecimal color value
        Raised if the input hex string is not valid.


### Examples

# Parse white hexadecimal color value into Colors256-key.
>>> parse_hex(“#ffffff”)
‘hex_ffffff’

# Raise TypeError with hexadecimal color value is wrong.
>>> parse_hex(“ffffff”)
Traceback (most recent call last):
…
TypeError: “ffffff” is not a valid hexadecimal color value

# Raise TypeError with hexadecimal color value is wrong.
>>> parse_hex(“#gfffff”)
Traceback (most recent call last):
…
TypeError: “#gfffff” is not a valid hexadecimal color value


### pyansiescapes.utils.parsing_switcher(argc: int, arg: Union[int, pyansiescapes.enums.Colors, pyansiescapes.enums.Colors256, str, Tuple[int, int, int], List[int]])
Return get color_id function for argument arg.

If argument is ‘name’, parse name first to check if user did not
provide a hexadecimal, rgb or hsl value.


* **Parameters**

    
    * **argc** – The positional argument count [1-4] which specifies the argument type.


    * **arg** – The color argument.



* **Returns**

    The get_color_id_from_{type} function obj.



* **Return type**

    func-obj


## Module contents
