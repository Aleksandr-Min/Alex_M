doska = list(range(1, 10))

def greet():
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")


def igrovaya_doska():
    print("_____________")
    for a in range(3):
        print('|', doska[0 + a * 3], '|', doska[1 + a * 3], '|', doska[2 + a * 3], '|')
    print("_____________")


def vvod(hod_igroka):
    while True:
        value = input('Ваш ход ' + hod_igroka)
        if not (value in '123456789'):
            print('Неверный координат! Повторите ход.')
            continue
        value = int(value)
        if str(doska[value - 1]) in 'XO':
            print('Клетка занята')
            continue
        doska[value-1] = hod_igroka
        break

pobed_komb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),  (0, 4, 8), (2, 4, 6))

def proverka():
    for symb in pobed_komb:
        if (doska[symb[0]]) == (doska[symb[1]]) == (doska[symb[2]]):
            return True
    else:
        return False

def igra():
    c = 0
    while True:
        igrovaya_doska()
        if c % 2 == 0:
            vvod('X')
        else:
            vvod('O')
        if c > 3:
            pobeditel = proverka()
            if pobeditel:
                igrovaya_doska()
                print('Победа!')
                break
        c += 1
        if c > 8:
            igrovaya_doska()
            print('Ничья!')
            break




greet()
igra()
