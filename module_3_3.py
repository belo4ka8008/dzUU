def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()

# Функция с параметрами по умолчанию

print_params(b = 25)
print_params(c = [1, 2, 3])

# Распаковка параметров

values_list = ['строчка', True, 224]
values_dict = {'a': 'строчечка' , 'b': False, 'c': 25467}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отделные параметры

values_list_2 = ('тире', 678)
print_params(*values_list_2, 42)