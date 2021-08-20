import re
vowelRegex = re.compile(r'[aeiouAEIOU]')# с помощью квадратных скобок можно задавать собственный символьный клас
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)


vowelRegex = re.compile(r'[^aeiouAEIOU]')# знак ^ создает инвертированый символьный клас
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)