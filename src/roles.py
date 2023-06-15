from card import Card
from hand import Hand
from helpers import combinations

class Player: 
    def __init__(self, name: str, private_cards: list[Card] = [], common_cards: list[Card] = []):
        self.name = name
        self.private_cards = private_cards
        self.common_cards = common_cards

    def get_hands(self) -> list:
        return [Hand(c) for c in combinations((self.private_cards + self.common_cards), n = 5)]
    
    def get_best_hand(self) -> Hand:
        return Hand(max(self.get_hands()))

    def __repr__(self) -> str:
        return self.name