from random import random, randint

GAME_TABLE = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def winner():
    global GAME_TABLE
    for row in GAME_TABLE:
        if row.count('X') == 3:
            return True
        elif row.count('C') == 3:
            return False

    for column in range(3):
        array_columns = [GAME_TABLE[row][column] for row in range(len(GAME_TABLE))]
        if array_columns.count('X') == 3:
            return True
        elif array_columns.count('C') == 3:
            return False

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for diagonal in diagonals:
        vector_diagonal = [GAME_TABLE[r][c] for r, c in diagonal]
        if vector_diagonal.count('X') == 3:
            return True
        elif vector_diagonal.count('C') == 3:
            return False

    return None  # No hay ganador


def show_table(table):
    for row in table:
        print(" ".join(str(element) for element in row))


def player_turn():
    while True:
        try:
            r = int(input("Choose a row (0-2): "))
            c = int(input("Choose a column (0-2): "))
            if GAME_TABLE[r][c] == 0:
                GAME_TABLE[r][c] = 'X'
                show_table(GAME_TABLE)
                break
            else:
                print("Position already occupied. Choose another.")
        except (IndexError, ValueError):
            print("Invalid input. Please choose valid row and column numbers (0-2).")


def random_place():
    empty_zero = check_tie()
    while not empty_zero:
        i = randint(0, 2)
        j = randint(0, 2)

        global GAME_TABLE
        if GAME_TABLE[i][j] == 0:
            GAME_TABLE[i][j] = 'C'
            break


def check_tie():
    global GAME_TABLE
    for row in GAME_TABLE:
        if 0 in row:
            return False
    return True


def winner():
    global GAME_TABLE
    for row in GAME_TABLE:
        if row.count('X') == 3:
            return "You WIN! "
        elif row.count('C') == 3:
            return "Computer Wins!"

    for column in range(3):
        array_columns = [GAME_TABLE[row][column] for row in range(len(GAME_TABLE))]

        if array_columns.count('X') == 3:
            return "You Win!"
        elif array_columns.count('C') == 3:
            return "Computer Wins!"

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for diagonal in diagonals:
        vector_diagonal = [GAME_TABLE[r][c] for r, c in diagonal]
        if vector_diagonal.count('X') == 3:
            return "You Win!"
        elif vector_diagonal.count('C') == 3:
            return "Computer Wins"

    return None


def search_row():
    global GAME_TABLE
    for row in range(3):
        vector_row = [GAME_TABLE[row][j] for j in range(3)]
        if vector_row.count('C') == 2 and vector_row.count(0) == 1:
            for x in range(3):
                if vector_row[x] == 0:
                    GAME_TABLE[row][x] = 'C'
                    return True

    for another_row in range(3):
        a_vector_row = [GAME_TABLE[another_row][j] for j in range(3)]
        if a_vector_row.count('X') == 2 and a_vector_row.count(0) == 1:
            for y in range(3):
                if a_vector_row[y] == 0:
                    GAME_TABLE[another_row][y] = 'C'
                    return True
    return False


def search_column():
    global GAME_TABLE
    for j in range(3):
        vector_columns = [GAME_TABLE[i][j] for i in range(3)]
        if vector_columns.count('C') == 2:
            for i in range(len(vector_columns)):
                if vector_columns[i] == 0:
                    GAME_TABLE[i][j] = 'C'
                    return True

    for k in range(3):
        vector_columns = [GAME_TABLE[i][k] for i in range(3)]
        if vector_columns.count('X') == 2:
            for i in range(len(vector_columns)):
                if vector_columns[i] == 0:
                    GAME_TABLE[i][k] = 'C'
                    return True
    return False


def search_diagonals():
    global GAME_TABLE
    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]
    for diagonal in diagonals:
        x_positions = [GAME_TABLE[r][c] for r, c in diagonal]
        empty_position = [(r, c) for r, c in diagonal if GAME_TABLE[r][c] == 0]

        if x_positions.count('X') == 2 and len(empty_position) == 1:
            i, j = empty_position[0]
            GAME_TABLE[i][j] = 'C'
            return True
    return False


def computer_turn():
    if search_row() or search_column() or search_diagonals():
        return
    random_place()


def main():
    to_continue = True
    global GAME_TABLE
    is_player_turn = True
    while to_continue:
        if is_player_turn:
            player_turn()
            is_player_turn = False
        else:
            print("--Computer choice--")
            computer_turn()
            is_player_turn = True

            show_table(GAME_TABLE)
            result = winner()
            if result:
                print(result)
                break
            if check_tie():
                print("It's a tie!")
                break
    print("Done!")

main()