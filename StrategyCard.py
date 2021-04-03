import random as r
class Strategy():
	# 5 Strategy cards per side
	# all cards must be used before useing the same card again
	CARDS = {
		"Bureaucracy": "If you lose the event, gain 2 influence tokens.",
		"Deception": "When determining victory, if neither player's total resouce value exceeds the event's objective value, the player who would lose the event wins the event instead.",
		"Direct Assault": "When determing victory, increase your total resource value by 2.",
		"Infiltration": "You choose your opponent's strategy card next round.",
		"Support": "When this card is revealed, you may add 1 character resource card from you reserve to your resource deck."
		}

	def __init__(self):
		self.cards = list(Strategy.CARDS.keys())
		self.strategy = (None,"Empty Description")

	def __str__(self):
		count = len(self.cards)
		if count > 1:
			rep = f"{count} Avaliable Strategy Cards:\n"
		else:
			rep = f"{count} Avaliable Strategy Card:\n"
		for i in range(count):
			rep += f"\t{i + 1}: {self.cards[i]} - {Strategy.CARDS[self.cards[i]]}\n"
		return rep

	def choose(self, random = False):
		if random:
			card = r.choice(self.cards)
			print("Your Strategy Card will be chosen at random this round.")
		else:
			print("Choose a Strategy Card for this round.\n")
			print(self)
			card = ''
			while not card and not random:
				choice = input("What Strategy Card will you use this round?\n")
				try:
					i = int(choice)
					if (i-1) < 0:
						raise IndexError
					card = self.cards[i-1]
				except ValueError:
					print("That wasn't a number!")
				except IndexError:
					print("That wasn't a valid card number!")
		self.remove(card)
		self.strategy = (card, Strategy.CARDS[card])
		print()
		self.current()
		print()

	def remove(self, card):
		self.cards.remove(card)
		if not len(self.cards):
			self.__init__()
		
	def current(self):
		print(f"Current Strategy: {self.strategy[0]}")
		print(self.strategy[1])
		print()

x = Strategy()
x.choose(True)
