N = int(input("Введите число N: "))count_zeros = 0
for _ in range(N):    num = int(input("Введите целое число: "))
    if num == 0:        count_zeros += 1
print(f"Количество нулевых чисел: {count_zeros}")

X = int(input("Введите натуральное число X: "))count_divisors = 0
for i in range(1, X + 1):    if X % i == 0:
        count_divisors += 1print(f"Количество натуральных делителей числа {X}: {count_divisors}")

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
for num in range(A, B + 1):    if num % 2 == 0:
        print(num, end=" ")
