import time

from selenium.webdriver.common.by import By


def test_dynami_calender(driver):
   driver.get("https://jqueryui.com/datepicker/")
   time.sleep(4)
   iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
   driver.switch_to.frame(iframe)

   driver.find_element(By.CSS_SELECTOR, ".hasDatepicker").click()



