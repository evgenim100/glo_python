import random


def is_valid(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1 and user_number <= 100:
            return True
        else:
            return False
    else:
        return False


def valid_secret(right_border):
    while True:
        if right_border.isdigit():
            right_border = int(right_border)
            break
        else:
            print('Введите число или цифру')
            right_border = input()
            continue
    return right_border


def secret(right_border):
    secret_number = random.randint(1, right_border)
    return secret_number


def make_store(right_border):
    store = []
    num = 0
    for i in range(1, right_border):
        store.append(num)
        num += 1
    return store


def calc_attempts(value):
    store = []
    store = make_store(right_border)
    mid = len(store) // 2
    low = 0
    high = len(store) - 1
    cnt_attempts = 0
    while store[mid] != value and low <= high:
        if value > store[mid]:
            low = mid + 1
            cnt_attempts += 1
        else:
            high = mid - 1
            cnt_attempts += 1
        mid = (low + high) // 2

    return cnt_attempts


print('Добро пожаловать в игру "Угадай число"')


while True:
    print('Введите правую границу диапазона:')
    right_border = input()
    right_border = valid_secret(right_border)
    secret_number = secret(right_border)
    cnt = 0
    cnt_attempts = calc_attempts(secret_number)
    while True:
        print('Введите число от 1 до', right_border)
        user_input = input()
        if not is_valid(user_input):
            continue
        user_number = int(user_input)

        if secret_number > user_number:
            print('Загаданное чилсо больше введенного')
            cnt += 1
        elif secret_number < user_number:
            print('Загаданное чилсо меньше введенного')
            cnt += 1
        else:

            print('Победа')
            print('Колчиество попыток:', cnt)
            print('Рекомендованное количество попыток:', cnt_attempts)
            cnt = 0
            break
    print('Введите "+", если хотите сыграть еще раз, если не хотите - введите "-"')
    answer = input()
    if answer == '+':
        continue
    else:
        break
