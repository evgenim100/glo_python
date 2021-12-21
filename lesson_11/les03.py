string = input('Введите строку: ')
numbers = string.split('.')
count = 0
for n in numbers:
    if 0 <= int(n) <= 255:
        count += 1
if count == 4:
    print('YES')
else:
    print('NO')




