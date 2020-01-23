from selenium import webdriver
import unittest
from Pages.Loginpage import Loginpage
from Pages.Homepage import Homepage
import time
from Values import locators

class Logintests(unittest.TestCase):
    base_url = 'https://github.com/'
    driver = webdriver.Chrome(executable_path='//Users/hemush/Downloads/chromedriver')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        print(cls.driver.title)

    def testUrl(self):
        hp = Homepage(self.driver)
        hp.Opelink()
        time.sleep(3)

    def testLogin(self):
        lp = Loginpage(self.driver)
        lp.setUsername(locators.username1)
        lp.setPassword(locators.password2)
        lp.setSubmit()
        time.sleep(4)
        lp.setLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main()
