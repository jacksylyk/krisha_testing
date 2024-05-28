import time
import unittest

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

import config
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.message_page import MessagePage


class TestSendMessage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.message_page = MessagePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test Send Message")
    @allure.description("This test verifies the message sending functionality.")
    def test_send_message(self):
        self.base_page.navigate_to_url("https://krisha.kz")
        self.login_page.login(config.number_send, config.password_send)
        time.sleep(2)
        self.message_page.open()
        time.sleep(2)
        self.message_page.click_close_tutorial_button()
        self.message_page.click_send_message_button()
        self.message_page.enter_message("Покупаю")
        self.message_page.click_send_button()

        allure.attach(self.driver.get_screenshot_as_png(), name="Message Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
