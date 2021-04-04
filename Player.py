from random import shuffle
class Rebel():
	def __init__(self):
		self.faction = "Rebel Faction"
		self.points = 0
		self.strategy = StratageyCard.Stratagey()
		self.influence = 2
		self.discard = []
		self.deck = ResourseCard.Resource()
		self.reserve = ResourceCard.Reserve()
		self.hand = []
		print("Choose 4 character resource cards to add to your deck.")
		for i in range(4):
			self.add_character()
		shuffle(self.deck)

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
				i = int(input(f"\t{question}\n")
				if i < 1 and i > max:
					raise IndexError
				else:
					return i-1
				except IndexError:
					print("\tThat isn't a valid card!")
				except ValueError:
					print("\tThat wasn't a number!")

	def add_character(self):
		print("Avaliable character cards to add:")
		if not len(self.reserve):
			print("No characters are left in your reserve!")
		else:
			print(self.reserve)
			i = get_num("What Reserve Character do you want to add?",len(self.reserve))
			card = self.reserve[i]
			self.deck.append(card)
			self.reserve.remove(card)

	def gain_influence(self, num):
		self.influence += num
	
	def use_influence(self, num):
		self.influence -= num
		if self.influence < 1:
			self.influence = 0

	def view_hand(self):
		print(f"You currently have {len(self.hand) cards in play for a total value of {self.value}.")
		for card in self.hand:
			print(card)
	
	def play_a_card(self):
		print("You play a card:")
		if not len(self.deck):
			print("\tYou're out of resource cards! Shuffeling your discard pile into your deck.")
			self.hand = self.discard[:]
			self.discard = []
			shuffle(self.hand)
		card = self.deck.pop(0)
		self.hand.append(card)
		print(card)
		print(f"\tYour current resource value is {self.value}")

	def spend_influence(self):
		running = True
		print("You choose to spend an Influence token:")
		if not self.influence:
			print("\tYou don't have any Influence tokens left to spend.")
		else:
			while running:
				print("\tChoose a resource to recharge:")
				list_hand(self.hand)
				i = get_num("What resource do you want to recharge?", len(self.hand))
				card = self.hand[i]
				if card.status:
					self.use_influence(1)
					card.status == True
					running == False
				if running:
					print(f"\tThat resourse isn't exhausted, try again.")
				else:
					print(f"\t\"{card.name}\" has been recharged. You have {self.influecne} Influence tokens left.")

	def use_a_power(self):
		running = True
		print("You choose to use a power:")
		while running:
			print("\tChoose a resourse power:")
			i = get_num("What card's power would you like to use?",len(self.hand))
			if self.hand[i].status:
				card.status == False
				running == False
				self.power(card)
			if running:
				print(f"\tCouldn't find a ready \"{choice}\" card, try again.")
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
		elif card.name in ResourceCard.Reserve.REBELLION_CHARACTERS:
			self.rebel_character()
		else:
			print("Something broke in Rebel.power() or Rebel.use_a_power(), this message shouldn't be possible")

	def diplomacy(self):
		running = True
		while running:
			print("\tChoose a card to discard:")
			list_hand(self.hand)
			i = get_num("Which card should be discarded?", len(self.hand))
			card = self.hand[i]
			self.discard.append(card)
			self.hand.remove(card)
			running = False
		if running:
			print("This shouldn't be possible unless you're out of cards - which you can't be because you're using a diplomacy card right now.")
			running = False
		else:
			print(f"\"{card.name}\" has been discarded.")
				
	def force(self):
		running = True
		all_exhausted = False
		while running:
			choice = 0
			while choice not in ("Y","O"):
				choice = input("\tWould you like to exhause one of (Y)our cards or one of your (O)pponents?\n").title()
			if choice == "Y":
				for card in self.hand:
					if card.status:
						all_exhausted = False
				if len(self.hand) == 0 or all_exhausted:
					print("You don't have any resourses to exhaust!")
					continue
				print("\tChoose one of your cards to exhaust:")
				i = 1
				for card in self.hand:
					print(f"\t{i} -- {card.name}: Exhausted:{not card.status}")
					i += 1
				try:
					i = int(input("\tWhich card should be exhausted?\n")
					if (i-1) < i:
						raise IndexError
					card = self.hand[i-1]
					if card.staus:
						self.hand[i-1].status = False
						running = False
					else:
						print(f"\t\"{card.name}\" is already exhausted!")
				except IndexError:
					print("\tThat isn't a valid card!")
				except ValueError:
					print("\tThat wasn't a number!")
			else:
				for card in Empire.hand:
					if card.status:
						all_exhausted = False
				if len(Empire.hand) == 0 or all_exhauseted:
					print("Your opponent doesn't have any resources to exhaust!")
					continue
				print("\tChoose one of your opponent's cards to exhaust:")
				i = 1
				for card in Empire.hand:
					print(f"\t{i} -- {card.name}: Exhausted: {not card.status}\n\t\t{card.power}")
					i += 1
				try:
					i = int(input("Which card should be exhausted?\n")
					if (i-1) < i:
						raise IndexError
					card = Empire.hand[i-1]
					if card.status:
						Empire.hand[i-1].status = False
						running = False
					else:
						print(f"\t\"{card.name}\" is already exhausted!")
				except IndexError:
					print("\tThat isn't a valid card!")
				except ValueError:
					print("\tThat wasn't a number!")

	def military(self):
		running = True
		while running:
			if len(Empire.hand) == 0:
				print("Your opponent doesn't have any resources left to discard!")
				running = False
				continue
			print("\tChoose one of your opponents resources to discard:")
			i = 1
			for card in Empire.hand:
				print(f"\t{i} -- {card.name}:{card.value}")
				if card.status:
					print(f"\t\t{card.power}

			
