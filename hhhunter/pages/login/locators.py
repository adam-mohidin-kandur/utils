from selenium.webdriver.common.by import By

class LoginPageLocators:
    ENTER_WITH_PASSWORD = (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/form/div[5]/button[2]")
    LOGIN = (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[1]/fieldset/input")
    PASSWORD = (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[2]/fieldset/input")
    ENTER = (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[5]/div/button[1]/span")

