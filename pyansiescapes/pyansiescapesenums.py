"""Enumerates for different types of ANSI Escape Sequences."""

from enum import IntEnum, Enum


class StrEnum(str, Enum):
    pass


class ANSICommands(StrEnum):
    """ANSI Escape Sequences defining a command."""
    start = "\u001b["
    _debug_esc = "\\u001b"
    stop = "m"
    separator = ";"


class TextAttributes(StrEnum):
    """ANSI Escape Sequences for rich text attributes."""
    reset = "0"  # turn all attributes off
    bold = "1"
    underscore = "4"  # aka underline
    underline = "4"  # aka underscore
    bright = "5"  # aka blink
    blink = "5"  # aka bright
    reversed = "7"
    concealed = "8"


class Colors(StrEnum):
    """ Enum for ANSI Colors"""
    black = "0"
    red = "1"
    green = "2"
    yellow = "3"
    blue = "4"
    magenta = "5"
    cyan = "6"
    white = "7"
    _blink = "8"


class ColorDrawingLevel(StrEnum):
    """ANSI color drawing level id-strings."""
    foreground = "3"
    background = "4"


class Colors256(StrEnum):
    """ Enum for 256bit colors. Uses Each colorId has a name and aliases corresponding to the hex, rgb or hsl value"""
    black = "0"
    maroon = "1"
    green = "2"
    olive = "3"
    navy = "4"
    purple = "5"
    teal = "6"
    silver = "7"
    grey = "8"
    red = "9"
    lime = "10"
    yellow = "11"
    blue = "12"
    fuchsia = "13"
    aqua = "14"
    white = "15"
    grey0 = "16"
    navyblue = "17"
    darkblue = "18"
    blue3 = "19"
    blue4 = "20"
    blue1 = "21"
    darkgreen = "22"
    deepskyblue4 = "23"
    deepskyblue5 = "24"
    deepskyblue6 = "25"
    dodgerblue3 = "26"
    dodgerblue2 = "27"
    green4 = "28"
    springgreen4 = "29"
    turquoise4 = "30"
    deepskyblue3 = "31"
    deepskyblue7 = "32"
    dodgerblue1 = "33"
    green3 = "34"
    springgreen3 = "35"
    darkcyan = "36"
    lightseagreen = "37"
    deepskyblue2 = "38"
    deepskyblue1 = "39"
    green5 = "40"
    springgreen5 = "41"
    springgreen2 = "42"
    cyan3 = "43"
    darkturquoise = "44"
    turquoise2 = "45"
    green1 = "46"
    springgreen6 = "47"
    springgreen1 = "48"
    mediumspringgreen = "49"
    cyan2 = "50"
    cyan1 = "51"
    darkred = "52"
    deeppink4 = "53"
    purple4 = "54"
    purple5 = "55"
    purple3 = "56"
    blueviolet = "57"
    orange4 = "58"
    grey37 = "59"
    mediumpurple4 = "60"
    slateblue3 = "61"
    slateblue4 = "62"
    royalblue1 = "63"
    chartreuse4 = "64"
    darkseagreen4 = "65"
    paleturquoise4 = "66"
    steelblue = "67"
    steelblue3 = "68"
    cornflowerblue = "69"
    chartreuse3 = "70"
    darkseagreen5 = "71"
    cadetblue = "72"
    cadetblue0 = "73"
    skyblue3 = "74"
    steelblue1 = "75"
    chartreuse5 = "76"
    palegreen3 = "77"
    seagreen3 = "78"
    aquamarine3 = "79"
    mediumturquoise = "80"
    steelblue2 = "81"
    chartreuse2 = "82"
    seagreen2 = "83"
    seagreen1 = "84"
    seagreen4 = "85"
    aquamarine1 = "86"
    darkslategray2 = "87"
    darkred0 = "88"
    deeppink5 = "89"
    darkmagenta = "90"
    darkmagenta0 = "91"
    darkviolet = "92"
    purple0 = "93"
    orange5 = "94"
    lightpink4 = "95"
    plum4 = "96"
    mediumpurple3 = "97"
    mediumpurple5 = "98"
    slateblue1 = "99"
    yellow4 = "100"
    wheat4 = "101"
    grey53 = "102"
    lightslategrey = "103"
    mediumpurple = "104"
    lightslateblue = "105"
    yellow5 = "106"
    darkolivegreen3 = "107"
    darkseagreen = "108"
    lightskyblue3 = "109"
    lightskyblue4 = "110"
    skyblue2 = "111"
    chartreuse6 = "112"
    darkolivegreen4 = "113"
    palegreen4 = "114"
    darkseagreen3 = "115"
    darkslategray3 = "116"
    skyblue1 = "117"
    chartreuse1 = "118"
    lightgreen = "119"
    lightgreen0 = "120"
    palegreen1 = "121"
    aquamarine2 = "122"
    darkslategray1 = "123"
    red3 = "124"
    deeppink6 = "125"
    mediumvioletred = "126"
    magenta3 = "127"
    darkviolet0 = "128"
    purple1 = "129"
    darkorange3 = "130"
    indianred = "131"
    hotpink3 = "132"
    mediumorchid3 = "133"
    mediumorchid = "134"
    mediumpurple2 = "135"
    darkgoldenrod = "136"
    lightsalmon3 = "137"
    rosybrown = "138"
    grey63 = "139"
    mediumpurple6 = "140"
    mediumpurple1 = "141"
    gold3 = "142"
    darkkhaki = "143"
    navajowhite3 = "144"
    grey69 = "145"
    lightsteelblue3 = "146"
    lightsteelblue = "147"
    yellow3 = "148"
    darkolivegreen5 = "149"
    darkseagreen6 = "150"
    darkseagreen2 = "151"
    lightcyan3 = "152"
    lightskyblue1 = "153"
    greenyellow = "154"
    darkolivegreen2 = "155"
    palegreen2 = "156"
    darkseagreen7 = "157"
    darkseagreen1 = "158"
    paleturquoise1 = "159"
    red4 = "160"
    deeppink3 = "161"
    deeppink7 = "162"
    magenta4 = "163"
    magenta5 = "164"
    magenta2 = "165"
    darkorange4 = "166"
    indianred0 = "167"
    hotpink4 = "168"
    hotpink2 = "169"
    orchid = "170"
    mediumorchid1 = "171"
    orange3 = "172"
    lightsalmon4 = "173"
    lightpink3 = "174"
    pink3 = "175"
    plum3 = "176"
    violet = "177"
    gold4 = "178"
    lightgoldenrod3 = "179"
    tan = "180"
    mistyrose3 = "181"
    thistle3 = "182"
    plum2 = "183"
    yellow6 = "184"
    khaki3 = "185"
    lightgoldenrod2 = "186"
    lightyellow3 = "187"
    grey84 = "188"
    lightsteelblue1 = "189"
    yellow2 = "190"
    darkolivegreen1 = "191"
    darkolivegreen6 = "192"
    darkseagreen8 = "193"
    honeydew2 = "194"
    lightcyan1 = "195"
    red1 = "196"
    deeppink2 = "197"
    deeppink1 = "198"
    deeppink8 = "199"
    magenta6 = "200"
    magenta1 = "201"
    orangered1 = "202"
    indianred1 = "203"
    indianred2 = "204"
    hotpink = "205"
    hotpink0 = "206"
    mediumorchid2 = "207"
    darkorange = "208"
    salmon1 = "209"
    lightcoral = "210"
    palevioletred1 = "211"
    orchid2 = "212"
    orchid1 = "213"
    orange1 = "214"
    sandybrown = "215"
    lightsalmon1 = "216"
    lightpink1 = "217"
    pink1 = "218"
    plum1 = "219"
    gold1 = "220"
    lightgoldenrod4 = "221"
    lightgoldenrod5 = "222"
    navajowhite1 = "223"
    mistyrose1 = "224"
    thistle1 = "225"
    yellow1 = "226"
    lightgoldenrod1 = "227"
    khaki1 = "228"
    wheat1 = "229"
    cornsilk1 = "230"
    grey100 = "231"
    grey3 = "232"
    grey7 = "233"
    grey11 = "234"
    grey15 = "235"
    grey19 = "236"
    grey23 = "237"
    grey27 = "238"
    grey30 = "239"
    grey35 = "240"
    grey39 = "241"
    grey42 = "242"
    grey46 = "243"
    grey50 = "244"
    grey54 = "245"
    grey58 = "246"
    grey62 = "247"
    grey66 = "248"
    grey70 = "249"
    grey74 = "250"
    grey78 = "251"
    grey82 = "252"
    grey85 = "253"
    grey89 = "254"
    grey93 = "255"
    hex_000000 = "0"
    hex_800000 = "1"
    hex_008000 = "2"
    hex_808000 = "3"
    hex_000080 = "4"
    hex_800080 = "5"
    hex_008080 = "6"
    hex_c0c0c0 = "7"
    hex_808080 = "8"
    hex_ff0000 = "9"
    hex_00ff00 = "10"
    hex_ffff00 = "11"
    hex_0000ff = "12"
    hex_ff00ff = "13"
    hex_00ffff = "14"
    hex_ffffff = "15"
    hex_00005f = "17"
    hex_000087 = "18"
    hex_0000af = "19"
    hex_0000d7 = "20"
    hex_005f00 = "22"
    hex_005f5f = "23"
    hex_005f87 = "24"
    hex_005faf = "25"
    hex_005fd7 = "26"
    hex_005fff = "27"
    hex_008700 = "28"
    hex_00875f = "29"
    hex_008787 = "30"
    hex_0087af = "31"
    hex_0087d7 = "32"
    hex_0087ff = "33"
    hex_00af00 = "34"
    hex_00af5f = "35"
    hex_00af87 = "36"
    hex_00afaf = "37"
    hex_00afd7 = "38"
    hex_00afff = "39"
    hex_00d700 = "40"
    hex_00d75f = "41"
    hex_00d787 = "42"
    hex_00d7af = "43"
    hex_00d7d7 = "44"
    hex_00d7ff = "45"
    hex_00ff5f = "47"
    hex_00ff87 = "48"
    hex_00ffaf = "49"
    hex_00ffd7 = "50"
    hex_5f0000 = "52"
    hex_5f005f = "53"
    hex_5f0087 = "54"
    hex_5f00af = "55"
    hex_5f00d7 = "56"
    hex_5f00ff = "57"
    hex_5f5f00 = "58"
    hex_5f5f5f = "59"
    hex_5f5f87 = "60"
    hex_5f5faf = "61"
    hex_5f5fd7 = "62"
    hex_5f5fff = "63"
    hex_5f8700 = "64"
    hex_5f875f = "65"
    hex_5f8787 = "66"
    hex_5f87af = "67"
    hex_5f87d7 = "68"
    hex_5f87ff = "69"
    hex_5faf00 = "70"
    hex_5faf5f = "71"
    hex_5faf87 = "72"
    hex_5fafaf = "73"
    hex_5fafd7 = "74"
    hex_5fafff = "75"
    hex_5fd700 = "76"
    hex_5fd75f = "77"
    hex_5fd787 = "78"
    hex_5fd7af = "79"
    hex_5fd7d7 = "80"
    hex_5fd7ff = "81"
    hex_5fff00 = "82"
    hex_5fff5f = "83"
    hex_5fff87 = "84"
    hex_5fffaf = "85"
    hex_5fffd7 = "86"
    hex_5fffff = "87"
    hex_870000 = "88"
    hex_87005f = "89"
    hex_870087 = "90"
    hex_8700af = "91"
    hex_8700d7 = "92"
    hex_8700ff = "93"
    hex_875f00 = "94"
    hex_875f5f = "95"
    hex_875f87 = "96"
    hex_875faf = "97"
    hex_875fd7 = "98"
    hex_875fff = "99"
    hex_878700 = "100"
    hex_87875f = "101"
    hex_878787 = "102"
    hex_8787af = "103"
    hex_8787d7 = "104"
    hex_8787ff = "105"
    hex_87af00 = "106"
    hex_87af5f = "107"
    hex_87af87 = "108"
    hex_87afaf = "109"
    hex_87afd7 = "110"
    hex_87afff = "111"
    hex_87d700 = "112"
    hex_87d75f = "113"
    hex_87d787 = "114"
    hex_87d7af = "115"
    hex_87d7d7 = "116"
    hex_87d7ff = "117"
    hex_87ff00 = "118"
    hex_87ff5f = "119"
    hex_87ff87 = "120"
    hex_87ffaf = "121"
    hex_87ffd7 = "122"
    hex_87ffff = "123"
    hex_af0000 = "124"
    hex_af005f = "125"
    hex_af0087 = "126"
    hex_af00af = "127"
    hex_af00d7 = "128"
    hex_af00ff = "129"
    hex_af5f00 = "130"
    hex_af5f5f = "131"
    hex_af5f87 = "132"
    hex_af5faf = "133"
    hex_af5fd7 = "134"
    hex_af5fff = "135"
    hex_af8700 = "136"
    hex_af875f = "137"
    hex_af8787 = "138"
    hex_af87af = "139"
    hex_af87d7 = "140"
    hex_af87ff = "141"
    hex_afaf00 = "142"
    hex_afaf5f = "143"
    hex_afaf87 = "144"
    hex_afafaf = "145"
    hex_afafd7 = "146"
    hex_afafff = "147"
    hex_afd700 = "148"
    hex_afd75f = "149"
    hex_afd787 = "150"
    hex_afd7af = "151"
    hex_afd7d7 = "152"
    hex_afd7ff = "153"
    hex_afff00 = "154"
    hex_afff5f = "155"
    hex_afff87 = "156"
    hex_afffaf = "157"
    hex_afffd7 = "158"
    hex_afffff = "159"
    hex_d70000 = "160"
    hex_d7005f = "161"
    hex_d70087 = "162"
    hex_d700af = "163"
    hex_d700d7 = "164"
    hex_d700ff = "165"
    hex_d75f00 = "166"
    hex_d75f5f = "167"
    hex_d75f87 = "168"
    hex_d75faf = "169"
    hex_d75fd7 = "170"
    hex_d75fff = "171"
    hex_d78700 = "172"
    hex_d7875f = "173"
    hex_d78787 = "174"
    hex_d787af = "175"
    hex_d787d7 = "176"
    hex_d787ff = "177"
    hex_d7af00 = "178"
    hex_d7af5f = "179"
    hex_d7af87 = "180"
    hex_d7afaf = "181"
    hex_d7afd7 = "182"
    hex_d7afff = "183"
    hex_d7d700 = "184"
    hex_d7d75f = "185"
    hex_d7d787 = "186"
    hex_d7d7af = "187"
    hex_d7d7d7 = "188"
    hex_d7d7ff = "189"
    hex_d7ff00 = "190"
    hex_d7ff5f = "191"
    hex_d7ff87 = "192"
    hex_d7ffaf = "193"
    hex_d7ffd7 = "194"
    hex_d7ffff = "195"
    hex_ff005f = "197"
    hex_ff0087 = "198"
    hex_ff00af = "199"
    hex_ff00d7 = "200"
    hex_ff5f00 = "202"
    hex_ff5f5f = "203"
    hex_ff5f87 = "204"
    hex_ff5faf = "205"
    hex_ff5fd7 = "206"
    hex_ff5fff = "207"
    hex_ff8700 = "208"
    hex_ff875f = "209"
    hex_ff8787 = "210"
    hex_ff87af = "211"
    hex_ff87d7 = "212"
    hex_ff87ff = "213"
    hex_ffaf00 = "214"
    hex_ffaf5f = "215"
    hex_ffaf87 = "216"
    hex_ffafaf = "217"
    hex_ffafd7 = "218"
    hex_ffafff = "219"
    hex_ffd700 = "220"
    hex_ffd75f = "221"
    hex_ffd787 = "222"
    hex_ffd7af = "223"
    hex_ffd7d7 = "224"
    hex_ffd7ff = "225"
    hex_ffff5f = "227"
    hex_ffff87 = "228"
    hex_ffffaf = "229"
    hex_ffffd7 = "230"
    hex_080808 = "232"
    hex_121212 = "233"
    hex_1c1c1c = "234"
    hex_262626 = "235"
    hex_303030 = "236"
    hex_3a3a3a = "237"
    hex_444444 = "238"
    hex_4e4e4e = "239"
    hex_585858 = "240"
    hex_626262 = "241"
    hex_6c6c6c = "242"
    hex_767676 = "243"
    hex_8a8a8a = "245"
    hex_949494 = "246"
    hex_9e9e9e = "247"
    hex_a8a8a8 = "248"
    hex_b2b2b2 = "249"
    hex_bcbcbc = "250"
    hex_c6c6c6 = "251"
    hex_d0d0d0 = "252"
    hex_dadada = "253"
    hex_e4e4e4 = "254"
    hex_eeeeee = "255"
    rgb_0_0_0 = "0"
    rgb_128_0_0 = "1"
    rgb_0_128_0 = "2"
    rgb_128_128_0 = "3"
    rgb_0_0_128 = "4"
    rgb_128_0_128 = "5"
    rgb_0_128_128 = "6"
    rgb_192_192_192 = "7"
    rgb_128_128_128 = "8"
    rgb_255_0_0 = "9"
    rgb_0_255_0 = "10"
    rgb_255_255_0 = "11"
    rgb_0_0_255 = "12"
    rgb_255_0_255 = "13"
    rgb_0_255_255 = "14"
    rgb_255_255_255 = "15"
    rgb_0_0_95 = "17"
    rgb_0_0_135 = "18"
    rgb_0_0_175 = "19"
    rgb_0_0_215 = "20"
    rgb_0_95_0 = "22"
    rgb_0_95_95 = "23"
    rgb_0_95_135 = "24"
    rgb_0_95_175 = "25"
    rgb_0_95_215 = "26"
    rgb_0_95_255 = "27"
    rgb_0_135_0 = "28"
    rgb_0_135_95 = "29"
    rgb_0_135_135 = "30"
    rgb_0_135_175 = "31"
    rgb_0_135_215 = "32"
    rgb_0_135_255 = "33"
    rgb_0_175_0 = "34"
    rgb_0_175_95 = "35"
    rgb_0_175_135 = "36"
    rgb_0_175_175 = "37"
    rgb_0_175_215 = "38"
    rgb_0_175_255 = "39"
    rgb_0_215_0 = "40"
    rgb_0_215_95 = "41"
    rgb_0_215_135 = "42"
    rgb_0_215_175 = "43"
    rgb_0_215_215 = "44"
    rgb_0_215_255 = "45"
    rgb_0_255_95 = "47"
    rgb_0_255_135 = "48"
    rgb_0_255_175 = "49"
    rgb_0_255_215 = "50"
    rgb_95_0_0 = "52"
    rgb_95_0_95 = "53"
    rgb_95_0_135 = "54"
    rgb_95_0_175 = "55"
    rgb_95_0_215 = "56"
    rgb_95_0_255 = "57"
    rgb_95_95_0 = "58"
    rgb_95_95_95 = "59"
    rgb_95_95_135 = "60"
    rgb_95_95_175 = "61"
    rgb_95_95_215 = "62"
    rgb_95_95_255 = "63"
    rgb_95_135_0 = "64"
    rgb_95_135_95 = "65"
    rgb_95_135_135 = "66"
    rgb_95_135_175 = "67"
    rgb_95_135_215 = "68"
    rgb_95_135_255 = "69"
    rgb_95_175_0 = "70"
    rgb_95_175_95 = "71"
    rgb_95_175_135 = "72"
    rgb_95_175_175 = "73"
    rgb_95_175_215 = "74"
    rgb_95_175_255 = "75"
    rgb_95_215_0 = "76"
    rgb_95_215_95 = "77"
    rgb_95_215_135 = "78"
    rgb_95_215_175 = "79"
    rgb_95_215_215 = "80"
    rgb_95_215_255 = "81"
    rgb_95_255_0 = "82"
    rgb_95_255_95 = "83"
    rgb_95_255_135 = "84"
    rgb_95_255_175 = "85"
    rgb_95_255_215 = "86"
    rgb_95_255_255 = "87"
    rgb_135_0_0 = "88"
    rgb_135_0_95 = "89"
    rgb_135_0_135 = "90"
    rgb_135_0_175 = "91"
    rgb_135_0_215 = "92"
    rgb_135_0_255 = "93"
    rgb_135_95_0 = "94"
    rgb_135_95_95 = "95"
    rgb_135_95_135 = "96"
    rgb_135_95_175 = "97"
    rgb_135_95_215 = "98"
    rgb_135_95_255 = "99"
    rgb_135_135_0 = "100"
    rgb_135_135_95 = "101"
    rgb_135_135_135 = "102"
    rgb_135_135_175 = "103"
    rgb_135_135_215 = "104"
    rgb_135_135_255 = "105"
    rgb_135_175_0 = "106"
    rgb_135_175_95 = "107"
    rgb_135_175_135 = "108"
    rgb_135_175_175 = "109"
    rgb_135_175_215 = "110"
    rgb_135_175_255 = "111"
    rgb_135_215_0 = "112"
    rgb_135_215_95 = "113"
    rgb_135_215_135 = "114"
    rgb_135_215_175 = "115"
    rgb_135_215_215 = "116"
    rgb_135_215_255 = "117"
    rgb_135_255_0 = "118"
    rgb_135_255_95 = "119"
    rgb_135_255_135 = "120"
    rgb_135_255_175 = "121"
    rgb_135_255_215 = "122"
    rgb_135_255_255 = "123"
    rgb_175_0_0 = "124"
    rgb_175_0_95 = "125"
    rgb_175_0_135 = "126"
    rgb_175_0_175 = "127"
    rgb_175_0_215 = "128"
    rgb_175_0_255 = "129"
    rgb_175_95_0 = "130"
    rgb_175_95_95 = "131"
    rgb_175_95_135 = "132"
    rgb_175_95_175 = "133"
    rgb_175_95_215 = "134"
    rgb_175_95_255 = "135"
    rgb_175_135_0 = "136"
    rgb_175_135_95 = "137"
    rgb_175_135_135 = "138"
    rgb_175_135_175 = "139"
    rgb_175_135_215 = "140"
    rgb_175_135_255 = "141"
    rgb_175_175_0 = "142"
    rgb_175_175_95 = "143"
    rgb_175_175_135 = "144"
    rgb_175_175_175 = "145"
    rgb_175_175_215 = "146"
    rgb_175_175_255 = "147"
    rgb_175_215_0 = "148"
    rgb_175_215_95 = "149"
    rgb_175_215_135 = "150"
    rgb_175_215_175 = "151"
    rgb_175_215_215 = "152"
    rgb_175_215_255 = "153"
    rgb_175_255_0 = "154"
    rgb_175_255_95 = "155"
    rgb_175_255_135 = "156"
    rgb_175_255_175 = "157"
    rgb_175_255_215 = "158"
    rgb_175_255_255 = "159"
    rgb_215_0_0 = "160"
    rgb_215_0_95 = "161"
    rgb_215_0_135 = "162"
    rgb_215_0_175 = "163"
    rgb_215_0_215 = "164"
    rgb_215_0_255 = "165"
    rgb_215_95_0 = "166"
    rgb_215_95_95 = "167"
    rgb_215_95_135 = "168"
    rgb_215_95_175 = "169"
    rgb_215_95_215 = "170"
    rgb_215_95_255 = "171"
    rgb_215_135_0 = "172"
    rgb_215_135_95 = "173"
    rgb_215_135_135 = "174"
    rgb_215_135_175 = "175"
    rgb_215_135_215 = "176"
    rgb_215_135_255 = "177"
    rgb_215_175_0 = "178"
    rgb_215_175_95 = "179"
    rgb_215_175_135 = "180"
    rgb_215_175_175 = "181"
    rgb_215_175_215 = "182"
    rgb_215_175_255 = "183"
    rgb_215_215_0 = "184"
    rgb_215_215_95 = "185"
    rgb_215_215_135 = "186"
    rgb_215_215_175 = "187"
    rgb_215_215_215 = "188"
    rgb_215_215_255 = "189"
    rgb_215_255_0 = "190"
    rgb_215_255_95 = "191"
    rgb_215_255_135 = "192"
    rgb_215_255_175 = "193"
    rgb_215_255_215 = "194"
    rgb_215_255_255 = "195"
    rgb_255_0_95 = "197"
    rgb_255_0_135 = "198"
    rgb_255_0_175 = "199"
    rgb_255_0_215 = "200"
    rgb_255_95_0 = "202"
    rgb_255_95_95 = "203"
    rgb_255_95_135 = "204"
    rgb_255_95_175 = "205"
    rgb_255_95_215 = "206"
    rgb_255_95_255 = "207"
    rgb_255_135_0 = "208"
    rgb_255_135_95 = "209"
    rgb_255_135_135 = "210"
    rgb_255_135_175 = "211"
    rgb_255_135_215 = "212"
    rgb_255_135_255 = "213"
    rgb_255_175_0 = "214"
    rgb_255_175_95 = "215"
    rgb_255_175_135 = "216"
    rgb_255_175_175 = "217"
    rgb_255_175_215 = "218"
    rgb_255_175_255 = "219"
    rgb_255_215_0 = "220"
    rgb_255_215_95 = "221"
    rgb_255_215_135 = "222"
    rgb_255_215_175 = "223"
    rgb_255_215_215 = "224"
    rgb_255_215_255 = "225"
    rgb_255_255_95 = "227"
    rgb_255_255_135 = "228"
    rgb_255_255_175 = "229"
    rgb_255_255_215 = "230"
    rgb_8_8_8 = "232"
    rgb_18_18_18 = "233"
    rgb_28_28_28 = "234"
    rgb_38_38_38 = "235"
    rgb_48_48_48 = "236"
    rgb_58_58_58 = "237"
    rgb_68_68_68 = "238"
    rgb_78_78_78 = "239"
    rgb_88_88_88 = "240"
    rgb_98_98_98 = "241"
    rgb_108_108_108 = "242"
    rgb_118_118_118 = "243"
    rgb_138_138_138 = "245"
    rgb_148_148_148 = "246"
    rgb_158_158_158 = "247"
    rgb_168_168_168 = "248"
    rgb_178_178_178 = "249"
    rgb_188_188_188 = "250"
    rgb_198_198_198 = "251"
    rgb_208_208_208 = "252"
    rgb_218_218_218 = "253"
    rgb_228_228_228 = "254"
    rgb_238_238_238 = "255"
    hsl_0_0_0 = "0"
    hsl_0_100_25 = "1"
    hsl_120_100_25 = "2"
    hsl_60_100_25 = "3"
    hsl_240_100_25 = "4"
    hsl_300_100_25 = "5"
    hsl_180_100_25 = "6"
    hsl_0_0_75 = "7"
    hsl_0_0_50 = "8"
    hsl_0_100_50 = "9"
    hsl_120_100_50 = "10"
    hsl_60_100_50 = "11"
    hsl_240_100_50 = "12"
    hsl_300_100_50 = "13"
    hsl_180_100_50 = "14"
    hsl_0_0_100 = "15"
    hsl_240_100_18 = "17"
    hsl_240_100_26 = "18"
    hsl_240_100_34 = "19"
    hsl_240_100_42 = "20"
    hsl_120_100_18 = "22"
    hsl_180_100_18 = "23"
    hsl_197_100_26 = "24"
    hsl_207_100_34 = "25"
    hsl_213_100_42 = "26"
    hsl_217_100_50 = "27"
    hsl_120_100_26 = "28"
    hsl_162_100_26 = "29"
    hsl_180_100_26 = "30"
    hsl_193_100_34 = "31"
    hsl_202_100_42 = "32"
    hsl_208_100_50 = "33"
    hsl_120_100_34 = "34"
    hsl_152_100_34 = "35"
    hsl_166_100_34 = "36"
    hsl_180_100_34 = "37"
    hsl_191_100_42 = "38"
    hsl_198_100_50 = "39"
    hsl_120_100_42 = "40"
    hsl_146_100_42 = "41"
    hsl_157_100_42 = "42"
    hsl_168_100_42 = "43"
    hsl_180_100_42 = "44"
    hsl_189_100_50 = "45"
    hsl_142_100_50 = "47"
    hsl_151_100_50 = "48"
    hsl_161_100_50 = "49"
    hsl_170_100_50 = "50"
    hsl_0_100_18 = "52"
    hsl_300_100_18 = "53"
    hsl_282_100_26 = "54"
    hsl_272_100_34 = "55"
    hsl_266_100_42 = "56"
    hsl_262_100_50 = "57"
    hsl_60_100_18 = "58"
    hsl_0_0_37 = "59"
    hsl_240_17_45 = "60"
    hsl_240_33_52 = "61"
    hsl_240_60_60 = "62"
    hsl_240_100_68 = "63"
    hsl_77_100_26 = "64"
    hsl_120_17_45 = "65"
    hsl_180_17_45 = "66"
    hsl_210_33_52 = "67"
    hsl_220_60_60 = "68"
    hsl_225_100_68 = "69"
    hsl_87_100_34 = "70"
    hsl_120_33_52 = "71"
    hsl_150_33_52 = "72"
    hsl_180_33_52 = "73"
    hsl_200_60_60 = "74"
    hsl_210_100_68 = "75"
    hsl_93_100_42 = "76"
    hsl_120_60_60 = "77"
    hsl_140_60_60 = "78"
    hsl_160_60_60 = "79"
    hsl_180_60_60 = "80"
    hsl_195_100_68 = "81"
    hsl_97_100_50 = "82"
    hsl_120_100_68 = "83"
    hsl_135_100_68 = "84"
    hsl_150_100_68 = "85"
    hsl_165_100_68 = "86"
    hsl_180_100_68 = "87"
    hsl_0_100_26 = "88"
    hsl_317_100_26 = "89"
    hsl_300_100_26 = "90"
    hsl_286_100_34 = "91"
    hsl_277_100_42 = "92"
    hsl_271_100_50 = "93"
    hsl_42_100_26 = "94"
    hsl_0_17_45 = "95"
    hsl_300_17_45 = "96"
    hsl_270_33_52 = "97"
    hsl_260_60_60 = "98"
    hsl_255_100_68 = "99"
    hsl_60_100_26 = "100"
    hsl_60_17_45 = "101"
    hsl_0_0_52 = "102"
    hsl_240_20_60 = "103"
    hsl_240_50_68 = "104"
    hsl_240_100_76 = "105"
    hsl_73_100_34 = "106"
    hsl_90_33_52 = "107"
    hsl_120_20_60 = "108"
    hsl_180_20_60 = "109"
    hsl_210_50_68 = "110"
    hsl_220_100_76 = "111"
    hsl_82_100_42 = "112"
    hsl_100_60_60 = "113"
    hsl_120_50_68 = "114"
    hsl_150_50_68 = "115"
    hsl_180_50_68 = "116"
    hsl_200_100_76 = "117"
    hsl_88_100_50 = "118"
    hsl_105_100_68 = "119"
    hsl_120_100_76 = "120"
    hsl_140_100_76 = "121"
    hsl_160_100_76 = "122"
    hsl_180_100_76 = "123"
    hsl_0_100_34 = "124"
    hsl_327_100_34 = "125"
    hsl_313_100_34 = "126"
    hsl_300_100_34 = "127"
    hsl_288_100_42 = "128"
    hsl_281_100_50 = "129"
    hsl_32_100_34 = "130"
    hsl_0_33_52 = "131"
    hsl_330_33_52 = "132"
    hsl_300_33_52 = "133"
    hsl_280_60_60 = "134"
    hsl_270_100_68 = "135"
    hsl_46_100_34 = "136"
    hsl_30_33_52 = "137"
    hsl_0_20_60 = "138"
    hsl_300_20_60 = "139"
    hsl_270_50_68 = "140"
    hsl_260_100_76 = "141"
    hsl_60_100_34 = "142"
    hsl_60_33_52 = "143"
    hsl_60_20_60 = "144"
    hsl_0_0_68 = "145"
    hsl_240_33_76 = "146"
    hsl_240_100_84 = "147"
    hsl_71_100_42 = "148"
    hsl_80_60_60 = "149"
    hsl_90_50_68 = "150"
    hsl_120_33_76 = "151"
    hsl_180_33_76 = "152"
    hsl_210_100_84 = "153"
    hsl_78_100_50 = "154"
    hsl_90_100_68 = "155"
    hsl_100_100_76 = "156"
    hsl_120_100_84 = "157"
    hsl_150_100_84 = "158"
    hsl_180_100_84 = "159"
    hsl_0_100_42 = "160"
    hsl_333_100_42 = "161"
    hsl_322_100_42 = "162"
    hsl_311_100_42 = "163"
    hsl_300_100_42 = "164"
    hsl_290_100_50 = "165"
    hsl_26_100_42 = "166"
    hsl_0_60_60 = "167"
    hsl_340_60_60 = "168"
    hsl_320_60_60 = "169"
    hsl_300_60_60 = "170"
    hsl_285_100_68 = "171"
    hsl_37_100_42 = "172"
    hsl_20_60_60 = "173"
    hsl_0_50_68 = "174"
    hsl_330_50_68 = "175"
    hsl_300_50_68 = "176"
    hsl_280_100_76 = "177"
    hsl_48_100_42 = "178"
    hsl_40_60_60 = "179"
    hsl_30_50_68 = "180"
    hsl_0_33_76 = "181"
    hsl_300_33_76 = "182"
    hsl_270_100_84 = "183"
    hsl_60_100_42 = "184"
    hsl_60_60_60 = "185"
    hsl_60_50_68 = "186"
    hsl_60_33_76 = "187"
    hsl_0_0_84 = "188"
    hsl_240_100_92 = "189"
    hsl_69_100_50 = "190"
    hsl_75_100_68 = "191"
    hsl_80_100_76 = "192"
    hsl_90_100_84 = "193"
    hsl_120_100_92 = "194"
    hsl_180_100_92 = "195"
    hsl_337_100_50 = "197"
    hsl_328_100_50 = "198"
    hsl_318_100_50 = "199"
    hsl_309_100_50 = "200"
    hsl_22_100_50 = "202"
    hsl_0_100_68 = "203"
    hsl_345_100_68 = "204"
    hsl_330_100_68 = "205"
    hsl_315_100_68 = "206"
    hsl_300_100_68 = "207"
    hsl_31_100_50 = "208"
    hsl_15_100_68 = "209"
    hsl_0_100_76 = "210"
    hsl_340_100_76 = "211"
    hsl_320_100_76 = "212"
    hsl_300_100_76 = "213"
    hsl_41_100_50 = "214"
    hsl_30_100_68 = "215"
    hsl_20_100_76 = "216"
    hsl_0_100_84 = "217"
    hsl_330_100_84 = "218"
    hsl_300_100_84 = "219"
    hsl_50_100_50 = "220"
    hsl_45_100_68 = "221"
    hsl_40_100_76 = "222"
    hsl_30_100_84 = "223"
    hsl_0_100_92 = "224"
    hsl_300_100_92 = "225"
    hsl_60_100_68 = "227"
    hsl_60_100_76 = "228"
    hsl_60_100_84 = "229"
    hsl_60_100_92 = "230"
    hsl_0_0_3 = "232"
    hsl_0_0_7 = "233"
    hsl_0_0_10 = "234"
    hsl_0_0_14 = "235"
    hsl_0_0_18 = "236"
    hsl_0_0_22 = "237"
    hsl_0_0_26 = "238"
    hsl_0_0_30 = "239"
    hsl_0_0_34 = "240"
    hsl_0_0_40 = "242"
    hsl_0_0_46 = "243"
    hsl_0_0_54 = "245"
    hsl_0_0_58 = "246"
    hsl_0_0_61 = "247"
    hsl_0_0_65 = "248"
    hsl_0_0_69 = "249"
    hsl_0_0_73 = "250"
    hsl_0_0_77 = "251"
    hsl_0_0_81 = "252"
    hsl_0_0_85 = "253"
    hsl_0_0_89 = "254"
    hsl_0_0_93 = "255"
