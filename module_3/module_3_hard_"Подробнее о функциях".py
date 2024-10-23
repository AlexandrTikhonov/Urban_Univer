data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_ = []
print(1, type([1, 2, 3]))
print(2, type({'a': 4, 'b': 5}))
print(3, type((6, {'cube': 7, 'drum': 8})))
print(4, type("Hello"))
print(5, type((), [{(2, 'Urban', ('Urban2', 35))}]))
print(6, type(data_structure))

# def calculate_structure_sum(*list_1, count=0, **dict_1):
#     for item in data_structure:
#         list_.append(*list_1.upper(), **dict_1)
#         return
#     return list_

# calculate_structure_sum(data_structure)
# print(list_)
#
