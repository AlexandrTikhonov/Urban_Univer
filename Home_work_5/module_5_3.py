class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = None


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.number_of_floors < self.new_floor or self.new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self.number_of_floors

    def __iadd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __add__
h_1 = h1 + 10  # без не большего исправления не получалось исправить ошибку
print(h1)
print(h1 == h2)

# __iadd__

h1 += 10
print(h1)

# __radd__
h_2 = 10 + h2  # без не большего исправления не получалось исправить ошибку
print(h2)