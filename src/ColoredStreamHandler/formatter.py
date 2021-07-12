import logging
from logging import LogRecord

from .extras import ColorMethod, default_colors, TerminalColors


class ColorFormatter(logging.Formatter):

    def __init__(self, color_mode: ColorMethod = ColorMethod.LEVEL, fmt=None, datefmt=None, style='%', validate=True):
        super().__init__(fmt, datefmt, style, validate)
        self._color_mode = color_mode
        self._colors = default_colors

    def setMode(self, mode: ColorMethod):
        self._color_mode = mode

    def format(self, record: LogRecord) -> str:
        if self._color_mode == ColorMethod.NO_COLOR:
            return super().format(record)
        elif self._color_mode == ColorMethod.ALL:
            color_str = self._colors.get(record.levelno, TerminalColors.NO_COLOR).value
            return color_str + super().format(record) + TerminalColors.NO_COLOR.value
        elif self._color_mode == ColorMethod.LEVEL:
            msg = self._reformat_message("%(levelname)s", record)
            return msg
        elif self._color_mode == ColorMethod.MESSAGE:
            msg = self._reformat_message("%(message)s", record)
            return msg

    def _reformat_message(self, param: str, record: LogRecord):
        color_str = self._colors.get(record.levelno, TerminalColors.NO_COLOR).value
        original_fmt = self._style._fmt
        self._style._fmt = original_fmt.replace(param, color_str + param + TerminalColors.NO_COLOR.value)
        msg = super().format(record)
        self._style._fmt = original_fmt
        return msg
