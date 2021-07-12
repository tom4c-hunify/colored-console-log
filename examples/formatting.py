import logging

from ColoredStreamHandler.extras import TerminalColors, ColorMethod
from ColoredStreamHandler.formatter import ColorFormatter
from ColoredStreamHandler.handler import ColoredStreamHandler

logging.root.setLevel(logging.NOTSET)
logging.addLevelName(1, 'verbose')
logging.addLevelName(2, 'custom')
h = ColoredStreamHandler()
h.setFormatter(ColorFormatter("%(asctime)s-%(message)s", ColorMethod.MESSAGE))
h.formatter.setLevelColor(1, TerminalColors.LIGHT_MAGENTA)
h.formatter.setLevelColor(2, TerminalColors.LIGHT_CYAN)
h.setLevel(logging.NOTSET)
logging.root.addHandler(h)

logging.log(1, "verbose")
logging.log(2, "CUSTOM")
h.setColorMode(ColorMethod.ALL)

logging.log(1, "verbose")
logging.log(2, "CUSTOM")
