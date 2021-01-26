import pickle
from player import player, MiniMax_AI
from game import game


""" p1 = player("X")
p1.load("My little AI")
p2 = player("O") """

p2 = player("X")
p1 = MiniMax_AI("O", p2)
newgame = game(p1, p2)
""" for i in range(3):    
    while newgame.winner() == False:
        player = newgame.active_player
        newgame.make_move(player.get_move(newgame.board), player)
    newgame.reset() """

for i in range(1):    
    while newgame.winner() == False:
        player = newgame.active_player
        if player == p1:
            newgame.make_move(player.get_move(newgame.board), p1)
        else:
            r = int(input("Rows:"))
            c = int(input("Cols:"))
            newgame.make_move((r, c), p2)
    print(newgame.winner().symbol + " wins!")
    newgame.reset()

""" p1.save() """