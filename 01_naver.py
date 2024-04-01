import itertools

import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# requests 는 사이트 가져올 때 사용
# 이거 딱 가져왔을 때의 상태를 분석하는 것!
req = requests.get(url, headers=headers)

# print(req.raise_for_status)
# 쓸 수 있는 걸 보자
# print(dir(req))

# 우리가 url로 요청을 하면 이 헤더를 보낸다 -> User-Agent에 python-requests 어쩌구로 나옴
# 그런데 이 헤더를 보고 우리를 차단하는 사이트가 있다!
# -> 내가 따로 설정해 주는게 좋다!
# print(req.request.headers)
# print(dir(req.request))

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36

html = req.text
#
# # print(html)
#
# # html 을 html.parser로 분석해서 객체를 만들어준다.
soup = BeautifulSoup(html, "html.parser")
#
# # .클래스명
# # #아이디명
# logo = soup.select_one("#special-logo").text
# # print(logo)

total_area = soup.select(".news_area")
timeline_area = soup.select(".timeline_area")


# news_tit
# titles = soup.select(".news_tit")   # 빈칸을 점으로 바꿔야 함 주의
# names = soup.select(".info.press")
# print(result)
# print(list(result))


# for result in zip(names, titles): #-> zip() 쌍을 가진 튜플로 만들어줌
#     # print(result['href'])
#     # print(result['onclick']) # 키 에러가 뜨는 경우도 있음 .get() 사용하기
#     # print(result.get('asdf')) # get을 사용하면 에러가 안나고 None을 리턴
#     print(result[0].text)
#     print(result[1].text)
#     print(result[1]['href'])
#     print()
#     # 만약에 출처가 없는 글이 있으면 개수가 맞지 않아서 밀림

# 이 조건문 처리가 중요함!
# if total_area:
#     areas = total_area
# elif timeline_area:
#     areas = timeline_area
# else:
#     print("확인 요망")
#     areas = None

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

# print(len(items)) # -> 접속했을 당시의 html을 사용하는 것 동적 페이지는 selenium 써야 함.

# 검색엔진 크롤링을 할 때는 최대한 많은 검색을 해봐야 함.
# 클래스명이 다 다르고 계속 바뀌기 때문에
# if 광고가 있음 -> 광고를 제거하기 : 광고만 가지고 있는 테그를 찾아라!
