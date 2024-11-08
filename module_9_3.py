#Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = ((len(x) - len(y)) for x, y in zip(first, second) if len(x) != len (y))

#во время составления сборок можно объединять и складывать списки!

second_result = (len(first[x]) == len(second[x]) for x in range(min(len(first),len(second))))

#х - счетчик слов начиная с позиции "0". Задаем количество позициий в списках с помощью range
#min - минимальная/самая первая позиция для перебора

print(list(first_result))
print(list(second_result))

