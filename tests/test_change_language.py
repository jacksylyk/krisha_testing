import unittest
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import config
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.language_page import LanguagePage
from pages.login_page import LoginPage
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
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def language_page(driver):
    return LanguagePage(driver)


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


class TestChangeLanguage:
    @pytest.mark.usefixtures("driver", "home_page", "language_page")
    def test_change_language(self, driver, home_page, language_page):
        base_page = BasePage(driver)

        with allure.step("Перейти на страницу krisha.kz"):
            base_page.navigate_to_url("https://krisha.kz")
        with allure.step("Навести курсор на переключатель языка"):
            language_page.hover_lang_switcher()
            time.sleep(2)
        with allure.step("Выбрать другой язык"):
            language_page.click_language_option()

        with allure.step("Проверка изменения языка страницы"):
            assert "Крыша. Қазақстандағы жылжымайтын мүлік — Қазақстандағы жылжымайтын мүлік сату туралы хабарландырулар" in driver.title

        allure.attach(driver.get_screenshot_as_png(), name="Language Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
