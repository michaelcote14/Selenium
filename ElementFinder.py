import os
from selenium import webdriver
import keyboard

# brings in "by" locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Opens Chrome
os.environ['Path'] += r"C:\Users\micha\OneDrive\Pycharm"
driver = webdriver.Chrome()

# website you want chrome to go to
driver.get("https://www.chase.com/personal/offers/secureshopping")

# makes the driver wait between task
driver.implicitly_wait(10)

# clicks on the element you specify
try:
    my_element = driver.find_element(By.ID, "main")
    #my_element.send_keys("test")
    login_box = main.find_element(By.ID, "userId-text-input-field")
except:
    print("can't find element")
