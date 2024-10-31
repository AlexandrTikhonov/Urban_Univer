class Human:
    def __init__(self, name):
        self.name = name


den = Human('Денис')
max = Human('Макс')

print(den == max)  # --> False
print(den is max)  # --> False
print(id(den), id(max))  # --> 135636965129344 135636965129200
