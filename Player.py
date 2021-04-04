from random import shuffle
class Player():
	OPTIONS = ResourceCard.Resource.
	def __init__(self, name = "Computer", faction = "Imperial Faction"):
		self.name = name
		self.faction = faction
		self.points = 0
		self.strategy = StratageyCard.Stratagey()
		self.influence = 2
		self.discard = []
		self.deck = ResourseCard.Resource()
		self.reserve = ResourceCard.Reserve()
		self.hand = []
		#choose 4 character cards to add to deck, the rest go in the reserve
		for i in range(4):
			self.add_character()
		shuffle(self.deck)

	def add_character(self):
		print("Avaliable character cards to add:")
		if not len(self.reserve):
			print("No characters are left in your reserve!")
		else:
			print(self.reserve)
			card = ''
			while not card:
				choice = input("What Reserve Character do you want to add?\n")
				try:
					i = int(choice)
					if (i-1) < 0:
						raise IndexError
					card = self.reserve[i-1]
				except ValueError:
					print("That wasn't a number!")
				except IndexError:
					print("That wasn't a valid card number!")
			self.deck.append(card)
			self.reserve.remove(card)

	def gain_influence(self, num):
		self.influence += num
	
	def use_influence(self, num):
		self.influence -= num
		if self.influence < 1:
			self.influence = 0

	@property
	def value(self):
		value = 0
		for card in self.hand:
			value += card.value
		return value

	def view_hand(self):
		print(f"You currently have {len(self.hand) cards in play for a total value of {self.value}.")
		for card in self.hand:
			print(card)
	
	def play_a_card(self):
		print("You play a card:")
		card = self.deck.pop(0)
		self.hand.append(card)
		print(card)
		print(f"Your current resource value is {self.value}")

	def spend_influence(self):
		print("You choose to spend an Influence token to ready a card.")
		if not self.influence:
			print("You don't have any Influence tokens left to spend.")
		else:
			running = True
			while running:
				choice = input("What card would your like to recharge?\n").title()
				if choice not in 
				for card in self.hand:
					if card.name == choice:
						self.use_influence(1)
						card.status == True
						running == False
						break
