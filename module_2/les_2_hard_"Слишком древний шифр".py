import random

num = random.randint(3, 20)


def find_code():
    print(num)
    for i in range(1, int(num / 2 + 1)):
        for j in range(2, 21):
            if num % (i + j) == 0 and i != j:
                print(i, j, end="", sep="")


find_code()
