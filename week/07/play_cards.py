#!/usr/bin/python3

from random import shuffle
from carddeck import ShuffledDeck

def draw_one():

    deck = ShuffledDeck()

    card1 = deck.draw()
    card2 = deck.draw()
    print("Player 1 has\t{}".format(card1))
    print("Player 2 has\t{}".format(card2))
    if card1 > card2:
        print("Player 1 wins!")
    elif card1 < card2:
        print("Player 2 wins!")
    else:
        print("It's a draw!")


if __name__ == '__main__':
    draw_one()
