from bs4 import BeautifulSoup
import requests
from config import client_id, client_secret

keyword = input("검색어를 입력하세요: ")

url = f"https://msearch.shopping.naver.com/search/all?query={keyword}&vertical=search"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

headers = {
    "User-Agent": user_agent,
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret

}
cookie = {"a": "b"}
req = requests.get(url, headers=headers, cookies=cookie)
html = req.text
print(html)
soup = BeautifulSoup(html, "html.parser")
