x = float(input("������� ����������� ����� ����������:"))a = float(input("������ ����� ����� � ������:"))
b = float(input("������� ����� ����� � �����:"))if a >= x and b >= x:
    print(2)elif a >= x:
    print("Make")elif b >= x:
    print("Ivan")elif a + b >= x:
    print(1)else:
    print(0)