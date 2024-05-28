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
        self.filter_page.navigate_to_url("https://krisha.kz")
        self.filter_page.click_category_link()

        self.assertIn("Купить недвижимость в Казахстане — цены на доске бесплатных объявлений — Крыша",
                      self.driver.title)

        self.filter_page.select_category("sell")
        self.filter_page.select_rooms(config.rooms)
        self.filter_page.select_city(config.city_num)
        self.filter_page.select_region(config.region_num)
        self.filter_page.click_select_button()
        self.filter_page.click_search_button()

        self.assertIn(
            "Купить двухкомнатную квартиру в Алматы р-н Астаны 🏘 Продажа 2-комнатных квартир – объявления на Крыше",
            self.driver.title)

        self.filter_page.click_close_tutorial_button()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        allure.attach(self.driver.get_screenshot_as_png(), name="Filter Page", attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    unittest.main()
