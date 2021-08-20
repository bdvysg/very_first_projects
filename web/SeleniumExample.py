from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Firefox(executable_path = 'C:/Users/Admin/AppData/Roaming/Python/Python38/geckodriver.exe')

browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('html')

for i in range(100):
    time.sleep(1)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    htmlElem.send_keys(Keys.ARROW_UP)
    time.sleep(1)
    htmlElem.send_keys(Keys.ARROW_LEFT)
    time.sleep(1)
    htmlElem.send_keys(Keys.ARROW_RIGHT)


