from random import shuffle

# filled
CLUB = '\033[90m\u2663\033[0m'
DIAMOND = '\033[91m\u2666\033[0m'
HEART = "\033[91m\u2665\033[0m"
SPADE = '\033[90m\u2660\033[0m'

#outline
#CLUB = '\033[90m\u2667\033[0m'
#DIAMOND = '\033[91m\u2662\033[0m'
#HEART = "\033[91m\u2661\033[0m"
#SPADE = '\033[90m\u2664\033[0m'

SUITS = (CLUB, DIAMOND, HEART, SPADE)
COLORS = {CLUB:'black', DIAMOND:'red', HEART:'red', SPADE:'black'}
VALUES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

class Card:

    #TODO: Add to_string function and method of 
    # comparing the value of two Card objects.
    def __init__(self, suit, color, value):

        self.suit = suit
        self.color = color
        self.value = value


#TODO: Add a CardHand class that is instantiated 
# with a list of five cards and that can be compared
# readily to other CardHand objects.
# Also a method to sort the cards would be cool.
#class CardHand:


class ShuffledDeck:

    def __init__(self):
        
        self.deck = []

        for suit in SUITS:
            for value in VALUES:
                self.deck.append( Card(suit, COLORS[suit], value) )

        shuffle(self.deck)

    def draw(self):

        return self.deck.pop()
