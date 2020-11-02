# -*- coding: utf-8 -*-
"""
    <项目名称>:<文件名称>
    <文件描述>
    :copyright: (c) 2019 by debris.
    :license: GPLv3, see LICENSE File for more details.
"""
from bs4 import BeautifulSoup
import requests

i = 0
url = 'https://unsplash.com/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')

img_class = soup.find_all('div', {"class": "IEpfq"})  # 找到div里面有class = "IEpfq"的内容
for img_list in img_class:
    imgs = img_list.find_all('img')  # 接着往下找到 img 标签
for img in imgs:
    src = img['src']  # 以"src"为 key，找到 value
r = requests.get(src, stream=True)
image_name = 'unsplash_' + str(i) + '.jpg'  # 图片命名
i += 1
with open('./img/%s' % image_name, 'wb') as file:  # 打开文件
    for chunk in r.iter_content(chunk_size=1024):  # 以chunk_size = 1024的长度进行遍历
        file.write(chunk)
print('Saved %s' % image_name)
