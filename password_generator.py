import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

count_p = int(input('Укажите количество паролей для генерации:\n'))
len_p = int(input('Укажите длину одного пароля:\n'))
dig_in = input('Включать ли цифры 0123456789? (y/n)\n')
if dig_in == 'y':
    chars += digits
ABC_in = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)\n')
if ABC_in == 'y':
    chars += uppercase_letters
abc_in = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)\n')
if abc_in == 'y':
    chars += lowercase_letters
sym_in = input('Включать ли символы !#$%&*+-=?@^_? (y/n)\n')
if sym_in == 'y':
    chars += punctuation
bad_sym_list = 'il1Lo0O'
bad_sym_in = input(f'Исключать ли неоднозначные символы {bad_sym_list}? (y/n)\n')
if bad_sym_in == 'y':
    for i in bad_sym_list:
        if i in chars:
            chars = chars.replace(i, '')


def generate_password(length, char):
    pas = ''
    for _ in range(length):
        pas += random.choice(char)
    return pas


for _ in range(count_p):
    try:
        print(generate_password(len_p, chars))
    except IndexError:
        print('Не из чего выбирать')
        break
