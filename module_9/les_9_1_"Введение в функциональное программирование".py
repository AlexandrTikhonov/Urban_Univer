### пример 1 - почему функция это объект
#
# def get_russian_name():
#     print(['Ваня', 'Коля', 'Маша',])
#
#
# get_russian_name()
#
# print(type(get_russian_name))
# print(get_russian_name.__name__)
#
# my_func = get_russian_name
# print(my_func())
# print(my_func.__name__)

### --------------------
# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша', ]
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry', ]
#
# name_getters = [get_russian_names, get_british_names]
#
# for name_getter in name_getters:
#     print(name_getter())

### -------------------
# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res
#
#
# def multiplier(args):
#     res = 1
#     for number in args:
#         res *= number
#     return res
#
#
# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f'Получилось: {result}')
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# process_numbers(numbers=my_numbers, function=adder)
# process_numbers(numbers=my_numbers, function=multiplier)

### ----------------------------
######################### ФУНКЦИЯ map ######################
#
# def mul_by_2(x):
#     return x * 2
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = map(mul_by_2, my_numbers)
# print(result)
# print(list(result))

### -------------------------
######################## ФУНКЦИЯ filter #############################

def is_odd(x):
    return x % 2

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = filter(is_odd, my_numbers)
print(result)
print(list(result))