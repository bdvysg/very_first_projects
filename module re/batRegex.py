import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # выбор альтернативынй вариантов при помощи канала 
mo = batRegex.search('Batmobile потерял колесо')
print(mo.group())