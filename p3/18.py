x = int(input())
c = 0
a = 1
while a * a < x:
    b = a
    while a * a + b * b <= x:
        if a * a + b * b == x:
            c += 1
        b += 1
    a += 1
print(c)