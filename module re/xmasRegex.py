import re
xmasRegex = re.compile(r'\d+\s\w+')# d означает любую цифру, s - пробел и w - букву.
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladiess,8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 parttidge')
print(mo)