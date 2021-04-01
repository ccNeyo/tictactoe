game_active = True
player = "X"

field = [" ",
             "_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3]+ "     1 | 2 | 3")
    print(field[4] + "|" + field[5] + "|" + field[6]+ "     4 | 5 | 6")
    print(field[7] + "|" + field[8] + "|" + field[9]+ "     7 | 8 | 9")

def player_input():
    global game_active
    while True:
        turn = input("field: ")
        if turn == "c":
            game_active =False
            return

        try:
            turn= int(turn)
        except ValueError:
            print("input number from 1 to 9")
        else:
            if turn >=1 and turn <= 9:
                if field[turn] == 'X' or field[turn] == 'O':
                    print("field is taken, choose another one!")
                else:
                    return turn
            else:
                print("input has to be between 1 and 9")

def change_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def status_controll():
    # row controll
    if field[1] == field[2] == field[3] != "_":
        return field[1]
    if field[4] == field[5] == field[6] != "_":
        return field[4]
    if field[7] == field[8] == field[9] != "_":
        return field[7]
    # column controll
    if field[1] == field[4] == field[7] != "_":
        return field[1]
    if field[2] == field[5] == field[8] != "_":
        return field[2]
    if field[3] == field[6] == field[9] != "_":
        return field[3]
    # diagonal controll
    if field[1] == field[5] == field[9] != "_":
        return field[5]
    if field[7] == field[5] == field[3] != "_":
        return field[5]

def tie_controll():
    if (field[1] == 'X' or field[1] == 'O') \
    and (field[2] == 'X' or field[2] == 'O') \
    and (field[3] == 'X' or field[3] == 'O') \
    and (field[4] == 'X' or field[4] == 'O') \
    and (field[5] == 'X' or field[5] == 'O') \
    and (field[6] == 'X' or field[6] == 'O') \
    and (field[7] == 'X' or field[7] == 'O') \
    and (field[8] == 'X' or field[8] == 'O') \
    and (field[9] == 'X' or field[9] == 'O'):
        return ('tie')

print_field()
while game_active:
    print()
    print("player" + player + "turn")
    turn = player_input()
    if turn:
        field[turn] = player
        print_field()
        win = status_controll()
        if win:
            game_active =False
            break
        tie = tie_controll()
        if tie:
            print("the game is a tie")
            game_active = False
        change_player()
print()
