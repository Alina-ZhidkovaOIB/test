
a = int(input("������� ����� a."))
b = int(input("������� ����� b."))

if a <= b:
    for num in range(a, b + 1):
        if num % 2 == 0:
          print(num,end='')
else:
    print("����� a ������ ���� ������ ��� ����� �����  b.")

