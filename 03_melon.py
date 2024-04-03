import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def get_song_nums(song_num_text):
    '''song_num = []
    for num in song_num_text:
        if num.isdigit():
            song_num.append(num)

    song_num = "".join(song_num)
    return song_num'''

    song_num = "".join([num for num in song_num_text if num.isdigit()])
    return song_num

url = "https://naver.com"

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=headers)
html = req.text

soup = BeautifulSoup(html, "html.parser")

'''
1
lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lst = lst50 + lst100

2
lst = soup.select(".lst50, .lst100")

3
lst = soup.find_all(class_=["lst50", "lst100"])
'''

lst = soup.find_all(class_=["lst50", "lst100"])


for rank, i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a") # 태그를 정확하게 지정해주기

    singer = i.select_one(".ellipsis.rank02 > a")
    singer_link = get_song_nums(singer['href'])

    album = i.select_one(".ellipsis.rank03 > a")
    album_link = get_song_nums(album['href'])

    print(f"{rank} : {title.text}")
    print(f"{singer.text} : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"{album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}")
    print()
    # .string은 정확하게 그 태그가 가지고 있는 걸 출력해줌
    # .text는 text를 찾아서 출력해줌
