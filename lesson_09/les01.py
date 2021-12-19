print('Введите целые числа')
n = int(input())
while n <= 100:
    if n < 10:
        n = int(input())
    else:
        print(n)
        n = int(input())
