import logging
import sys
from logging import Formatter

from .extras import ColorMethod
from .formatter import ColorFormatter


class ColoredStreamHandler(logging.StreamHandler):

    def __init__(self, stream=sys.stdout, mode: ColorMethod = ColorMethod.LEVEL) -> None:
        super().__init__(stream)
        self._mode = mode
        self._fmt = ColorFormatter(mode, "%(levelname)s - %(message)s")
        self.setFormatter(self._fmt)

    def setFormatter(self, fmt: Formatter) -> None:
        self._fmt = ColorFormatter(self._mode, fmt._fmt)
        super().setFormatter(self._fmt)

    def setColorMode(self, color_mode: ColorMethod):
        self._fmt.setMode(color_mode)
