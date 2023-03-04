def startgame():
    print("--------------------")
    print("игра крестики нолики")
    print("--------------------")
    print("1 число номер строки")
    print("2 число номер строки")
    print("вводим 2 числа через")
    print("пробел              ")
startgame()

field = [[ " " ] * 3 for i in range(3)]


def game_spase():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" --------------- ")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" --------------- ")
    print()
game_spase()

def ask():
    while True:
        cords = input(" Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите две координаты ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапозона ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята ")
            continue

        return x, y
ask()

# num = 0
# while True:
#     num += 1
#     game_spase()
#     if num % 2 == 1:
#         print(" Ходит крестик ")
#     else:
#         print(" Ходит нолик ")
#     x, y = ask()
#     if num % 2 == 1:
#         field[x][y] = "X"
#     else:
#         field[x][y] = "0"
#         break
#     if num == 9:
#         print(" Ничья ")
#         break

# def check_win():
#     for i in range(3):
#         symbols = []
#         for j in range(3):
#             symbols.append(field[i][j])
#         if symbols == ["X", "X", "X"]:
#             return True
#
#     for i in range(3):
#         symbols = []
#         for j in range(3):
#             symbols.append(field[j][i])
#         if symbols == ["X", "X", "X"]:
#             return True
#
#     symbols = []
#     for i in range(3):
#         for j in range(3):
#             symbols.append(field[i][i])
#         if symbols == ["X", "X", "X"]:
#             return True
#
#     symbols = []
#     for i in range(3):
#         for j in range(3):
#             symbols.append(field[i][2-i])
#         if symbols == ["X", "X", "X"]:
#             return True
#
#     return False
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False
check_win()

num = 0
while True:
    num += 1
    game_spase()
    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break
    if num == 9:
        print(" Ничья ")
        break
