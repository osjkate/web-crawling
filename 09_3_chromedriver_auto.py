from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# service = Service(ChromeDriverManager().install())
# 크롬 드라이버를 자동으로 설치하는 서비스를 만들었다라고 생각하기
# 버전 알아서 맞춰서 설치해 줌
# 업데이트 되어서 그냥 바로 됨

driver = webdriver.Chrome()

driver.get("https://google.com")
time.sleep(2)
