import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Сотовый: 415-555-9999. Рабочий: 212-555-0009')#возвращает первый найденый елемент в виде строки
print(mo.group())

mo1 = phoneNumRegex.findall('Сотовый: 415-555-9999. Рабочий: 212-555-0000')#возвращает все найденые елементы в виде списка
print(mo1)



phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3 = phoneNumRegex.findall('Сотовый: 415-555-9999. Рабочий: 212-555-0000')#возвращает все найденые елементы в виде списка
print(mo3)