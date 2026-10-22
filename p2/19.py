# k кварталов можно отделить тогда, когда k нацело делится на n или на m и k меньше общей площади района
n, m = map(int, input().split("x"))
k = int(input())
if (k % n == 0 or k % m == 0) and k < n * m:
    print("успешно")
else:
    print("неосуществимо")