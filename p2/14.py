k = int(input())
g = k // (29 * 17)
k = k % (29 * 17)
s = k // 29
k = k % 29
if g > 0:
    print(g, "галлеонов")
if s > 0:
    print(s, "сиклей")
if k > 0:
    print(k, "кнатов")