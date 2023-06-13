from card import Card, SYMBOLS

class Hand:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __init__(self, combination: list[Card]):
        self.combination = sorted(combination)
        self.cat = self.get_cat()
        self.cat_rank = self.get_cat_rank()

    @property
    def value_of_rank(self):
        if isinstance(self.cat_rank, tuple):
            if self.cat == Hand.TWO_PAIR:
                return sum(SYMBOLS.index(rank) + 2 for rank in self.cat_rank)
            return [SYMBOLS.index(rank) + 2 for rank in self.cat_rank]
        return SYMBOLS.index(self.cat_rank) + 2

    def is_straight_flush(self, values: list[int], len_set_values: int, len_set_suits: int) -> bool:
        return (len_set_suits == 1 and len_set_values == 5 and values[-1] - values[0] == 4)

    def is_four_of_a_kind(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 2 and values[0] == values[3]

    def is_full_house(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 2 and values[0] != values[3]

    def is_flush(slef, len_set_suits: int) -> bool:
        return len_set_suits == 1

    def is_straight(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 5 and values[-1] - values[0] == 4

    def is_three_of_a_kind(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 3 and values[0] == values[2]

    def is_two_pair(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 3 and values[1] != values[2]

    def is_one_pair(self, len_set_values: int) -> bool:
        return len_set_values == 4
    
    def ordered_repetition_values(self) -> list:
        '''Uso de función lambda para ordenar los valores en función del número de repeticiones'''
        values = [card.value for card in self.combination]
        return sorted(values, key=lambda v: values.count(v), reverse = True)

    def get_cat(self) -> int:
        values = self.ordered_repetition_values()
        suits = [card.suit for card in self.combination]
        len_set_values = len(set(values))
        len_set_suits = len(set(suits))
        if self.is_straight_flush(values, len_set_values, len_set_suits):
            return Hand.STRAIGHT_FLUSH
        if self.is_four_of_a_kind(values, len_set_values):
            return Hand.FOUR_OF_A_KIND
        if self.is_full_house(values, len_set_values):
            return Hand.FULL_HOUSE
        if self.is_flush(len_set_suits):
            return Hand.FLUSH
        if self.is_straight(values, len_set_values):
            return Hand.STRAIGHT
        if self.is_three_of_a_kind(values, len_set_values):
            return Hand.THREE_OF_A_KIND
        if self.is_two_pair(values, len_set_values):
            return Hand.TWO_PAIR
        if self.is_one_pair(len_set_values):
            return Hand.ONE_PAIR
        return Hand.HIGH_CARD

    def get_cat_rank(self) -> str|tuple[str]:
        values = self.ordered_repetition_values()
        first_repeated_value = values[0]
        if self.cat in [Hand.ONE_PAIR, Hand.THREE_OF_A_KIND, Hand.FOUR_OF_A_KIND]:
            return SYMBOLS[first_repeated_value - 2]
        if self.cat == Hand.TWO_PAIR:
            second_repeated_value = values[2]
            repeated_values = sorted((first_repeated_value, second_repeated_value), reverse = True)
            first_pair, second_pair = repeated_values
            return SYMBOLS[first_pair - 2], SYMBOLS[second_pair - 2]
        if self.cat == Hand.FULL_HOUSE:
            second_repeated_value = values[3]
            return SYMBOLS[first_repeated_value - 2], SYMBOLS[second_repeated_value - 2]
        return SYMBOLS[max(values) - 2]
    
    def __gt__(self, other):
        if self.cat > other.cat:
            return True
        if self.cat == other.cat:
            if self.value_of_rank > other.value_of_rank:
                return True
        if self == other:
            player1_hand = sorted(self, reverse = True)
            player2_hand = sorted(other, reverse = True)
            for card1, card2 in zip(player1_hand, player2_hand):
                if card1 > card2:
                    return True
                if card2 > card1:
                    return False
        return False
    
    def __eq__(self, other):
        return self.cat == other.cat and self.cat_rank == other.cat_rank
    
    def __repr__(self):
        return f'{self.combination}'
    
    def __contains__(self, card: Card):
        return card in self.combination
    
    def __iter__(self):
        return HandIterator(self)
    
class HandIterator:
    def __init__(self, hand: Hand):
        self.hand = hand
        self.pointer = 0

    def __next__(self):
        if self.pointer >= len(self.hand.combination):
            raise StopIteration
        card = self.hand.combination[self.pointer]
        self.pointer += 1
        return card