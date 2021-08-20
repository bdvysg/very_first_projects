import re

import os

matches = []

user_input_regular_expression = input('Введите регулярное выражение: ')
regular_expression = re.compile(user_input_regular_expression)

for file in os.listdir():
    if os.path.basename(file)[-4:] == '.txt':
        with open(file) as text_file:
            matches = regular_expression.findall(text_file.read())
            print('Найдено ', len(matches), 'совпадений в файле', os.path.basename(file))
            if len(matches) > 0:
                print('совпадения: ', matches)


