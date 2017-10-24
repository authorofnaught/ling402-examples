from random import shuffle
from enum import IntEnum

# We start by setting some global variables
# for the module...

# unicode and ANSI escape seqs 
# for filled and colored suits
CLUB = '\033[90m\u2663\033[0m'
DIAMOND = '\033[91m\u2666\033[0m'
HEART = "\033[91m\u2665\033[0m"
SPADE = '\033[90m\u2660\033[0m'

SUITS = (CLUB, DIAMOND, HEART, SPADE)
VALUES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

class CardRank(IntEnum):
    """ Enumeration of card ranks s.t. ranks are coded
    as readable names.  We will be able to access the 
    names themselves as well as the values they store.
    """
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5
    SIX=6
    SEVEN=7
    EIGHT=8
    NINE=9
    TEN=10
    JACK=11
    QUEEN=12
    KING=13
    ACE=14

RANKS = {   '2':CardRank.TWO
            ,'3':CardRank.THREE
            ,'4':CardRank.FOUR
            ,'5':CardRank.FIVE
            ,'6':CardRank.SIX
            ,'7':CardRank.SEVEN
            ,'8':CardRank.EIGHT
            ,'9':CardRank.NINE
            ,'10':CardRank.TEN
            ,'J':CardRank.JACK
            ,'Q':CardRank.QUEEN
            ,'K':CardRank.KING
            ,'A':CardRank.ACE
            }


class Card:
    """ Class representing a single card in a deck
    """
    def __init__(self, suit, value):

        self.suit = suit
        self.value = value
        self.rank = RANKS[value]

    # returns a string representation of this card
    def __str__(self):
        return self.value+self.suit

    # override ==, !=, >, >=, <, <= operators s.t. we can 
    # compare this card to another
    def __eq__(self, other):
        return self.rank == other.rank
    def __ne__(self, other):
        return self.rank != other.rank
    def __gt__(self, other):
        return self.rank > other.rank
    def __ge__(self, other):
        return self.rank >= other.rank
    def __lt__(self, other):
        return self.rank < other.rank
    def __le__(self, other):
        return self.rank <= other.rank


class ShuffledDeck:
    """ Class holding 52 unique Cards identified by 
    suit and value, randomized in order by default.
    """
    def __init__(self):
        
        self.deck = []

        for suit in SUITS:
            for value in VALUES:
                self.deck.append( Card(suit, value) )

        shuffle(self.deck)

    def draw(self):

        return self.deck.pop()
