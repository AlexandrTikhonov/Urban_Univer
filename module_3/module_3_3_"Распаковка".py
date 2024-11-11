### 1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


### 2. Распаковка параметров:
values_list = [1, 'item', True]
values_dict = {'a': 1, 'b': 'буква', 'c': True}

## 3. Распаковка + отдельные параметры:
values_list_2 = [3, '5']

# print_params()
# print_params(9)
# print_params(1, 2)
# print_params(b=25)
# print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)