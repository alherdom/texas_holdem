from helpers import combinations
from cards import Card, Hand

class Player:
    def __init__(self, name: str, private_cards: list[Card] = [], common_cards: list[Card] = []):
        self.name = name
        self.private_cards = private_cards
        self.common_cards = common_cards
    
    def __repr__(self) -> str:
        return self.name
    
    @property
    def hands(self):
        card_combinations = sorted(combinations((self.private_cards + self.common_cards), n = 5), reverse = True)
        return [Hand(combination) for combination in card_combinations]
    
    @property
    def best_hand(self):
        best_hand = self.hands[0]
        for hand in self.hands:
            if hand > best_hand:
                best_hand = hand
        return best_hand