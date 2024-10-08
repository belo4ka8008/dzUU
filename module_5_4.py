#class Example:
#    def __new__(cls, *args, **kwargs):
#        print(args)
#        print(kwargs)
#        return object.__new__(cls)
#    def __init__(self, first, second, third):
#        print(first)
#        print(second)
#        print(third)
#ex = Example('data', second=25, third=3.14)
# Задача "История строительства"

class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
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
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')
    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor
    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor
    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor
    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor
    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor
    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor
    def __add__(self, other):
        self.number_of_floor = self.number_of_floor + other
        return self
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        self.number_of_floor += other
        return self
    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


#доп задание
h4 = House ('Горьковский', 6)
print(House.houses_history)
h5 = House ('Жуковский', 17)
print(House.houses_history)

del h4
del h5

print(House.houses_history)