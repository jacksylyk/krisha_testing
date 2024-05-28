import time
import unittest

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.publication_page import PublicationPage
from pages.login_page import LoginPage


class TestSubmitAd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        self.publication_page = PublicationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test Создание нового объявления")
    @allure.description("This test verifies the submission of a new advertisement.")
    def test_submit_ad(self):
        self.publication_page.navigate_to_url("https://krisha.kz")
        self.login_page.login(config.number_login, config.password_login)

        try:
            tutorial_close_button = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "tutorial__close"))
            )
            if tutorial_close_button.is_displayed():
                tutorial_close_button.click()
                self.publication_page.click_submit_ad_button(
                    path="/html/body/div[2]/main/div[3]/div/div[1]/div[2]/a")
            else:
                self.publication_page.click_submit_ad_button(
                    path="/html/body/div[2]/main/div[4]/div/div[1]/div[2]/a")
        except TimeoutException:
            self.publication_page.click_submit_ad_button(path="/html/body/div[2]/main/div[4]/div/div[1]/div[2]/a")

        self.publication_page.click_sell_button()
        time.sleep(0.5)
        self.publication_page.click_category_button()

        self.assertIn("Подать объявление о продаже квартиры бесплатно на krisha.kz", self.driver.title)

        self.publication_page.enter_rooms(config.rooms)
        self.publication_page.enter_price(config.price)
        self.publication_page.select_flat_building(config.flat_type_value)
        self.publication_page.enter_year_of_construction(config.year_of_construction)
        self.publication_page.enter_area(config.area)
        self.publication_page.select_city(config.city_num)
        self.publication_page.select_region(config.region_num)
        self.publication_page.enter_complex(config.complex)
        self.publication_page.select_complex_value()
        self.publication_page.enter_street(config.street)
        self.publication_page.enter_house_num(config.house_num)
        self.publication_page.click_phone_checkbox()
        self.publication_page.enter_email(config.email)
        self.publication_page.click_submit_button()

        allure.attach(self.driver.get_screenshot_as_png(), name="Publication page", attachment_type=AttachmentType.PNG)
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
