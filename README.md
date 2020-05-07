ANSIEscapes: Python package for quick and readable ANSI Escapes Sequences
=========================================================================

This package provides human readable functions for adding ANSI escapes sequences to your python console outputs.
It's loosy based on [ansiescapes](https://github.com/kodie/ansiescapes), however offers more convenience functions
for formatting Rich Text.

Installation
-----------
NOTE: This Package is currently under development.

```zsh
git clone https://github.com/tillhainbach/pyansiscapes.git
cd pyansiecapes
pip install -e .
```

Usage
------------
```python
from pyansiescapes import ANSIEscapes as ansi

# Print blue text on white background:
print(ansi.formatText("Hello ANSI!", color = 'blue', background = 'white'))

```

API-Reference
--------------
You can acces the docs using `help(ansi)` in a python REPL or see [docs.md] (./docs.md).

NOTE: This Package is currently under development therefore not all functions will be documented appropiatly.
Documentation will be added succesively.

License
--------------

This repository is licensed under the MIT License. See [LICENSE](./LICENSE) for details.


