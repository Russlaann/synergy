# Задание 1
number = int(input("Введите целое число: "))


if number == 0:
    print("нулевое число")
else:
    if number > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    if number % 2 == 0:
        print(f"{sign} четное число")
    else:
        print(f"{sign} нечетное число")
        print("число не является четным")


# Задание 2
word = input("Введите слово из маленьких латинских букв: ").lower()

vowels = "aeiou"
consonants_count = 0
vowels_count = 0

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for letter in word:
    if letter in vowels:
        vowels_count += 1
        if letter == 'a':
            a_count += 1
        elif letter == 'e':
            e_count += 1
        elif letter == 'i':
            i_count += 1
        elif letter == 'o':
            o_count += 1
        elif letter == 'u':
            u_count += 1
    else:
        consonants_count += 1

print(f"Согласных букв: {consonants_count}")
print(f"Гласных букв: {vowels_count}")

print(f"a: {a_count if a_count > 0 else False}")
print(f"e: {e_count if e_count > 0 else False}")
print(f"i: {i_count if i_count > 0 else False}")
print(f"o: {o_count if o_count > 0 else False}")
print(f"u: {u_count if u_count > 0 else False}")


# Задание 3
X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Сколько долларов у Майкла: "))
B = int(input("Сколько долларов у Ивана: "))

can_mike = A >= X
can_ivan = B >= X

if can_mike and can_ivan:
    print(2)
elif can_mike:
    print("Mike")
elif can_ivan:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)