print('Введите целое трехзначное положительное число');
n = int(input())
first = n // 100
second = n % 100 // 10
third = n % 10
print('Cумма цифр числа', n, 'равна', first+second+third);