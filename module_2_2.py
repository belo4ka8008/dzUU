first = input('Введите одно целое число: ')
second = input('Введите одно целое число: ')
third = input('Введите одно целое число: ')

if first == second and first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
#elif first!=second and fisrt!=third and second!=third:
else:
    print(0)