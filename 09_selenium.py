from selenium import webdriver
import time

url = "https://naver.com"

driver = webdriver.Chrome()

driver.get(url)
# time.sleep(3)
# 브라우저가 뜨는 시간이 있기 때문에 BeautifulSoup보다 느리다.

# title = driver.title
# print(title)

html = driver.page_source
print(html[:500])
