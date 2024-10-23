# def print_params(a, b, c):      # *args, **kwargs
#     print(a, b, c)

# --------------------------------------------------
# def print_params_1(*args):
#     print(args)
#     print(*args)
#
# print_params_1(1, 2, 3)


# --------------------------------------------------
# def print_params_2(*params):
#     print(params)
#
# print_params_2(1, 2, 3, 4, 5)

# ---------------------------------------------------
# def params_1(a, b, c):
#     print(a, b, c)
#
# list_ = [1, 2, 3]
# params_1(*list_)

# ---------------------------------------------------
# def params_2(a, b, c):
#     print(a, b, c)
#     print(c)
#
# list_1 = [1, 2]
# params_2(*list_1, 4)

# ------------------------------------------------------
# def params_3(a, b, c):
#     print(a, b, c)
#
# dict_1 = {'a' : 1, 'b' : 2, 'c' : 3}
# params_3(**dict_1)

# -----------------------------------------------------
# def params_4(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# dict_2 = {'a' : 1, 'b' : 2, 'c' : 3}
# params_4(**dict_2)

# --------------------------------------------------------
def params_5(a, b, c):
        print(a, b, c)

list_2 = [1, 2]
dict_3 = {'c' : 3}
params_5(*list_2, **dict_3)

# ---------------------------------------------------------

