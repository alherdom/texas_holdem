from helpers import combinations
from cards import Card, Hand

class Player:
    def __init__(self, name: str, private_cards: list[Card] = [], common_cards: list[Card] = []):
        self.name = name
        self.private_cards = private_cards
        self.common_cards = common_cards
    
    @property
    def private_common_cards(self) -> list:
        return self.private_cards + self.common_cards
    
    def __repr__(self) -> str:
        return self.name
    
    def values_suits_combinations(self):
        values = []
        suits = []
        card_combinations = list(combinations(self.private_common_cards, n=5))
        for combination in card_combinations:   
            for card in sorted(combination, key=lambda c: c.value):
                values.append(card.value)
                suits.append(card.suit)
        values_combinatios = [values[i:i+5] for i in range(0, len(values), 5)]
        suits_combinatios = [suits[i:i+5] for i in range(0, len(suits), 5)]
        return values_combinatios, suits_combinatios
    
    def is_straight_flush(self, values: list, len_set_values: int, len_set_suits: int) -> bool:
        return len_set_suits == 1 and len_set_values == 5 and (values[-1] - values[0]) == 4
    
    def is_four_of_a_kind(self, values: list, len_set_values: int) -> bool:
        return len_set_values == 2 and values[1] == values[3]
    
    def is_full_house(self, values: list, len_set_values: int) -> bool:
        return len_set_values == 2 and values[1] != values[3]
    
    def is_flush(self, len_set_suits: int) -> bool:
        return len_set_suits == 1
    
    def is_straight(self, values: list, len_set_values: int) -> bool:
        return len_set_values == 5 and (values[-1]) - (values[0]) == 4
    
    def is_three_of_a_kind(self, values: list, len_set_values: int) -> bool:
        return len_set_values == 3 and values[0] == values[2] or values[-1] == values[2]
    
    def is_two_pairs(self, values: list, len_set_values: int) -> bool:
        return len_set_values == 2 and values[0] != values[2] or values[-1] != values[2]
    
    def is_one_pair(self, len_set_values: int) -> bool:
        return len_set_values == 4
    
    def is_high_card(self, len_set_values: int) -> bool:
        return len_set_values == 5
    
    def best_hand(self):
        best_combination = [ None, None, 0]
        values_combinations, suits_combinations = self.values_suits_combinations()
        for values, suits in zip(values_combinations, suits_combinations):
            len_set_values = len(set(values))
            len_set_suits = len(set(suits))
            
            if self.is_straight_flush(values, len_set_values, len_set_suits):
                current_combination = [values, suits, Hand.STRAIGHT_FLUSH]
            elif self.is_four_of_a_kind(values, len_set_values):
                current_combination = [values, suits, Hand.FOUR_OF_A_KIND]
            elif self.is_full_house(values, len_set_values):
                current_combination = [values, suits, Hand.FULL_HOUSE]
            elif self.is_flush(len_set_suits):
                current_combination = [values, suits, Hand.FLUSH]
            elif self.is_straight(values, len_set_values):
                current_combination = [values, suits, Hand.STRAIGHT]
            elif self.is_three_of_a_kind(values, len_set_values):
                current_combination = [values, suits, Hand.THREE_OF_A_KIND]
            elif self.is_two_pairs(values, len_set_values):
                current_combination = [values, suits, Hand.TWO_PAIR]
            elif self.is_one_pair(len_set_values):
                current_combination = [values, suits, Hand.ONE_PAIR]
            elif self.is_high_card(len_set_values):
                current_combination = [values, suits, Hand.HIGH_CARD]
        
            if current_combination[2] > best_combination[2]:
                best_combination = current_combination
        return best_combination

    def get_cat_rank(self) -> str | tuple[str]:
        values, suits, cat = self.best_hand()
        if Hand.FULL_HOUSE:
            return tuple(set(Card.SYMBOLS[v - 1] for v in values)) # posicion trio y pareja
        if Hand.TWO_PAIR:
            return tuple(set(Card.SYMBOLS[v - 1] for v in values)) # ordenar de mayor a menor
        # if Card.A_VALUE in values:
        #     return Card.SYMBOLS[Card.A_VALUE - 1]
        card_value = max(values)
        return Card.SYMBOLS[card_value - 1]
        
    def create_hand(self) -> Hand:
        hand_cards = []
        values, suits, cat = self.best_hand()
        for value, suit in zip(values, suits):
            card_value = Card.SYMBOLS[value - 1]
            hand_cards.append(Card(card_value+suit))
        new_hand = Hand(hand_cards)
        new_hand.cat = cat
        new_hand.cat_rank = self.get_cat_rank()
        return new_hand
    
    
# players = [Player('Player 1'), Player('Player 2')]
# common_cards = [Card('8♠'), Card('9❤'), Card('K♣'), Card('8❤'), Card('6♠')]
# private_cards = [[Card('Q♣'), Card('8♣')], [Card('2❤'), Card('10◆')]]
# players[0].common_cards = common_cards
# players[0].private_cards = private_cards[0]
# players[1].common_cards = common_cards
# players[1].private_cards = private_cards[1]
# print(players[0].best_hand())
# print(players[1].best_hand())