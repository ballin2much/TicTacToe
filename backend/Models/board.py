import numpy as np
import copy

class board:
    def __init__(self, b=np.full((3,3), " ")): 
        self.board = b
    
    def print_board(self):
        for i in self.board:
            print(i[0]+"|"+i[1]+"|"+i[2])

    def boardHash(self):
        return str(self.board)

    def possible_moves(self):
        moves = []
        for i, row in enumerate(self.board):
            for y, col in enumerate(row):
                if col == " ": moves.append((i,y))
        return moves

    def reset(self):
        self.board = np.full((3,3), " ")

    def winner(self, player1, player2):
        for counter in range(0,3):
            if (self.board[counter][0] == player1.symbol and self.board[counter][1] == player1.symbol and self.board[counter][2] == player1.symbol) \
            or (self.board[0][counter] == player1.symbol and self.board[1][counter] == player1.symbol and  self.board[2][counter] == player1.symbol):
                return player1
        if self.board[1][1] == player1.symbol and ((self.board[0][0] == player1.symbol and self.board[2][2] == player1.symbol) \
        or (self.board[0][2] == player1.symbol and self.board[2][0] == player1.symbol)):
            return player1

        for counter in range(0,3):
            if (self.board[counter][0] == player2.symbol and self.board[counter][1] == player2.symbol and self.board[counter][2] == player2.symbol) \
            or (self.board[0][counter] == player2.symbol and self.board[1][counter] == player2.symbol and  self.board[2][counter] == player2.symbol):
                return player2
        if self.board[1][1] == player2.symbol and ((self.board[0][0] == player2.symbol and self.board[2][2] == player2.symbol) \
        or (self.board[0][2] == player2.symbol and self.board[2][0] == player2.symbol)):
            return player2

        for i in self.board:
            for x in i:
                if x == " ":
                    return False
        return "Tie"
    
    def simulate_move(self, place, player):
        if self.board[place[0]][place[1]] == " ":
            stupid = copy.deepcopy(self)
            stupid.board[place[0]][place[1]] = player.symbol
            return [True, stupid]
        return [False, board]

