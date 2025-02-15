from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Elements.button import Button
from Elements.frame import Frame


class FramesPage(BasePage):
    __button_frames_in_navbar_on_left_panel = Button(
        (By.XPATH, '//ul[@class = "menu-list"]//*[@id = "item-2"]//*[contains(text(), "Frames")]'),
        'Button "Frames"')

    __big_frame_window = Frame((By.ID, 'frame1'), 'Big frame window')

    __text_from_big_frame = Frame((By.XPATH, '//*[@id = "sampleHeading"]'), "Text from big frame")

    __small_frame_window = Frame((By.ID, 'frame2'), 'Small frame window')

    __text_from_small_frame = Frame((By.XPATH, '//*[@id = "sampleHeading"]'), "Text from small frame")

    __exit_frames = Frame(None, 'Exit all frames')

    def __init__(self):
        super().__init__((By.XPATH, '//*[@id = "framesWrapper"]//*[@class = "text-center"]'),
                         'Frames Page')

    def click_button_frames_on_left_panel(self):
        self.__button_frames_in_navbar_on_left_panel.click()
        self.__button_frames_in_navbar_on_left_panel.log_action('was clicked')

    def switch_to_big_frame_window(self):
        self.__big_frame_window.switch_to_frame()
        self.__big_frame_window.log_action('was switched')

    def get_text_from_big_frame(self):
        self.__text_from_big_frame.log_action('was received')
        return self.__text_from_big_frame.get_text()

    def switch_to_small_frame_window(self):
        self.__small_frame_window.switch_to_frame()
        self.__small_frame_window.log_action('was switched')

    def get_text_from_small_frame(self):
        self.__text_from_small_frame.log_action('was received')
        return self.__text_from_small_frame.get_text()

    def exit_frames(self):
        self.__exit_frames.switch_to_default_content()
        self.__exit_frames.log_action('have done')
