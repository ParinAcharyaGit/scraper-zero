from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

#Configuring Chrome options.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

Project_Url="https://github.com/collections/machine-learning"

def create_driver(url):
    driver = webdriver.Chrome(options=chrome_options)
    return driver
