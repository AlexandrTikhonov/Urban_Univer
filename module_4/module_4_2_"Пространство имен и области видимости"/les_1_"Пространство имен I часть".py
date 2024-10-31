import math

a = 5

def square(x):
    a = x ** 2
    print(locals())
    return a


print(a)               # --> 5
# print(math.sqrt(a))    # --> 2.23606797749979
# print(globals())

b = square(2)

print(a)
print(b)
print(a)