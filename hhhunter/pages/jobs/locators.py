from selenium.webdriver.common.by import By

class JobsPageLocators:
    MOSCOW_CHECKBOX = (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/aside/div[9]/fieldset/div[2]/ul/li[2]/label")
    PAGE = lambda x: (By.XPATH, "//*[@id=\"HH-React-Root\"]/div/div[3]/div[1]/div/div[2]/div[2]/div[2]/main/div[5]/div/span[{}]/a".format(x))
