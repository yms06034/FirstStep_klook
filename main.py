from selenium import webdriver
import time

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
browser.get("https://www.naver.com")
# https://www.klook.com/ko/coureg/10-south-korea-things-to-do/?start=1
time.sleep(10)
browser.quit()