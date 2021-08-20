import re

greedyHaRegex = re.compile(r'(Ha){3,5}')#жадная строка возвращает самую длинную строку
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')#не жадная строка возвращает самую короткую строку
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

