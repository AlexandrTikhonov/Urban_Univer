numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count = 0
Primes = []
Not_Primes = []

for num in numbers[1:]:
    count = 0
    for j in range(2, len(numbers)):
        if num % j == 0:
            count += 1
            if j == num:
                break
    if count == 1:
        Primes.append(num)
    else:
        Not_Primes.append(num)

print(Primes)
print(Not_Primes)