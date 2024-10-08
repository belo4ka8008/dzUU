#Developer - не только разработчик

class House:
    def __init__(self, name, floor_number):
        self.name = name
        self.number_of_floors = floor_number
    def go_to(self, new_floor):
        if new_floor > 0:
            for i in range(1, new_floor+1):
                if 1 <= new_floor and new_floor <= self.number_of_floors:
                    print(i)
                elif new_floor<1:
                    print('Такого этажа не существует.')
                    break
                elif new_floor > self.number_of_floors:
                    print('Такого этажа не существует.')
                    break
        elif new_floor <=0:
            print('Такого этажа не существует.')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

#доп задание
h3 = House ('Горьковский', 6)
h4 = House ('Жуковский', 17)
h3.go_to(-1)
h4.go_to(0)