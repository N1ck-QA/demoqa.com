from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button


class MainPage(BasePage):
    __button_alert_frame_windows = Button((By.XPATH, '//*[@class="card mt-4 top-card"][3]'),
                                          'Button "Alert, Frame & Windows"')

    __button_elements = Button((By.XPATH, '//*[@class="card mt-4 top-card"]'),
                               'Button "Elements"')

    __button_widgets = Button((By.XPATH, '//*[@class="card mt-4 top-card"][4]'),
                              'Button "Widgets"')

    def __init__(self):
        super().__init__((By.XPATH, '//*[@class = "banner-image"]'),
                         'Main Page')

    def click_alert_button_on_main_page(self):
        self.__button_alert_frame_windows.click()
        self.__button_alert_frame_windows.log_action('was clicked')

    def click_elements_button_on_main_page(self):
        self.__button_elements.click()
        self.__button_elements.log_action('was clicked')

    def click_widgets_button_on_main_page(self):
        self.__button_widgets.click()
        self.__button_widgets.log_action('was clicked')
