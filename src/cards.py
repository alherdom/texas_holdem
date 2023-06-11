from __future__ import annotations

class Card:
    GLYPHS = {
        '♣':'🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞',
        '◆':'🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎',
        '❤':'🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾',
        '♠':'🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'
        }
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    
    def __init__(self, card: str) -> None:
        self.value = Card.SYMBOLS.index(card[:-1]) + 1
        self.suit = card[-1]
    
    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][self.value -1]
    
    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE
    
    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE
    
    def __eq__(self, other: Card) -> bool:
        return self.value == other.value and self.suit == other.suit
    
    def __gt__(self, other: Card) -> bool:
        return self.value == max(self.value, other.value)
    
    def __lt__(self, other: Card) -> bool:
        return self.value == min(self.value, other.value)


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
    
    def __init__(self, cards: list[Card]) -> None:
        self.hand = cards
        self.cat: int
        self.cat_rank: str | tuple[str]
    
    def __getitem__(self, index: int) -> Card:
        return self.hand[index]
    
    def __len__(self) -> int:
        return len(self.hand)
    
    def __iter__(self) -> HandIterator:
        return HandIterator(self)
    
    def __repr__(self) -> str:
        return " ".join(str(card) for card in self.hand)
    
    def __contains__(self, card: Card):
        return card in self.hand
    
    def __gt__(self, other):
        if self.cat_rank == other.cat_rank and self.cat == other.cat:
            return [card.value for card in self.hand] > [card.value for card in other.hand]
        if self.cat > other.cat: 
            return True
        return self.cat == other.cat and self.cat_rank > other.cat_rank

    def __eq__(self, other):
        if self.cat_rank == other.cat_rank and self.cat == other.cat:
            return [card.value for card in self.hand] == [card.value for card in other.hand]
        return False


class HandIterator:
    def __init__(self, hand: Hand):
        self.hand = hand
        self.counter = 0

    def __next__(self) -> Card:
        if self.counter >= len(self.hand):
            raise StopIteration
        item = self.hand[self.counter]
        self.counter += 1
        return item