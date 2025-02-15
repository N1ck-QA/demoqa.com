from Elements.base_element import BaseElement
from selenium.webdriver.common.keys import Keys


class Input(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys(self, data):
        self.find_element().send_keys(Keys.COMMAND + "a") or self.find_element().send_keys(Keys.CONTROL + "a")
        self.find_element().send_keys(Keys.BACKSPACE)
        self.find_element().send_keys(data)
