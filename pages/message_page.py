from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MessagePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://krisha.kz/a/show/694140508")

    def click_close_tutorial_button(self):
        close_tutorial_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "notes-tutorial__close"))
        )
        close_tutorial_button.click()

    def click_send_message_button(self):
        send_message_button = self.driver.find_element(By.CLASS_NAME, "message-send-button")
        send_message_button.click()

    def enter_message(self, message):
        message_field = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[2]/main/div[2]/div/div[1]/div/div[3]/form/span")
        message_field.click()
        message_field.send_keys(message)

    def click_send_button(self):
        send_button = self.driver.find_element(By.XPATH,
                                               "/html/body/div[2]/main/div[2]/div/div[1]/div/div[3]/form/button[1]/span")
        send_button.click()
