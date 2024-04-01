from bs4 import BeautifulSoup

html = """
<a class="logo_naver">
    <span class="blind">네 이버</span>
</a>
"""

soup = BeautifulSoup(html, "html.parser")

logo = soup.select_one(".logo_naver")

print(f"text : {logo.text.strip()}")
print(f"string : {logo.string}")

'''
text : 그 태그 안의 모든 글자를 추출한다. 
string : 한 개의 태그만 줘야 함. 
즉, 빈칸이 많이 있으면 많은 태그 중에 어떤 것을 가져와야 할 지 몰라 None 출력

text만 하면 두루뭉실하게 할 수 있지만, 되도록 상세하게 지정해주는 것이 좋다!
'''