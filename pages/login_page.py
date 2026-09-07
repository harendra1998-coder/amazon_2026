from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.locaters import Locater


class LoginPage:

    locate = Locater
    def __init__(self,driver):
        self.driver = driver

    def openurl(self,url):
        self.driver.get(url)
    def enter_credits(self):
        username = WebDriverWait(self.driver, 10).until(
         EC.visibility_of_element_located(self.locate.username))
        username.send_keys("Admin")
        self.driver.find_element(*self.locate.password).send_keys("admin123")
        self.driver.find_element(*self.locate.login).click()
