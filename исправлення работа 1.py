a = []
n = int(input("������� ���������� ��������:"))
for i in range(n):
    a.append(int(input("������� ��������: ")))
a.reverse()
print(*a)
