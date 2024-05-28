import time
import unittest

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestChangeUsername(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test Send Message")
    @allure.description("This test verifies the message sending functionality.")
    def test_change_username(self):
        self.base_page.navigate_to_url("https://krisha.kz")
        self.login_page.login(config.number_login, config.password_login)
        time.sleep(2)

        try:
            tutorial_close_button = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "tutorial__close"))
            )
            if tutorial_close_button.is_displayed():
                tutorial_close_button.click()
                self.profile_page.open()
            else:
                self.profile_page.open()
        except TimeoutException:
            pass

        self.profile_page.set_username()
        self.profile_page.submit()

        allure.attach(self.driver.get_screenshot_as_png(), name="Change Username Page",
                      attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
