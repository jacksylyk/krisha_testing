import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import config
from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test: Авторизация")
    def test_registration_link(self):
        driver = self.driver
        base_page = BasePage(driver)
        login_page = LoginPage(driver)

        with allure.step("Перейти на страницу krisha.kz"):
            base_page.navigate_to_url("https://krisha.kz")
        with allure.step("Нажать на кнопку Регистрация"):
            base_page.click_element(By.CLASS_NAME, "registration-link-item")

        self.assertIn("Войти на Krisha.kz", driver.title)

        login_page.enter_login(config.number_login)
        self.assertEqual(login_page.get_login_value(), config.number_login)

        login_page.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")
        time.sleep(1)

        login_page.enter_password(config.password_login)
        self.assertEqual(login_page.get_password_value(), config.password_login)

        login_page.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")

        allure.attach(self.driver.get_screenshot_as_png(), name="Registration Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
