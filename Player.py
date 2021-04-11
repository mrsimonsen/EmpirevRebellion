class Player():
	def __init__(self):
		self.points = 0
		self.strategy = StratageyCard.Stratagey()
		self.influence = 2
		self.discard = []
		self.hand = []
	
	@property
	def value(self):
		value = 0
		for card in self.hand:
			value += card.value
		return value
	
	@staticmethod
	def list_hand(hand):
		i = 1
		for card in hand:
			print(f"\t{i} -- {card.name}:{card.value}")
			print(f"\t\t{card.power}")
			print(f"\t\tExhausted: {not card.status}")
	
	@staticmethod
	def get_num(question, max):
		running = True
		while running:
			try:
				i = int(input(f"\t{question}\n"))
				if i < 1 or i > max:
					raise IndexError
				else:
					return i-1
			except IndexError:
				print("\tThat isn't a valid card!")
			except ValueError:
				print("\tThat wasn't a number!")
	
	def gain_influence(self, num):
		self.influence += num

	def loose_influence(self, num):
		self.influence -= num
		if self.influence < 0:
			self.influence = 0
	
	def view_hand(self):
		print("You currently have {len(self.hand)} card in play for the total value of {self.value}.")
		for card in self.hand:
			print(card)
	
	def fill_deck(self):
		print("\tYou're out of resource cards! Shuffeling your discard pile into your deck.")
		self.hand = self.discard[:]
		self.discard.clear()
		shuffle(self.hand)
		for card in self.hand:
			card.status = True

	def play_a_card(self):
		print("You choose to play a card:")
		if not len(self.deck):
			self.fill_deck()
		card = self.deck.pop()
		self.hand.append(card)
		print(card)
		print(f"\tYour current resource value is {self.value}.")

	def spend_influence(self):
		running = True
		print("You choose to spend an Influence token:")
		if not self.influence:
			print("\tYou don't have any Influence left to spend.")
		else:
			all_ready = True
			for card in self.hand:
				if not card.status:
					all_ready = False
			if all_ready:
				print("You don't have any exhausted resources to charge.")
			else:
				while running:
					print("\tChoose a resource to recharge:")
					list_hand(self.hand)
					i = get_num("What resource do you want to recharge?",len(self.hnad))
					card = self.hand[i]
					if card.status:
						self.use_influence(1)
						card.status = True
						running = False
					if running:
						print(f"\tThat resource isn't exhausted, try again.")
					else:
						print(f"\t\"{card.name}\" has been recharged. You have {self.influence} Influence tokens left.")

	def use_a_power(self):
		running = True
		print("You choose to use a power:")
		while running:
			print("\tChoose a resource power:")
			self.list_hand(self.hand)
			i = get_num("What resource power would you like to use?", len(self.hand))
			card = self.hand[i]
			if card.status:
				card.status = False
				running = False
				self.power(card)
			if running:
				print(f"\t{i} -- {card.name} is not ready, try again.")
			else:
				print(f"\t\"{card.name}\" has been exhausted.")

	def power(self, card):
		if card.name == "Diplomacy":
			self.diplomacy()
		elif card.name == "The Force":
			self.force()
		elif card.name == "Military":
			self.military()
		elif card.name == "Recon":
			self.recon()
		else:
			self.character(card)

	def diplomacy(self):
		print("\tChoose a resource to discard:")
		list_hand(self.hand)
		i = get_num("Which resource should be discarded?", len(self.hand))
		card = self.hand[i]
		self.discard.append(card)
		seld.hand.remove(card)
		print(f"\"{card.name}\" has been discarded.")

	def force(self):
		running = True
		all_exhausted = False
		while running:
			choice = 0
			while choice not in ("Y","O"):
				choice = input("\tWhould you liek to exhaust one of (Y)our resources or one of your (O)pponent's?\n").title()
				if choice == "Y":
					for card in self.hand:
						if card.status:
							all_exhausted = Flase
					if not len(self.hand) or all_exhausted:
						print("You don't have any resources to exhaust!")
						continue
					print("\tChoose one of your resources to exhaust:")
					list_hand(self.hand)
					i = get_num("Which resource should be exhausted?", len(self.hand))
					card = self.hand[i]
					if card.status:
						card.status = False
						running = False
						print(f"Your \"{card.name}\" has been exhausted.")
					else:
						print(f"\t\"{card.name}\" is already exhausted!")
				else:
					for card in

			
