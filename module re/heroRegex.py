import re

heroRegex  = re.compile(r'Batman|Tina Fey')# выбор альтернативный груп с помощью канала

mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
