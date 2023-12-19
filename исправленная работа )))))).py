
A = int(input("¬ведите число A: "))
B = int(input("¬ведите число B: "))

for num in range(A, B + 1):
    if num % 2 == 0:
        print(num, end=" ")

print()