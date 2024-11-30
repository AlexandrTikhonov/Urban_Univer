def add_everything_up(a: int | float | str, b: int | float | str):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(5, 9))

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
