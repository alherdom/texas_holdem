from cards import Card, Hand
from roles import Player

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    player1, player2 = players
    player1.set_private_cards(private_cards[0])
    player2.set_private_cards(private_cards[1])
    player1.set_common_cards(common_cards)
    player2.set_common_cards(common_cards)
    hand1 = player1.create_hand()
    hand2 = player2.create_hand()
    if hand2.cat == hand1.cat:
        return None, hand1
    if hand2.cat > hand1.cat:
        return player2, hand2
    return player1, hand1

players = [Player('Player 1'), Player('Player 2')]
common_cards = [Card('10◆'), Card('9◆'), Card('8♠'), Card('6❤'), Card('5♠')]
private_cards = [[Card('Q♠'), Card('4◆')], [Card('8♣'), Card('3❤')]]
print(get_winner(players, common_cards, private_cards))