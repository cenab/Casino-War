from Player import Player
from Table import Table
from Card import Card
from queue import Queue

#in the main function we call game function which is the integral part of the game, we call several
#parameters from inside of the main such as player and table class and stat variables
def main():
	print("Welcome to Casino War")
	print("")
	player = Player()
	table = Table()
	shoe = table.make_shoe()
	playnumber = 0.0
	wargames = 0.0
	averagebet = 0.0
	averageprofit = 0.0
	gameswon = 0.0
	print("First hand of the shoe, burning one card.")
	table.dequeue() #we dequeue the first card
	game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
	return

#this is the real game function
def game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe):
	if shoe.size() < (312*0.16): #if shoe falls under 60 percent it just discards all the cards and make a new shoe
		table.clear()
		shoe = table.make_shoe()
	print("Play(P)")
	print("Buy chips(B)")
	try:
		n = str(input("Quit(Q): "))
	except:
		print("Invalid choice, choices includes P, B, and Q.")
		game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
	if n.upper() == "P":
		print("Place your bet!")
		try:
			bet = int(input("The bet should be an even number 2-100: "))
		except:
			print("Bet should be an intiger")
			game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
		#meeting couple of spesifications spesified in the assignment description about betting
		if bet % 2 == 1:
			print("Bet is not even number")
			print("")
			print("You currently have %d chips."%(player.get_chips()))
			print("What would you like to do?")
			game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe) #call the function again because
			#as to continue the game until you quit
		elif bet >100:
			print("Bet is too large.")
			print("")
			print("You currently have %d chips."%(player.get_chips()))
			print("What would you like to do?")
			game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
		elif bet < 2:
			print("Bet is too small.")
			print("")
			print("You currently have %d chips."%(player.get_chips()))
			print("What would you like to do?")
			game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
		table.set_bet(bet) #sets the bet inputted by user
		table.set_shoe(shoe) #creates the shoe in the main function and here we set the shoe as the official shoe
		print("No more bets!")
		playerCardValue, playerCard = table.dequeueshow() #created a function in the table class
		dealerCardValue, dealerCard = table.dequeueshow() #so that I can get the rank of the card I have dequeued
		print("Player shows %s, Dealer shows %s"%(playerCardValue, dealerCardValue))
		if playerCardValue == dealerCardValue:
			wargames = wargames + 1 #adds one to wargames for statistics at the end
			war = str(input("War!!! Would you like to go to war(W) or surrender(S)? "))
			while war.upper() != "W" or war.upper() != "S":
				print("Invalid input.")
				war = str(input("War!!! Would you like to go to war(W) or surrender(S)? "))
				if war.upper() == "W" or war.upper() == "S":
					break
			if war.upper() == "S":
				print("Player surrendered, getting the half of bet back")
				#if surrenders or looses we remove chips
				player.remove_chips(table.get_bet()/2)
			elif war.upper() == "W":
				print("We are going to war!!! You doubled up your bet.")
				table.set_bet(table.get_bet()*2)
				#dequeue three card when we go to war
				for i in range(3):
					table.dequeue()
				#player and dealer cards
				playerCardValue, playerCard = table.dequeueshow()
				dealerCardValue, dealerCard = table.dequeueshow()
				#compare the cards and come to a solution for the game
				if playerCardValue == dealerCardValue:
					#if game is tied two times player gets 4 times of their money
					table.set_bet(table.get_bet()/2)
					print("Player tied two times gets the four times of the bet")
					player.add_chips(table.get_bet())
					#adds up stats
					playnumber = playnumber + 1
					averagebet = averagebet + table.get_bet()
					averageprofit = averageprofit + table.get_bet()
					gameswon = gameswon
					game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
				elif playerCardValue > dealerCardValue:
					print("Player wins!")
					player.add_chips(bet)
					print("")
					print("You currently have %d chips."%(player.get_chips()/2))
					print("What would you like to do?")
					playnumber = playnumber + 1
					averagebet = averagebet + table.get_bet()
					averageprofit = averageprofit + table.get_bet()
					gameswon = gameswon
					game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
				elif playerCardValue < dealerCardValue:
					print("Dealer wins.")
					player.remove_chips(table.get_bet())
					print("")
					print("You currently have %d chips."%(player.get_chips()))
					print("What would you like to do?")
					playnumber = playnumber + 1
					averagebet = averagebet + table.get_bet()
					averageprofit = averageprofit - table.get_bet()
					gameswon = gameswon
					game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
		elif playerCardValue > dealerCardValue:
			print("Player wins!")
			player.add_chips(table.get_bet())
			print("")
			print("You currently have %d chips."%(player.get_chips()))
			print("What would you like to do?")
			playnumber = playnumber + 1
			averagebet = averagebet + table.get_bet()
			averageprofit = averageprofit + table.get_bet()
			gameswon = gameswon + 1
			game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
		elif playerCardValue < dealerCardValue:
			print("Dealer wins.")
			player.remove_chips(table.get_bet())
			print("")
			print("You currently have %d chips."%(player.get_chips()))
			print("What would you like to do?")
			playnumber = playnumber + 1
			averagebet = averagebet + table.get_bet()
			averageprofit = averageprofit - table.get_bet()
			gameswon = gameswon
			game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
	elif n.upper() == "B":
		buy = int(input("How many chips would you like to buy?(1-1000): "))
		player.add_chips(buy)
		print("")
		print("You currently have %d chips."%(player.get_chips()))
		print("What would you like to do?")
		game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)
	elif n.upper() == "Q":
		print("Played %.2f hands."%(playnumber))
		print("From these hands, %.2f were war hands"%(wargames))
		print("The average bet was %.2f chips"%(averagebet))
		print("The average profit of the session was %.2f"%(averageprofit))
		print("Player won %.2f out of %.2f hands, or %.2f"%(gameswon, playnumber, gameswon/playnumber *100), "%")
		print("Goodbye")
		return
	else:
		print("")
		game(player, table, playnumber, wargames, averagebet, averageprofit, gameswon, shoe)

