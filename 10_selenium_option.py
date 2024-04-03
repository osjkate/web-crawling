from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

user_data = r"/Users/sujinoh/projects/webcrawling/10_selenium_option/sujin"

options = Options()

options.add_experimental_option("detach", True)

options.add_argument(f"user-agent={user_agent}")
options.add_argument(f"user-data-dir={user_data}")

# options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
options.add_argument("window-size=500,500")

# 헤드리스 모드 : 크롬 창이 뜨지 않음, 모두 개발 완료하고 확실하다 싶을 때 사용하기!
# options.add_argument("--headless")
# 헤드리스 모드가 안되면 필요함
# options.add_argument("--disable-gpu")

# 음소거, 유튜브 등 자동재생 소리 없앨 때 사용함
# options.add_argument("--mute-audio")
# options.add_argument("incognito") # 시크릿 모드로 접속

# 시크릿 모드에서 자동화 소프트웨어에 의해 켜졌다는 메시지를 보이지 않게 함.
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

url = "https://naver.com"
driver.get(url)

print(driver.page_source[:1000])

# driver.quit()
