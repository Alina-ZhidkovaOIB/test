N = int(input("������� ����� N: "))count_zeros = 0
for _ in range(N):    num = int(input("������� ����� �����: "))
    if num == 0:        count_zeros += 1
print(f"���������� ������� �����: {count_zeros}")

X = int(input("������� ����������� ����� X: "))count_divisors = 0
for i in range(1, X + 1):    if X % i == 0:
        count_divisors += 1print(f"���������� ����������� ��������� ����� {X}: {count_divisors}")

A = int(input("������� ����� ����� A: "))
B = int(input("������� ����� ����� B: "))
for num in range(A, B + 1):    if num % 2 == 0:
        print(num, end=" ")
