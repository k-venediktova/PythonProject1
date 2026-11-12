t = float(input())
c = 0
while t != 0:
    k = float(input())
    if k == 0:
        break
    if k < t:
        c += 1
    t = k
print(c)