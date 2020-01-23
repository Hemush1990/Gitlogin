class Homepage():
    base_url = 'https://github.com/'
    sign_link_text = 'Sign in'

    def __init__(self, driver):
        self.driver = driver

    def Opelink(self):
        self.driver.find_element_by_link_text(self.sign_link_text).click()


