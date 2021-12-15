print('Введите одно шестизначное целое число - номер билета');
n = int(input())
first = n // 100000
second = n % 100000 // 10000
third = n % 10000 // 1000
forth = n % 1000 // 100
fifth = n % 100 // 10
sixth = n % 10
# print(first, second, third, forth, fifth, sixth);
if first + second + third == forth + fifth + sixth:
    print('Билет', n, 'счастливый');
else:
    print('Билет', n, 'не счастливый');