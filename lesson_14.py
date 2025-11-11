# Задание 1

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list(lst):
    if len(lst) > 0:
        print(lst[0])
        print_list(lst[1:])
    else:
        print("Конец списка")

print_list(my_list)