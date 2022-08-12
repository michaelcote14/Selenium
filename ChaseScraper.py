import os
from selenium import webdriver
import time
#used for explicit waits + "by" locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# brings in "by" locator
from selenium.webdriver.common.by import By


# opens Chrome
os.environ['Path'] += r"C:\Users\micha\OneDrive\Pycharm"
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

# maximizes the driver window
#driver.maximize_window()
# website you want chrome to go to
driver.get("https://www.chase.com/personal/offers/secureshopping")

# makes the driver wait between task
driver.implicitly_wait(20)


# types in keys to a text box
try:
    my_element =
#my_element.send_keys(15)
#my_element.click()

# clicks on a clickable element
#search_button = driver.find_element(By.CLASS_NAME,"btn-primary")
#search_button.click()
