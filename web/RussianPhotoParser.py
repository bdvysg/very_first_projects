import requests

from bs4 import BeautifulSoup

import shutil

from os import mkdir

mkdir('C:/Users/Admin/Desktop/Russian Photo')

errorDonwloads = []

for i in range(1, 18):

    res = requests.get('https://www.loc.gov/collections/prokudin-gorskii/?c=150&sp=%s&st=list' % (i))
    res_soup = BeautifulSoup(res.text, 'html.parser')
    next_page_link = res_soup.find('a', class_ = 'next')
    img_blocks=res_soup.find_all('span', class_ = 'item-description-title')

    for img_block in img_blocks:

        img_page_link = img_block.a.get('href')
        img_page_res = requests.get(img_page_link)
        img_page_soup = BeautifulSoup(img_page_res.text, 'html.parser')
        img_link = img_page_soup.find('img', class_ = 'iconic screen-dependent-image')

        if img_link != None:
            try:
                r = requests.get(img_link.get('data-image-tablet'), stream=True)
                if r.status_code == 200:
                    with open('C:/Users/Admin/Desktop/Russian Photo/' + img_page_soup.cite.text + '.jpg', 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
            except:
                print('Name Error')
                errorDonwloads.append(img_link.get('data-image-tablet'))
        
            print('Загружено - ', img_page_soup.cite.text)
        else:
            errorDonwloads.append(img_page_link)

print(errorDonwloads)







