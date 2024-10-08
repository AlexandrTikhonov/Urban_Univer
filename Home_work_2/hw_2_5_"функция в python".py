# def say_hello():
#     print("Hello")
#
# say_hello()

# def say_hello(name):                                  # принимающая функция
#     print("Hello", name)
#
# say_hello('Denis')
# say_hello('Max')
# say_hello('Anton')
#

# import random
# def lottery():                                        # возвращающая функция
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win
#
# win = lottery()
# print(win)

# import random
# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win_1 = random.choice(tickets)
#     tickets.remove(win_1)
#     win_2 = random.choice(tickets)
#     print(mon, thue)
#     return win_1, win_2
#
# win_1, win_2 = lottery('mon', 'thue')
# print(win_1, win_2)

# import random
# def lottery(*args, **kwargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win_1 = random.choice(tickets)
#     tickets.remove(win_1)
#     win_2 = random.choice(tickets)
#     print(*args)
#     return win_1, win_2
#
# win_1, win_2 = lottery(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(win_1, win_2)
#
# def test(a = 2, b = True):
#     print(a, b)
#
# test(False, 'ok')
# test([1, 2])
# test(*[1, 2])
# test(**[1, 2])


def get_matrix(n, m, value):
   matrix = []
   for i in range(n):
       matrix.append([])
       #print(i, matrix)
       for j in range(m):
           matrix[i].append(value)
           #print(matrix, end= '\n')
   return matrix



print(get_matrix(3, 4, 8))


