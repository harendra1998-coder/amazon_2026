
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from pages.locaters import  Locater


class OrangePage:


    def __init__(self,driver):
        self.driver = driver
        self.locate= Locater

    def click_admin_user(self):
        admin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locate.admin))
        admin.click()
        self.driver.implicitly_wait(10)
        assert "/admin/viewSystemUsers" in self.driver.current_url

    def click_add(self):
        self.driver.find_element(*self.locate.click_add).click()


