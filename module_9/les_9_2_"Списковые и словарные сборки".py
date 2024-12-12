### пример 1 - как выглядит объединение функций map и filter
#
# def by_3(x):
#     return x * 3
#
#
# def is_odd(x):
#     return x % 2
#
#
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(by_3, filter(is_odd, my_numbers))
# print(list(result))

### ---------------------

# list_comp_1 = [x*2 for x in my_numbers]
# print(list_comp_1)

### ----------------------
# пример 2 - списковая сборка
# аналог map

# result = [x*3 for x in my_numbers]
# print(result)
#
# list_comp_2 = [x*2 for x in my_numbers if x > 5]
# print(list_comp_2)

### ---------------------------
# пример 3 - списковая сборка с if
# аналог filter

# result = [x*3 for x in my_numbers if x % 2]
# print(result)
#
# list_comp_3 = [x*2 if x > 2 else x * 10 for x in my_numbers]
# print(list_comp_3)

### ----------------------------
# пример 4 - условия перед циклом (для того чтобы не отфильтровывать данные, а поменять операции над ними)

# my_num = ["A", 1, 4, "B", 5, "C", 2, 6]
# res = [x if type(x) == str else x * 5 for x in my_num]
# print(res)

# list_comp_4 = [x * y for x in my_numbers for y in my_num]
# print(list_comp_4)

### ------------------------------------
# пример 5 - можно делать вложенные списки

# last_number = [2, 7, 1, 8, 2, 8, 1, 8]
#
# result = [x * y for x in my_numbers for y in last_number]
# print(result)
#
# result = [x * y for x in my_numbers for y in last_number if x % 2]
# print(result)
#
# result = [x * y for x in my_numbers for y in last_number if x % 2 and y // 2]
# print(result)

### ------------------------------------
# пример 6 - можно создать на лету множества и словари

result = {x for x in my_numbers}
print(result)

result = {x: x ** 2 for x in my_numbers}
print(result)