from frandom import shuflfle
class Empire(Player):
	def __init__(self):
		super().__init__(self)
		self.faction = "Imperial Faction"
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
			i = self.get_num("What character resource do you want to add?", len(self.reserve))
			card = self.reserve[i]
			self.reserve.remove(card)
			return card

	def exhaust(self):
		running = True
		if self.have_ready(self.hand):
			while running:
				print("\tChoose an Empire resource to exhaust:")
				self.list_hand(self.hand)
				i = self.get_num("Which resource should be exhausted?", len(self.hand))
				card = self.hand[i]
				if card.status:
					card.status = False
					running = False
					print(f"Empire's \"{card.name}\" has been exhausted.")
				else:
					print("\t\"{card.name}\" is already exhausted, choose a different resource!")
		else:
			print("They don't have any resources to exhaust!")

	def discard(self):
		running = True
		if len(self.hand):
			print("\tChoose a Empire resource to discard:")
			self.list_hand()
			i = self.get_num("Which resource should be discarded?", len(self.hand))
			card = self.hand[i]
			self.discard_pile.append(card)
			self.hand.remove(card)
			print(f"Empire's \"{card.name}:{card.value}\" resource has been discarded.")
		else:
			print("The Empire doesn't have any resources left to discard!")

	def r_deck(self):
		if len(self.deck) < 2:
			self.fill_deck()
		cards = (self.deck.pop(), se;f.deck.pop())
		print(f"\tCjppse a respirce tp lee[ amd a respirce tp doscard for the Empire:")
		self.list_hand(cards)
		i = self.get_num("Which resource should be kept?",2)
		self.deck.append(cards[i])
		self.discard_pile.append(cards[int(not i)])
		print("\"{self.deck[-1].name}\" kept and \"{self.discard_pile[-1].name}\" discarded.")

	def character(self, card):
		if card.name == "Admiral Piett":
			self.piett()
		elif card.name == "Boba Fett":
			self.boba()
		elif card.name == "Darth Vader":
			self.vader()
		elif card.name == "Emperor Palpatine":
			self.emperor()
		elif card.name == "General Veers":
			self.veers()
		elif card.name == "Grand Moff Tarkin":
			self.tarkin()
		elif card.name == "IG-88":
			self.ig()
		elif card.name == "Jabba the Hutt":
			self.jabba()

	def piett(self):
		print("\tChoose a resource card from either discard pile to place on top of the resource deck:")
		if len(self.discard_pile):
			print(f"\t\t(E)mpire    - {self.discard_pile[-1]}")
			E = True
		else:
			print(f"\t\tEmpire    - no discarded resources!")
			E = False
		if len(Rebel.discard_pile):
			print(f"\t\t(R)ebellion - {Rebel.discard_pile[-1]}")
			R = True
		else:
			print(f"\t\tRebellion - no discarded resources!")
			R = False
		if E and R:
			fac = 'a'
			while f not in ('e','r'):
				f = input("Choose a faction:\n").lower()
		elif E:
			fac = 'e'
		elif R:
			fac = 'r'
		else:
			fac = None
		if not fac:
			print("Neither faction has an discarded resources.")
		else:
			if fac == 'r':
				card = Rebel.discard_pile.pop()
				Rebel.deck.append(card)
				print(f"\"{card.name}\" placed on top of Rebellion resource deck")
			else:
				card = self.discard_pile.pop()
				self.deck.append(card)
				print(f"\"{card.name}\" placed on top of Empire resource deck")

	def boba(self):
		c = 'a'
		while c not in ('y','n'):
			c = input("\tWould you like to discard a Rebellion resource?Y/n").lower()
		if c == 'y' and len(Rebel.hand):
			print("\tWhich Rebellion resource would you like to discard?")
			self.list_hand(Rebel.hand)
			i = self.get_num("Which Rebel resource should be discarded?")
			card = Rebel.hand.pop(i)
			Rebel.discard_pile.append(card)
			print(f"\"{card.name}\" has been discarded.")
		elif not len(Rebel.hand):
			print("The Rebellion has no resources to discard")
		c = 'a'
		while c not in ('r','e','n'):
			c = input("\tWould you like to exhaust a (R)ebellion resource, (E)mpire resource, or (N)iether?\n").lower()
		if c == 'r' and len(Rebel.hand):
			if self.have_ready(Rebe.hand):
				print("\tWhich Rebellion resource would you like to exhaust?")
				self.list_hand(Rebel.hand)
				i = self.get_num("Which Rebel resource should be exhausted?", len(Rebel.hand))
				card = Rebel.hand[i]
				if card.status:
					card.status = False
					print(f"\"{card.name}\" has been exhausted.")
				else:
					print(f"\t{card.name}\" is already exhausted!")
			else:
				print("All of the Rebellion's resources are already exhausted!")
		elif c == 'e' and len(self.hand):
			if self.have_ready(self.hand):
				print("\tWhich Empire resource would you like to exhaust?")
				self.list_hand(self.hand)
				i = self.get_num("Which Imperial resource should be exhausted?", len(self.hand))
				card = self.hand[i]
				if card.status:
					card.status = False
					print(f"\"{card.name}\" has been exhausted.")
				else:
					print(f"\"{card.name}\" is already exhausted!")
			else:
				print("All of the Empire's resources are already exhausted!")
		elif c == 'r' and not len(Rebel.hand):
			print("The Rebellion doesn't have any resources to exhaust!")
		elif c == 'e' and not len(self.hand):
			print("The Empire doesn't have any resources to exhaust!")


	def vader(self):
		c = input("Would you like to discard an exhausted (E)mpire resource or (R)ebellion resource?\n").lower()
		exhausted_cards = []
		if c == 'r':
			for card in Rebel.hand:
				if not card.status:
					exhausted_cards.append(card)
			if len(exhausted_cards):
				print("\tWhich Rebellion exhaused resourse whould you like to discard?")
				self.list_hand(exhausted_cards)
				i = self.get_num("Which Rebel resourse should be discarded?", len(exhausted_cards))
				card = exhausted_cards[i]
				if card.name not in ("Recon","Military","The Force","Diplomacy"):
					Rebel.hand.remove(card)
					Rebel.reserve.append(card)
					print(f"Exhausted {card.name} has been returned to the Rebellion's reserve.")
				else:
					Rebel.hand.remove(card)
					Rebel.discard.append(card)
					print(f"Rebellion's exhausted {card.name} has been discarded.")
			else:
				print("The Rebellion doesn't have any exhaused resources!")
		elif c == 'e':
			for card in self.hand:
				if not card.status:
					exhausted_cards.append(card)
			if len(exhausted_cards):
				print("\tWhich Imperial exhaused resourse whould you like to discard?")
				self.list_hand(exhausted_cards)
				i = self.get_num("Which Empire resourse shoudl be discarded?", len(exhausted_cards))
				card = exhausted_cards[i]
				if card.name not in ("Recon", "Military", "The Force", "Diplomacy"):
					self.hand.remove(card)
					self.reserve.append(card)
					print(f"Exhausted {card.name} has been returned to the Empire's reserve.")
				else:
					self.hand.remove(card)
					self.discard.append(card)
					print(f"Empire's exhausted {card.name} has been discarded.")
			else:
				print("The Empire doesn't have any exhaused resources!")

	def emperor(self):
		print("The Rebellion must choose a new strategy card.")
		Rebel.
	def veers(self):
	def tarkin(self):
	def ig(self):
	def jabba(self):
