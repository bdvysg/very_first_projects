import requests

import os

import urllib.request

from bs4 import BeautifulSoup
from requests.api import get

os.mkdir('C:/Users/Admin/Desktop/Stamps of Soviet Union/')

#get response from url
url = 'https://commons.wikimedia.org/wiki/Category:Stamps_of_the_Soviet_Union_by_year'
res = requests.get(url)

#make soup from html in response
soup = BeautifulSoup(res.text, 'html.parser')

#make list of item of year-buy-year list
item_main_list = soup.find_all('ul')[2]

#make list of 'a', for further extract of href
a = item_main_list.find_all('a')

#iteration for every href in a
for i in range(len(a)):

    os.mkdir('C:/Users/Admin/Desktop/Stamps of Soviet Union/%s/' % (str(1923 + i) ))

    every_year_res = requests.get('https://commons.wikimedia.org/' + a[i].get('href'))
    every_year_soup = BeautifulSoup(every_year_res.text, 'html.parser')
    every_year_div = every_year_soup.find('div', class_ = 'CategoryTreeItem')
    every_year_a = every_year_div.find('a') 
    
    page_with_pic_res = requests.get('https://commons.wikimedia.org/' + every_year_a.get('href'))
    page_with_pic_soup = BeautifulSoup(page_with_pic_res.text, 'html.parser')
    a_pic_list = page_with_pic_soup.find_all('img', height = '120')
    
    for a_tag in range(len(a_pic_list)):

        src = a_pic_list[a_tag].get('src')
        alt = a_pic_list[a_tag].get('alt')

        requests.get(src, headers = {'User-agent': 'your bot 0.1'})

        try:
            urllib.request.urlretrieve(src, "C:/Users/Admin/Desktop/Stamps of Soviet Union/%s/" % (str(1923 + i) ) + alt)
        except OSError:
            print('Name Error')
        print('Загружено - ' +  alt + ' в папку ' + str(1923 + i))
        

        

    


