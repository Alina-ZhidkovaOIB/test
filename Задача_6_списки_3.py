
from re import I


m,n,c=int(input()), int(input()), 0
t=sorted([int(input()) for _ in range(n)], reverse = True)
if t[0]>m:
    print("������ �� ����� �������")
    exit()
while len(t):
    c += 1
    k = m - t.pop(0)
    for i in range(len(t)):
        if t[i]<=k:
            t.pop(I)
            break
