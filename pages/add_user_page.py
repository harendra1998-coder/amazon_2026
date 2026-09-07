import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locaters import Locater



class AddUserPage:
    def __init__(self,driver):
        self.driver=driver
        self.locate = Locater

    def user_data(self,option):
        self.driver.find_element(*self.locate.user).click()
        user_locator = (
            self.locate.user_name[0],
            self.locate.user_name[1] % option
        )

        # Click option
        self.driver.find_element(*user_locator).click()

    def status(self,option):
        self.driver.find_element(*self.locate.status ).click()
        status_locator = (
            self.locate.status_click[0],
            self.locate.status_click[1] % option
        )
        self.driver.find_element(*status_locator).click()
    def employee(self):
        self.driver.find_element(self.locate.employee).Send_Keys("Demo Open Source")
        # for suggestion dropdown
        # location = Locater.SUGGESTION.format(option=option1)
        #
        # WebDriverWait(self.driver, 10).until(
        # EC.element_to_be_clickable(location)
        # ).click()
