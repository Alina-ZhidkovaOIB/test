
summa=int(input("����������� ����� ����������"))
maikl=int(input("������� �������� � ������-"))
ivan=int(input("������� �������� � �����-"))
if (maikl>=summa) and (ivan>=summa):
    print(2)
elif (maikl>=summa) and (ivan<=summa):
    print("Maikl")
elif (maikl<=summa) and (ivan>=summa):
    print("Ivan")
elif (maikl<=summa) and (ivan<=summa) and (maikl+ivan)>=summa):
    print(1)
elif (maikl<=summa) and (ivan<=summa) and (maikl+ivan)<=summa):
    print(0)

