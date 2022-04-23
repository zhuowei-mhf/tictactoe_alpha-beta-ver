## 井字遊戲 alpha-beta剪枝法版本（TicTacToe alpha-beta algorithm version)

# 程式版本(requirement)
  python 3.9.5
  
# 遊玩方式（how to play)
 棋盤：
 1 ｜ 2 ｜ 3  
   ｜   ｜  
 4 ｜ 5 ｜ 6  
   ｜   ｜  
 7 ｜ 8 ｜ 9  
  
  先決定玩家為Ｏ或Ｘ
  玩家先手，跟電腦進行遊戲
  
# 設計流程（program flow)
  利用alpha-beta剪枝法判斷是否勝利
  ```
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
  ```
