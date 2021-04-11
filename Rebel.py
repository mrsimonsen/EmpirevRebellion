from random import shuffle
class Rebel(Player):
	def __init__(self):
		super().__init__(self)
		self.faction = "Rebel Faction"
		self.reserve = ResourceCard.Reserve(self.faction)
		print("Choose 4 character resource cards to add to your deck.")
		for i in range(4):
			card = self.add_character()
			self.deck.append(card)
		shuffle(self.deck)

	def add_character(self):
		print("Avaliable characters to add:")
		if not len(self.reserve):
			print("No characters are left in your reserve!")
		else:
			print(self.reserve)
			i = get_num("What character resource do you want to add?",len(self.reserve))
			card = self.reserve[i]
			self.reserve.remove(card)
			return card

				
	def force(self):
		running = True
		all_exhausted = False
		while running:
			choice = 0
			while choice not in ("Y","O"):
				choice = input("\tWould you like to exhaust one of (Y)our resources or one of your (O)pponent's?\n").title()
			if choice == "Y":
				for card in self.hand:
					if card.status:
						all_exhausted = False
				if len(self.hand) == 0 or all_exhausted:
					print("You don't have any resourses to exhaust!")
					continue
				print("\tChoose one of your resources to exhaust:")
				list_hand(self.hand)
				i = get_num("Which resource should be exhausted?", len(self.hand))
				card = self.hand[i]
				if card.staus:
					card.status = False
					running = False
					print(f"Your \"{card.name}\" has been exhausted.")
				else:
					print(f"\t\"{card.name}\" is already exhausted!")
			else:
				for card in Empire.hand:
					if card.status:
						all_exhausted = False
				if len(Empire.hand) == 0 or all_exhauseted:
					print("Your opponent doesn't have any resources to exhaust!")
					continue
				print("\tChoose one of your opponent's resources to exhaust:")
				list_hand(Empire.hand)
				i = get_num("Which resource should be exhausted?",len(Empire.hand))
				card = Empire.hand[i]
				if card.status:
					card.status = False
					running = False
					print(f"Opponents \"{card.name}\" has been exhausted.")
				else:
					print(f"\t\"{card.name}\" is already exhausted!")

	def military(self):
		if len(Empire.hand) == 0:
			print("Your opponent doesn't have any resources left to discard!")
		else:
			print("\tChoose one of your opponent's resources to discard:")
			list_hand(Empire.hand)
			i = get_num("Which resource should be discarded?", len(Empire.hand))
			card = Empire.hand[i]
			Empire.discard.append(card)
			Empire.hand.remove(card)
			print(f"Opponent's \"{card.name}\" resource has been discarded.")
	
	def recon(self):
		choice = 0
		while choice not in ("Y","O"):
			choice = input("\tWould you like to Recon (Y)our resources or your (O)pponent's?\n").title()
		if choice == "Y":
			if len(self.deck) < 2:
				self.fill_deck()
			cards = (self.deck.pop(),self.deck.pop())
			print(f"\tChoose a resource to keep and a resource to discard:")
			list_hand(cards)
			i = get_num("Which resource should be kept?",2)
			self.deck.append(cards[i])
			self.discard.appned(cards[int(not i)])
			print("\"{self.deck[-1].name}\" kept and \"{self.discard[-1].name}\" discarded.")
		else:
			if len(Empire.deck) < 2:
				Empire.fill_deck()
			cards = (Empire.deck.pop(),Empire.deck.pop())
			print(f"\tChoose a resource to keep and a resource to discard:")
			list_hand(cards)
			i = get_num("Which resource should be kept?",2)
			Empire.deck.append(cards[i])
			Empire.discard.appned(cards[int(not i)])
			print("\"{Empire.deck[-1].name}\" kept and \"{Empire.discard[-1].name}\" discarded.")

	def character(self, card):
		if card.name == "Chewbacca":
			self.chewbacca()
		elif card.name == "Han Solo":
			self.han()
		elif card.name == "Lando Calrissian":
			self.lando()
		elif card.name == "Leia Organa":
			self.leia()
		elif card.name == "Luke Skywalker":
			self.luke()
		elif card.name == "Obi-Wan Kenobi":
			self.kenobi()
		elif card.name == "R2-D2 and C-3PO":
			self.droids()
		elif card.name == "Yoda":
			self.yoda()
		else:
			print("this meesage shouldn't be possible, something went wrong in Rebel.rebel_characters()")

	def yoda(self):
		gain_influence(1)
		print(f"You gain 1 influence, you now have {self.influence}.")

	def kenobi(self):
		print("\tChoose a resource card from your discard pile to play:")
		list_hand(self.discard)
		i = get_num("Which resource would you like to play?",len(self.discard))
		card = self.discard[i]
		card.status = True
		self.hand.append(card)
		self.discard.remove(card)
		print("\"{card.name}\" has been played from the discard pile.")

	def leia(self):
		print("\tChoose a character resource from your reserve:")
		card = self.add_character()
		choice = 0
		while choice not in ("D","P"):
			choice = input("\tWould you like to (P)lay the card or add it to your (D)eck?\n").title()
		if chocie == "D":
			self.deck.append(card)
			shuffle(self.deck)
			print("\"{card.name}\" had been added to your resource deck and the cards have been shuffled")
		else:
			self.hand.append(card)
			print("\"{card.name}\" has been played.")

	def han(self):
		print("\tChoose a resource card from your deck to play:")
		list_hand(self.deck)
		i = get_num("Which resource would you like to play?",len(self.deck))
		card = self.deck[i]
		self.deck.remove(card)
		self.hand.append(card)
		shuffle(self.deck)
		print("\"{card.name}\" has been played and your resource deck has been shuffled.")
		print(f"\tYour current resource value is {self.value}")

	def chewbacca(self):
		all_exhausted = True
		for card in Empire.hand:
			if card.status:
				all_exhausted = False
		if len(Empire.hand) == 0 or all_exhausted:
			print("Your opponent doesn't have any resources left to exhaust!")
		else:
			num = ("1st","2nd")
			for n in num:
				selecting = True
				while selecting:
					print(f"\tChoose the {n} opponent resource to exhaust:")
					list_hand(Empire.hand)
					i = get_num("Which opponent resource should be exhausted?", len(Empire.hand))
					card = Empire.hand[i]
					if card.staus:
						card.status = False
						print(f"Opponent's \"{card.name}\" has been exhausted.")
						selecting = False
					else:
						print(f"\t\"{card.name}\" is already exhausted!")
				choice = 0
				while choice not in ("Y","N"):
					choice = input("\tWould you like to exhaust another opponent resource? (Y)es/(N)o\n").title()
				if choice == "Y":
					continue
				else:
					break
	def lando(self):
		selecting = True
		selection = []
		while selecting:
			print("\tChoose a resource to discard:")
			list_hand(self.hand)
			i = get_num("Which resource should be discarded?", len(self.hand))
			card = self.hand[i]
			selection.append(card)
			self.hand.remove(card)
			again = 0
			while again not in ("Y","N"):
				again = input("\tWould you like to discard another resource? (Y)es/(N)o\n").title()
			if again == "N":
				selecting = False
			else:
				if len(self.hand) > 0:
					print(f"\tCurrently discarding {len(selection)} resources.")
				else:
					print("\tYou don't have any resources left!")
					selecting = False
		num = len(selection)
		print(f"\tDiscarded {num} resources and now playing {num} resources.")
		for card in selection:
			self.discard.append(card)
		for i in range(num):
			self.play_a_card()

	def luke(self):
		choice = 0
		while choice not in ("B","Y","O"):
			choice = input("\tWould you like to discard 1 of (Y)our resources, 1 of your (O)pponent's resources, or (B)oth?\n")
		if choice in "BY":
			print("\tChoose a resource to discard:")
			list_hand(self.hand)
			i = get_num("Which resource should be discarded?",len(self.hand))
			card = self.hand[i]
			self.hand.remove(card)
			self.discard.append(card)
			print(f"\"{card.name}\" resource has been discarded.")
		elif choice in "BO":
			print("\tChooase a Opponent's resource to discard:")
			list_hand(Empire.hand)
			i = get_num("Which resource should be discarded?", len(Empire.hand))
			card = Empire.hand[i]
			Empire.hand.remove(card)
			Empire.discard.append(card)
			print(f"Opponent's \"{card.name}\" resource has been discarded.")

	def droids(self):
		print("\tChoose a new Strategy Card for this round:")
		self.strategy.choose()

