a = []
n = int(input("¬ведите количество значений:"))
for i in range(n):
    a.append(int(input("¬ведите значение: ")))
a.reverse()
print(*a)
