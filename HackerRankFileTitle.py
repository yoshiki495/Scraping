import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time

#ブラウザの立ち上がる
driver = webdriver.Chrome() 
driver.get('https://www.hackerrank.com/domains/python')

#20回スクロールの動作を行う
for i in range(20):
    # ページの一番下までスクロールする
    driver.execute_script('window.scrollTo(0 ,document.body.scrollHeight);')
    time.sleep(10)

source = driver.find_elements(By.CLASS_NAME, value='challengecard-title')

'''
# beautifulsoupを使用したデータ取得（スクロールが発生する場合は使用できないためコメントアウト）
title_texts = soup.find_all(class_='challengecard-title')
'''

# データ整形（ファイル名が見やすいように）
title_array = []
for title in source:
    title = title.text
    title = title.split('Easy')[0]
    title = title.split('Medium')[0]
    title = title.split('Hard')[0]
    title = title.split('.')[0]
    title = title.split('\n')[0]
    title_array.append(title)   

# ファイル作成
for title in title_array:
    path = '../HackerRank/' + '[Caption' + str(title_array.index(title)) + ']' + title + '.py'
    f = open(path, 'w')
    f.write("")
    print(title)