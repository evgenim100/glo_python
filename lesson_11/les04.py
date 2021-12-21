string = input('Введите строку: ')
numbers = string.split()
repeats = []
for n in numbers:
    repeats.append(numbers.count(n)-1)
print(int(sum(repeats)/2))