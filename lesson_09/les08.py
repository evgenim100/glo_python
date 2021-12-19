print('Введите n')
count = 0
n = int(input())
for a in range(1, n+1):
    while a != 0:
        digit = a % 10
        if digit == 5:
            count += 1
        a = a // 10
print('count', count)