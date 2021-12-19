print('Введите a')
a = int(input())
count = 0
while a % 2 == 0:
    a = a // 2
    count += 1
print(count)
