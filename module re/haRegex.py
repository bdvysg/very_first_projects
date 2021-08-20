import re
haRegex = re.compile(r'(Ha){3,5}')#ищет На которое повторяется 3, 4 или 5 раз

mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('HaHaHaHa')
print(mo2.group())

mo3 = haRegex.search('HaHaHaHaHa')
print(mo3.group())

mo4 = haRegex.search('Ha')
print(mo4 == None)


haRegex = re.compile(r'(Ha)+')# значение в скобках встречается одни ли большер раз, а символ * когда ноль или больше раз 


mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('HaHaHaHa')
print(mo2.group())

mo3 = haRegex.search('HaHaHaHaHa')
print(mo3.group())

mo4 = haRegex.search('Ha')
print(mo4.group())

