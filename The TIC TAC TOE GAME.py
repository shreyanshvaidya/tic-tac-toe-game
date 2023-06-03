# The TIC TAC TOE GAME
# the game board creation
def game_grid(values):
    print("\n        ___________________")
    print("\t|     |     |     |")
    print("\t|  {}  |  {}  |  {}  |".format(values[0], values[1], values[2]))
    print("\t|_____|_____|_____|")
    # second row
    print("\t|     |     |     |")
    print("\t|  {}  |  {}  |  {}  |".format(values[3], values[4], values[5]))
    print("\t|_____|_____|_____|")
    # third row
    print("\t|     |     |     |")
    print("\t|  {}  |  {}  |  {}  |".format(values[6], values[7], values[8]))
    print("\t|_____|_____|_____|")
    print("\n")


def move(symbol):
    if symbol == "X":
        print(name1, "your turn")
    elif symbol == "O":
        print(name2, "your turn")
    choice = int(input("enter your move from(1-9): ").strip())
    if value[choice - 1] == " ":
        value[choice - 1] = symbol
    else:
        print()
        print("That spot is already taken")


# checking if the match is toward its end
def does_win(symbol):
    if (value[0] == value[1] == value[2] == symbol) or \
            (value[3] == value[4] == value[5] == symbol) or \
            (value[6] == value[7] == value[8] == symbol) or \
            (value[0] == value[3] == value[6] == symbol) or \
            (value[1] == value[4] == value[7] == symbol) or \
            (value[2] == value[5] == value[8] == symbol) or \
            (value[0] == value[4] == value[8] == symbol) or \
            (value[2] == value[4] == value[6] == symbol):
        return True
    else:
        return False


def is_draw():
    if " " not in value:
        return True
    else:
        return False


value = [" " for x in range(9)]
game_grid(value)
name1 = input("enter the first player name: ")
name2 = input("enter the second player name: ")
while True:
    game_grid(value)
    move("X")
    game_grid(value)
    if does_win("X"):
        print(name1, " wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    move("O")
    if does_win("O"):
        game_grid(value)
        print(name2, "wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
print("THE GAME IS OVER")