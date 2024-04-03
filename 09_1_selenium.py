from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/home"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)

html = driver.page_source

# req = requests.get(url)
#
# html = req.text

print(html)

# soup = BeautifulSoup(html, "html.parser")

# logo = soup.title.text

# print(logo)