from card import Card
from hand import Hand
from helpers import combinations

class Player:
    def __init__(self, name: str):
        self.name = name
        self.private_cards = []
        self.common_cards = []
        self.hand = []
    
    def set_private_cards(self, private_cards: list[Card]):
        self.private_cards = private_cards
    
    def set_common_cards(self, common_cards: list[Card]):
        self.common_cards = common_cards
    
    @property
    def private_common_cards(self):
        return self.private_cards + self.common_cards
    
    def __str__(self):
        return f'{self.name}'
        
    def get_best_hand(self) -> tuple: # type: ignore
        values = []
        suits = []
        card_combinations = list(combinations(self.private_common_cards, n=5))
        for combination in card_combinations:
            for card in sorted(combination, key=lambda c: c.value):
                values.append(card.value)
                suits.append(card.suit)
        des_values = []
        des_suits = []
        i = 0
        while i < len(values):
            des_values.append(values[i:i+5])
            des_suits.append(suits[i:i+5])
            i += 5
        for value, suit in zip(des_values, des_suits):
            len_set_value = len(set(value))
            len_set_suit = len(set(suit))
            if (value[-1] - value[0]) == 4 and len_set_value == 5 and len_set_suit == 1:
                return value, suit, Hand.STRAIGHT_FLUSH
            if len_set_value == 2:
                if value[1] == value[3]:
                    return value, suit, Hand.FOUR_OF_A_KIND
                else:
                    return value, suit, Hand.FULL_HOUSE
            if len_set_suit == 1:
                return value, suit, Hand.FLUSH
            if (value[-1]) - (values[0]) == 4 and len_set_value == 5:
                return value, suit, Hand.STRAIGHT
            if len_set_value == 3:
                if value[0] == value[2] or value[-1] == value[2]:
                    return value, suit, Hand.THREE_OF_A_KIND
                else:
                    return value, suit, Hand.TWO_PAIR
            if len_set_value == 4:
                return value, suit, Hand.ONE_PAIR
            return value, suit, Hand.HIGH_CARD
    
    def create_hand(self):
        hand_cards = []
        values, suits, cat = self.get_best_hand()
        for value, suit in zip(values, suits):
            card_value = Card.SYMBOLS[value - 1]
            hand_cards.append(Card(card_value+suit))
        new_hand = Hand(hand_cards)
        new_hand.cat = cat
        new_hand.cat_rank = 13
        return new_hand
        
new_player = Player('Player 1')
print(new_player)
new_player.set_common_cards([Card('A♣'), Card('K❤'), Card('K◆'), Card('Q◆'), Card('9♠')])
new_player.set_private_cards([Card('K♠'), Card('K♣')])
print(new_player.get_best_hand())
print(new_player.create_hand())
