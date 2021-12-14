print('Введите число');
n = int(input())
first = n % 10
second = n % 100 // 10
third = n % 1000 // 100
print('У числа', n, 'сумма последних трех цифр равна', first+second+third);