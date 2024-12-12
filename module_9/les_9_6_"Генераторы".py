# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
#
# obj = (func_generator(12))
# print(obj)
#
# for i in obj:
#     print(i, end=(', '))

### -------------
# def fibonacci_v1(n):
#     res = []
#     a, b = 0, 1
#     for _ in range(n):
#         res.append(a)
#         a, b = b, a + b
#     return res
#
# def fibonacci_v2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# fib_1 = fibonacci_v1(n=10)
# print(fib_1)
#
# for value in fib_1:
#     print(value, end=', ')
#
# fib_2 = fibonacci_v2(n=10)
# print(fib_2)
#
# for value in fib_2:
#     print(value, end=', ')

### -------------------------
# def fibonacci_v3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for value in fibonacci_v3():
#     print(value)
#     if value > 10 ** 6:
#         break

### --------------------------
import time                       # в данном задании будет ошибка потому что у нас нет файла "large_file.txt"

start = time.time()

def read_large_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    print(line)

fin = time.time()

print((fin -strart) * 1000)