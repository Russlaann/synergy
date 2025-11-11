# Задание 1

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

for i in range(N-1, -1, -1):
    print(arr[i])


# Задание 2

N = int(input())
arr = list(map(int, input().split()))

if N > 0:
    last = arr[-1]
    for i in range(N-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last

print(" ".join(map(str, arr)))


# Задание 3

m = int(input())
n = int(input())
weights = []
for i in range(n):
    weight = int(input())
    weights.append(weight)

weights.sort()
left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1

print(boats)