from selenium.webdriver.common.by import By
from Values import locators
class Loginpage():
    login = "//input[@type='text' and @name = 'login']"
    password = "//input[@type='password' and @name = 'password']"
    submit = "//input[@type='submit' and @name = 'commit']"
    logout = "//*[@class ='Header-link'] //*[@alt = '@Hemush1990']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.login).is_enabled()
        self.driver.find_element(By.XPATH, self.login).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password).is_enabled()
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def setSubmit(self):
        self.driver.find_element(By.XPATH, self.submit).click()

    def setLogout(self):
        self.driver.find_element(By.XPATH, self.logout).click()

    def setincorrect(self):
        assert self.driver.find_element(By.XPATH, self.login).send_keys(locators.username1), 'Incorrect login'
        assert self.driver.find_element(By.XPATH, self.password).send_keys(locators.password2), 'Incorrect password'



