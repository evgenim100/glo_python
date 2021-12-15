print('Введите номер кармана');
n = int(input())
if n == 0:
    print('Green');
elif (0 < n and n<= 10) or (19 <= n and  n <= 28):
    if n % 2 == 0:
        print('Black');
    else:
        print('Red');
elif (11 <= n and n <= 18) or (29 <= n and n <= 36):
    if n % 2 == 0:
        print('Red');
    else:
        print('Black');
else:
    print('Ошибка ввода');