print('Введите n')
n = int(input())
min = 9
max = 0
while n != 0:
    digit = n % 10
    if min > digit:
        min = digit
    if max < digit:
        max = digit
    n = n // 10
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)
