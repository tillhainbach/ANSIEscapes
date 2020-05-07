from pyansiescapes import ANSIEscapes as ansi
import logging

logging.basicConfig(level = logging.DEBUG)

print(ansi.color('navy'), "Hello!")

print(ansi.blue() + "Hello!")
