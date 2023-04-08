from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support \
    import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_clickable_element(self, locator, time=100):
        return WebDriverWait(self.driver, time)\
            .until(EC.element_to_be_clickable(locator))

    def click_clickable_element(self, locator, time=100):
        self.find_clickable_element(locator, time=time).click()

    def find_element(self, locator):
        pass
