import os
import time
import unittest

import allure
import pytest
from selenium import webdriver

from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv

load_dotenv()
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)


class TestChangeUsername:
    @pytest.mark.usefixtures("driver", "base_page", "login_page", "profile_page")
    def test_change_username(self, driver, base_page, login_page, profile_page):
        with allure.step("Перейти на страницу krisha.kz"):
            base_page.navigate_to_url("https://krisha.kz")

        with allure.step("Войти в систему"):
            login_page.login(config.number_login, config.password_login)
            time.sleep(2)

        with allure.step("Закрыть обучение, если оно отображается"):
            try:
                tutorial_close_button = WebDriverWait(driver, 3).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "tutorial__close"))
                )
                if tutorial_close_button.is_displayed():
                    tutorial_close_button.click()
                    profile_page.open()
                else:
                    profile_page.open()
            except TimeoutException:
                profile_page.open()

        with allure.step("Изменить имя пользователя"):
            profile_page.set_username()
            profile_page.submit()

        with allure.step("Сделать скриншот страницы изменения имени пользователя"):
            allure.attach(driver.get_screenshot_as_png(), name="Change Username Page",
                          attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
