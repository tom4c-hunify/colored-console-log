import logging

from src.ColoredStreamHandler import utils as lutils


lutils.set_root_logger(logging.NOTSET)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
