import re
batRegex = re.compile(r'Bat(wo)?man') #указание необязательной групы символов с помощью "?""

mo1 = batRegex.search('The adventure of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventure of Batwoman')
print(mo2.group())