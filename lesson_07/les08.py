print('Введите n')
n = int(input())
max = int(input())
min = int(input())
if max < min:
   min2 = min
   min = max
   max = min2
for i in range(0, n-2):
    num = int(input())
    if max < num:
        max = num
    if min > num:
        min = num
print('Минимум равен', min)
print('Максимум равен', max)