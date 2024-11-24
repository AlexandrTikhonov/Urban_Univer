data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# print(type([1, 2, 3]))
# print(type({'a': 4, 'b': 5}))
# print(type((6, {'cube': 7, 'drum': 8})))
# print(type("Hello"))
# print(type((), [{(2, 'Urban', ('Urban2', 35))}])
# print(type(data_structure))

lst = []

def calculate_structure_sum(struc):
    res = 0

    if isinstance(struc, (float, int)):
        return struc
    elif isinstance(struc, str):
        return len(struc)


    for item in struc:
        if isinstance(item, (float, int)):
            res += item
        elif isinstance(item, str):
            res += len(item)
        elif isinstance(item, (tuple, set, list)):
            res += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                res += calculate_structure_sum(key)
                res += calculate_structure_sum(value)
    return res





res =calculate_structure_sum(data_structure)
print(res)


