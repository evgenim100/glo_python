from random import randint

def is_answer(string):
    while True:
        if string == 'Да' or string == 'Нет':
            break
        else:
            string = input('Введите "Да" или "Нет"')
            continue
    return string

def is_digit(digit):
    while True:
        if digit.isdigit():
            digit = int(digit)
            break
        else:
            print('Введите число или цифру')
            digit = input()
            continue
    return digit

def ask_question(question):
    print(question, 'Введите "Да" или "Нет"')
    answer = input()
    answer = is_answer(answer)
    if answer == 'Да':
        return True
    else:
        return False



def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = randint(0, len(chars)-1)
        password += chars[random_index]
    return password


while True:
    print('Привет, Я генератор паролей, я задам немколько вопросв и сгенерирую пароль.')
    print('Сколько паролей вы хотите сгенерировать?')
    ammount = input()
    ammount = is_digit(ammount)
    print('Введите длину пароля')
    length = input()
    length = is_digit(length)

    digits_enabled = ask_question('Включать ли цифры?')
    latin_lowercase_enabled = ask_question(
        'Включать ли строчные латинские буквы?')
    latin_uppercase_enabled = ask_question(
        'Включать ли заглавные латинские буквы')
    russian_lowercase_enabled = ask_question(
        'Включать ли строчные русские буквы?')
    russian_uppercase_enabled = ask_question(
        'Включать ли заглавные русские буквы?')
    punctuation_enabled = ask_question('Включать ли специальные символы?')
    enabled_chars = ''
    digits = '0123456789'
    latin_lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
    latin_uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    russian_lowercase_letters = 'йцукенгшщзфывапролдячсмить'
    russian_uppercase_letters = 'ЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬ'
    punctuation = '!@#$%^&*()_-+=:;",.'

    if digits_enabled:
        enabled_chars += digits
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase_letters
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase_letters
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase_letters
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase_letters
    if punctuation_enabled:
        enabled_chars += punctuation
    for i in range(ammount):
        password = generate_password(length, enabled_chars)
        print(password)
    print('Сгенерировать ещё рдин пароль?')
    answer = input()
    answer = is_answer(answer)
    if answer == 'Да':
        continue
    else:
        break
