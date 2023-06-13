from cards import Card, Hand
from roles import Player

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    player1 = players[0]
    player2 = players[1]
    player1.private_cards, player1.common_cards = private_cards[0], common_cards
    player2.private_cards, player2.common_cards = private_cards[1], common_cards
    player1_hand = player1.best_hand
    player2_hand = player2.best_hand
    if player1_hand > player2_hand:
        return player1, player1_hand
    if player2_hand > player1_hand:
        return player2, player2_hand
    if player2_hand == player1_hand: 
        return None, player1_hand
    
# players = [Player('Player 1'), Player('Player 2')]
# common_cards = [Card('A❤'), Card('9♠'), Card('3◆'), Card('3❤'), Card('2◆')]
# private_cards = [[Card('7♠'), Card('4◆')], [Card('5♠'), Card('4❤')]]
# print(get_winner(players, common_cards, private_cards))
# 'Player 1',
# [Card('3◆'), Card('3❤'), Card('A❤'), Card('9♠'), Card('7♠')],
# Hand.ONE_PAIR,
# '3',
# id="9",