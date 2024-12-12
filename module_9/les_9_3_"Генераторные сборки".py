my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# result = (x ** 2 for x in my_numbers)
# print(result)
#
# for elem in result:
#     print(elem)
#
# print('Еще разок')
#
# for elem in result:
#     print(elem)

### --------------------------
# import time
#
# start_time = time.time()
#
# result = [x ** 3000 for x in my_numbers]
# print(result)
#
# for i in result:
#     print(i)
#
# finish_time = time.time()
# print(f'время в миллисекундах: {(finish_time-start_time)*1000}')

### ---------------------------
# import time
#
# start_time = time.time()
#
# result = (x ** 300 for x in my_numbers)
# print(result)
#
# for i in result:
#     print(i)
#
# finish_time = time.time()
# print(f'время в миллисекундах: {(finish_time-start_time)*1000}')

### ---------------------------------
last_number = [5, 2, 9, 1, 2, 9, 4, 7]

ran = range(10, 30)
zp = zip(my_numbers, last_number)
mp = map(str, last_number)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))