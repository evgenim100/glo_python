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
