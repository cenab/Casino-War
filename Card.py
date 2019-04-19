class Card:
	def __init__(self, rank, suit):
		self.__rank = rank
		self.__suit = suit
		return
	def get(self):
		return self.__rank + self.__suit

	def get_rank(self):
		assert self.__rank == "2" or self.__rank == "3" or self.__rank == "4" or self.__rank == "5" or self.__rank == "6" or self.__rank == "7" or self.__rank == "8" or self.__rank == "9" or self.__rank == "T" or self.__rank == "J" or self.__rank == "Q" or self.__rank == "K" or self.__rank == "A", "Invalid Rank"
		return self.__rank

	def get_suit(self):
		assert self.__suit == "H" or self.__suit == "C" or self.__suit == "D" or self.__suit == "S", "Invalid Suit"
		return self.__suit

	def convert_rank(self, rank):
		if rank.isdigit() == True:
			return int(rank)
		elif rank == "T":
			return 10
		elif rank == "J":
			return 11
		elif rank == "Q":
			return 12
		elif rank == "K":
			return 13
		elif rank == "A":
			return 14
	def __gt__(self, other):
		return self.convert_rank(self.__rank) > other.convert_rank(other.__rank)


	def __lt__(self, other):
		return self.convert_rank(self.__rank) < other.convert_rank(other.__rank)

	def __eq__(self, other):
		return self.convert_rank(self.__rank) == other.convert_rank(other.__rank)
	def __str__(self):
		#TODO
		return str(self.__rank) + str(self.__suit)
