from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseScreen(object):
    """Base class for other Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.instance.title

    def select_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def select_elements(self, locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        return elements

    def wait_until_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def presence_of_element_located(self, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located(locator))
