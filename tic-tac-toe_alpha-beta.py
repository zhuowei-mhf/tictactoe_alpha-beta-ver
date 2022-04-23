board = [' ' for x in range(10)] #九宮格大小

chess = ['O','X']

def input_letter(letter,position): 
    board[position] = letter


def printboard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] )
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] )
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] )
    print("   |   |")

def emptyspace(position):
    return board[position] == ' '


def win(letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter)or(board[4] == letter and board[5] == letter and board[6] == letter)or(board[7] == letter and board[8] == letter and board[9] == letter)or(board[1] == letter and board[4] == letter and board[7] == letter)or (board[2] == letter and board[5] == letter and board[8] == letter)or(board[3] == letter and board[6] == letter and board[9] == letter)or(board[1] == letter and board[5] == letter and board[9] == letter)or(board[3] == letter and board[5] == letter and board[7] == letter)


def boardfull(board):
    if board.count(' ') > 1:
        return False
    
    else:
        return True
 
def playermove():
    run = True
    while run:
        p_move = int(input("要將 " + chess[0] + " 放在哪一格? (1- 9):"))
        if p_move > 0 and p_move < 10:
            if emptyspace(p_move):
                input_letter(chess[0], p_move)
                run = False
            else:
                print("這格子已經被佔領過了，請選擇其他未佔領的格子")
        else:
            print("輸入錯誤")
def computermove():
    bestscore = -100
    bestmove = 0
    for key in range(1,10):
        board[key] = chess[1]
        score  = minimax(board,0,False)
        board[key]= ' '
        if(score >  bestscore):
            bestscore = score
            bestmove = key
    
    return bestmove

def minimax(board, depth, ifmax):
    if (win(board,chess[1])):
        return 1
    elif (win(board,chess[0])):
        return -1
    else:
        return 0

    if (ifmax):
        bestscore = -100
        for key in range(1,10):
            if(emptyspace(key)):
                board[key] = chess[1]
                score = minimax(board, depth +1, False)
                board[key] = ' '
                if (score > bestscore):
                    bestscore = score
        return bestscore

    else:
        bestscore = 100
        for key in range(1,10):
            if (emptyspace(key)):
                board[key] = chess[0]
                score = minimax(board, depth +1, True)
                board[key] = ' '
                if (score < bestscore):
                    bestscore = score
        return bestscore

def random(a):
    import random as r
    ln = len(a)
    r = r.randrange(0,ln)
    return a[r]
        
def main():
    print("九宮格遊戲！")
    printboard(board)
    
    while boardfull(board) == False:
        if win(board, chess[0]):
            print('玩家勝利')
            
            
        else:
            playermove()
            printboard(board)
            if win(board, chess[0]):
                print('玩家勝利')
                break
            if (boardfull(board)):
                print("平手")
                break

        if win(board, chess[1]):
            print('電腦獲勝')
            
        else:
            move = computermove()
            if move == 0:
                print("平手")
            else:
                
                print("電腦將" , chess[1] , "放在第" ,move, "格")
                printboard(board)

                if win(board, chess[1]):
                    print('電腦獲勝')
                    break
                if (boardfull(board)):
                    print("遊戲結束")
                    break
        
main()       
    
