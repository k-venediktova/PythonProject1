best = 0
while True:
    s = int(input())
    if s == -1:
        break
    if s > best:
        best = s
print(best)