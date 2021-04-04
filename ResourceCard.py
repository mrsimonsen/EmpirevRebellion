import random as r
class Card():
	def __init__(self,name = None,ready = 0, exaust = 0, power = None):
		self.name = name
		self.ready_value = ready
		self.exaust_value = exaust
		self.power = power
		# True = Ready, False = Exausted
		self.status = True

	@property
	def value(self):
		if self.status:
			return self.ready_value
		else:
			return self.exaust_value
	
	def __str__(self):
		rep = f"Card: {self.name}\nResource Value: "
		if self.status:
			rep += f"{self.value}\nPower: {self.power}"
		else:
			rep += f"{self.value}\nPower: Exhausted"
		return rep

class Resource():
	# 16 regular resource cards per side split into 4 groups
	RESOURCE = {
		"Diplomacy": "Discard this card or 1 of your other resource cards of your choice.",
		"The Force": "Exaust 1 ready resource card of your choice of either faction.",
		"Military": "Discard 1 of your opponet's resource cards of your choice.",
		"Recon": "Look at the top 2 cards of either resource deck. Discard 1 of them and place the other on the top of that deck."
		}
	def __init__(self, deck = []):
		self.deck = deck
		for name in self.RESOURCE:
			for value in range(2,6):
				self.deck.append(Card(name, value, value, self.RESOURCE[name]))
		r.shuffle(self.deck)



class Reserve():
	#8 character resource cards per faction
	REBELLION_CHARACTERS = {
		"Chewbaca": "Exhaust up to 2 of your opponet's resource cards of your choice.",
		"Han Solo": "Search your resource deck for 1 card of your choice and play it. Then shuffle your resource deck.",
		"Lando Calrissian": "Discard any number of your resource cards of your choice. Then play an equal number of resource cards from the top of your deck.",
		"Leia Organa": "Choose 1 character resource card from your reserve. Play that card or shuffle it into your resource deck.",
		"Luke Skywalker": "Discard 1 of your resource cards of your choice and/or 1 of your opponent's resource cards of your choice.",
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
	
	def __init__(self, faction = "Imperial Faction"):
		self.reserve = []
		self.faction = faction
		if self.faction == "Rebel Faction":
			characters = list(self.REBELLION_CHARACTERS.keys())
			for i in range(8):
				if len(characters) > 1:
					x = characters.pop(0)
				else:
					x = characters[0]
				self.reserve.append(Card(x,6,1,self.REBELLION_CHARACTERS[x]))
		else:
			characters = list(self.EMPIRE_CHARACTERS.keys())
			for i in range(8):
				if len(characters) > 1:
					x = characters.pop(0)
				else:
					x = characters[0]
				self.reserve.append(Card(x,6,1,self.EMPIRE_CHARACTERS[x]))
		
	def __str__(self):
		rep = "Character card reserve:\n"
		i = 1
		for card in self.reserve:
			rep += f"{i} -- {card.name}\n\t{card.power}\n"
			i += 1
		return rep




x = Reserve("Rebel Faction")
print(x)
