import cards
import random

# https://github.com/jeremytarling/python-tarot

def one_card():
    my_deck = cards.get_deck()
    my_card = cards.get_cards(my_deck)
    return my_card
    
def max_cards(max_cards = 4):
    my_deck = cards.get_deck()
    hand = []
    num = 1
    for num in range(max_cards):    
        my_card = cards.get_cards(my_deck)
        hand.append(my_card)
    return hand
