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

# try: 
#     stars = project.find_element(By.CSS_SELECTOR, "a[href*='/stargazers']").strip()
#     print(f"Stars: {stars}") 
#     project_df["Stars"] = stars # store in the Pandas dataframe
# except (TimeoutException, StaleElementReferenceException):
#     print("Error occurred while fetching stars.")   
