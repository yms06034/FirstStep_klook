from multiprocessing.connection import wait
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import re

# Options Setting
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('no-sandox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('incognito')
# Header Setting
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")

browser = webdriver.Chrome("./chromedriver.exe" ,options=options)

browser.get("https://shopping.naver.com/")
# wait= WebDriverWait(browser, 10)

# def find(wait, css_selector):
#   return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)))

# search = find(wait, "input[class='_searchInput_search_text_3CUDs']")
def find(css_selector):
  return browser.find_element(By.CSS_SELECTOR, css_selector) # 단수처리

search = find("input[class='_searchInput_search_text_3CUDs']")
search.send_keys('아이패드 프로2세대 케이스\n') # \n = Enter

browser.implicitly_wait(3)

# button = find("button[class='_searchInput_button_search_1n1aw']")
# button.() # click보다 Enter가 훨씬 빠르다

# time.sleep(2)
# print(search)


browser.close()