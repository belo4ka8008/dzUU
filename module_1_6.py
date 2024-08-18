#словарь
my_dict = {'Alena' : 1999,'Denis' : 1997,'Sasha': 1977}
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Lena'))
my_dict.update({'Marina':1964,'Alex':1989})
print(my_dict)
print(my_dict.pop('Denis'))
print(my_dict)

#множество
my_set = {1,2,3,1,2,3, 'Rodion', 55.0167}
print(my_set)
my_set.remove(2)
my_set.add(5)
print(my_set)