import logging

from cclogs.extras import TerminalColors, ColorMethod
from cclogs.formatter import ColorFormatter
from cclogs.handler import ColoredStreamHandler

logging.root.setLevel(logging.NOTSET)
logging.addLevelName(1, 'verbose')
logging.addLevelName(22, 'custom')
h = ColoredStreamHandler()
f = ColorFormatter("%(asctime)s - %(levelname)s - %(message)s", ColorMethod.MESSAGE)
h.setFormatter(f)
h.formatter.setLevelColor(1, TerminalColors.LIGHT_MAGENTA)
h.formatter.setLevelColor(22, TerminalColors.LIGHT_CYAN)
h.setLevel(logging.NOTSET)
logging.root.addHandler(h)

logging.log(1, "verbose")
logging.log(22, "CUSTOM")

h.setLevel(20)
h.setColorMode(ColorMethod.ALL)

logging.log(1, "verbose")
logging.log(22, "CUSTOM")
