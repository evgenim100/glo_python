print('Введте email')
m = input()
if '@' in m and '.' in m:
    print('Корректный')
else:
    print('Некорректный')