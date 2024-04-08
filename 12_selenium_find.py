from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

# driver.find_element(By.CLASS_NAME)
# driver.find_element(By.ID)
# driver.find_element(By.CSS_SELECTOR)
# driver.find_element(By.NAME)
# driver.find_element(By.TAG_NAME)
# driver.find_element(By.XPATH)

# xpath를 대신해서 사용해볼 것
# driver.find_element(By.LINK_TEXT)
# driver.find_element(By.PARTIAL_LINK_TEXT)

"""
<input id="query" name="query" type="search" title="검색어를 입력해 주세요." 
placeholder="검색어를 입력해 주세요." maxlength="255" 
autocomplete="off" class="search_input" data-atcmp-element="">
"""

# driver.find_element(By.XPATH, '//*[@title="검색어를 입력해 주세요."]').send_keys("블랙핑크", Keys.ENTER)
# time.sleep(2)
#
# # 3번째 뉴스임
# # driver.find_elements(By.XPATH, '//*[text()="뉴스"]')[2].click()
# driver.find_element(By.LINK_TEXT, "뉴스").click()
# time.sleep(2)
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "카").click()


navs = driver.find_elements(By.CLASS_NAME, "link_service")

# print(navs)
# print()
# print(dir(navs[0]))
# print()
# print(len(navs))

for num, nav in enumerate(navs, 1):
    # print(f"<<{num}>>")
    # print(nav.get_attribute("outerHTML"))
    # print(nav.text)
    # print()
    if nav.text == "쇼핑":
        nav.click()
        break

time.sleep(2)
driver.quit()