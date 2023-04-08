from pages.base import BasePage 
from pages.first.locators import FirstPageLocators


class FirstPage(BasePage):
    def click_login(self):
        self.click_clickable_element(FirstPageLocators.ENTER)
