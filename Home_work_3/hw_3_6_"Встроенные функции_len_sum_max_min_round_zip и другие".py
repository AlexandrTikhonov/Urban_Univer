# int()   --> int(input())  - целое число
# float()                   - число с плавающей точкой
# bool()                    - логическое число (True, False)
# str()                     - строка
# list()                    - список
# tuple()                   - кортеж
# dict()                    - словарь
# set()                     - множество

# ------------------------------------------------------
salary = [2300, 1800.8555, 5000, 1234.5858, 7500.252524]
# print(salary, '- список зарплат')
# print(len(salary), '- количество получателей зарплаты')
# print(round(sum(salary), 2), '- сумма зарплат')
# print(round(sum(salary) / len(salary), 2), '- средняя зарплата')
# print(round(max(salary), 2), '- максимальная зарплата')
# print(round(min(salary), 2), '- минимальная зарплата')

# names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
# # zipped = zip(names, salary)
# # print(list(zipped))
# # print(dict(zipped))
#
# zipped = dict(zip(names, salary))
# print(zipped['Денис'])

# --------------------------------------------------------
a = [True, False, False]
a_1 = ['b', 'c', '5']
a_2 = [1, 0, 0]
a_3 = [1, 1, 1]
b = [1, 1, 1]

# print(any(a))
# print(all(a_1))
# print(dir(a_2))
# print(type(a_3))
# print(isinstance(a, str)) # --> print(type(a) == str)
# print(a_3 == b)
# print(id(a_3))
# print(id(b))
# print(a_3 is b)

c = b
c[0] = 2

print(c)
print(b)
print(id(c))
print(id(b))
print(c is b)

print(help(a))
print(help(print))

# ---------------------------------------