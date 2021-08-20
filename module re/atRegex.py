import re
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat')
print(mo)

