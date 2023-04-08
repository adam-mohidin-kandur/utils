from pages.base import BasePage 
from pages.login.locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, login, password):
        self.click_clickable_element(
            LoginPageLocators.ENTER_WITH_PASSWORD)

        self.find_clickable_element(LoginPageLocators.LOGIN).send_keys(login)
        self.find_clickable_element(LoginPageLocators.PASSWORD).send_keys(password)

        self.click_clickable_element(LoginPageLocators.ENTER)
