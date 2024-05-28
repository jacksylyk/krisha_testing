import time
import unittest

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.login_page import LoginPage
from pages.publication_page import PublicationPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def publication_page(driver):
    return PublicationPage(driver)


class TestSubmitAd:
    @pytest.mark.usefixtures("driver", "login_page", "publication_page")
    def test_submit_ad(self, driver, login_page, publication_page):
        with allure.step("Перейти на страницу krisha.kz"):
            publication_page.navigate_to_url("https://krisha.kz")

        with allure.step("Войти в систему"):
            login_page.login(config.number_login, config.password_login)

        with allure.step("Закрыть обучение, если оно отображается"):
            try:
                tutorial_close_button = WebDriverWait(driver, 3).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "tutorial__close"))
                )
                if tutorial_close_button.is_displayed():
                    tutorial_close_button.click()
                    publication_page.click_submit_ad_button(path="/html/body/div[2]/main/div[3]/div/div[1]/div[2]/a")
                else:
                    publication_page.click_submit_ad_button(path="/html/body/div[2]/main/div[4]/div/div[1]/div[2]/a")
            except TimeoutException:
                publication_page.click_submit_ad_button(path="/html/body/div[2]/main/div[4]/div/div[1]/div[2]/a")

        with allure.step("Выбрать опцию продажи"):
            publication_page.click_sell_button()
            time.sleep(0.5)

        with allure.step("Выбрать категорию"):
            publication_page.click_category_button()

        with allure.step("Проверить заголовок страницы"):
            assert "Подать объявление о продаже квартиры бесплатно на krisha.kz" in driver.title

        with allure.step("Заполнить информацию о квартире"):
            publication_page.enter_rooms(config.rooms)
            publication_page.enter_price(config.price)
            publication_page.select_flat_building(config.flat_type_value)
            publication_page.enter_year_of_construction(config.year_of_construction)
            publication_page.enter_area(config.area)
            publication_page.select_city(config.city_num)
            publication_page.select_region(config.region_num)
            publication_page.enter_complex(config.complex)
            publication_page.select_complex_value()
            publication_page.enter_street(config.street)
            publication_page.enter_house_num(config.house_num)
            publication_page.click_phone_checkbox()
            publication_page.enter_email(config.email)

        with allure.step("Отправить объявление"):
            publication_page.click_submit_button()

        with allure.step("Сделать скриншот страницы публикации"):
            allure.attach(driver.get_screenshot_as_png(), name="Publication page", attachment_type=AttachmentType.PNG)
            time.sleep(2)


if __name__ == "__main__":
    unittest.main()
