from webdriver import WebDriver
from utils.config_util import ConfigUtil
from selenium.common.exceptions import TimeoutException
from Elements.base_element import BaseElement
from utils.logger import logger


class BasePage:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    @staticmethod
    def open_url():
        WebDriver().driver.get(ConfigUtil.load_config().base_url)

    def log_action(self, message='is displayed', level=ConfigUtil.load_config().logger_level):
        if level == "DEBUG":
            logger.debug(f"{self.name}: {message}")
        elif level == "INFO":
            logger.info(f"{self.name}: {message}")
        elif level == "WARNING":
            logger.warning(f"{self.name}: {message}")
        elif level == "ERROR":
            logger.error(f"{self.name}: {message}")
        elif level == "CRITICAL":
            logger.critical(f"{self.name}: {message}")
        else:
            logger.info(f"{self.name}: {message}")

    def is_displayed(self):
        self.log_action()
        try:
            return BaseElement(self.locator, self.name).find_element().is_displayed()
        except TimeoutException:
            return False


