from selenium import webdriver # launches the browser
from selenium.webdriver.common.by import By # search by parameters
from selenium.webdriver.support.ui import WebDriverWait # waits for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout 