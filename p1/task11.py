import math
r1 = int(input())
r2 = int(input())
b = max(r1, r2)
m = min(r1, r2)
s = math.pi * (b**2 - m**2)
print(s)