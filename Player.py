class Player:
	#we initialize with chips equal to zero
	def __init__(self):
		self.__chips = 0
		return

	#adds specified amount of chips to the self.__chips we give exceptions if the parameter is not intiger
	#and if it is larger or lower than some level of number it gives error
	def add_chips(self, chips):
		try:
			if not 1 <= chips <= 1000:
				raise Exception()
			self.__chips += chips
			return self.__chips
		except TypeError:
			print("Invalid transaction, chips should be intiger.")
			print("Returning to main menu.")
			return None
		except Exception:
			print("Invalid transaction, a number between 1 and 1000 should be inserted.")
			print("Returning to main menu.")
			return None

	#removes some amount of chips
	def remove_chips(self, chips):
		self.__chips -= chips
		return

	#returns the amount of chips
	def get_chips(self):
		return self.__chips
