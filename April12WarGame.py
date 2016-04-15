import random

def shuffled_deck():
	deck = range(2, 15) * 4
	random.shuffle(deck)
	return deck

deck = shuffled_deck()

def player_turn(player_name):
    card = deck.pop()
    print player_name + " drew a " + str(card)
    return str(card)

while deck:
    if player_turn(player1):
