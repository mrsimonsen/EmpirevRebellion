import random as rand

class Card():
	def __init__(self, name = None, d = "Empty Description"):
		self.name = name
		self.description = d

	def __str__(self):
		rep = f"Strataegy: {self.name}\n{self.description}"
		return rep

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
		self.deck = []
		for card in self.CARDS.keys():
			self.deck.append(Card(card,self.CARDS[card]))
		self.current = None
		self.used = []

	def refill(self):
		self.deck += self.used[:]
		self.used.clear()

	def __str__(self):
		if not len(self.deck):
			self.refill()
		l = len(self.deck)
		if l > 1:
			rep = f"{l} Avaliable Strategy Cards:\n"
		else:
			rep = f"{l} Avaliable Strategy Card:\n"
		i = 1
		for card in self.deck:
			rep += f"{i} -- {card.name}:{card.description}\n"
			i += 1
		return rep

	def discard(self):
		self.used.append(self.current)
		self.current = None

	def choose(self, random = False):
		#fill the deck if it's empty
		if not len(self.deck):
			self.refill()
		#discard the current card
		if self.current:
			self.discard()
		# randomly selected?
		if random:
			self.current = self.deck.pop(rand.randrange(len(self.deck)))
			print("Your Strategy Card will be chosen at random this round.")
		else:# then choose your card
			print("Choose a Strategy Card for this round.\n")
			print(self)
			while not self.current:
				choice = input("What Strategy Card will you use this round?\n")
				try:
					i = int(choice)
					if (i-1) < 0:
						raise IndexError
					self.current = self.deck.pop(i-1)
				except ValueError:
					print("That wasn't a number!")
				except IndexError:
					print("That wasn't a valid card number!")
		print(self.current)

	#method of getting your card chosen for you
	@staticmethod
	def chosen(Other):
		Other.discard()
		print("Choose your opponent's Strategy Card.")
		print(Other)
		while not Other.current:
			choice = input("What Strategy Card do you choose for your opponent?\n")
			try:
				i = int(choice)
				if (i-1) < 0:
					raise IndexError
				Other.current = Other.deck.pop(i-1)
			except ValueError:
				print("That wasn't a number!")
			except IndexError:
				print("That wasn't a valid card number!")
		print(f"{Other.current.name} has been chosen for your opponent.")
