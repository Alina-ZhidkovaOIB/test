
summa=int(input("Минимальная сумма инвестиций"))
maikl=int(input("Сколько долларов у Майкла-"))
ivan=int(input("Сколько долларов у Ивана-"))
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

