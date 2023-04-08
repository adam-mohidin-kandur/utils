import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base import BasePage 
from pages.jobs.locators import JobsPageLocators


class JobsPage(BasePage):
    def check_moscow_checkbox(self) -> None:
        moscow_checkbox = self\
            .find_clickable_element(JobsPageLocators.MOSCOW_CHECKBOX)

        if moscow_checkbox.is_selected() is False:
            moscow_checkbox.click()
            time.sleep(2)

    def find_jobs(self) -> list:
        jobs_element = self.driver\
                           .find_element("xpath", "//*[@id=\"a11y-main-content\"]")
        return jobs_element.find_elements_by_class_name("serp-item")

    def make_tmpdriver(self) -> WebDriver:
        options = Options()
        options.add_argument("--start-fullscreen")
        return webdriver.Chrome(options=options)

    def click_page(self, page: int) -> None:
        self.click_clickable_element(JobsPageLocators.PAGE(page))
        time.sleep(5)
