list_a = input('Введмите список а:').split(' ')
list_b = input('Введмите список b:').split(' ')

def find_max(list):
    max = int(list[0])
    for i in list:
        if max < int(i):
            max = int(i)
    return max

print(find_max(list_a)*find_max(list_b))