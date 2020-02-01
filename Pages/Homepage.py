from Pages.Basescreen import BaseScreen
import time

class Homepage(BaseScreen):
    base_url = 'https://github.com/'
    sign_link_text = 'Sign in'

    def __init__(self, driver):
        self.driver = driver

    def Opelink(self):
        element = self.wait_until_clickable(self.driver.find_element_by_link_text(self.sign_link_text))
        element.click()
        time.sleep(20)
        print(self.driver.current_window_handle)
        self.driver.window_handles



