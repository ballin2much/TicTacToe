import numpy as np
import pickle
import math
import random
import copy

class player:
    def __init__(self, symbol):
        self.symbol = symbol

class ML_AI(player):
    def __init__(self, symbol, alpha=0.9, gamma=0.95, q_init=0.6, q={}): 
        self.symbol = symbol
        self.history = []
        self.q = q
        self.learning_rate = alpha
        self.value_discount = gamma
        self.default_q = q_init
        super().__init__(symbol)

    def get_q(self, board):
        if type(board) != str:
            board_hash = board.boardHash()
        else:
            board_hash = board
        if board_hash in self.q:
            qvals = self.q[board_hash]
        else:
            qvals = np.full((3,3), -1.0)
            for move in board.possible_moves():
                qvals[move[0]][move[1]] = self.default_q
                self.q[board_hash] = qvals
        return qvals

    def get_move(self, board):
        board_hash = board.boardHash()
        qvals = self.get_q(board)
        index = np.argmax(qvals)
        col = (index)%3
        row = math.floor(index/3)
        move = (row, col)
        self.history.append([board_hash,move])
        return move

    def giveReward(self, amount):
        self.history.reverse()
        next_max = -1
        for move in self.history:
            qvals = self.get_q(move[0])
            if next_max < 0:
                qvals[move[1][0]][move[1][1]] = amount
            else:
                qvals[move[1][0]][move[1][1]] = qvals[move[1][0]][move[1][1]] * (1 - self.learning_rate) + self.learning_rate * self.value_discount * next_max
            next_max = np.amax(qvals)
    
    def newGame(self):
        self.history = []

    def save(self, file_name):
        fw = open(file_name, "wb")
        pickle.dump(self.q, fw)
        fw.close()
    
    def load(self, file):
        fr = open(file, 'rb')
        self.q = pickle.load(fr)
        fr.close()

class MiniMax_AI(player):
    def __init__(self, symbol, min_player): 
        self.symbol = symbol
        self.min_player = min_player
        super().__init__(symbol)

    def eval_board(self, board):
        if board.winner(self, self.min_player) == self:
            return 10
        elif board.winner(self, self.min_player) == self.min_player:
            return -10
        elif board.winner(self, self.min_player) == "Tie":
            return 0

    def minimax(self, board, depth, is_max):
        analysis = self.eval_board(board) 
        if analysis == 10:
            return analysis - depth
        elif analysis == -10:
            return analysis + depth
        elif analysis == 0:
            return 0;
        else:
            scores = []
            if is_max:
                for rowindex, row in enumerate(board.board):
                    for colindex, col in enumerate(row):
                        if col == " ":
                            scores.append(self.minimax(board.simulate_move((rowindex, colindex), self)[1], depth+1, not is_max))
                return max(scores)
            else:
                for rowindex, row in enumerate(board.board):
                    for colindex, col in enumerate(row):
                        if col == " ":
                            scores.append(self.minimax(board.simulate_move((rowindex, colindex), self.min_player)[1], depth+1, not is_max))
                return min(scores)

    def get_move(self, board):
        bestmove = [None,None,-1000]
        for rowindex, row in enumerate(board.board):
            for colindex, col in enumerate(row):
                if col == " ":
                    score = self.minimax(board.simulate_move([rowindex, colindex], self)[1],0, False)
                    if score > bestmove[2]: bestmove = [rowindex, colindex, score]
        return bestmove