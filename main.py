from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
browser.get("https://www.klook.com/ko/coureg/10-south-korea-things-to-do/?start=1")

"""CSS backgrouind-image URL get"""
my_property = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 
  "div[class='m_bg lazy lazy-hot lazy-loaded']"))).value_of_css_property("background-image")
print(re.split('[()]',my_property)[1])

browser.implicitly_wait(5)
browser.quit()