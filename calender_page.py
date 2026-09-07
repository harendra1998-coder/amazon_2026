import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait




"""""""""
def test_navigation(driver):

    driver.get("https://jqueryui.com/datepicker/")
    time.sleep(10)

    iframe = driver.find_element(By.CSS_SELECTOR,".demo-frame")
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR,".hasDatepicker").click()

    Exp_date =  24
    Exp_month = "August"
    Exp_year = "2027"

    while True:
        Actual_month = driver.find_element(By.XPATH,"//div/span[@class='ui-datepicker-month']").text
        Actual_year =  driver.find_element(By.XPATH,"//div/span[@class='ui-datepicker-year']").text
        if Exp_month == Actual_month and Exp_year == Actual_year:
         break
        else:
            driver.find_element(By.XPATH,"//a/span[text()='Next']").click()
    all_dates = driver.find_elements(By.XPATH,"//table/tbody/tr/td/a")
    for date in all_dates:
        if date == Exp_date:
            date.click()
            break

    time.sleep(5)
    driver.quit()
# ===================================================================================================================
#  
#
from datetime import datetime
# from selenium.webdriver.common.by import By
#
#
def test_calender(driver):
    driver.get("https://jqueryui.com/datepicker/")
    time.sleep(4)
    iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(iframe)

    driver.find_element(By.CSS_SELECTOR, ".hasDatepicker").click()

    # Target date
    target_date = datetime(2021, 8, 24)


    while True:

        # Get currently displayed month and year
        actual_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        actual_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

        # Convert displayed month/year into datetime
        actual_date = datetime.strptime(f"{actual_month} {actual_year}", "%B %Y")

        print("Actual:",actual_date.strftime("%B %Y"))
        print("Target:",target_date.strftime("%B %Y"))

        # Target month reached
        if actual_date.year == target_date.year and \
                actual_date.month == target_date.month:
            break

        # Target is in future → Next
        elif actual_date < target_date:
            driver.find_element(
                By.XPATH,
                "//a[@title='Next']"
            ).click()

        # Target is in past → Previous
        else:
            driver.find_element(
                By.XPATH,
                "//a[@title='Prev']"
            ).click()

    # Get all dates
    all_dates = driver.find_elements(
        By.XPATH,
        "//table[contains(@class,'ui-datepicker-calendar')]"
        "//tbody//tr//td/a"
    )

    # Select target day
    for date in all_dates:

        if date.text == str(target_date.day):
            date.click()

        break


       
 # =======================================================================================================================
    """""
from datetime import date, timedelta
from selenium.webdriver.common.by import By


def test_calender(driver):
    driver.get("https://jqueryui.com/datepicker/")
    time.sleep(4)
    iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(iframe)
    target_date = date.today() + timedelta(days=1)

    date_value = target_date.strftime("%Y-%m-%d")

    element = driver.find_element(By.XPATH,"//input[@id='datepicker']")

    driver.execute_script(
        "arguments[0].value = arguments[1];",
        element,
        "23/12/2026"


)
# ===============================================================================================================
    # 1. Calculate tomorrow dynamically
    target_date = date.today() + timedelta(days=1)

    # 2. HTML date input requires YYYY-MM-DD
    date_value = target_date.strftime("%Y-%m-%d")

    print("Target date:", date_value)
