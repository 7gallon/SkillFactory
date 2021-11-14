def hod(sign):
    correct_value = False
    while not correct_value:
        coll = input("Введите значение по вертикали (1 - 3): ")
        row = input("Введите значение по горизонтали (1 - 3): ")
        try:
            coll = int(coll) - 1
            row = int(row) - 1
        except:
            print('Недопустимое значение, вы ввели не число')
            continue
        if (coll not in range(0, 3)) or (row not in range(0, 3)):
            print('Недопустимое значение, введите значение от 1 до 3')
            continue
        elif Field[coll][row] in 'xo':
            print('Клетка занята!')
        else:
            Field[coll][row] = sign
            correct_value = True


def checkforwin(cntr):
    for n in range(3):
        if Field[n] == (['o', 'o', 'o'] or ['x', 'x', 'x']) or (Field[0][n] == Field[1][n] == Field[2][n] != '-'):
            return 'win'
    if Field[1][1] == Field[2][2] == Field[0][0] != '-' or Field[0][2] == Field[1][1] == Field[2][0] != '-':
        return 'win'
    if cntr == 9:
        return 'draw'


Field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
turn = 'x'
counter = 0
print('Певые ходят крестики!')

for i in range(10):
    counter += 1
    hod(turn)
    for j in range(3):
        print(' | '.join(Field[j]))
    if checkforwin(counter) == 'win':
        print(f'"{turn}" победили, поздравляем!')
        exit()
    elif checkforwin(counter) == 'draw':
        print(f'Ничья!')
        exit()
    else:
        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'
        print(f'Ходят "{turn}"')






