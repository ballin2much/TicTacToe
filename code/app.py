import copy

def start_game():
    board = [[" "," "," "],
            [" "," "," "],
            [" ", " "," "]]

    active_player = "X"
    not_active = "O"
    game_going = True
    while game_going:
        if active_player == "X":
            not_active = "O"
        else:
            not_active = "X"
        print(active_player + "'s turn")
        print_board(board)
        print("The best move is:")
        print(pickmove(board,active_player, not_active))
        valid_input = False
        while not valid_input:
            try:
                temp = [None, None];
                temp[0] = int(input("Row Num:"))
                if temp[0] == 10:
                    return
                temp[1] = int(input("Column Num:"))
                if temp[0] >= 0 and temp[0] <= 2 and temp[1] >= 0 and temp[1] <= 2:
                    ar = make_move(board, active_player, temp)
                    valid_input = ar[0]
                    board = ar[1]
                    if not valid_input:
                        print("Space is taken")
                else:
                    print("Not valid move")
            except ValueError:
                print("Not a number")
            except:
                print("Something Broke")
        if check_tie(board):
            game_going = False
            print_board(board)
            print("Cats Game!")
        else:        
            game_going = not check_win(board, active_player)
            if not game_going:
                print_board(board)
                print(active_player + " wins!")
            else:
                if active_player == "X":
                    active_player = "O"
                elif active_player == "O":
                    active_player = "X"

def check_win(board, player):
    for counter in range(0,3):
        if (board[counter][0] == player and board[counter][1] == player and board[counter][2] == player) \
          or (board[0][counter] == player and board[1][counter] == player and  board[2][counter] == player):
            return True
    if board[1][1] == player and ((board[0][0] == player and board[2][2] == player) \
      or (board[0][2] == player and board[2][0] == player)):
      return True
    return False

def make_move(board, player, place):
    if board[place[0]][place[1]] == " ":
        stupid = copy.deepcopy(board)
        stupid[place[0]][place[1]] = player
        return [True, stupid]
    return [False, board]

def check_tie(board):
    for i in board:
        for x in i:
            if x == " ":
                return False
    return True

def print_board(board):
    for i in board:
        print(i[0]+"|"+i[1]+"|"+i[2])

def eval_board(board, max_player, min_player):
    if check_win(board, max_player):
        return 10
    elif check_win(board, min_player):
        return -10
    else:
        return 0

def minimax(board, depth, max_player, min_player, is_max):
    if eval_board(board, max_player, min_player) == 10:
        return eval_board(board, max_player, min_player) - depth
    elif eval_board(board, max_player, min_player) == -10:
        return eval_board(board, max_player, min_player) + depth
    elif check_tie(board):
        return 0;
    else:
        scores = []
        if is_max:
            for rowindex, row in enumerate(board):
                for colindex, col in enumerate(row):
                    if col == " ":
                        scores.append(minimax(make_move(board, max_player, [rowindex, colindex])[1], depth+1, max_player, min_player, not is_max))
            return max(scores)
        else:
            for rowindex, row in enumerate(board):
                for colindex, col in enumerate(row):
                    if col == " ":
                        scores.append(minimax(make_move(board, min_player, [rowindex, colindex])[1], depth+1, max_player, min_player, not is_max))
            return min(scores)

def pickmove(board, max_player, min_player):
    bestmove = [None,None,-1000]
    for rowindex, row in enumerate(board):
        for colindex, col in enumerate(row):
            if col == " ":
                score = minimax(make_move(board, max_player, [rowindex, colindex])[1],0,max_player,min_player, False)
                if score > bestmove[2]: bestmove = [rowindex, colindex, score]
    return bestmove

start_game()