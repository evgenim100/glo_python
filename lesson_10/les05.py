print('Введите первый символ')
a = input()
print('Введите второй символ')
b = input()
for i in range(min(ord(a), ord(b)), max(ord(a), ord(b))+1):
    print(chr(i), end=' ')