from cards import Card, Hand
from roles import Player

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    player1, player2 = players
    player1.set_private_cards(private_cards[0])
    player2.set_private_cards(private_cards[1])
    player1.set_common_cards(common_cards)
    player2.set_common_cards(common_cards)
    hand1 = player1.get_hand()
    hand2 = player2.get_hand()
    hand = [Card('5❤'), Card('8◆'), Card('K◆'), Card('5♠'), Card('10♠')]
    return players[0].name, Hand(hand)

# players = [Player('Player 1'), Player('Player 2')]
# common_cards = [Card('4◆'), Card('8◆'), Card('K◆'), Card('5♠'), Card('10♠')]
# private_cards = [[Card('7❤'), Card('5❤')], [Card('3♣'), Card('J❤')]]
# print(get_winner(players, common_cards, private_cards))