def auto_play(n, bet = 0): #gets n as an input and bet as an input which equals to zero with this way we dont have to type the bet while quitting the game
	try: #creates the files if they dont exist and closes
		a = open("autoplay_amount.txt", "x")
		ashoe = open("autoplay_shoe.txt", "x")
		astat = open("autoplay_statistics.txt", "x")
		astat.close()
		ashoe.close()
		a.close()
	except:
		#just to use try and except, use a useless variable
		b= 0
	try:
		n = str(n)
		bet = int(bet)
	except:
		return -1
	player = Player()
	table = Table()
	#creates the files which can be read and appended
	f = open("autoplay_amount.txt", "r+")
	fshoe = open("autoplay_shoe.txt", "r+")
	fstat = open("autoplay_statistics.txt", "r+")
	readlinesstat = fstat.read()
	#getting the last stat values or if they dont exist we are creating them and equal them to zero
	if readlinesstat != "":
		readlinesstatlist = readlinesstat.split("\n")
		readlinesstatlist.remove('')
		lateststat = readlinesstatlist[len(readlinesstatlist)-1]
		lateststat = lateststat.split(" ")
		playnumber = float(lateststat[0])
		wargames = float(lateststat[1])
		averagebet = float(lateststat[2])
		averageprofit = float(lateststat[3])
		gameswon = float(lateststat[4])
	else:
		playnumber = 0.0
		wargames = 0.0
		averagebet = 0.0
		averageprofit = 0.0
		gameswon = 0.0
	readlines = f.readlines()
	readlinesshoe = fshoe.read()
	#call the amount of chips we have
	if readlines != []:
		amount = int(readlines[-1][:-1])
		for i in range(amount):
			player.add_chips(1)
	#this part is very similar to main and game function
	if n.upper() == "P":
		if bet % 2 == 1:
			return False
		elif bet >100:
			return False
		elif bet < 2:
			return False
		table.set_bet(bet)
		decklist1 = Queue()
		#turn every card into string to store in the text file and turn them to class later
		if readlinesshoe != "":
			deck = str(readlinesshoe)
			decklist = deck.split(" ")
			decklist.pop()
			for i in range(len(decklist)):
				decklist1.enqueue(Card(decklist[i][0], decklist[i][1]))
			table.set_shoe(decklist1)
			fshoe.close()
			fshoe = open("autoplay_shoe.txt", "w")
		else:
			table.make_shoe()
			table.dequeue()
		if table.get_shoe().size() < (0.12*312):
			table.clear()
			table.make_shoe()
			table.dequeue()
		playerCardValue, playerCard = table.dequeueshow()
		dealerCardValue, dealerCard = table.dequeueshow()
		if playerCardValue == dealerCardValue:
			wargames += 1
			if bet >= (player.get_chips()-table.get_bet()):
				war = "S"
			else:
				war = "W"
			if war.upper() == "S":
				print("Player surrendered, getting the half of bet back")
				table.remove_chips(table.get_bet()/2)
				f.write(str(int(player.get_chips())))
				f.write("\n")
				for card in table.get_shoe():
					fshoe.write(card.get())
					fshoe.write(" ")
				fshoe.write("\n")
				fshoe.close()
				#write everything to the files
				fstat.write("%f "%(playnumber + 1))
				fstat.write("%f "%(wargames))
				fstat.write("%f "%(averagebet + table.get_bet()))
				fstat.write("%f "%(averageprofit - table.get_bet()))
				fstat.write("%f\n"%(gameswon))
				return player.get_chips()
			elif war.upper() == "W":
				table.set_bet(table.get_bet()*2)
				for i in range(3):
					table.dequeue()
				playerCardValue, playerCard = table.dequeueshow()
				dealerCardValue, dealerCard = table.dequeueshow()
				if playerCardValue > dealerCardValue:
					player.add_chips(table.get_bet()/2)
					f.write(str(int(player.get_chips())))
					f.write("\n")
					for i in range(table.get_shoe().size()):
						showcard, card= table.dequeueshow()
						fshoe.write(showcard)
						fshoe.write(" ")
					fshoe.write("\n")
					fshoe.close()
					fstat.write("%f "%(playnumber + 1))
					fstat.write("%f "%(wargames))
					fstat.write("%f "%(averagebet + table.get_bet()))
					fstat.write("%f "%(averageprofit + table.get_bet()))
					fstat.write("%f\n"%(gameswon + 1))
					return player.get_chips()
				elif playerCardValue < dealerCardValue:
					player.remove_chips(table.get_bet())
					f.write(str(int(player.get_chips())))
					f.write("\n")
					for i in range(table.get_shoe().size()):
						showcard, card= table.dequeueshow()
						fshoe.write(showcard)
						fshoe.write(" ")
					fshoe.write("\n")
					fshoe.close()
					fstat.write("%f "%(playnumber + 1))
					fstat.write("%f "%(wargames))
					fstat.write("%f "%(averagebet + table.get_bet()))
					fstat.write("%f "%(averageprofit - table.get_bet()))
					fstat.write("%f\n"%(gameswon))
					return player.get_chips()
				elif playerCardValue == dealerCardValue:
					table.add_chips(table.get_bet())
					f.write(str(int(player.get_chips())))
					f.write("\n")
					for i in range(table.get_shoe().size()):
						showcard, card= table.dequeueshow()
						fshoe.write(showcard)
						fshoe.write(" ")
					fshoe.write("\n")
					fshoe.close()
					fstat.write("%f "%(playnumber))
					fstat.write("%f "%(wargames))
					fstat.write("%f "%(averagebet + table.get_bet()*2))
					fstat.write("%f "%(averageprofit + table.get_bet()*2))
					fstat.write("%f\n"%(gameswon))
					return player.get_chips()
		elif playerCardValue > dealerCardValue:
			player.add_chips(table.get_bet())
			f.write(str(int(player.get_chips())))
			f.write("\n")
			for i in range(table.get_shoe().size()):
				showcard, card= table.dequeueshow()
				fshoe.write(showcard)
				fshoe.write(" ")
			fshoe.write("\n")
			fshoe.close()
			fstat.write("%f "%(playnumber + 1))
			fstat.write("%f "%(wargames))
			fstat.write("%f "%(averagebet + table.get_bet()))
			fstat.write("%f "%(averageprofit + table.get_bet()))
			fstat.write("%f\n"%(gameswon + 1))
			return player.get_chips()
		elif playerCardValue < dealerCardValue:
			player.remove_chips(table.get_bet())
			f.write(str(int(player.get_chips())))
			f.write("\n")
			for i in range(table.get_shoe().size()):
				showcard, card= table.dequeueshow()
				fshoe.write(showcard)
				fshoe.write(" ")
			fshoe.write("\n")
			fshoe.close()
			fstat.write("%f "%(playnumber+1))
			fstat.write("%f "%(wargames))
			fstat.write("%f "%(averagebet + table.get_bet()))
			fstat.write("%f "%(averageprofit - table.get_bet()))
			fstat.write("%f\n"%(gameswon))
			return player.get_chips()
	elif n.upper() == "B":
		try:
			player.add_chips(bet)
			f.write(str(int(player.get_chips())))
			f.write("\n")
			return True
		except:
			return False
	elif n.upper() == "Q":
		#return to statistics
		f.close()
		fshoe.close()
		f = open("autoplay_amount.txt", "w")
		fshoe = open("autoplay_shoe.txt", "w")
		f.close()
		fshoe.close()
		fstat.close()
		stats = [playnumber, wargames, averagebet/playnumber, averageprofit/playnumber, gameswon, playnumber, gameswon/playnumber]
		fstat = open("autoplay_statistics.txt", "w")
		fstat.close()
		return stats
	else:
		return -1

if __name__ == "__main__":
	main()
