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
        
    def get_info_best_hand(self):
        values = []
        suits = []
        card_combinations = list(combinations(self.private_common_cards, n = 5))
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
        best_combination = []
        for value, suit in zip(des_values, des_suits):
            len_set_value = len(set(value))
            len_set_suit = len(set(suit))
            if len_set_suit == 1 and len_set_value == 5 and (value[-1] - value[0]) == 4:
                current_combination = [value, suit, Hand.STRAIGHT_FLUSH]
            if len_set_value == 2:
                if value[1] == value[3]:
                    current_combination = [value, suit, Hand.FOUR_OF_A_KIND]
                else:
                    current_combination = [value, suit, Hand.FULL_HOUSE]
            if len_set_suit == 1:
                current_combination = [value, suit, Hand.FLUSH]
            if len_set_value == 5 and (value[-1]) - (values[0]) == 4:
                current_combination = [value, suit, Hand.STRAIGHT]
            if len_set_value == 3:
                if value[0] == value[2] or value[-1] == value[2]:
                    current_combination = [value, suit, Hand.THREE_OF_A_KIND]
                else:
                    current_combination = [value, suit, Hand.TWO_PAIR]
            if len_set_value == 4:
                current_combination = [value, suit, Hand.ONE_PAIR]
            if len_set_value == 5:
                current_combination = [value, suit, Hand.HIGH_CARD]
            if len(best_combination) == 3 and best_combination[2] < current_combination[2]:
                best_combination = current_combination
            # if best_combination[2] == current_combination[2]:
            #     if sum(best_combination[0]) > sum(current_combination[1]):
            #         pass
            # COMPROBAR CUANDO SE PUEDAN DAR LA MISMA COMBINACIÓN, COGER LA MÁS ALTA Y SI SIGUEN SIENDO
            # IGUALES LA x CARTA MAS ALTA!
            if len(best_combination) == 0:
                best_combination = current_combination
            
        return best_combination
       
    def get_cat_rank(self) -> str | tuple[str]:
        values, suits, cat = self.get_info_best_hand()
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
        values, suits, cat = self.get_info_best_hand()
        for value, suit in zip(values, suits):
            card_value = Card.SYMBOLS[value - 1]
            hand_cards.append(Card(card_value+suit))
        new_hand = Hand(hand_cards)
        new_hand.cat = cat
        new_hand.cat_rank = self.get_cat_rank()
        return new_hand
    
    
players = [Player('Player 1'), Player('Player 2')]
common_cards = [Card('8♠'), Card('9❤'), Card('K♣'), Card('8❤'), Card('6♠')]
private_cards = [[Card('Q♣'), Card('8♣')], [Card('2❤'), Card('10◆')]]
players[0].common_cards = common_cards
players[0].private_cards = private_cards[0]
players[1].common_cards = common_cards
players[1].private_cards = private_cards[1]
print(players[0].get_info_best_hand())
print(players[1].get_info_best_hand())