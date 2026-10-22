n, k, m = map(int, input().split())
if k > m:
    s = k - m
else:
    s = m - k
s1 = s - 1
s2 = n - s - 1
if s1 < s2:
    print(s1)
else:
    print(s2)