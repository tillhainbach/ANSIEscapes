PyANSIEscapes - Console Manipulation using ANSI Escapes Sequences
=========================================================================

This package provides human readable functions for adding ANSI escapes sequences to your python console outputs.
It's loosy based on [ansiescapes](https://github.com/kodie/ansiescapes), however offers more convenience functions
for formatting Rich Text.

Installation
-----------
```zsh
git clone https://github.com/tillhainbach/pyansiscapes.git
cd pyansiecapes
# you need to have version_query installed
pip install -U version_query
pip install -e .
```

Usage
------------
```python
import pyansiescapes.commands as ansi

# Print blue text on white background:
print(ansi.format("Hello ANSI!", color = 'blue', background = 'white'))

```

API-Reference
--------------
You can acces the docs using `help(ansi)` in a python REPL or see [docs](./docs/docs.md).
You may the doc-html-files using sphinx with napoleon extentions.

````zsh
pip install -U sphinx
mkdir docs/build
sphinx-build -b html docs/source docs/build
```

Open the `index.html`-file to browse through the documentation.
 

License
--------------

This repository is licensed under the MIT License. See [LICENSE](./LICENSE) for details.


