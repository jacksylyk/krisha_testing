import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Авторизация по номеру телефона и паролю")
    def login(self, number, password):
        self.click_button(By.CLASS_NAME, "registration-link-item")
        self.enter_login(number)
        self.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")
        self.enter_password(password)
        self.click_button(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[5]/div/button")

    @allure.step("Ввод номера телефона")
    def enter_login(self, number):
        login_input = self.driver.find_element(By.ID, "login")
        login_input.send_keys(number)

    @allure.step("Получить введенный номер телефона")
    def get_login_value(self):
        login_input = self.driver.find_element(By.ID, "login")
        return login_input.get_attribute("value")

    @allure.step("Ввод password")
    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)

    @allure.step("Получить введенный пароль")
    def get_password_value(self):
        password_input = self.driver.find_element(By.ID, "password")
        return password_input.get_attribute("value")

    @allure.step('Нажать на кнопку "Продолжить"')
    def click_button(self, by, selector):
        button = self.driver.find_element(by, selector)
        button.click()
