#Задача "Записать и запомнить"

from pprint import pprint

def custom_write(file_name, strings):
    string_positions = {}
    string_number = 1
    file = open(file_name, 'w', encoding = 'utf-8')
    for i in strings:
        start_ = file.tell()
        file.write(f'\n{i}')
        key = (string_number, start_)
        string_positions[key] = i
        string_number +=1
    file.close()
    return string_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)