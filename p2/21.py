k = input()
l1 = k[0]
r1 = int(k[1])
l2 = k[3]
r2 = int(k[4])
# Переводим первую букву в число
if l1 == "a":
    x1 = 1
elif l1 == "b":
    x1 = 2
elif l1 == "c":
    x1 = 3
elif l1 == "d":
    x1 = 4
elif l1 == "e":
    x1 = 5
elif l1 == "f":
    x1 = 6
elif l1 == "g":
    x1 = 7
else:
    x1 = 8
# Переводим вторую букву в число
if l2 == "a":
    x2 = 1
elif l2 == "b":
    x2 = 2
elif l2 == "c":
    x2 = 3
elif l2 == "d":
    x2 = 4
elif l2 == "e":
    x2 = 5
elif l2 == "f":
    x2 = 6
elif l2 == "g":
    x2 = 7
else:
    x2 = 8
# Находим пройденное расстояние по горизонтали
if x1 > x2:
    x = x1 - x2
else:
    x = x2 - x1
# Находим пройденное расстояние по вертикали
if r1 > r2:
    y = r1 - r2
else:
    y = r2 - r1
# Конь всегда делает один шаг по одной оси и два шага по другой
if (x == 1 and y == 2) or (x == 2 and y == 1):
    print("верно")
else:
    print("ошибка")