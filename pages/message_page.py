import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


class MessagePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть объявление")
    def open(self):
        self.driver.get(config.url_send)

    @allure.step("Закрыть окно подсказки")
    def click_close_tutorial_button(self):
        close_tutorial_button = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "notes-tutorial__close"))
        )
        close_tutorial_button.click()

    @allure.step("Нажать на кнопку Написать сообщение")
    def click_send_message_button(self):
        send_message_button = self.driver.find_element(By.CLASS_NAME, "message-send-button")
        send_message_button.click()

    @allure.step("Ввести сообщение")
    def enter_message(self):
        message_field = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[2]/main/div[2]/div/div[1]/div/div[3]/form/span")
        message_field.click()
        message_field.send_keys("Покупаю!")

    @allure.step("Нажать Отправить")
    def click_send_button(self):
        send_button = self.driver.find_element(By.XPATH,
                                               "/html/body/div[2]/main/div[2]/div/div[1]/div/div[3]/form/button[1]/span")
        send_button.click()
