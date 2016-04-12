import random

def shuffled_deck():
	basic_deck = range(2, 15) * 4
	random.shuffle(basic_deck)
	return basic_deck
