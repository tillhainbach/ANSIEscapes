from setuptools import setup, find_packages
import os
from version_query import predict_version_str

fileDir = os.path.abspath(os.path.dirname(__file__))
__version__ = predict_version_str() 

# Get the long description from the README file
with open(os.path.join(fileDir, 'README.md'), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = 'ansiescapecodes',
    version = __version__,
    description = 'API for human-readable console manipulation',
    long_description = long_description,
    url='https://github.com/tillhainbach/ANSIEscapes',
    author='Till Hainbach',
    classifiers=[
        'Development Stats :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 ',
    ],
    packages = find_packages('ansiescapes'),
    python_requires='>=3.5',
)
