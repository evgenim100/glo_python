print('Введите a')
a = int(input())
count = 0
while a != 0:
    digit = a % 10
    if digit == 5:
        count += 1
    a //= 10
print(count)