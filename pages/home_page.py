import time

from selenium.webdriver.common.by import By

import config
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://krisha.kz"

    def open(self):
        self.driver.get(self.url)

    def change_language_to_kazakh(self):
        lang_switcher = self.wait_for_element((By.CLASS_NAME, "lang-switcher"))
        lang_switcher.click()

        lang_options = self.wait_for_element((By.CLASS_NAME, "lang-switcher__options"))
        kazakh_option = lang_options.find_element(By.XPATH, "//li[contains(text(),'Қазақша')]")
        kazakh_option.click()

