from selenium import webdriver
import time
from re import sub
import openpyxl
import requests
from io import BytesIO


def get_book_list(word):
    # set options for better perfomance
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # start webdriver
    driver = webdriver.Firefox(executable_path = 'C:/Users/Admin/AppData/Roaming/Python/Python38/geckodriver.exe', firefox_options=options)
    driver.get(f'https://play.google.com/store/search?q={word}&c=books')

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # get list of book blocks
    book_blocks = driver.find_elements_by_class_name('Vpfmgd')
    print('Получен список книг')

    # append book info into list
    books_info = []
    for block in book_blocks:
        try:
            img = block.find_element_by_class_name('T75of').get_attribute('data-src')
        except:
            print('Отсутствие изображение')
            img = ''

        try:
            title = block.find_element_by_class_name('WsMG1c').text
        except:
            print('Отсутствие названия')
            title = ''

        try:
            author = block.find_elements_by_class_name('KoLSrc')[0].text
        except:
            print('Отсутвие автора')
            author = ''

        try:
            price = block.find_element_by_class_name('VfPpfd').find_element_by_tag_name('span').text
        except:
            print('Отсутствие цены')
            price = ''

        try:
            description = block.find_element_by_class_name('f5NCO').find_element_by_tag_name('a').  get_attribute('innerHTML')
        except:
            print('Отсутствие описания')
            description = ''

        try:
            description = sub(r'\<[^>]*\>', '', description)
            books_info.append([img, title, author, description, price])
        except:
            print('Ошибка при заполнении списка')


    driver.quit()
    print('Загружен список книг')
    return books_info


def write_excel_file(word):
    # create excel file 
    wb = openpyxl.Workbook()
    sheet = wb.active
    book_list = get_book_list(word)
    print('Запись файлов')

    # set title of column
    sheet['A1'].value = 'Изображение'
    sheet['B1'].value = 'Название'
    sheet['C1'].value = 'Автор'
    sheet['D1'].value = 'Описание'
    sheet['E1'].value = 'Цена'

    #set width every column
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 15
    sheet.column_dimensions['C'].width = 20
    sheet.column_dimensions['D'].width = 35

    # create style obj
    style = openpyxl.styles.Alignment(wrap_text=True, vertical='top')

    # add data in every row
    for book in range(2, len(book_list)):
        try:
            # add title, author, description, price
            sheet['B' + str(book)].value = book_list[book][1]
            sheet['C' + str(book)].value = book_list[book][2]
            sheet['D' + str(book)].value = book_list[book][3]
            sheet['E' + str(book)].value = book_list[book][4]

            # add image
            res = requests.get(book_list[book][0])
            img = BytesIO(res.content)
            img = openpyxl.drawing.image.Image(img)
            sheet.add_image(img, 'A' + str(book))

            # set style for every cell
            sheet['A' + str(book)].alignment = style
            sheet['B' + str(book)].alignment = style
            sheet['C' + str(book)].alignment = style
            sheet['D' + str(book)].alignment = style
            sheet['E' + str(book)].alignment = style
            sheet.row_dimensions[book].height = 175
        except Exception as ex:
            print(ex)

    wb.save('C:/Users/Admin/Desktop/books.xlsx')

write_excel_file('django')

