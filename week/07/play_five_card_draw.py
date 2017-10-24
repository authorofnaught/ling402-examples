#!/usr/bin/python3

import sys
from carddeck import ShuffledDeck
from pokerrules import PokerHand

def play_five_card_draw(players=4):
    """ Play a game of five card draw
    """
    deck = ShuffledDeck()

    # deal the cards
    hands = [list() for _ in range(players)]
    for i in range(5):
        for hand in hands:
            hand.append(deck.draw())

    # make hands a list of PokerHand objects
    hands = [PokerHand(player, hand) for player, hand in enumerate(hands)]

    for hand in hands:
        print("\nPlayer {} has a {}:".format(hand.player, hand.rank.name))
        print(hand)

    # winners can be determined using the comparison 
    # operators which were overridden for the 
    # PokerHand class
    winners = []
    winning_hand = None
    for hand in hands:
        if not winning_hand or hand > winning_hand:
            winning_hand = hand
            winners = [winning_hand]
        elif hand == winning_hand:
            winning_hand
            winners.append(hand)

    if len(winners) == 1:
        print("Player {} wins with a {}!".format(winners[0].player, winners[0].rank.name))
    else:
        print("Players {} tie with a {}!".format(' and '.join([w.player for w in winners]), winners[0].rank.name))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        play_five_card_draw(int(sys.argv[1]))
    else:
        play_five_card_draw()
