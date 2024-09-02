#Рекурсивное умножение цифр
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

#get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203)
# -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

#после добавления if и else код заработал. Без них - ошибка (бесконечная рекурсия?)

result = get_multiplied_digits(40203)
print(result)