import pickle
from player import player, MiniMax_AI, ML_AI
from game import game


p1 = ML_AI("X")
p2 = ML_AI("O")

newgame = game(p1, p2)
for i in range(1000):    
    while newgame.winner() == False:
        player = newgame.active_player
        newgame.make_move(player.get_move(newgame.board), player)
    newgame.reset()

p1.save("1000GamesAI")