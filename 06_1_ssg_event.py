import requests
from bs4 import BeautifulSoup

url = "https://www.ssg.com/event/eventMain.ssg"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

evt_osmu_lst = soup.select_one(".evt_osmu_lst")
units = evt_osmu_lst.select(".eo_link")
# print(len(eo_link))

for i, unit in enumerate(units, 1):
    link = unit['href']
    if link.startswith("https"):
        print(f"{i} : {link}")
    else:
        print(f"https://event.ssg.com{link}")
