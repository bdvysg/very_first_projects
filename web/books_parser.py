import requests
import openpyxl
from bs4 import BeautifulSoup
from io import BytesIO


headers = {
    
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}
def get_book_count(word):
    res = requests.get(f'https://www.litres.ru/pages/rmd_search/?q={word}', headers=headers)
    if res.status_code == 200:
        res_soup = BeautifulSoup(res.text, 'html.parser')
        count = int(res_soup.find('a', href = f'/pages/rmd_search_arts/?q={word}').span.get_text())
        print(count)
        return count
    else:
        print('ошибка при получении страници')





def get_book_list_litres(word):
    book_list = []
    for i in range(1, 3):
        res = requests.get(f'https://www.litres.ru/pages/rmd_search_arts/page-{str(i)}/?q={word}&lite=1&gu_ajax=true&=', headers=headers)
        if res.status_code == 200:
            res_soup = BeautifulSoup(res.text, 'html.parser')
            divs = res_soup.find_all(itemtype="http://schema.org/Book")
            for book in divs:
                try:
                    book_info = []
                    src = book.img.get('src')
                    name = book.img.get('alt')
                    author = book.find('div', class_ = 'art-item__author').a.getText()
                    book_info.append(name)
                    book_info.append(author)
                    book_info.append(src)
                    book_list.append(book_info)
                except Exception as ex:
                    print(ex)
        else:
            print('ошибка при получении списка книг')
    print('Загружено - ', len(book_list), ' книг')
    return book_list


def get_links_list(book_list):
    for book in book_list:
        res = requests.get(f'https://flibusta.is/booksearch?ask=' + book[0].replace(' ', '+').replace(',', '2C').replace('+', '2B') + '&chb=on')
        


def write_excel_file(word):
    wb = openpyxl.Workbook()
    sheet = wb.active
    book_list = get_book_list_litres(word)

    sheet['A1'].value = 'Название книги'
    sheet['B1'].value = 'Автор'
    sheet['C1'].value = 'Изображение'

    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 15
    sheet.column_dimensions['C'].width = 20

    style = openpyxl.styles.Alignment(wrap_text=True, vertical='top')

    for book in range(2, len(book_list)):
        try:
            sheet['B' + str(book)].value = book_list[book][1]
            if book_list[book][0].strip().find('(pdf+epub)') != -1:
                sheet['A' + str(book)].value = book_list[book][0].replace('(pdf+epub)', '')
            else:
                sheet['A' + str(book)].value = book_list[book][0]

            res = requests.get(book_list[book][2])
            img = BytesIO(res.content)
            img = openpyxl.drawing.image.Image(img)
            sheet.add_image(img, 'C' + str(book))

            sheet['A' + str(book)].alignment = style
            sheet['B' + str(book)].alignment = style
            sheet.row_dimensions[book].height = 144
        except Exception as ex:
            print(ex)

    wb.save('C:/Users/Admin/Desktop/books.xlsx')

write_excel_file('rust')