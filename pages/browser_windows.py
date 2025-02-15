from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button
from Elements.caption import Caption
from Elements.base_element import BaseElement


class BrowserWindows(BasePage):
    __button_browser_windows_in_navbar_on_left_panel = Button(
        (By.XPATH, '//ul[@class = "menu-list"]//*[contains (text(), "Browser Windows")]'),
        'Button "Browser Windows"')

    __button_new_tab = Button(
        (By.XPATH, '//*[@id = "tabButton"]'),
        'Button "New tab"')

    __caption_on_new_tab = Caption(
        (By.XPATH, '//*[@id = "sampleHeading"]'),
        'Text on new tab')

    def __init__(self):
        super().__init__((By.XPATH, '//*[@id = "tabButton"]'),
                         'Browser Windows Page')

    def click_button_browser_windows_on_left_panel(self):
        self.__button_browser_windows_in_navbar_on_left_panel.click()
        self.__button_browser_windows_in_navbar_on_left_panel.log_action("was clicked")

    @staticmethod
    def switch_to_new_tab():
        BaseElement(None, 'Tab interaction').switch_to_new_tab()
        BaseElement(None, 'Tab interaction').log_action('Switching to new tab')

    @staticmethod
    def switch_to_home_tab():
        BaseElement(None, 'Tab interaction').switch_to_home_tab()
        BaseElement(None, 'Tab interaction').log_action('Switching to home tab')

    @staticmethod
    def close_the_tab():
        BaseElement(None, 'Tab interaction').close_the_tab()
        BaseElement(None, 'Tab interaction').log_action('Tab was closed')

    def click_new_tab_button(self):
        self.__button_new_tab.click()
        self.__button_new_tab.log_action('was clicked')

    def get_text_on_new_tab(self):
        self.__caption_on_new_tab.log_action('Text from opened tab was received')
        return self.__caption_on_new_tab.get_text()
