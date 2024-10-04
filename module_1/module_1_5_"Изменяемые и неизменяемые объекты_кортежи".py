immutable_var = (1, 2, 3, "test", True, 5.0)

print(immutable_var)

# immutable_var[0] = 200   # выпадает ошибка, прерывающую программу

mutable_list = [1, 2, 3, "test", True, 5.0]

print(mutable_list + ["Modified"])