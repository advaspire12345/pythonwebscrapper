from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys as k
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import os
import requests
from selenium.webdriver.common.action_chains import ActionChains
import random
import urllib
import re
from datetime import datetime
import json
from selenium.webdriver.common.keys import Keys
import setting1

PATH = r"C:\Users\khsra\Desktop\python webscrapping\chromedriver\chromedriver.exe"
websitePath = "https://www.facebook.com/"
USERNAME = "erikaariffin90@gmail.com"
PASSWORD = "Erikaariffin_90"
print(PATH)
print(USERNAME)
print(PASSWORD)

driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com/")

email = driver.find_element(By.ID, "email")
email.send_keys(USERNAME)
password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)
time.sleep(1)
password.send_keys(Keys.RETURN)

print(driver.current_url)

action = ActionChains(driver)

RANDOM_CAT_ID = [{"category_ID": "C1639059613", "title": "Property"},
                    {"category_ID": "C1644386246", "title": "Recruitment"},
                    {"category_ID": "C1649236426", "title": "Digital Marketing"},
                    {"category_ID": "C1652755672", "title": "Healthcare"},
                    {"category_ID": "C1656578687", "title": "Beauty"}]

print(RANDOM_CAT_ID)

NEWSFEED_SCRAPER = True
POSTS = []
NO_MORE_POSTS = False

print("running line 56")

only_int = []
share_count = 0
comments_count = 0

sponsor_class = "x15bjb6t x1qlqyl8 xjb2p0i xt0psk2 x9f619"

SCROLL_PAUSE_TIME = 5
# e = driver.find_element(By.TAG_NAME, 'body')
# e.click()
# Get scroll height
lh = driver.execute_script("return document.body.scrollHeight")
if NEWSFEED_SCRAPER:
    # rimuovi la barra bianca di facebook che da problemi e a volte viene cliccato in automatico
    topbar = driver.find_elements(By.XPATH, '//*[@role="banner"]')
    if len(topbar):
        driver.execute_script('arguments[0].remove();', topbar[0])
    while not NO_MORE_POSTS:
        # Scroll down to bottom
        action.scroll_by_amount(0, 50).perform()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        print("I'm scrolling down 50 lines")
        time.sleep(SCROLL_PAUSE_TIME)

        

        
        # Calculate new scroll height and compare with last scroll height
        nh = driver.execute_script("return document.body.scrollHeight")
        if nh == lh:
            break
        lh = nh - 2