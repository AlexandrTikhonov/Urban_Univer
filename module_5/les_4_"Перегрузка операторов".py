class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()


    def say_info(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}")


    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')


    def __str__(self):
        return f'{self.name}'


    def __len__(self):
        return self.age


    def __lt__(self, other):
        return self.age < other.age


    def __gt__(self, other):
        return self.age > other.age


    def __eq__(self, other):
        return self.age == other.age


    def __bool__(self):
        return bool(self.age)


den = Human('Денис', 22)
max = Human('Макс', 25)

# if den:
#     den.say_info()

print(den == max)

print(den, max)
