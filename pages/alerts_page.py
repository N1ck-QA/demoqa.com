from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button
from Elements.caption import Caption
from Elements.base_element import BaseElement


class AlertPage(BasePage):
    __button_alert_in_navbar_on_left_panel = Button(
        (By.XPATH, '//ul[@class = "menu-list"]//*[contains (text(), "Alerts")]'),
        '"Alert" button on the left panel')

    __button_to_see_alert = Button((By.XPATH, '//*[@id="alertButton"]'),
                                   'Button "Click to see alert"')

    __button_confirm_box_will_appear = Button(
        (By.XPATH, '//*[@id="confirmButton"]'),
        'Button "confirm box will appear"')

    __caption_you_selected_ok = Caption(
        (By.XPATH, '//*[@id="confirmResult"]'),
        'Caption "You selected Ok"')

    __caption_you_entered_random_text = Caption(
        (By.XPATH, '//*[@id="promptResult"]'),
        'Typed random text')

    __button_prompt_box_will_appear = Button(
        (By.XPATH, '//*[@id="promtButton"]'),
        'On button click, prompt box will appear')

    def __init__(self):
        super().__init__((By.XPATH, '//*[@id="alertButton"]'),
                         'Alert Page')

    def click_button_alert_on_left_panel(self):
        self.__button_alert_in_navbar_on_left_panel.click()
        self.__button_alert_in_navbar_on_left_panel.log_action('was clicked')

    def click_button_to_see_alert(self):
        self.__button_to_see_alert.click()
        self.__button_to_see_alert.log_action("was clicked")

    def click_button_confirm_box_will_appear(self):
        self.__button_confirm_box_will_appear.click()
        self.__button_confirm_box_will_appear.log_action('was clicked')

    def click_button_prompt_box_will_appear(self):
        self.__button_prompt_box_will_appear.click()
        self.__button_confirm_box_will_appear.log_action('was clicked')

    def get_text_from_caption_you_selected_ok(self):
        self.__caption_you_selected_ok.log_action('is displayed')
        return self.__caption_you_selected_ok.get_text()

    def get_text_from_caption_you_entered_random_text_(self):
        self.__caption_you_entered_random_text.log_action('is displayed')
        return ' '.join(self.__caption_you_entered_random_text.get_text().split(' ')[2:])

    @staticmethod
    def get_text_from_alert_():
        BaseElement(None, 'Alert window interaction').log_action('Text from alert window was received')
        return BaseElement(None, 'Alert window interaction').get_text_from_alert()

    @staticmethod
    def accept_alert():
        BaseElement(None, 'Alert window interaction').log_action('Alert was accepted')
        return BaseElement(None, 'Alert window interaction').accept_alert()

    @staticmethod
    def type_text_to_input_in_alert():
        BaseElement(None, 'Alert window interaction').log_action('Text was typed to input field')
        return BaseElement(None, 'Alert window interaction').type_text_to_input_in_alert()
