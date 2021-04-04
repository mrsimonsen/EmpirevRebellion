from random import choice
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
			self.deck.append(Card(card,CARDS[card]))
		self.current = None
		self.discard = []

	def refill(self):
		self.deck = self.discard[:]
		self.discard.clear()				

	def __str__(self):
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


x = Strategy()
x.choose(True)
