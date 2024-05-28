import time
import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.language_page import LanguagePage


class TestChangeLanguage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test Change Language")
    @allure.description("This test verifies the language change functionality.")
    def test_change_language(self):
        driver = self.driver
        base_page = BasePage(driver)
        language_page = LanguagePage(driver)

        base_page.navigate_to_url("https://krisha.kz")
        language_page.hover_lang_switcher()
        time.sleep(2)
        language_page.click_language_option()

        self.assertIn(
            "Крыша. Қазақстандағы жылжымайтын мүлік — Қазақстандағы жылжымайтын мүлік сату туралы хабарландырулар",
            driver.title)

        allure.attach(self.driver.get_screenshot_as_png(), name="Language Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
