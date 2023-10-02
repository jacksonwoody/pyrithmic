import logging


logger = logging.getLogger(__name__)


def get_log_format():
    log_format = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    return log_format


def configure_logging(logger_obj, level=logging.DEBUG):
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(get_log_format())
    logger_obj.setLevel(level)
    logger_obj.addHandler(console_handler)
