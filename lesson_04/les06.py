print('Введите целое четырехзначное число');
n = int(input())
first = n // 1000
second = n % 1000 // 100
third = n % 100 // 10
forth = n % 10
print('У числа', n, 'максимальная цифра равна', max(first, second, third, forth));