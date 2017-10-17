#!/usr/bin/python3

from random import shuffle

#CLUB = '\u2667'
#DIAMOND = '\u2662'
#HEART = '\u2661'
#SPADE = '\u2664'

CLUB = '\u2663'
DIAMOND = '\u2666'
HEART = '\u2665'
SPADE = '\u2660'
SUITS = (CLUB, DIAMOND, HEART, SPADE)
COLORS = {CLUB:'black', DIAMOND:'red', HEART:'red', SPADE:'black'}
VALUES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

POKER_RANK={ 'A':13
            ,'K':12
            ,'Q':11
            ,'J':10
            ,'10':9
            ,'9':8
            ,'8':7
            ,'7':6
            ,'6':5
            ,'5':4
            ,'4':3
            ,'3':2
            ,'2':1
            }


class Card:

    def __init__(self, suit, color, value):

        self.suit = suit
        self.color = color
        self.value = value


class ShuffledDeck:

    def __init__(self):
        
        self.deck = []

        for suit in SUITS:
            for value in VALUES:
                self.deck.append( Card(suit, COLORS[suit], value) )

        shuffle(self.deck)

    def draw(self):

        return self.deck.pop()


def draw_one():

    deck = ShuffledDeck()

    card1 = deck.draw()
    card2 = deck.draw()
    print("Player 1 has\t{} {}".format(card1.value, card1.suit))
    print("Player 2 has\t{} {}".format(card2.value, card2.suit))
    if POKER_RANK[card1.value] > POKER_RANK[card2.value]:
        print("Player 1 wins!")
    elif POKER_RANK[card1.value] < POKER_RANK[card2.value]:
        print("Player 2 wins!")
    else:
        print("It's a draw!")


if __name__ == '__main__':
    draw_one()
