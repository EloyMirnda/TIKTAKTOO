field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

active_player = "X"
run = True

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def move():
    global run
    while True:
        set = input("Gebe eine Zahl von 1 - 9 um deinen Zug zu setzten: ")
        if active_player == "q":
            run = False
            return
        set = int(set)
        if set >= 1 and set <= 9:
            if field[set] == "X" or field[set] == "O":
                print("Das Feld ist schon besetzt")
            else:
                return set
            return set
        else:
            print("Bitte gebe eine Zahl im Gewünschtem Zahlen bereich an (1 -9)... ")

def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"

def check_win():
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]

def check_draw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != "5" and\
            field[6] != "6" and field[7] != "7" and field[8] != "8" and field[9] != "9":
        return True

while run:
    print_field()
    set = move()
    if set != None:
        field[set] = active_player
        if check_win():
            print("Player " + check_win() + " has won!")
            run = False
        if check_draw():
            print("Es ist ein Unentschieden.")
            

        change_player()