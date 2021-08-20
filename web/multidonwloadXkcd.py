import requests

import os

from bs4 import BeautifulSoup

import threading

import urllib.request

import time

os.mkdir('C:/Users/Admin/Desktop/Xkcd',)

def downloadXkcd(startComic, endComic):

    url = 'https://xkcd.com/'

    for page in range(startComic, endComic):

        try:
            res = requests.get(url + str(page))
            page_soup = BeautifulSoup(res.text, 'lxml')
            img = page_soup.find('img', style = "image-orientation:none")

            urllib.request.urlretrieve('https:' + img.get('src'), 'C:/Users/Admin/Desktop/Xkcd/' + img.get('alt') + '.png')

            print('Загружено - ', img.get('alt'))
        except:
            print('Download error')


startTime = time.time()

downloadThreads = []
for i in range(0, 2000, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args = (i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

endTime = time.time()

print('Время загрузки всех файлов - ', endTime - startTime)



