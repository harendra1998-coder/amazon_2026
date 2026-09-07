


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from conftest import driver
from pages.add_user_page import AddUserPage
from pages.login_page import LoginPage
from pages.newuser_page import OrangePage



def test_new_added_user(driver,url):

   login = LoginPage(driver)
   login.openurl(url)
   login.enter_credits()

   orange = OrangePage(driver)
   orange.click_admin_user()
   orange.click_add()

   user = AddUserPage(driver)
   user.user_data("ESS")
   user.status("Enabled")
   user.employee()

