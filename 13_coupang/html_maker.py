from datetime import datetime

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}
cookie = {"a": "b"}

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색할 상품을 입력하세요: ")

search_url = base_url + keyword

req = requests.get(search_url, timeout=5, headers=headers, cookies=cookie)

html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")

rank = 1
main_text = ""
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
    link = f"https://coupang.com{link}"

    print(f"{rank}위")
    print(name.text.strip())
    print(f"{price.text}원")
    print(link)
    if thumb.get('data-img-src'):
        img_url = f"http:{thumb.get('data-img-src')}"
    else:
        img_url = f"http:{thumb['src']}"

    img_url = img_url.replace("230x230ex", "1000x1000ex")
    print(img_url)
    print()

    main_text += f"""<a href='{link}' target='_blank'>
                        <div class='image main'>
                            <img src='{img_url}' alt='' />
                        </div>
                    </a>
                    <p>
                        <h2>{rank}위 : {name.text}</h2>
                        <b>가격 : {price.text}원</b>
                    </p>"""

    rank += 1
    if rank == 11:
        break

now = datetime.now()
today_date = f"{now.year}년 {now.month}월 {now.day}일"

file_name = "index.html"
title_text = f"오늘의 {keyword}"
summary_text = f"{today_date} 오늘의 {keyword} 인기상품 Top10 입니다. "

html_text = f"""<!DOCTYPE HTML>
<!--
	Massively by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>{title_text}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<a href="index.html" class="logo">Massively</a>
					</header>

				<!-- Main -->
					<div id="main">

						<!-- Post -->
							<section class="post">
								<header class="major">
									<span class="date">{today_date}</span>
									<h1>{title_text}</h1>
									<p>{summary_text}</p>
								</header>
								{main_text}
							</section>

					</div>

				<!-- Copyright -->
					<div id="copyright">
						<ul><li>&copy; Untitled</li><li>Design: <a href="https://html5up.net">HTML5 UP</a></li></ul>
					</div>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>"""


with open(f"html5up-massively/{file_name}", 'w', encoding='utf-8') as f:
    f.write(f"{html_text}")

