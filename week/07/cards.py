#!/usr/bin/python3

import random

class PlayingCard:
    def __init__(self, value, suit):
        self.suit  = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit

if __name__ == "__main__":
   suits = ["♠︎", "♣︎", "♥︎", "♦︎"]
   values = ["2","3","4","5","6","7","8","9","10",
             "J","Q","K","A" ]
   deck = []
   for suit in suits:
       for value in values:
           card = PlayingCard(value, suit)
           deck.append(card)

   random.shuffle(deck)

   x = deck[0]
   y = deck[1]
   print(x)
   print(y)
   print(x.value == y.value)
