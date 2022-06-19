import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#ブラウザの立ち上がる
browser = webdriver.Chrome() 
browser.get('https://www.hackerrank.com/domains/python') #この部分でエラー発生中

html = browser.find_element_by_class_name('challengecard-title')
print(html)

'''
# beautifulsoupを使用したデータ取得（スクロールが発生する場合は使用できない）
title_texts = soup.find_all(class_='challengecard-title')

# データ整形（ファイル名が見やすいように）
title_array = []
for title in title_texts:
    title = title.text
    title = title.split('Easy')[0]
    title = title.split('Medium')[0]
    title = title.split('Hard')[0]
    title_array.append(title)

print(title_array)
'''

'''
# ファイル作成
title = 'a' 
path = '../HackerRank/' + title + '.py'
f = open(path, 'w')
f.write("")
'''