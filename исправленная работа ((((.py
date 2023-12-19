x = float(input("Введите минимальную сумму инвестиций:"))a = float(input("Ведите сумму денег у Майкла:"))
b = float(input("Введите сумму денег у Ивана:"))if a >= x and b >= x:
    print(2)elif a >= x:
    print("Make")elif b >= x:
    print("Ivan")elif a + b >= x:
    print(1)else:
    print(0)