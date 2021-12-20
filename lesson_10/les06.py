print('Введите строку')
s = input()
new = '';
for i in s:
    if i.isdigit():
        new = new + i
print(new)