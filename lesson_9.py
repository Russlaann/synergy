# Задание 1

N = int(input())
numbers = list(map(int, input().split()))

unique_numbers = set(numbers)
print(len(unique_numbers))


# Задание 2

n = int(input())
list1 = []
for i in range(n):
    num = int(input())
    list1.append(num)

m = int(input())
list2 = []
for i in range(m):
    num = int(input())
    list2.append(num)

set1 = set(list1)
set2 = set(list2)
common = set1 & set2
print(len(common))


# Задание 3

numbers = list(map(int, input().split()))
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)