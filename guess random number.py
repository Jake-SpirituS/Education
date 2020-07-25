import random


def is_valid(a, b):
    if 1 <= a <= b:
        return True
    else:
        return False


print('Добро пожаловать в числовую угадайку')
print('Хотите изменить правую границу (сейчас она равна 10) ? Нажми Y - да, N - нет')
if input().upper() == 'Y':
    print('Введите число')
    n = int(input())
else:
    n = 10
x = random.randint(1, n)
count = 0

while True:
    print(f'Введите любое число от 1 до {n}')
    y = int(input())
    count += 1
    if is_valid(y, n) is False:
        print(f'А может быть все-таки введем целое число от 1 до {n}?')
    elif is_valid(y, n) is True:
        if y < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif y > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif y == x:
            print('Вы угадали, поздравляем!')
            print(f'Число попыток равно {count}')
            print("Сыграем еще разок? Нажми Y - да, N - нет")
            q = input()
            if q.upper() == 'Y':

                x = random.randint(1, 10)
                count = 0
                print('Новое число загадано')
            elif q.upper() == 'N':
                break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
