# Задание 1

s = input()
if s == s[::-1]:
    print("yes")
else:
    print("no")


# Задание 2

s = input()
result = []
prev_char = ''

for char in s:
    if char == ' ' and prev_char == ' ':
        continue
    result.append(char)
    prev_char = char

print(''.join(result))