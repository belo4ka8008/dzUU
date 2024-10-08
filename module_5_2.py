#Магические здания

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
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол - во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
