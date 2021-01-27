from django.shortcuts import render
from Models.player import MiniMax_AI, player
from Models.board import board
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import numpy as np

# Create your views here.
@api_view(['POST'])
def make_move(req):
    req = req.data
    symbol = req["symbol"]
    human = player(symbol)
    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"
    AI = MiniMax_AI(symbol, human)
    tempBoard = board(np.array(req["board"]))
    move = AI.get_move(tempBoard)
    return Response({"board": tempBoard.simulate_move(move, AI)[1].board})

