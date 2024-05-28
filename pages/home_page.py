from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://krisha.kz"

    def open(self):
        self.driver.get(self.url)

