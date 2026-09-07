from click import option
from selenium.webdriver.common.by import By


class Locater:


       admin = (By.XPATH,"//span[text()='Admin']")
       username = (By.XPATH,"//input[@name='username']")
       password = (By.XPATH,"//input[@name='password']")
       login = (By.XPATH,"//button[@type='submit']")
       click_add = (By.XPATH,"//button[normalize-space()='Add']")
       user= (By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
       user_name = (By.XPATH,"//div[contains(normalize-space(),'%s')]")
       status = (By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")
       status_click = (By.XPATH,"//div[contains(normalize-space(),'%s')]")
       employee = (By.XPATH,"//div[@class='oxd-autocomplete-wrapper']")
       SUGGESTION = "//div[contains(@class,'suggestion')]//span[normalize-space()='{option}']"

