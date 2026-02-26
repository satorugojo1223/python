the_board = { "7" : " ",  "8" : " ",  "9" : " " ,
             "4" : " ",  "5" : " ",  "6" : " ",
             "1" : " ",  "2" : " ",  "3" : " "
}

board_keys = []

for key in the_board:
    board_keys.append(key)
print(board_keys)

def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|"+ board["9"])
    print("_+_+_")
    print(board["4"] + "|" + board["5"] + "|"+ board["6"])
    print("_+_+_")
    print(board["1"] + "|" + board["2"] + "|"+ board["3"])

def game():
    turn = "X"
    turn = "O"
    
    for i in range(10):
        printBoard(the_board)
        print("itz ur turn,"+turn+".move to which place??????")
        move = input()
        
        if the_board[move] == " ":
            the_board[move] = turn
            count=+1
        else:
            print("the place is already filled move somewhere else \n move to which place ???")
            continue

        if count >= 5:
            if the_board[7] == the_board[8] == the_board[9] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break         
            elif the_board[4] == the_board[5] == the_board[6] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
            elif the_board[1] == the_board[2] == the_board[3] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
            elif the_board[7] == the_board[4] == the_board[1] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
            elif the_board[8] == the_board[5] == the_board[2] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
            elif the_board[9] == the_board[6] == the_board[3] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
            elif the_board[7] == the_board[5] == the_board[3] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
            elif the_board[9] == the_board[5] == the_board[1] != " ":
                printBoard(the_board)
                print("game over :(")
                print("*********"+turn+"won*********")
                break
        if count == 9:
            print("game over")
            print("itz a tie")
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    restart = input("do ya wanna play again? i bet no")
    if restart == "y" or restart == "y":
        for key in board_keys:
            the_board[key] = " "

        game()


if __name__ == "__main__":
    game()