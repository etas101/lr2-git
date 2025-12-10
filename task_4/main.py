import math
# Вводим числа
x = float(input("Введите число x: "))
y = float(input("Введите число y: "))
z = float(input("Введите число z: "))

# Вычисляем косинусы
cos_x = math.cos(x)
cos_y = math.cos(y)
print(f"Косинус x = {cos_x}")
print(f"Косинус y = {cos_y}")

# Разница между косинусами
raznica = abs(cos_x - cos_y)
print(f"Разница между косинусами = {raznica}")

# Вычисляем синус y
sin_y = math.sin(y)
print(f"Синус y = {sin_y}")

# Степень для первой части
stepen = 1 + 2 * (sin_y ** 2)
print(f"Степень = {stepen}")

# Первая часть формулы
chast1 = raznica ** stepen
print(f"Первая часть = {chast1}")

# Вторая часть формулы
chast2 = 1 + z + (z*z)/2 + (z*z*z)/3 + (z*z*z*z)/4
print(f"Вторая часть = {chast2}")

# Результат
w = chast1 * chast2

print()
print("=" * 30)
print(f"ОТВЕТ: w = {w}")
print("=" * 30)