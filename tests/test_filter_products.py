import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import config
from pages.filter_page import FilterPage


class TestFilterProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.filter_page = FilterPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test Фильтрация")
    def test_filter_products(self):
        with allure.step("Перейти на страницу krisha.kz"):
            self.filter_page.navigate_to_url("https://krisha.kz")
        with allure.step("Найти и открыть раздел Продажа."):
            self.filter_page.click_category_link()

        self.assertIn("Купить недвижимость в Казахстане — цены на доске бесплатных объявлений — Крыша",
                      self.driver.title)

        with allure.step("Выбрать из списка Купить."):
            self.filter_page.select_category("sell")
        with allure.step("Выбрать из списка 2-комн."):
            self.filter_page.select_rooms(config.rooms)
        with allure.step("В списке Весь Казахстан выбрать Астана (откроется окно с районами)"):
            self.filter_page.select_city(config.city_num)
        with allure.step("В списке районов выбрать Алматы р-н"):
            self.filter_page.select_region(config.region_num)
            self.filter_page.click_select_button()
        with allure.step("Нажать на кнопку Найти"):
            self.filter_page.click_search_button()

        self.assertIn(
            "Купить двухкомнатную квартиру в Алматы р-н Астаны 🏘 Продажа 2-комнатных квартир – объявления на Крыше",
            self.driver.title)

        with allure.step("Закрыть окно Оставить заметку"):
            self.filter_page.click_close_tutorial_button()
        with allure.step("Проскроллить объявления"):
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        allure.attach(self.driver.get_screenshot_as_png(), name="Filter Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
