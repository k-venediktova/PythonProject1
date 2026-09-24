X, Y, N = map(int, input().split())
a = (100*X + Y) * N
r = a//100
k = a%100
print(r, "руб.", k, "коп.")