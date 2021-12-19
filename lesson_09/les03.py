print('Введите a')
count = 0
a = int(input())
while a != 0:
    digit = a % 10
    if digit == 1:
        count += 1
    a = a // 10
if count > 0:
    print('YES')
else:
    print('NO')
