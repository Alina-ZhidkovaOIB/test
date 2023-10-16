
a = int(input("¬ведите число a."))
b = int(input("¬ведите число b."))

if a <= b:
    for num in range(a, b + 1):
        if num % 2 == 0:
          print(num,end='')
else:
    print("„исло a должно быть меньше или равен числу  b.")

