from setuptools import setup, find_packages
import os
from version_query import predict_version_str

file_dir = os.path.abspath(os.path.dirname(__file__))
__version__ = predict_version_str()
name = 'pyansiescapes'

# Get the long description from the README file
with open(os.path.join(file_dir, 'README.md'), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = name,
    version = __version__,
    description = 'Python package for quick and readable console manipulation using ANSI Escapes Sequences',
    long_description = long_description,
    url='https://github.com/tillhainbach/' + name,
    author='Till Hainbach',
    classifiers=[
        'Development Stats :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 ',
        'Programming Language :: Python :: 3 :: only',
    ],
    packages = find_packages(name),
    python_requires='>=3.5',
)

