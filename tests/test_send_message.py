import time
import unittest

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

import config
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.message_page import MessagePage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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
def message_page(driver):
    return MessagePage(driver)


class TestSendMessage:
    @pytest.mark.usefixtures("driver", "base_page", "login_page", "message_page")
    def test_send_message(self, driver, base_page, login_page, message_page):
        with allure.step("Перейти на страницу krisha.kz"):
            base_page.navigate_to_url("https://krisha.kz")

        with allure.step("Войти в систему"):
            login_page.login(config.number_send, config.password_send)
            time.sleep(2)

        with allure.step("Открыть страницу сообщений"):
            message_page.open()
            time.sleep(5)

        with allure.step("Закрыть обучение, если оно отображается"):
            message_page.click_close_tutorial_button()

        with allure.step("Нажать на кнопку отправки сообщения"):
            message_page.click_send_message_button()

        with allure.step("Ввести сообщение"):
            message_page.enter_message()

        with allure.step("Нажать на кнопку отправки"):
            message_page.click_send_button()

        with allure.step("Сделать скриншот страницы сообщений"):
            allure.attach(driver.get_screenshot_as_png(), name="Message Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
