from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FilterPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_category_link(self):
        category_link = self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div[1]/nav/ul/li[1]/a")
        category_link.click()

    def select_category(self, category):
        category_select = Select(self.driver.find_element(By.CLASS_NAME, "category-type"))
        category_select.select_by_value(category)

    def select_rooms(self, rooms):
        rooms_block = self.driver.find_element(By.CLASS_NAME, "specs_kvartiry")
        rooms_select = Select(
            rooms_block.find_element(By.XPATH, '/html/body/main/section[1]/form/div[1]/div[2]/div[2]/div/select'))
        rooms_select.select_by_value(rooms)

    def select_city(self, city_value):
        city_select = self.driver.find_element(By.ID, "region-selected-value")
        city_select.click()

        cities = Select(self.driver.find_element(By.XPATH,
                                                 "/html/body/main/section[1]/form/div[1]/div[1]/div[5]/div/div/div/div[2]/div[1]/select"))
        cities.select_by_value(city_value)

    def select_region(self, region_value):
        regions = Select(self.driver.find_element(By.XPATH,
                                                  "/html/body/main/section[1]/form/div[1]/div[1]/div[5]/div/div/div/div[2]/div[2]/select"))
        regions.select_by_value(region_value)

    def click_select_button(self):
        select_button = self.driver.find_element(By.XPATH,
                                                 "/html/body/main/section[1]/form/div[1]/div[1]/div[5]/div/div/div/div[2]/div[2]/a")
        select_button.click()

    def click_search_button(self):
        search_block = self.driver.find_element(By.CLASS_NAME, "search-block-submit")
        search_button = search_block.find_element(By.CSS_SELECTOR, "button.kr-btn--blue")
        search_button.click()

    def click_close_tutorial_button(self):
        close_tutorial_button = self.driver.find_element(By.CLASS_NAME, "notes-tutorial__close")
        close_tutorial_button.click()
