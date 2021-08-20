import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Мой номер: 415-555-4242.')
print('Найденый телефонный номер: ' + mo.group())

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())
areaCode, mainNumber = mo.groups()
print('Area code is ' + areaCode)
print('Main number is ' + mainNumber)
