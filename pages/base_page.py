class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_element(self, by, selector):
        element = self.driver.find_element(by, selector)
        element.click()

    def assert_in_title(self, text):
        assert text in self.driver.title
