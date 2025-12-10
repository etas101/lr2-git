import math
# Ввод сторон
a = float(input("Основа 1 (a): "))
b = float(input("Основа 2 (b): "))
c = float(input("Боковая сторона 1 (c): "))
d = float(input("Боковая сторона 2 (d): "))

# Вычисление
p = (a + b + c + d) / 2
pod_kornem = (p - a) * (p - b) * (p - a - c) * (p - a - d)

if a == b:
    print("Ошибка! Основы должны быть разными!")
elif pod_kornem < 0:
    print("Ошибка! Неправильные стороны трапеции!")
else:
    S = ((a + b) / abs(a - b)) * math.sqrt(pod_kornem)
    print(f"Площадь трапеции: {S}")