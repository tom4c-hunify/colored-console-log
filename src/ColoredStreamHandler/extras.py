import logging
from enum import Enum


class ColorMethod(Enum):
    NO_COLOR = 0
    LEVEL = 1
    MESSAGE = 2
    ALL = 3


class TerminalColors(Enum):
    NO_COLOR = "\x1b[0m"
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"


default_colors = {
    logging.NOTSET: TerminalColors.NO_COLOR,
    logging.DEBUG: TerminalColors.BLUE,
    logging.INFO: TerminalColors.GREEN,
    logging.WARNING: TerminalColors.YELLOW,
    logging.ERROR: TerminalColors.RED,
    logging.CRITICAL: TerminalColors.MAGENTA
}
