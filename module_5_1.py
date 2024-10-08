#Developer - не только разработчик

class House:
    def __init__(self, name, floor_number):
        self.name = name
        self.number_of_floors = floor_number
    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if 1 <= new_floor and new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует.')
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)