from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import pandas as pd

#Configuring Chrome options.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

project_url="https://github.com/collections/machine-learning"

#Created web driver.
def create_driver():
    driver = webdriver.Chrome(options=chrome_options)
    return driver

#Created a webdriver instance.
driver1 = create_driver()
driver1.get(project_url)

articles = driver1.find_elements(By.TAG_NAME, "article")
article_names = []
article_links = []
article_stars = []

#This for loop section iterates through each article element found on the page, 
# extracting the link and name of each article and appending them to the respective lists.
for article in articles: 
    article_links.append(article.find_element(By.CSS_SELECTOR, "h1 > a").get_attribute("href"))
    article_names.append(article.find_element(By.CSS_SELECTOR, "h1 > a").text)
    article_stars.append(article.find_element(By.CSS_SELECTOR, "a[href*='/stargazers']").text.strip())

df = pd.DataFrame({
    "Name": article_names,
    "Link": article_links,
    "Stars": article_stars
})
article_csv = df.to_csv(index=False)

with open("./projects.csv", mode="a") as file:
    file.write(article_csv)
