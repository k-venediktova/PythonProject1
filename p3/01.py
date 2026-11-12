c = 0
for i in range(100, 1000):
    if i % 17 == 0:
        print(i, end=" ")
        c += 1
print()
print(c)