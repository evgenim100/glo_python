print('Введите n')
sum = 0
n = int(input())
sqr_int = 10
while sqr_int > 9:
    while n != 0:
        digit = n % 10
        sum += digit
        n = n // 10
    sqr_int = sum
    n = sqr_int
    sum = 0
print('Цифровой корень', sqr_int)