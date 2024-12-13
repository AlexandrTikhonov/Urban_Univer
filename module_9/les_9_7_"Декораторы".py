### ---- пример 1 - создания простого декоратора ---------

# def null_decorator(func):
#     return func
#
#
# def greet():
#     return 'Hello!'
#
#
# greet = null_decorator(greet)
#
# print(greet())

### ---- пример 2 - можно использовать синтаксис Python @ для декорирования функции за один шаг -----

# def null_decorator(func):
#     return func
#
#
# @null_decorator
# def greet():
#     return 'Hello!'
#
# print(greet())

### ---- пример 3 - почему нужно внутри декоратора определить еще одну функцию -----

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


# @uppercase                      # если работать без синтаксиса python, можно вызывать просто функцию greet и задекорированную
# def greet():
#     return 'Hello!'
#
# print(greet())

#
# def greet():
#      return 'Hello!'
#
# greet_dec = uppercase(greet)
#
# print(greet())
# print(greet_dec())

### ---- пример 4  ------

import time
import sys

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate

@time_track
def digits(*args):
    total = 1
    for num in args:
        total *= num ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)