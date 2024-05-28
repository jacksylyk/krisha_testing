import unittest
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

import config
from pages.filter_page import FilterPage
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
def filter_page(driver):
    return FilterPage(driver)


class TestFilterProducts:
    @pytest.mark.usefixtures("driver", "filter_page")
    def test_filter_products(self, driver, filter_page):
        with allure.step("Перейти на страницу krisha.kz"):
            filter_page.navigate_to_url("https://krisha.kz")

        with allure.step("Нажать на ссылку категории"):
            filter_page.click_category_link()

        with allure.step("Проверить заголовок страницы"):
            assert "Купить недвижимость в Казахстане — цены на доске бесплатных объявлений — Крыша" in driver.title

        with allure.step("Выбрать категорию, количество комнат, город и регион"):
            filter_page.select_category("sell")
            filter_page.select_rooms(config.rooms)
            filter_page.select_city(config.city_num)
            filter_page.select_region(config.region_num)

        with allure.step("Нажать на кнопку выбора и кнопку поиска"):
            filter_page.click_select_button()
            filter_page.click_search_button()

        with allure.step("Проверить заголовок страницы после поиска"):
            assert "Купить двухкомнатную квартиру в Алматы р-н Астаны 🏘 Продажа 2-комнатных квартир – объявления на Крыше" in driver.title

        with allure.step("Закрыть обучение, если оно отображается, и прокрутить страницу вниз"):
            filter_page.click_close_tutorial_button()
            driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        with allure.step("Сделать скриншот страницы фильтрации"):
            allure.attach(driver.get_screenshot_as_png(), name="Filter Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
