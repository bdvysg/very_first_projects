import requests 

url = 'https://vk.com/al_wall.php?act=get_wall'

proxy = {'79.143.87.138': '9090'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cookie': 'remixlang=0; remixstid=1215713109_GykpFNkJDL0Nc7CUJJH1j835B1gcf5ZdX3lgTYdD1h4; remixrefkey=0e85d3fe4b362faa46; remixflash=0.0.0; remixscreen_width=1366; remixscreen_height=768; remixscreen_dpr=1; remixscreen_depth=24; remixscreen_winzoom=1; remixdt=0; remixuas=NzBlODNmNzE0ODVhODc1MTE4YTdiYjFk; remixseenads=0; remixscreen_orient=1; remixgp=43b713bcfb71d3131797923859f3890e; remixua=33%7C-1%7C307%7C2650595215; remixexp=1; remixbdr=0; remixsid=bab92c6f036473abb261ffdda83b49b975c1300aa61c831d196e454dbf7c3',
    }
    
res = requests.get(url, headers= headers)
res.raise_for_status()

with open('C:/Users/Admin/Desktop/page.json', 'wb') as file:
    for chunk in res.iter_content():
        file.write(chunk)

