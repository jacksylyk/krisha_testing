from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PublicationPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_submit_ad_button(self, path):
        submit_ad_button = self.driver.find_element(By.XPATH, path)
        submit_ad_button.click()

    def click_sell_button(self):
        sell_button = self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div[2]/div[2]/ul/li[1]")
        sell_button.click()

    def click_category_button(self):
        category_button = self.driver.find_element(By.XPATH,
                                                   "/html/body/main/div/div[1]/div/div/div[2]/div[2]/ul[2]/li[1]")
        category_button.click()

    def enter_rooms(self, rooms):
        live_rooms_input = self.driver.find_element(By.ID, "live_rooms")
        live_rooms_input.send_keys(rooms)

    def enter_price(self, price):
        price_input = self.driver.find_element(By.ID, "price")
        price_input.send_keys(price)

    def select_flat_building(self, flat_building_value):
        flat_building_select = Select(self.driver.find_element(By.ID, "flat_building"))
        flat_building_select.select_by_value(flat_building_value)

    def enter_year_of_construction(self, year):
        year_of_construction_input = self.driver.find_element(By.ID, "house_year")
        year_of_construction_input.send_keys(str(year))

    def enter_area(self, area):
        area_input = self.driver.find_element(By.ID, "live_square")
        area_input.send_keys(str(area))

    def select_city(self, city_value):
        city_select = self.driver.find_element(By.CSS_SELECTOR,
                                               'select[name="{}"][data-level="2"]'.format("map_geo_id"))
        city_options = city_select.find_elements(By.TAG_NAME, "option")
        for option in city_options:
            if option.get_attribute("value") == city_value:
                option.click()
                break

    def select_region(self, region_value):
        region_select = self.driver.find_element(By.CSS_SELECTOR,
                                                 'select[name="{}"][data-level="3"]'.format("map_geo_id"))
        region_options = region_select.find_elements(By.TAG_NAME, "option")
        for option in region_options:
            if option.get_attribute("value") == region_value:
                option.click()
                break

    def enter_complex(self, complex_name):
        complex_click = self.driver.find_element(By.XPATH,
                                                 "/html/body/main/div/div[2]/form/div[11]/div/div/div/div/div")
        complex_click.click()
        complex_input = self.driver.find_element(By.XPATH,
                                                 "/html/body/main/div/div[2]/form/div[11]/div/div/div/div/ul/li[1]/input")
        complex_input.send_keys(complex_name)

    def select_complex_value(self):
        city_select_li = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/main/div/div[2]/form/div[11]/div/div/div/div/ul/li[1992]"))
        )
        city_select_li.click()

    def enter_street(self, street):
        street_input = self.driver.find_element(By.ID, "map_street")
        street_input.send_keys(street)

    def enter_house_num(self, house_num):
        house_num_input = self.driver.find_element(By.ID, "map_house_num")
        house_num_input.send_keys(str(house_num))

    def click_phone_checkbox(self):
        phone_checkbox = self.driver.find_element(By.XPATH,
                                                  "/html/body/main/div/div[2]/form/div[38]/div/div/div/div/div/div/label/span")
        phone_checkbox.click()

    def enter_email(self, email):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.XPATH, "/html/body/main/div/div[2]/form/div[46]/button[1]")
        submit_button.click()
