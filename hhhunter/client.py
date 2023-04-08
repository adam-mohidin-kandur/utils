from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.first.page import FirstPage
from pages.login.page import LoginPage
from pages.main.page import MainPage
from pages.jobs.page import JobsPage


class Client:
    __driver = None

    def __init__(self):
        if Client.__driver is None:
            options = Options()
            # options.add_argument("--headless")
            options.add_argument("--start-fullscreen");
            Client.__driver = webdriver.Chrome(options=options)
            Client.__driver.delete_all_cookies()
            Client.__driver.get("https://hh.ru/")

    def close_driver(self):
        Client.__driver.close()

    def get_driver(self):
        return Client.__driver

    def set_driver(self, newdriver):
        Client.__driver = newdriver

    @property
    def first_page(self):
        return FirstPage(self.__driver)

    @property
    def login_page(self):
        return LoginPage(self.__driver)

    @property
    def main_page(self):
        return MainPage(self.__driver)

    @property
    def jobs_page(self):
        return JobsPage(self.__driver)
