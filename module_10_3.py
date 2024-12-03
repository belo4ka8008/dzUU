#"Банковские операции"

#смысл: замок изначально открыт, снимаем деньги до тех пор пока они неч кончатся
#начинаем закидывать деньги пока они не станут больше 500 (чтобы точно можно было что то снять)
#снимаем замок тк есть что снимать

import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        n = 0
        while n <= 100:
            money_in = randint(50, 500)
            self.balance += money_in
            n += 1
            print(f'Пополнение: {money_in}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        n = 0
        while n <= 100:
            money_out = randint(50, 500)
            print(f'Запрос на: {money_out}')
            if money_out <= self.balance:
                self.balance -= money_out
                n += 1
                print(f'Снятие: {money_out}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен. Недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()
th1.join()
th2.join()
