num_a = int(input('Введмите а:'))
num_b = int(input('Введмите b:'))

def rank(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count

print(rank(num_a)*rank(num_b))