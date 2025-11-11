# Задание 1

N = int(input("Введите количество чисел: "))
count_zero = 0

for i in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        count_zero += 1

print(count_zero)


# Задание 2

X = int(input("Введите натуральное число: "))
count = 0

for i in range(1, X + 1):
    if X % i == 0:
        count += 1

print(count)


# Задание 3

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

result = []
for num in range(A, B + 1):
    if num % 2 == 0:
        result.append(str(num))

print(" ".join(result))