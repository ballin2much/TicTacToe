import numpy as np
import random
from board import board
from player import player, ML_AI

class game:
    def __init__(self, player1, player2): 
        self.board = board()
        self.player1 = player1
        self.player2 = player2
        self.board.print_board()
        start = random.randint(1,2)
        if start == 1:
            self.active_player = player1
        else:
            self.active_player = player2

    def reward(self):
        if self.winner() == self.player1:
            if isinstance(self.player1, ML_AI): self.player1.giveReward(1)
            if isinstance(self.player2, ML_AI): self.player2.giveReward(0)
        elif self.winner() == self.player2:
            if isinstance(self.player1, ML_AI): self.player1.giveReward(0)
            if isinstance(self.player2, ML_AI): self.player2.giveReward(1)
        else:
            if isinstance(self.player1, ML_AI): self.player1.giveReward(0.5)
            if isinstance(self.player2, ML_AI): self.player2.giveReward(0.5)

    def make_move(self, move, player):
        if self.board.board[move[0]][move[1]] == " ":
            self.board.board[move[0]][move[1]] = player.symbol
            if player == self.player1:
                self.active_player = self.player2
            else:
                self.active_player = self.player1
            self.board.print_board()
            if self.winner() != False:
                self.reward()
                return [True, True]
            else:
                return [True, False]
        else:
            return [False, False]

    def reset(self):
        self.board.reset()
        if isinstance(self.player1, ML_AI): self.player1.newGame()
        if isinstance(self.player2, ML_AI): self.player2.newGame()
        start = random.randint(1,2)
        if start == 1:
            self.active_player = self.player1
        else:
            self.active_player = self.player2
        self.board.print_board()
    
    def winner(self):
        return self.board.winner(self.player1, self.player2)

