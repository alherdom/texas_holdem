SYMBOLS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

class Card:

    def __init__(self, value_suit: str):
        self.value_suit = value_suit
        self.suit = self.value_suit[-1]
        self.value_symbol = self.value_suit[:-1]

    @property
    def value(self) -> int:
        '''Se le suma 2 al índice ya que la constante SYMBOLS comienza por "2"'''
        return SYMBOLS.index(self.value_symbol) + 2

    def __repr__(self) -> str:
        return self.value_suit

    def __gt__(self, other) -> bool:
        return self.value > other.value
    
    def __eq__(self, other) -> bool:
        return self.value == other.value