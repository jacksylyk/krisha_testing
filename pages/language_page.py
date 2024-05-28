from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LanguagePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Set the wait time to 10 seconds

    @allure.step("Навестись на переключатель языка")
    def hover_lang_switcher(self):
        lang_switcher = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "lang-switcher"))
        )
        ActionChains(self.driver).move_to_element(lang_switcher).perform()

    @allure.step("Нажатие на опцию языка")
    def click_language_option(self):
        lang_options = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "lang-switcher__options"))
        )
        language_option = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/header/div[1]/div[2]/ul/li[1]/div/ul/li[1]"))
        )
        language_option.click()
