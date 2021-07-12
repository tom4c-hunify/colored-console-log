import logging

from ColoredStreamHandler import utils as lutils
from ColoredStreamHandler.extras import ColorMethod

lutils.set_root_logger(logging.NOTSET)
logging.log(0, "notset")
logging.log(5, "custom")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

lutils.set_root_logger(logging.NOTSET, color_mode=ColorMethod.ALL)
logging.log(0, "notset")
logging.log(5, "custom")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
