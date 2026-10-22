k, a, s = map(int, input().split())
if k >= a and k >= s:
    r = k
elif a >= k and a >= s:
    r = a
else:
    r = s
print(r)