from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button
from Elements.link import Link
from Elements.base_element import BaseElement


class LinksPage(BasePage):
    __button_elements_in_navbar_on_left_panel = Button(
        (By.XPATH, '//div[@class = "element-group"]//*[contains (text(), "Elements")]/..'),
        'Button "Elements"')

    __button_links_inside_elements_in_navbar_on_left_panel = Button(
        (By.XPATH, '//*[@class = "menu-list"]//*[contains (text(), "Links")]'),
        'Button "Links"')

    __link_home = Link(
        (By.XPATH, '//*[@id = "simpleLink"]'),
        'Link "Home')

    def __init__(self):
        super().__init__((By.XPATH, '//*[@id = "simpleLink"]'),
                         'Links Page')

    def click_button_links_on_left_panel(self):
        self.__button_elements_in_navbar_on_left_panel.click()
        self.__button_elements_in_navbar_on_left_panel.log_action('was clicked')
        self.__button_links_inside_elements_in_navbar_on_left_panel.click()
        self.__button_links_inside_elements_in_navbar_on_left_panel.log_action('was clicked')

    @staticmethod
    def switch_to_new_tab():
        BaseElement(None, 'Tab interaction').switch_to_new_tab()
        BaseElement(None, 'Tab interaction').log_action('Switching to new tab')

    @staticmethod
    def switch_to_home_tab():
        BaseElement(None, 'Tab interaction').switch_to_home_tab()
        BaseElement(None, 'Tab interaction').log_action('Switching to home tab')

    def click_on_link_home(self):
        self.__link_home.click()
        self.__link_home.log_action('was clicked')
