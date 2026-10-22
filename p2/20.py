k = input()
l = k[0]
r = int(k[1])
if l == "a":
    n = 1
elif l == "b":
    n = 2
elif l == "c":
    n = 3
elif l == "d":
    n = 4
elif l == "e":
    n = 5
elif l == "f":
    n = 6
elif l == "g":
    n = 7
else:
    n = 8
# На шахматной доске клетка черная, если сумма координат четная
if (n + r) % 2 == 0:
    print("черный")
else:
    print("белый")