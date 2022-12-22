
board = {
    1:"   ",2:"   ",3:"   ",
    4:"   ",5:"   ",6:"   ",
    7:"   ",8:"   ",9:"   "
}

def showboard():
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("---+---+---")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("---+---+---")
    print(board[7]+"|"+board[8]+"|"+board[9])

def checkrepeat(position):
    if(board[position]=="   "):
        return False
    return True

def checkwinner(player):
    if(board[1]==board[2] and board[2]==board[3] and board[1]==player):
        return True
    elif(board[4]==board[5] and board[5]==board[6] and board[4]==player):
        return True
    elif(board[7]==board[8] and board[8]==board[9] and board[7]==player):
        return True
    elif(board[1]==board[4] and board[4]==board[7] and board[1]==player):
        return True
    elif(board[2]==board[5] and board[5]==board[8] and board[2]==player):
        return True
    elif(board[3]==board[6] and board[6]==board[9] and board[3]==player):
        return True
    elif(board[1]==board[5] and board[5]==board[9] and board[1]==player):
        return True
    elif(board[3]==board[5] and board[5]==board[7] and board[3]==player):
        return True
    return False

def checkdraw():
    for i in board.values():
        if(i=="   "):
            return False
    return True

showboard()
print()

turn = " x "

def switchturn(turn):
    if(turn==" x "):
        return " o "
    return " x "


while(True):
    print(f"Present player: {turn}")
    print()
    position = input("Enter a number between 1-9? ")
    print()
    if(not position.isnumeric()):
        print("Invalid input.")
        print()
        continue
    position=int(position)
    if(position<1 or position>9):
        print("Invalid Input.")
        print()
        continue
    if(checkrepeat(position)):
        print("Position is already taken.")
        print()
        continue
    board[position] = turn
    showboard()
    print()
    if(checkwinner(turn)):
        print(f"Winner: {turn}")
        break
    if(checkdraw()):
        print("It's a draw.")
    turn = switchturn(turn)
