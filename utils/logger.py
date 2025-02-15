import logging
import os


def setup_logger(name, log_file=os.path.join(os.path.dirname(__file__), "..", "logs/test.log"), level=logging.DEBUG):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    return logger


logger = setup_logger("test_logger")
