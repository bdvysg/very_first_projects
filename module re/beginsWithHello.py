import re
beginsWithHello = re.compile(r'^Hello')# ищет регулярное выражени вначале текста
mo = beginsWithHello.search('Hello World!')
print(mo.group())


mo2 = beginsWithHello.search('He said Hello')
print(mo2 == None)



endsWithNumber = re.compile(r'\d$')
mo3 = endsWithNumber.search('Tour number is 24')#ищет регулярное выражения вконце текста.
print(mo3.group())