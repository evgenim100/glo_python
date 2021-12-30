
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


print('Добро пожаловать в игру "Угадай число"')


cnt = 0
while True:
    print('Введите правую границу диапазона:')
    right_border = input()
    right_border = valid_secret(right_border)
    secret_number = secret(right_border)
    cnt = 0
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
            break
    print('Введите "+", если хотите сыграть еще раз, если не хотите - введите "-"')
    answer = input()
    if answer == '+':
        continue
    else:
        break