from Card import Card


def test_card():
	#Creates a card which is the Ace of Diamonds
	my_card = Card("A", "D")

	#tests get function
	assert my_card.get() == "AD", "Invalid card"
	#tests rank function
	assert my_card.get_rank() == "A", "Invalid rank"
	#tests suit function
	assert my_card.get_suit() == "D", "Invalid suit"

	#tests a rank convertion function
	assert my_card.convert_rank("A") == 14, "Invalid conversion"
	assert my_card.convert_rank("K") == 13, "Invalid conversion"
	assert my_card.convert_rank("Q") == 12, "Invalid conversion"
	assert my_card.convert_rank("J") == 11, "Invalid conversion"
	assert my_card.convert_rank("T") == 10, "Invalid conversion"
	assert my_card.convert_rank("9") == 9, "Invalid conversion"
	assert my_card.convert_rank("8") == 8, "Invalid conversion"
	assert my_card.convert_rank("7") == 7, "Invalid conversion"
	assert my_card.convert_rank("6") == 6, "Invalid conversion"
	assert my_card.convert_rank("5") == 5, "Invalid conversion"
	assert my_card.convert_rank("4") == 4, "Invalid conversion"
	assert my_card.convert_rank("3") == 3, "Invalid conversion"
	assert my_card.convert_rank("2") == 2, "Invalid conversion"

	#tests that the suit has no influence on comparison __eq__
	assert Card("A","D") == Card("A","S") == Card("A","H") == Card("A","C"), "Invalid comparison =="

	#tests rank comparison function _gt__
	assert Card("A","H") > Card("K", "H") > Card("2", "S"), "Invalid comparison >"

	#tests the __str__ function
	assert str(my_card) == "AD", "Invalid string"

	#returns True to sinalize that it has passed all tests
	return True
def test_player():
	# creates a deck
	my_player = Player()
	# adds chips while chips were zero and checks if the amount is correct
	assert my_player.add_chips(500) == 500, "Invalid addition"
	#checks for errors, lower number
	assert my_player.add_chips(0) == None, "Invalid parameter"
	#checks for errors, higher number
	assert my_player.add_chips(1100) == None, "Invalid parameter"
	#checks if there is a problem with removing the chips
	assert my_player.remove_chips(500) == 0, "Invalid subtraction"
	#gets the number of chips
	assert my_player.get_chips() == 0, "Invalid parameter"
	return True

def test_table():
	#creates the table class
	my_table = Table()
	#sets the bets and checks if we can get that bet
	my_table.set_bet(500)
	assert my_table.get_bet() == 500, "Invalid value"
	#creates a deck and puts that deck into validate_deck and checks if the created deck is valid
	assert my_table.validate_deck(my_table.create_deck()) == True, "Invalid deck"
	#creates a shoe and calls that shoe with the get_shoe function
	shoe = my_table.make_shoe()
	assert my_table.get_shoe() == shoe, "Invalid deck"
	return True
