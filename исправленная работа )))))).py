
A = int(input("������� ����� A: "))
B = int(input("������� ����� B: "))

for num in range(A, B + 1):
    if num % 2 == 0:
        print(num, end=" ")

print()