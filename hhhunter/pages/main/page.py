from pages.base import BasePage
from pages.main.locators import MainPageLocators


class MainPage(BasePage):
    def search(self, job_name):
        self.find_clickable_element(MainPageLocators.SEARCH_BOX).send_keys(job_name)
        self.click_clickable_element(MainPageLocators.SEARCH_BUTTON)
