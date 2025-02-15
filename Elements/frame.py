from Elements.base_element import BaseElement


class Frame(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def switch_to_frame(self):
        super().switch_to_frame()

    def switch_to_inner_frame(self):
        super().switch_to_inner_frame()

    def switch_to_default_content(self):
        super().switch_to_default_content()
