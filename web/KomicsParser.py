import requests

from bs4 import BeautifulSoup

import urllib.request

from os import mkdir

url = 'https://xkcd.com/'

errorDownloads = {}

mkdir('C:/Users/Admin/Desktop/Comics')

for page in range(1, 100):

    try:
        res = requests.get(url + str(page))
        page_soup = BeautifulSoup(res.text, 'lxml')
        img = page_soup.find('img', style = "image-orientation:none")

        urllib.request.urlretrieve('https:' + img.get('src'), 'C:/Users/Admin/Desktop/Comics/' + img.get('alt') + '.png')

        print('Загружено - ', img.get('alt'))
    except:
        print('Download error')
        errorDownloads.update({img.get('alt') : 'https:' + img.get('src')}) 
    



