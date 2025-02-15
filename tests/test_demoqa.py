import time
from datetime import datetime

from pages.alerts_page import AlertPage
from pages.nested_frames_page import NestedFramePage
from pages.frames_page import FramesPage
from pages.tables_page import TablesPage
from pages.browser_windows import BrowserWindows
from pages.links_page import LinksPage
from pages.main_page import MainPage
from pages.date_picker_page import DatePickerPage


class TestCasesDemoQa:

    def test_for_alert_page(self):
        main_page = MainPage()
        alert_page = AlertPage()
        main_page.open_url()
        assert main_page.is_displayed(), "Main Page isn't displayed"
        main_page.click_alert_button_on_main_page()
        alert_page.click_button_alert_on_left_panel()
        assert alert_page.is_displayed(), "Alert page isn't displayed"

        alert_page.click_button_to_see_alert()
        assert alert_page.get_text_from_alert_() == 'You clicked a button', "Actual doesn't match expected"
        alert_page.accept_alert()

        alert_page.click_button_confirm_box_will_appear()
        assert alert_page.get_text_from_alert_() == 'Do you confirm action?', "Actual doesn't match expected"
        alert_page.accept_alert()
        assert alert_page.get_text_from_caption_you_selected_ok() == "You selected Ok"

        alert_page.click_button_prompt_box_will_appear()
        fake_text = alert_page.type_text_to_input_in_alert()
        alert_page.accept_alert()
        assert alert_page.get_text_from_caption_you_entered_random_text_() == fake_text, \
            "Actual typed text doesn't match text displayed on page"

    def test_for_frames_pages(self):
        main_page = MainPage()
        nested_frames_page = NestedFramePage()
        frames_page = FramesPage()

        main_page.open_url()
        main_page.click_alert_button_on_main_page()
        nested_frames_page.click_button_nested_frames_on_left_panel()
        assert nested_frames_page.is_displayed(), "Nested Frames page isn't displayed"

        nested_frames_page.switch_to_parent_frame()
        assert nested_frames_page.get_text_from_parent_frame() == 'Parent frame', \
            "Actual text from parent frame doesn't match expected"

        nested_frames_page.switch_to_child_frame()
        assert nested_frames_page.get_text_from_child_frame() == 'Child Iframe', \
            "Actual text from child frame doesn't match expected"

        nested_frames_page.exit_frames()

        frames_page.click_button_frames_on_left_panel()
        assert frames_page.is_displayed(), "Frames page isn't displayed"
        time.sleep(5)
        frames_page.switch_to_big_frame_window()
        time.sleep(5)
        text_from_big_frame = frames_page.get_text_from_big_frame()
        frames_page.exit_frames()

        frames_page.switch_to_small_frame_window()
        assert frames_page.get_text_from_small_frame() == text_from_big_frame, \
            "Text from big frame doesn't match text from small frame"
        frames_page.exit_frames()

    def test_for_tables_page(self, user_data):
        main_page = MainPage()
        tables_page = TablesPage()
        main_page.open_url()
        main_page.click_elements_button_on_main_page()
        tables_page.click_button_web_tables_on_left_panel()
        assert tables_page.is_displayed(), "Web tables page isn't displayed"

        tables_page.click_button_add()
        tables_page.fill_registration_form(user_data)
        tables_page.click_button_submit()
        assert tables_page.is_user_in_table(user_data.email), "User isn't added in table"

        tables_page.delete_user(user_data.email)
        assert not tables_page.is_user_in_table(user_data.email), "User isn't deleted in table"

    def test_related_with_handles(self):
        main_page = MainPage()
        browser_windows_page = BrowserWindows()
        links_page = LinksPage()

        main_page.open_url()
        main_page.click_alert_button_on_main_page()
        browser_windows_page.click_button_browser_windows_on_left_panel()
        assert browser_windows_page.is_displayed(), "Browser windows page isn't displayed"

        browser_windows_page.click_new_tab_button()
        browser_windows_page.switch_to_new_tab()
        assert browser_windows_page.get_text_on_new_tab() == 'This is a sample page', \
            "Text on new tab doesn't match expected text"
        browser_windows_page.close_the_tab()
        browser_windows_page.switch_to_home_tab()
        assert browser_windows_page.is_displayed(), "Browser windows page isn't displayed"

        links_page.click_button_links_on_left_panel()
        assert links_page.is_displayed(), "Links page isn't displayed"
        links_page.click_on_link_home()
        links_page.switch_to_new_tab()
        assert main_page.is_displayed(), "Main page isn't displayed"
        links_page.switch_to_home_tab()
        assert links_page.is_displayed(), "Links page isn't displayed"

    def test_for_date_picker_age(self):
        main_page = MainPage()
        date_picker_page = DatePickerPage()

        main_page.open_url()
        main_page.click_widgets_button_on_main_page()
        date_picker_page.click_button_date_picker_on_left_panel()
        assert date_picker_page.get_date_from_input_select_date() == datetime.now().strftime("%m/%d/%Y"), \
            "Date from input field doesn't match current date"
        assert date_picker_page.get_date_from_input_date_and_time() == datetime.now().strftime("%B %-d, %Y %-I:%M %p"), \
            "Date and time from input field doesn't match current date and time"
        date_picker_page.type_date_to_input_date_and_time()
        assert date_picker_page.get_date_from_input_date_and_time() == 'February 29, 2028 12:00 AM', \
            "Date and time from input field doesn't match expected date and time"




