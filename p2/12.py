q = int(input())
n = q % 10
if 11 <= q <= 14:
    print(q, "попугаев")
elif n == 1:
    print(q, "попугай")
elif 2 <= n <= 4:
    print(q, "попугая")
else:
    print(q, "попугаев")