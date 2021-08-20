import requests
import os

url = 'http://learnlibrary.com/romeo-juliet/romeo-and-juliet_4.htm'
os.chdir('C:/Users/Admin/Desktop/programs/web')
re = requests.get(url)
print(re.status_code == requests.codes.ok)
with open('romeo_and_juilet.html', 'wb') as text:
    for chunk in re.iter_content(5000):
        text.write(chunk)
        print(len(chunk))
