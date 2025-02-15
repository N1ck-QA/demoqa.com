from webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_util import ConfigUtil
from utils.logger import logger
from utils.random_util import generate_fake_text


class BaseElement:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def log_action(self, message, level=ConfigUtil.load_config().logger_level):
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

    def find_element(self, wait_time=ConfigUtil.load_config().wait_time):
        return WebDriverWait(WebDriver().driver, wait_time).until(
            EC.element_to_be_clickable(self.locator),
            message=f"Can't find element by locator {self.locator}",
        )

    @staticmethod
    def wait_and_switch_to_alert(wait_time=ConfigUtil.load_config().wait_time):
        WebDriverWait(WebDriver().driver, wait_time).until(EC.alert_is_present())
        return WebDriver().driver.switch_to.alert

    def get_text_from_alert(self):
        return self.wait_and_switch_to_alert().text

    def type_text_to_input_in_alert(self):
        alert = self.wait_and_switch_to_alert()
        fake_text = generate_fake_text()
        alert.send_keys(fake_text)
        return fake_text

    def accept_alert(self):
        return self.wait_and_switch_to_alert().accept()

    def switch_to_frame(self):
        parent_frame = self.find_element()
        WebDriver().driver.switch_to.frame(parent_frame)

    def switch_to_inner_frame(self):
        child_frame = self.find_element()
        WebDriver().driver.switch_to.frame(child_frame)

    @staticmethod
    def switch_to_default_content():
        WebDriver().driver.switch_to.default_content()

    @staticmethod
    def switch_to_new_tab():
        WebDriver().driver.switch_to.window(WebDriver().driver.window_handles[1])

    @staticmethod
    def switch_to_home_tab():
        WebDriver().driver.switch_to.window(WebDriver().driver.window_handles[0])

    @staticmethod
    def close_the_tab():
        WebDriver().driver.close()

    def click(self):
        return self.find_element().click()

    def click_js(self):
        WebDriver().driver.execute_script("arguments[0].click();", self.find_element())

    def get_text(self) -> str:
        return self.find_element().text
