#"За честь и отвагу!"

import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
    def run(self):
        enemy_power = 100
        print(f'{self.name}, на нас напали!')
        n = 0
        while enemy_power > 0:
            alive = enemy_power - self.power
            sleep(1)
            n += 1
            print(f'{self.name} сражается {n} день(дня), осталось {alive} воинов.')
            enemy_power = alive
            continue
        if enemy_power == 0:
            print(f'{self.name} одержал победу спустя {n} дней (дня)!')
        return

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')