import random as r
class Card():
	def __init__(self,name = None,ready = 0, exaust = 0, power = None):
		self.name = name
		self.ready = ready
		self.exaust = exaust
		self.power = power
		# True = Ready, False = Exausted
		self.status = True
	
	def __str__(self):
		rep = f"Card: {self.name}\nResource Value: "
		if self.status:
			rep += f"{self.ready}\nPower: {self.power}"
		else:
			rep += f"{self.exaust}\nPower: Exhausted"
		return rep

class Regular():
	# 16 regular resource cards per side split into 4 groups
	RESOURCE = {
		"Diplomacy": "Discard this card or 1 of your other resource cards of your choice.",
		"The Force": "Exaust 1 ready resource card of your choice of either faction.",
		"Military": "Discard 1 of your opponet's resource cards of your choice.",
		"Recon": "Look at the top 2 cards of either resource deck. Discard 1 of them and place the other on the top of that deck."
		}
	def __init__(self):
		self.deck = []
		for name in self.RESOURCE:
			for value in range(2,6):
				self.add(name, value, value, self.RESOURCE[name])
		r.shuffle(self.deck)
	
	def add(self, *args):
		name, rv, ev, power = args 
		self.deck.append(Card(name, rv, ev, power))

	def remove(self, card):
		self.discard.append(card)
		self.deck.remove(card)

class Character():
	#8 character resource cards per faction
	REBELLION_CHARACTERS = {
		"Chewbaca": "Exhaust up to 2 of your opponet's resource cards of your choice.",
		"Han Solo": "Search your resource deck for 1 card of your choice and play it. Then shuffle your resource deck.",
		"Lando Calrissian": "Discard any number of your resource cards of your choice. Then play an equal number of resource cards from the top of your deck.",
		"Leia Organa": "Choose 1 character resource card from your reserve. Play that card or shuffle it into your resource deck.",
		"Obi-Wan Kenobi": "Play 1 resource card of your choice from your discard pile.",
		"R2-D2 and C-3PO": "Discard your chosen strategy card and choose a new strategy card.",
		"Yoda": "Gain 1 influence token."
		}
	EMPIRE_CHARACTERS = {
		"Admiral Piett": "Choose 1 resource card in either discard pile. Put that card on top of its resource deck.",
		"Boba Fett": "Discard 1 of your opponet's resource cards of your choice and/or exhaust 1 resource card of your choice of either faction.",
		"Darth Vader": "Discard 1 exhausted resource card of your choice. If it is a character resource card, place it into its faction's reserve.",
		"Emperor Palpatine": "Your opponent must discard his chosen strategy card and choose a new strategy card.",
		"General Veers": "Discard the top card of your resource deck. Then discard all of your opponent's resource cards with resource value less than the discarded card.",
		"Grand Moff Tarkin": "Your opponent must discard 2 influence tokens.",
		"IG-88": "Search either resource deck for 2 cards. Then discard 1 and place the other on top of that deck after shuffling it.",
		"Jabba the Hutt": "Look at the top card of your resource deck. You may discard 1 of your resource cards and/or play the top resource card of your deck."
		}		
	
	def __init__(self):
		if self.faction == "Rebel Faction":
			characters = list(self.REBELLION_CHARACTERS.keys())
			for i in range(8):
				x = chracters.pop(0)
				self.reserve.append(Card(x,6,1,self.REBELLION_CHARACTERS[x]))
		else:
			characters = list(self.EMPIRE_CHARACTERS.keys())
			for i in range(8):
				x = characters.pop(0)
				self.reserve.append(Card(x,6,1,self.EMPIRE_CHARACTERS[x]))
				print("Select 4 character resource cards to add to your deck")
		for i in range(4):
			self.add_character()

		def add_character(self):
		print("Avaliable character cards to add:")
		if not len(self.reserve):
			print("No characters are left in your reserve!")
		else:
			for i in range(len(self.reserve)):
				print(f"{i+1} - {self.reserve[i].name}\n\t{self.reserve[i].power}")
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


x = Resource("Imperial Faction")
print(x)
