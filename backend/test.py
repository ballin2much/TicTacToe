class Player():
      def __init__(self, symbol): 
        self.symbol = symbol
      def getSymbol(self):
       	return self.symbol
      
class PlayerAI(Player):
      def __init__(self, symbol, val): 
        self.val = val
        self.symbol = symbol
        super().__init__(symbol)
        
t = Player("X")

print(t.getSymbol())

t = PlayerAI("O", 5)

print(t.symbol)
print(t.getSymbol())
print(t.val)