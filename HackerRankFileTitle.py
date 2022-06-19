import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver #モジュールのインポート

browser = webdriver.Chrome() #ブラウザの立ち上がる
browser.get('https://www.hackerrank.com/domains/python') 

html = browser.find_element_by_class_name('challengecard-title')
print(html)

'''
# title タグの文字列を取得する
title_array = []
title_texts = soup.find_all(class_='challengecard-title')
for title in title_texts:
    title = title.text
    title = title.split('Easy')[0]
    title = title.split('Medium')[0]
    title = title.split('Hard')[0]
    title_array.append(title)

print(title_array)
'''

'''
title = 'a' 
path = '../HackerRank/' + title + '.py'
f = open(path, 'w')
f.write("")
'''