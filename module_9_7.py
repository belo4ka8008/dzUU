#Задание: Декораторы в Python

def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        for i in range(2, total):
            if total % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return total
    return wrapper


@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total

result = sum_three(2, 3, 6)
print(result)