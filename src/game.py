from card import Card
from hand import Hand
from roles import Player

# def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:       
#     player1 = players[0]
#     player2 = players[1]
#     player1.private_cards, player1.common_cards = private_cards[0], common_cards
#     player2.private_cards, player2.common_cards = private_cards[1], common_cards
#     player1_hand = player1.get_best_hand()
#     player2_hand = player2.get_best_hand()
#     if player1_hand > player2_hand:
#         return player1, player1_hand
#     if player2_hand > player1_hand:
#         return player2, player2_hand
#     if player2_hand == player1_hand: 
#         return None, player1_hand

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> list[tuple[Player | None, Hand]]:
    players_hands = {}
    for player, private_card in zip(players, private_cards):
        player.private_cards, player.common_cards = private_card, common_cards
        players_hands[player] = player.get_best_hand()
    hands = [hand for hand in players_hands.values()]
    max_hand = max(hands)
    winner_hands = hands.count(max_hand)
    if winner_hands > 1:
        return None, max_hand
    winner_player = [player for player, hand in players_hands.items() if hand == max_hand]
    return winner_player[0], max_hand

players = [Player('Player 1'), Player('Player 2')]
common_cards = [Card('A❤'), Card('K◆'), Card('Q♣'), Card('9❤'), Card('3♣')]
private_cards = [[Card('J◆'), Card('4◆')], [Card('J◆'), Card('4◆')]]
# 'Player 1',
# [Card('3◆'), Card('3♣'), Card('A❤'), Card('K◆'), Card('Q♣')]
print(get_winner(players,common_cards, private_cards))