import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}
# 쿠키 : 주고 받은 데이터를 서버가 아닌 내 브라우저에 저장하는 것
cookie = {"a": "b"}

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색할 상품을 입력하세요: ")

search_url = base_url + keyword

req = requests.get(search_url, timeout=5, headers=headers, cookies=cookie)
# timeout <- 가져올 때 걸리는 시간 제한

html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")
# print(len(items))

rank = 1
for item in items:
    badge_rocket = item.select_one(".badge.rocket > img")
    if not badge_rocket:
        continue
    elif badge_rocket['alt'] != "로켓배송":
        continue

    name = item.select_one(".name")
    price = item.select_one(".price-value")
    thumb = item.select_one(".search-product-wrap-img")
    link = item.a['href']

    print(f"{rank}위")
    print(name.text.strip())
    print(f"{price.text}원")
    print(f"https://coupang.com{link}")
    if thumb.get('data-img-src'):
        img_url = f"http:{thumb.get('data-img-src')}"
    else:
        img_url = f"http:{thumb['src']}"
    print(img_url)
    print()

    img_req = requests.get(img_url)
    with open(f"08_coupang/{rank}.png", "wb") as f:
        f.write(img_req.content)


    rank += 1