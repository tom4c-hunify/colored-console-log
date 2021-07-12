import logging
import sys
from logging import Formatter

from .extras import ColorMethod
from .formatter import ColorFormatter


class ColoredStreamHandler(logging.StreamHandler):

    def __init__(self, stream=sys.stdout, mode: ColorMethod = ColorMethod.LEVEL) -> None:
        super().__init__(stream)
        self._mode = mode
        self.formatter: ColorFormatter = ColorFormatter("%(levelname)s - %(message)s", mode)

    def setFormatter(self, fmt: Formatter) -> None:
        super().setFormatter(fmt)

    def setColorMode(self, color_mode: ColorMethod):
        if type(self.formatter) == ColorFormatter:
            self.formatter.setMode(color_mode)
