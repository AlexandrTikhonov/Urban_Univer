import math

d = 5

def square(x):
    d = x ** 2
    def even(x):
        d = x * 2
        if d % 2 == 0:
            print("Четное")
        else:
            print("Нечетное")
    even(x)
    return d


b = square(2)
print(d)
print(b)