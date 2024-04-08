from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options)
url = "https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(2)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)


driver.find_element(By.CLASS_NAME, "banner_full_close").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(2)

# type_1
chart_list = driver.find_element(By.CSS_SELECTOR, "#_chartList")
items = chart_list.find_elements(By.CSS_SELECTOR, ".list_item")

# type_2
# items = driver.find_elements(By.CSS_SELECTOR, ".list_item")

# for item in items[:]:
#     try:
#         ranking_num = item.find_element(By.CSS_SELECTOR, ".ranking_num")
#     except NoSuchElementException:
#         print("링크가 없어서 삭제합니다. ")
#         items.remove(item)

action = ActionChains(driver)
action.move_to_element(items[90]).perform()

for rank, item in enumerate(items[:10], 1):
    action.move_to_element(item).perform()

    title = item.find_element(By.CSS_SELECTOR, ".title.ellipsis")
    name = item.find_element(By.CSS_SELECTOR, ".name.ellipsis")

    thumb = item.find_element(By.CSS_SELECTOR, ".inner > span")
    thumb.click()

    time.sleep(1)
    album_url = driver.current_url
    driver.back()
    time.sleep(1)

    print(f"<<<{rank}>>>")
    print(title.text)
    print(name.text)
    print(f"album_url : {album_url}")
    time.sleep(1)

# print(len(items))
driver.quit()