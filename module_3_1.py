calls = 0


def count_calls():
    global calls #не понимаю к чему обращаяется calls. calls = 0 это счетчик,
    #сalls == count_calls?
    #решил методом подбора
    calls +=1


def string_info(string):
    count_calls()
    return len(string),string.upper(),string.lower()

def is_contains(string, list_to_search):
    for i in range(len(list_to_search)): #чтобы проверить совпадение: перебрать каждый элемент
                                        # + привести к одному регистру. Как упростить?
        if str(list_to_search[i]).lower() == string.lower():#очень долго подбирал
            result = True #retunr ставить только в конце функции. Создать переменную!
        else:
            result = False
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)