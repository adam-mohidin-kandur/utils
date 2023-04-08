import time

from selenium.webdriver.remote.webelement import WebElement
from client import Client


def apply_jobs(client: Client, job: WebElement,
               login: str, password: str) -> None:
    element = job.find_elements_by_tag_name("a")[-1]
    maindriver = client.get_driver()
    tmpdriver = client.jobs_page.make_tmpdriver()
    tmpdriver.get("https://hh.ru/")
    client.set_driver(tmpdriver)
    client.first_page.click_login()
    client.login_page.login(login, password)
    time.sleep(5)
    client.main_page.driver.get(element.get_attribute("href"))
    time.sleep(5)
    client.main_page.driver.close()
    client.set_driver(maindriver)
