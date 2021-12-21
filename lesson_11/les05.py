string = input('Введите список: ')
numbers = string.split()
for n in numbers:
    if numbers.count(n) == 1:
        print(n, end=' ')