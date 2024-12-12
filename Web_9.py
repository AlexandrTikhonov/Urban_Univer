# def get_rus_names():
#     print(['Ваня', 'Коля', 'Маша'])  # --> ['Ваня', 'Коля', 'Маша']
#
# get_rus_names()
#
# print(type(get_rus_names))      # --> <class 'function'>
#
# print(get_rus_names.__name__)   # --> get_rus_names
#
# my_func = get_rus_names        # --> ['Ваня', 'Коля', 'Маша']
# print(my_func())               # --> None
#
# print(my_func.__name__)        # --> get_rus_names
#
# ### -------------------
# def get_rus_names():
#     return ['Ваня', 'Коля', 'Маша']
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry']
#
# # print(get_rus_names(), get_british_names())
#
# list_ = [get_rus_names, get_british_names]
# for i in list_:
#     print(i(), end='')               # --> ['Ваня', 'Коля', 'Маша']['Oliver', 'Jack', 'Harry']

### ---------------------
# def adder(args):
#     res = 0
#     for num in args:
#         res += num
#     return res
#
# def mult(args):
#     res = 1
#     for num in args:
#         res *= num
#     return res
#
# def process(numbers, function):
#     res = function(numbers)
#     print(f'Получилось: {res}')
#
# my_num = [3, 1, 4, 5, 6, 77]
#
# process(my_num, adder)  # --> Получилось: 96
# process(my_num, mult)   # --> Получилось: 27720

### -----------------------
# list_ = ['Kirill', 'Ivan', 'Max']
# num = [[1, 2, 3, 4], [5, 2, 3, 3], [5, 4, 5, 5]]
# num_avg = []
#
# for i in num:
#     num_avg.append(sum(i) / len(i))
#
# print(dict(zip(list_, num_avg)))  # --> {'Kirill': 2.5, 'Ivan': 3.25, 'Max': 4.75}

### -------------------------
# def multy_2(x):
#     return x * 2
#
# my_num = [3, 2, 3, 1, 4, 5, 10]
#
# res = map(multy_2, my_num)
# print(res)                         # --> <map object at 0x75355e103cd0>
# print(list(res))                   # --> [6, 4, 6, 2, 8, 10, 20]
#
# def is_odd(x):
#     return x % 2
#
# res = filter(is_odd, my_num)
# print(list(res))                 # --> [3, 3, 1, 5]

### --------------------------------
# """                                 lambda                 """
# def func(x, y):
#     return x + y
#
# my_func = func(1, 2)
# print(my_func)                                   # --> 3
#
# my_func = lambda x, y: x + y
# print(my_func(3, 2))                       # --> 5
#
# print((lambda x, y: x + y)(3, 5))          # --> 8

### ----------------------------
# def is_odd(x):
#     return x % 2
#
# def is_mult(x):
#     return x *3
#
# my_num = [1, 2, 3, 4, 5, 6, 7]
#
# res = map(is_mult, filter(is_odd, my_num))
# print(list(res))                                # --> [3, 9, 15, 21]

### ---------------------------
# my_num = [1, 2, 3, 4, 5, 6, 7]
#
# res = [x * 3 for x in my_num]
# print(res)
#
# res_1 = [x * 3 for x in my_num if x % 2]  # добавляем условие для фильтрации нечетных чисел
# print(res_1)

### ----------------------------
# my_num_1 = [3, 1, 'aa', 4, 5, 'str1', 6, 7, 8, 10]
# res_2 = [x if type(x) == str else x * 5 for x in my_num_1]
# print(res_2)

### ---------------------
# my_num_1 = [3, 1, 'aa', 4, 5, 'str1', 6, 7, True , False, [1, 2, 3]]
# my_num_2 = [2, 3, 4]
#
# res_3 = [x if type(x) == str else x * y for x in my_num_1 for y in my_num_2]
# print(res_3)

### --------------------------------
# list_ = [1, 2, 3, 'str', False, True]
#
# res = [x * 5 for x in list_ if isinstance(x, (int, float))]  # прописано условие при котором строки не будут выводится
# print(res)

### ---------------------------
# def null_(func):
#     return func
#
# def greet():
#     return 'Hello'
#
# greet = null_(greet)
# print(greet())

### -----------------------          декораторы
# def upper_str(func):
#     def wrapper():
#         orig = func()
#         up_ = orig.upper()
#         return up_
#     return wrapper
#
# @upper_str
# def greet():
#     return 'Hello'
#
#
# print(greet())