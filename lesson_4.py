# Задание 1

a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))

area = a * b
perimeter = 2 * (a + b)

print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")


# Задание 2

number = int(input("Введите пятизначное число: "))

units = number % 10           # 5 (единицы)
tens = (number // 10) % 10    # 7 (десятки)
hundreds = (number // 100) % 10  # 2 (сотни)
thousands = (number // 1000) % 10  # 6 (тысячи)
ten_thousands = number // 10000  # 4 (десятки тысяч)

result = (tens ** units) * hundreds / (ten_thousands - thousands)

print(f"Результат: {result}")