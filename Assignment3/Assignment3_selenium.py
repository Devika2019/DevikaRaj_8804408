# Importing required libraries

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Setting up the webdriver
PATH = "C:/webdrivers/chromedriver.exe"
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH,options=options)


# # Navigating to the bestbuy.ca homepage
driver.get("https://www.bestbuy.ca/en-ca")
time.sleep(3)
#
# # Finding the search bar and entering text
# # search_bar = driver.find_element_by_id("id","twotabsearchtextbox")
search_bar = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[1]/div[2]/div[1]/div/div/form/div/input")
search_bar.send_keys("cocomelon toy")
# # Submitting the search query
search_bar.send_keys(Keys.RETURN)
driver.maximize_window()
time.sleep(10)
product_link = driver.find_element("xpath","/html/body/div[1]/div/div[2]/div[1]/div/main/div[1]/div[2]/div[2]/div[2]/ul/div/div[1]/div/a/div/div/div[1]/div/div/div/div")
product_link.click()
time.sleep(10)
# # Add product to cart
cart_link = driver.find_element("xpath","/html/body/div[1]/div/div[4]/section[4]/div[2]/div/div[2]/div/div[1]/div[2]/div/form/button")
cart_link.click()
time.sleep(10)
viewcart_link = driver.find_element("xpath","/html/body/div[1]/div/div[3]/div/header/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/section/div/button/span")
viewcart_link.click()
time.sleep(5)

# # Navigate back to homepage
homepage_link = driver.find_element("xpath","/html/body/div[1]/div/header/div/div/div[1]/div[2]/a")
homepage_link.click()
time.sleep(5)
# # view top deals
topdeal_dropdown = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div/div/div[2]/div/ul[1]/li[3]/button/span")
topdeal_dropdown.click()
time.sleep(5)
topdeal_option = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div/div/div[2]/div/ul[1]/li[3]/div[2]/div/a[1]")
topdeal_option.click()
time.sleep(5)
# # Navigate back to homepage
homepage_link = driver.find_element("xpath","/html/body/div[1]/div/header/div/div/div[1]/div[2]/a")
homepage_link.click()
time.sleep(5)
driver.close()




