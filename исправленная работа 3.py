m = int(input("������� ������������ ����� ������� ����� ��������� �����:"))
n = int(input("������� ���������� �������:"))
a = list(map(int, input("������� ��� ���������������:").split()))
a.sort()

i = 0
j = 0
boats = 0

while i < n:
    if a[i] + a[j+1] <= m and j <= n:
        j += 1
    else:
        boats += 1
        j = 0
    i += 1
    
boats += 1
if n //1.9 > boats:
    print(n//1.9)
else:
    print("���������� �����:", boats)
