#!/usr/bin/python3

import sys
from carddeck import ShuffledDeck
from cardrules import poker_hand, high_card

def play_five_card_draw(players=4):

    deck = ShuffledDeck()
    
    hands = [list() for _ in range(players)]

    for i in range(5):
        for hand in hands:
            hand.append(deck.draw())

    best_hands = [poker_hand(hand) for hand in hands]

    for player in range(players):
        print("\nPlayer",player+1,"has a",best_hands[player].name+":")
        for card in hands[player]:
            print('\t',card.value,card.suit)
    
    high_hand = max(best_hands)
    winners = []
    if best_hands.count(high_hand) == 1:
        winners.append(best_hands.index(high_hand))
    else:
        highest_card = -1
        for player in range(players):
            if best_hands[player] == high_hand:
                player_high_card = high_card(hands[player])
                if player_high_card > highest_card:
                    highest_card = player_high_card
                    winners = [player]
                elif player_high_card == highest_card:
                    winners.append(player)
    if len(winners) == 1:
        print("\nPlayer",winners[0]+1,"wins with a",best_hands[winners[0]].name,"!")
    elif len(winners) > 1:
        print("\nIt's a",best_hands[winners[0]].name,"tie between players",
                " and ".join([str(w+1) for w in winners]),"!")



if __name__ == '__main__':
    if len(sys.argv) > 1:
        play_five_card_draw(int(sys.argv[1]))
    else:
        play_five_card_draw()
