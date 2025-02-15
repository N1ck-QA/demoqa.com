from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button
from Elements.frame import Frame


class NestedFramePage(BasePage):
    __button_nested_frames_in_navbar_on_left_panel = Button(
        (By.XPATH, '//ul[@class = "menu-list"]//*[contains (text(), "Nested Frames")]'),
        'Button "Nested Frames"')

    __parent_frame = Frame((By.ID, 'frame1'), 'Parent Frame')

    __text_from_parent_frame = Frame((By.XPATH, "//body[contains(text(), 'Parent frame')]"), 'Text from Parent Frame')

    __child_frame = Frame((By.TAG_NAME, 'iframe'), 'Child Frame')

    __text_from_child_frame = Frame((By.XPATH, "//p[contains(text(), 'Child Iframe')]"), 'Text from Child Frame')

    __exit_frames = Frame(None, 'Exit all frames')

    def __init__(self):
        super().__init__((By.ID, 'frame1'), 'Nested Frames Page')

    def click_button_nested_frames_on_left_panel(self):
        self.__button_nested_frames_in_navbar_on_left_panel.click()
        self.__button_nested_frames_in_navbar_on_left_panel.log_action('was clicked')

    def switch_to_parent_frame(self):
        self.__parent_frame.switch_to_frame()
        self.__parent_frame.log_action('was switched')

    def switch_to_child_frame(self):
        self.__child_frame.switch_to_inner_frame()
        self.__child_frame.log_action('was switched')

    def get_text_from_parent_frame(self):
        self.__text_from_parent_frame.log_action('was received')
        return self.__text_from_parent_frame.get_text()

    def get_text_from_child_frame(self):
        self.__text_from_child_frame.log_action('was received')
        return self.__text_from_child_frame.get_text()

    def exit_frames(self):
        self.__exit_frames.switch_to_default_content()
        self.__exit_frames.log_action('have done')
