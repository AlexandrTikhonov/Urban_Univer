# # пример 1 - ошибка летит по стеку вызовов функций
#
# def f1(number):
#     return 10 / number
#
#
# def f2():
#     print('Какой хороший день')
#     result_f1 = f1(0)
#     return result_f1
#
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так - {exc}, но мы устояли')

### ----------------------------
# # пример 2
#
# def f1(number):
#     return 10 / number
#
#
# def f2():
#     print('Какой хороший день')
#     summ = 0
#     for i in range(-2, 2):
#         summ += f1(i)
#     return
#
#
# try:
#     total = f2()
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так - {exc}, но мы устояли')

###----------------------
# # пример 3
#
# def f1(number):
#     return 10 / number
#
# def f2():
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(f'внутри f1 что-то пошло не так: {exc}, но программа жива, мы молодцы')
#     return summ / 1    # если поменять на другой return, то получим другое решение return summ / 0
#
#
# try:
#     total = f2()
#     print(f'вот ваш результат функции: {total}')
# except ZeroDivisionError as exc:
#     print(f'внутри f2 что-то пошло не так: {exc}, но мы устояли')

### --------------------------------
# пример 4

def f1(number):
    return total / number


def f2():
    try:
        result_f1 = f1(0)
        print(result_f1)
    except ZeroDivisionError as exc:
        print(f'внутри f1 что-то пошло не так: {exc}, но мы устояли')
    return result_f1 / 0


try:
    f2()
except NameError as exc:    # except ZeroDivisionError as exc:
    print(f'внутри f2 что-то пошло не так: {exc}, но мы устояли')