
N=int(iput("Введите количесво элементов"))
spisok = list(map(int,input().split()))[:n]
e=set(spisok)
print(len(e))
