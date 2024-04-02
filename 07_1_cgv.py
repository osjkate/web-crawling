import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

sect_movie_chart = soup.select_one(".sect-movie-chart")

movie_chart = sect_movie_chart.select("li")
# print(len(movie_chart))

for rank, movie in enumerate(movie_chart, 1):
    title = movie.select_one(".title")
    score = movie.select_one(".score")
    ticketing = score.select_one(".percent")
    egg_gage = score.select_one(".egg-gage > .percent")
    info = movie.select_one(".txt-info > strong").next_element
    # 말 그대로 다음 요소를 가져오는 것.
    # <strong> : 첫 번째 요소
    # 2024.04.10 : 두 번째 요소

    print(f"<<<{rank}위>>>")
    print(title.text)
    print(ticketing.get_text(" : ")) # text 사이에 넣어줌
    print(egg_gage.text)
    # print(info.text.strip())
    print(f"{info.strip()} 개봉")
    print()