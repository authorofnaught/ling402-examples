from carddeck import SUITS, COLORS, VALUES
from enum import IntEnum

#TODO: An enumeration would be more portable
class BestHand(IntEnum):
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

#TODO: Is this the best representation?
# Maybe so if different games have different ranks.
# Then different rankings can be stored in different 
# dictionaries.
ACE_HIGH_RANK={ 'A':13
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

ACE_LOW_RANK={  'K':13
                ,'Q':12
                ,'J':11
                ,'10':10
                ,'9':9
                ,'8':8
                ,'7':7
                ,'6':6
                ,'5':5
                ,'4':4
                ,'3':3
                ,'2':2
                ,'A':1
                }
        
def cards_are_in_sequence(values):
    sorted_hand = sorted(values)
    for i in range(len(sorted_hand) - 1):
        if ACE_HIGH_RANK[sorted_hand[i]] != ( ACE_HIGH_RANK[sorted_hand[i+1]]-1 ):
            return False
    return True

def value_counts(values):
    return [values.count(c) for c in set(values)]

def poker_hand(hand):

    suits = []
    values = []

    for card in hand:
        suits.append(card.suit)
        values.append(card.value)

    if all(v in values for v in ['A','K','Q','J','10']) and len(set(suits)) == 1:
        return BestHand.ROYAL_FLUSH

    elif cards_are_in_sequence(values) and len(set(suits)) == 1:
        return BestHand.STRAIGHT_FLUSH
    
    elif 4 in value_counts(values):
        return BestHand.FOUR_OF_A_KIND
    
    elif 3 in value_counts(values) and 2 in value_counts(values):
        return BestHand.FULL_HOUSE
    
    elif len(set(suits)) == 1:
        return BestHand.FLUSH
    
    elif cards_are_in_sequence(values):
        return BestHand.STRAIGHT

    elif 3 in value_counts(values):
        return BestHand.THREE_OF_A_KIND
    
    elif len(set(values)) == 3:
        return BestHand.TWO_PAIR
    
    elif len(set(values)) == 4:
        return BestHand.PAIR
    
    else:
        return BestHand.HIGH_CARD


def high_card(hand):

    # TODO: Does not yet handle situation where two players have full houses 
    # with equal triplets or two pair with equal high pair (i.e. situations
    # where a second-highest card would have to be examined.
    values = []
    max_value = -1
    for card in hand:
        values.append(ACE_HIGH_RANK[card.value])
    best_hand = poker_hand(hand)
    if best_hand.name in ['ROYAL_FLUSH', 'STRAIGHT_FLUSH', 'FLUSH', 'STRAIGHT', 'HIGH_CARD']:
        max_value = max(values)
    elif best_hand.name in ['FOUR_OF_A_KIND', 'FULL_HOUSE', 'THREE_OF_A_KIND', 'PAIR']:
        max_count = max([values.count(value) for value in values])
        for value in values:
            if values.count(value) == max_count:
                max_value = value
    elif best_hand.name == 'TWO_PAIR':
        pairs = set()
        for value in values:
            if values.count(value) == 2:
                pairs.update(value)
        max_value = max(pairs)
    return max_value



#    high_card = None
#    for card in hand:
#        if not high_card or ACE_HIGH_RANK[card.value] > ACE_HIGH_RANK[high_card.value]:
#            high_card = card
