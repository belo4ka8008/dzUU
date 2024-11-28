#Задача "Потоковая запись в файлы":
from threading import Thread
from time import sleep
from datetime import datetime

# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding = 'utf-8')
    for i in range(word_count+1):
        file.write(f'Какое - то слово № {i}\n')
    file.close()
    sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')

time_start_1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_1 = datetime.now()

print(f'\nВремя выполнения потока: {time_end_1 - time_start_1}\n')

t_5 = Thread(target = write_words, args= (10, 'example5.txt'))
t_6 = Thread(target = write_words, args = (30, 'example6.txt'))
t_7 = Thread(target = write_words, args = (200, 'example7.txt'))
t_8 = Thread(target = write_words, args = (100, 'example8.txt'))

time_start_2 = datetime.now()

t_5.start()
t_5.join()

t_6.start()
t_6.join()

t_7.start()
t_7.join()

t_8.start()
t_8.join()

time_end_2 = datetime.now()

print(f'\nВремя выполнения потока: {time_end_2 - time_start_2}\n')