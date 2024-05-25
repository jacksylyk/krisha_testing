import time
import unittest

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

import allure
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

        with allure.step("Ввести № телефона в поле «Введите номер телефона» "):
            login_page.enter_login("87016782222")
        self.assertEqual(login_page.get_login_value(), "87016782222")

        with allure.step("Нажать на кнопку Продолжить "):
            login_page.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")
        time.sleep(1)

        with allure.step("Ввести пароль "):
            login_page.enter_password("Qwe*12345")
        self.assertEqual(login_page.get_password_value(), "Qwe*12345")

        with allure.step("Нажать на кнопку Вход "):
            login_page.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")

        allure.attach(self.driver.get_screenshot_as_png(), name="Registration Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
