import random
import string
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_random_username(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть профиль")
    def open(self):
        wait = WebDriverWait(self.driver, 5)
        profile_dropdown = wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/header/div[2]/div/ul/li[6]/a")))
        profile_dropdown.click()
        profile_settings = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "js-init-tutorial-btn")))
        profile_settings.click()

    @allure.step("Ввести рандомное имя пользователя")
    def set_username(self):
        random_username = generate_random_username()
        wait = WebDriverWait(self.driver, 5)
        form = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "personal-data-form")))
        field = wait.until(EC.visibility_of_element_located((By.ID, "name")))
        field.click()
        field.clear()
        field.send_keys(random_username)

    @allure.step("Нажать на кнопку сохранить")
    def submit(self):
        wait = WebDriverWait(self.driver, 5)
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kr-btn--blue-gradient")))
        button.click()
