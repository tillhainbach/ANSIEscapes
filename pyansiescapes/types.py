from typing import List, Dict, Tuple, Callable, Any, Optional, Iterator, Union
from pyansiescapes.pyansiescapesenums import *

ColorBins = List[int]
ColorValueTuple = Tuple[int, int, int]
ColorValueList = List[int]
ColorValue = Union[ColorValueTuple, ColorValueList]
ColorArg = Union[int, Colors, Colors256, str, ColorValue]
ColorArgTuple = Tuple[int, ColorArg]
ColorEnum = Union[Colors, Colors256]
DrawingLevelArg = Union[int, bool, str, ColorDrawingLevel]
