import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

print(soup.h1)
print()

h1 = soup.find('h1')
print(h1)
print()

h1 = soup.select_one('h1')
print(h1)
print()

# find(id="") 아이디는 _ 필요없음
h1 = soup.find(class_="search_logo")
print(h1)
print()

nav = soup.find("span", string="뉴스")
print(nav)
print()

navs = soup.find_all(class_="shortcut_item")
print(navs)
print(len(navs))