from carddeck import CardRank
from enum import IntEnum

class HandRank(IntEnum):
    """ Enumeration of hand ranks s.t. ranks are coded
    as readable names. We will be able to access the names 
    themselves, as well as the values they store.
    """
    HIGH_CARD=0
    PAIR=1
    TWO_PAIR=2
    THREE_OF_A_KIND=3
    STRAIGHT=4
    FLUSH=5
    FULL_HOUSE=6
    FOUR_OF_A_KIND=7
    STRAIGHT_FLUSH=8
    ROYAL_FLUSH=9


class PokerHand:
    """ Class representing a hand of five Cards for 
    playing five-card draw poker.
    """
    def __init__(self, player, cards):
        self.player = str(player)
        self.cards = cards
        self.rank = self._find_rank()
        self.high_card = self._find_high_card()

    # returns a string representation of this hand
    def __str__(self):
        return '\n'.join(['{}{}'.format(
            card.value, card.suit) for card in self.cards])

    # override ==, !=, >, >=, <, <= operators s.t. we can 
    # compare this hand to another
    def __eq__(self, other):
        return self.rank == other.rank and self.high_card == other.high_card
    def __ne__(self, other):
        return self.rank != other.rank or self.high_card != other.high_card
    def __gt__(self, other):
        if self.rank == other.rank:
            return self.high_card > other.high_card
        return self.rank > other.rank
    def __ge__(self, other):
        if self.rank == other.rank:
            return self.high_card >= other.high_card
        return self.rank >= other.rank
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.high_card < other.high_card
        return self.rank < other.rank
    def __le__(self, other):
        if self.rank == other.rank:
            return self.high_card >= other.high_card
        return self.rank <= other.rank

    # below are a few auxilliary functions that help to rank
    # the hand objects based on their cards
    def _cards_are_in_sequence(self, ranks):
        sorted_ranks = sorted(ranks)
        for i in range( len(sorted_ranks) - 1 ):
            if i == 0 and sorted_ranks[i] == CardRank.ACE:
                pass #special case where ace is low card in straight
            if sorted_ranks[i] != ( sorted_ranks[i+1] - 1 ):
                return False
        return True


    def _value_counts(self, ranks):
        return [ranks.count(c) for c in set(ranks)]

    def _find_rank(self):

        suits = [card.suit for card in self.cards]
        ranks = [card.rank for card in self.cards]

        if all(v in ranks for v in ['A','K','Q','J','10']) and len(set(suits)) == 1:
            return HandRank.ROYAL_FLUSH

        elif self._cards_are_in_sequence(ranks) and len(set(suits)) == 1:
            return HandRank.STRAIGHT_FLUSH
        
        elif 4 in self._value_counts(ranks):
            return HandRank.FOUR_OF_A_KIND
        
        elif 3 in self._value_counts(ranks) and 2 in self._value_counts(ranks):
            return HandRank.FULL_HOUSE
        
        elif len(set(suits)) == 1:
            return HandRank.FLUSH
        
        elif self._cards_are_in_sequence(ranks):
            return HandRank.STRAIGHT

        elif 3 in self._value_counts(ranks):
            return HandRank.THREE_OF_A_KIND
        
        elif len(set(ranks)) == 3:
            return HandRank.TWO_PAIR
        
        elif len(set(ranks)) == 4:
            return HandRank.PAIR
        
        else:
            return HandRank.HIGH_CARD


    # we can determine the highest ranked card in a hand
    # using the comparison operators which were overridden
    # for the Card class
    def _find_high_card(self):

        ranks = [card.rank for card in self.cards]

        if self.rank in [HandRank.FOUR_OF_A_KIND, HandRank.FULL_HOUSE, HandRank.THREE_OF_A_KIND, HandRank.PAIR]:
            max_count = max([ranks.count(rank) for rank in ranks])
            for rank in ranks:
                if ranks.count(rank) == max_count:
                    high_card = rank
        elif self.rank == HandRank.TWO_PAIR:
            pairs = set()
            for rank in ranks:
                if ranks.count(rank) == 2:
                    pairs.update([rank])
            high_card = max(pairs)
        else:
            high_card = max(ranks)
        return high_card
