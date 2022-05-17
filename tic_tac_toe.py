board = {
    "T1": " ", "T2": " ", "T3": " ",
    "M1": " ", "M2": " ", "M3": " ",
    "B1": " ", "B2": " ", "B3": " ",
}

player = 1
total_turn = 0
end_check = 0


def check():
    "player 1"
    """ horizontial position"""
    if board["T1"] == "X" and board["T2"] == "X" and board["T3"] == "X":
        print("Player 1 won the match !! ")
        return 1
    if board["M1"] == "X" and board["M2"] == "X" and board["M3"] == "X":
        print("Player 1 won the match !! ")
        return 1
    if board["B1"] == "X" and board["B2"] == "X" and board["B3"] == "X":
        print("Player 1 won the match !! ")
        return 1

    """ vertical position"""
    if board["T1"] == "X" and board["M1"] == "X" and board["B1"] == "X":
        print("Player 1 won the match !! ")
        return 1
    if board["T2"] == "X" and board["M2"] == "X" and board["B2"] == "X":
        print("Player 1 won the match !! ")
        return 1
    if board["T3"] == "X" and board["M3"] == "X" and board["B3"] == "X":
        print("Player 1 won the match !! ")
        return 1
    """ diagonal  position"""
    if board["T1"] == "X" and board["M2"] == "X" and board["B3"] == "X":
        print("Player 1 won the match !! ")
        return 1
    if board["T3"] == "X" and board["M2"] == "X" and board["B1"] == "X":
        print("Player 1 won the match !! ")
        return 1

    "player 2 "
    """ horizontial position"""
    if board["T1"] == "O" and board["T2"] == "O" and board["T3"] == "O":
        print("Player 2 won the match !! ")
        return 1
    if board["M1"] == "O" and board["M2"] == "O" and board["M3"] == "O":
        print("Player 2 won the match !! ")
        return 1
    if board["B1"] == "O" and board["B2"] == "O" and board["B3"] == "O":
        print("Player 2 won the match !! ")
        return 1

    """ vertical position"""
    if board["T1"] == "O" and board["M1"] == "O" and board["B1"] == "O":
        print("Player 2 won the match ! ")
        return 1
    if board["T2"] == "O" and board["M2"] == "O" and board["B2"] == "O":
        print("Player 2 won the match !! ")
        return 1
    if board["T3"] == "O" and board["M3"] == "O" and board["B3"] == "O":
        print("Player 2 won the match !! ")
        return 1
    """ diagonal  position"""
    if board["T1"] == "O" and board["M2"] == "O" and board["B3"] == "O":
        print("Player 2 won the match !! ")
        return 1
    if board["T3"] == "O" and board["M2"] == "O" and board["B1"] == "O":
        print("Player 2 won the match !! ")
        return 1
    return 0


print("---for reference---")
print("T1 | T2 | T3 ")
print("M1 | M2 | M3 ")
print("B1 | B2 | B3")
print("All the best .. ! ")

while True:
    print("------------")
    print("| " + board["T1"] + " | " + board["T2"] + " | " + board["T3"] + "| ")
    print("------------")
    print("| " + board["M1"] + " | " + board["M2"] + " | " + board["M3"] + "| ")
    print("------------")
    print("| " + board["B1"] + " | " + board["B2"] + " | " + board["B3"] + "| ")
    print("------------")
    end_check = check()
    if total_turn == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input("Player 1 turn ! ")
            if p1_input.upper() in board and board[p1_input.upper()] == " ":
                board[p1_input.upper()] = "X"
                player = 2
                break
            else:
                print("Given input is not valid .. !")
                continue
        else:
            p1_input = input("Player 2 turn ! ")
            if p1_input.upper() in board and board[p1_input.upper()] == " ":
                board[p1_input.upper()] = "O"
                player = 1
                break
            else:
                print("Give input is not valid .. !")
                continue
total_turn += 1
