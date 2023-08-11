

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    LoginPage =""
    login_option_link_text = "login"

    def click_on_login(self):
        self.driver.find_element().click

    def select_login_option(self):
        self.driver.find_element(By.ID,).click