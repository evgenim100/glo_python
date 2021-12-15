print('Введите n')
n = int(input())
max = int(input())
min = max
for i in range(0, n-1):
    num = int(input())
    if max < num:
        max = num
    if min > num:
        min = num
print('Минимум равен', min)
print('Максимум равен', max)
