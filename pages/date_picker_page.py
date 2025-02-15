from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button
from Elements.input import Input


class DatePickerPage(BasePage):
    __button_date_picker_in_navbar_on_left_panel = Button(
        (By.XPATH, '//*[@class = "menu-list"]//*[contains (text(), "Date Picker")]'),
        '"Data Picker" button on the left panel')

    __input_select_date = Input((By.XPATH, '//input[@id = "datePickerMonthYearInput"]'),
                                'Input "Select Date"')

    __input_date_and_time = Input((By.XPATH, '//input[@id = "dateAndTimePickerInput"]'),
                                  'Input "Date and Time"')

    def __init__(self):
        super().__init__((By.XPATH, '//input[@id = "datePickerMonthYearInput"]'),
                         'Data Picker page')

    def click_button_date_picker_on_left_panel(self):
        self.__button_date_picker_in_navbar_on_left_panel.click_js()
        self.__button_date_picker_in_navbar_on_left_panel.log_action('was clicked')

    def get_date_from_input_select_date(self):
        self.__input_select_date.log_action("date is displayed")
        return self.__input_select_date.find_element().get_attribute("value")

    def get_date_from_input_date_and_time(self):
        self.__input_date_and_time.log_action("date and time is displayed")
        return self.__input_date_and_time.find_element().get_attribute("value")

    def type_date_to_input_date_and_time(self):
        self.__input_date_and_time.send_keys('February 29, 2028 12:00 AM')
        self.__input_date_and_time.log_action("date and time was typed")
