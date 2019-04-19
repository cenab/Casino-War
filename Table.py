from Card import Card
from random import shuffle
from queue import Queue

class Table:
	# initialize several values that are important encapsulated components of this class
	def __init__(self):
		self.__player_card = None
		self.__dealer_card = None
		self.__discard = Queue()
		self.__shoe = None
		self.__bet = None
		return

	#compares the ranks of the class with another class and comes up the winner of the round
	def resolve_round(self, player, dealer):
		if player.get_rank() > dealer.get_rank():
			return 1
		if player.get_rank() == dealer.get_rank():
			return 0
		if player.get_rank() < dealer.get_rank():
			return -1

	#gets an intiget input and sets it as the self.__bet
	def set_bet(self, bet):
		self.__bet = bet
		return

	#returns to self.__bet without getting any parameter
	def get_bet(self):
		return self.__bet

	#dequeues all the elements in the self.__shoe and enqueues them to self.__discard one by one
	def clear(self):
		for i in range(self.__shoe.size()):
			self.__discard.enqueue(self.__shoe.dequeue())
		return

	#returns to the lenght of the self.__shoe
	def get_size(self):
		return len(self.__shoe)

	#creates a deck using combination of all of the ranks and suits and puts them into a list as a class
	def create_deck(self):
		ranklist = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
		suitlist = ["H", "C", "D", "S"]
		deck = []
		for rank in ranklist:
			for suit in suitlist:
				deck.append(Card(rank, suit))
		return deck

	#creates a list of the combination of rank and suit and checks if every element given as an input
	#is in the list created and deletes every element in the created list
	def validate_deck(self, deck):
		ranklist = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
		suitlist = ["H", "C", "D", "S"]
		validcardlist = []
		for rank in ranklist:
			for suit in suitlist:
				card = rank + suit
				validcardlist.append(card)
		if len(deck) != 52:
			return False
		for card in deck:
			if card.get().upper() in validcardlist:
				validcardlist.remove(card.get().upper())
			else:
				return False
		return True

	#shuffles the cards in the particular way specified in the assignment description
	#validates the deck and adds the list
	def make_shoe(self):
		queue1 = Queue()
		queue2 = Queue()
		queue3 = Queue()
		decklist = []
		for i in range(6):
			getdeck = []
			deck = self.create_deck()
			for card in deck:
				getdeck.append(card.get())
			assert self.validate_deck(deck) == True, "Invalid deck, given deck is not valid"
			decklist.append(deck)
		for i in range(6):
			shuffle(decklist[i])
			if i < 3:
				for j in decklist[i]:
					queue1.enqueue(j)
			if 3 <= i:
				for t in decklist[i]:
					queue2.enqueue(t)
		for i in range(6):
			shufflelist = []
			for i in range(26):
				shufflelist.append(queue1.dequeue())
				shufflelist.append(queue2.dequeue())
			shuffle(shufflelist)
			for card in shufflelist:
				queue3.enqueue(card)
		self.__shoe = queue3
		return self.__shoe

	def get_shoe(self):
		return self.__shoe

	def set_shoe(self, shoe):
		self.__shoe = shoe
		return

	def dequeue(self):
		return self.__shoe.dequeue()

	def dequeueshow(self):
		card = self.__shoe.dequeue()
		return card.get(), card
