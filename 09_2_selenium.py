from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#driver.execute_script("window.scrollTo(0,4000)")
for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2) # 스크롤하고 페이지가 로드되는 시간이 필요하기 때문

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

total_area = soup.select(".news_area")
timeline_area = soup.select(".timeline_area")

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