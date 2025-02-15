from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Elements.button import Button
from Elements.caption import Caption
from Elements.input import Input


class TablesPage(BasePage):
    __button_web_tables_in_navbar_on_left_panel = Button(
        (By.XPATH, '//ul[@class = "menu-list"]//*[contains (text(), "Web Tables")]'),
        'Button "Web tables"')

    __button_add = Button(
        (By.XPATH, '//*[@id = "addNewRecordButton"]'),
        'Button "Add"')

    @staticmethod
    def __button_delete(user_email):
        return Button((
            By.XPATH,
            f"//*[contains(text(), '{user_email}')]/ancestor::div[contains(@class, 'rt-tr')]//*[@title='Delete']"
        ), "Button delete")

    __input_first_name = Input((By.XPATH, '//input[@id = "firstName"]'), 'Input "First Name"')

    __input_last_name = Input((By.XPATH, '//input[@id = "lastName"]'), 'Input "Last Name"')

    __input_email = Input((By.XPATH, '//input[@id = "userEmail"]'), 'Input "Email"')

    __input_age = Input((By.XPATH, '//input[@id = "age"]'), 'Input "Age"')

    __input_salary = Input((By.XPATH, '//input[@id = "salary"]'), 'Input "Salary"')

    __input_department = Input((By.XPATH, '//input[@id = "department"]'), 'Input "Department"')

    __button_submit = Button(
        (By.XPATH, '//*[@id = "submit"]'),
        'Button "Submit"')

    def __init__(self):
        super().__init__((By.XPATH, '//*[@id = "addNewRecordButton"]'),
                         'Web tables Page')

    def click_button_web_tables_on_left_panel(self):
        self.__button_web_tables_in_navbar_on_left_panel.click()
        self.__button_web_tables_in_navbar_on_left_panel.log_action('was clicked')

    def click_button_add(self):
        self.__button_add.click()
        self.__button_add.log_action('was clicked')

    def click_button_submit(self):
        self.__button_submit.click()
        self.__button_submit.log_action('was clicked')

    def fill_registration_form(self, user_data):
        self.__input_first_name.send_keys(user_data.first_name)
        self.__input_first_name.log_action('was typed')
        self.__input_last_name.send_keys(user_data.last_name)
        self.__input_last_name.log_action('was typed')
        self.__input_email.send_keys(user_data.email)
        self.__input_email.log_action('was typed')
        self.__input_age.send_keys(user_data.age)
        self.__input_age.log_action('was typed')
        self.__input_salary.send_keys(user_data.salary)
        self.__input_salary.log_action('was typed')
        self.__input_department.send_keys(user_data.department)
        self.__input_department.log_action('was typed')

    def is_user_in_table(self, user_email):
        try:
            Caption((By.XPATH, f"//*[contains(text(), '{user_email}')]"),
                    'New user in table"').find_element()
            TablesPage.log_action(self, "User successfully added in table")
            return True
        except TimeoutException:
            TablesPage.log_action(self, "User isn't found")
            return False

    def delete_user(self, user_email):
        self.__button_delete(user_email).click_js()
        self.log_action('User was deleted')
