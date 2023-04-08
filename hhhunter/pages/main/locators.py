from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_BOX = (By.XPATH, "//*[@id=\"a11y-search-input\"]")
    SEARCH_BUTTON = (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/button/span/span[2]")
