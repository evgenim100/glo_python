print('Введите a')
a = int(input())
sum = 0
number = a
while a != 0:
    sum += a % 10
    a //= 10
if number % sum == 0:
    print('YES')
else:
    print('NO')
