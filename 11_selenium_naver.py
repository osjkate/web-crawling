from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup

options = Options()
options.add_argument("--start-maximum")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

driver.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(2)

# CSS_SELECTOR 아이디, 클래스 모두 적용 가능
driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
time.sleep(2)

# driver.find_elements(By.CLASS_NAME, "flick_bx")[1].click()
# time.sleep(2)

# 하위에 있는 모든 것에서 이걸 찾아내라!
# 어려우니까 text로 찾아야 할 때만 사용해라!
# # driver.find_element(By.XPATH, '//*[text()="뉴스"]').click()
# time.sleep(2)

driver.find_element(By.NAME, "query").clear()
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys("에스파")
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
time.sleep(2)

# 스크롤 여러번 하고 싶으면 반복문 사용하기
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(1)

driver.save_screenshot("11_selenium_naver/naver.png")
print("스크린샷을 저장하였습니다.")

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".api_ani_send")

rank_num = 1
for area in items:
    ad = area.select_one(".link_ad")
    if ad:
        # print("광고입니다. ")
        continue
    print(f"<<<{rank_num}>>>")
    title = area.select_one(".news_tit")  # 빈칸을 점으로 바꿔야 함 주의
    name = area.select_one(".info.press")
    print(name.text)
    print(title.text)
    print(title['href'])
    print()

    rank_num += 1
