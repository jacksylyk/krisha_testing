import unittest
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import config
from pages.base_page import BasePage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


class TestRegistration:
    @pytest.mark.usefixtures("driver", "login_page")
    def test_registration_link(self, driver, login_page):
        base_page = BasePage(driver)

        with allure.step("Перейти на страницу krisha.kz"):
            base_page.navigate_to_url("https://krisha.kz")
        with allure.step("Нажать на кнопку Регистрация"):
            base_page.click_element(By.CLASS_NAME, "registration-link-item")

        assert "Войти на Krisha.kz" in driver.title

        login_page.enter_login(config.number_login)
        assert login_page.get_login_value() == config.number_login

        login_page.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")
        time.sleep(1)

        login_page.enter_password(config.password_login)
        assert login_page.get_password_value() == config.password_login

        login_page.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")

        allure.attach(driver.get_screenshot_as_png(), name="Registration Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
