first = ['Strings', 'Student', 'Computer']
second = ['Стройка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))