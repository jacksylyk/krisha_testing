import random
import string
import time

import allure
from selenium.webdriver.common.by import By

import config


def generate_random_username(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть профиль")
    def open(self):
        profile_dropdown = self.driver.find_element(By.XPATH, "/html/body/header/div[2]/div/ul/li[6]/a")
        profile_dropdown.click()
        time.sleep(1)
        profile_settings = self.driver.find_element(By.CLASS_NAME, "js-init-tutorial-btn")
        profile_settings.click()

    @allure.step("Ввести рандомное имя пользователя")
    def set_username(self):
        random_username = generate_random_username()
        form = self.driver.find_element(By.CLASS_NAME, "personal-data-form")
        field = form.find_element(By.ID, "name")
        field.click()
        field.clear()
        field.send_keys(random_username)

    @allure.step("Нажать на кнопку сохранить")
    def submit(self):
        button = self.driver.find_element(By.CLASS_NAME, "kr-btn--blue-gradient")
        button.click()
