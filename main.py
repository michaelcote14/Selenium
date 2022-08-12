import os
from selenium import webdriver

# brings in "by" locator
from selenium.webdriver.common.by import By


#Opens Chrome
os.environ['Path'] += r"C:\Users\micha\OneDrive\Pycharm"
driver = webdriver.Chrome()

# website you want chrome to go to
driver.get("https://www.seleniumeasy.com/")

# makes the driver wait between task
driver.implicitly_wait(2)

# types in keys to a text box
my_element = driver.find_element(By.ID,"edit-search-block-form--2")
my_element.send_keys(15)

# clicks on a clickable element
search_button = driver.find_element(By.CLASS_NAME,"btn-primary")
search_button.click()



