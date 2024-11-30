# try:
#     i = 0
#     print(10/i)
#     print('сделано')
# except ZeroDivisionError:
#     print("на ноль делить нельзя")

###-------------------------
print('------Какой хороший день, предлагаю научиться работать с исключениями')
i = int(input('Введите число: '))

try:
    result = 10 * (1/i)
except ZeroDivisionError as exc_1:
    print('Нельзя делить на ноль', exc_1)
else:
    print('Ура, мы не делим на ноль')
finally:
    print('файнали, мы заканчиваем урок :)')