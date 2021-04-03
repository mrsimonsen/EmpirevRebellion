# 24 resource cards per side
# split into 16 Regular and 8 Heroes
# 16 regualr cards splits into 4 groups
# mechanics that make card powers not workd (can also happen to heros)
Unresolvable_cards = []
# 8 Hero cards per faction
HERO_READY = 6
HERO_EXAUST = 1
# Rebellion reserve
RHeroes = ("Chewbaca", "Han Solo", "Lando Calrissian", "Leia Organa", "Luke Skywalker", "Obi-Wan Kenobi", "R2-D2 and C-3PO", "Yoda")
RDescriptions = (
			"Exhaust up to 2 of your opponet's resource cards of your choice.",
			"Search your resource deck for 1 card of your choice and play it. Then shuffle your resource deck.",
			"Discard any number of your resource cards of your choice. Then play an equal number of resource cards from the top of your deck.",
			"Choose 1 character resource card from your reserve. Play that card or shuffle it into your resource deck.",
			"Discard 1 of your resource cards of your choice and/or 1 of your opponent's resource cards of your choice.",
			"Play 1 resource card of your choice from your discard pile.",
			"Discard your chosen strategy card and choose a new strategy card.",
			"Gain 1 influence token.",
			)
# Empire reserce
EHeroes = ("Admiral Piett", "Boba Fett", "Darth Vader", "Emperor Palpatine", "General Veers", "Grand Moff Tarkin", "IG-88", "Jabba the Hutt")
EDescriptions = (
			"Choose 1 resource card in either discard pile. Put that card on top of its resource deck.",
			"Discard 1 of your opponet's resource cards of your choice and/or exhaust 1 resource card of your choice of either faction.",
			"Discard 1 wchausted resource card of your choice. If it is a character resource card, place it into its faction's reserve.",
			"Your opponent must discard his chosen strategy card and choose a new strategy card.",
			"Discard the top card of your resource deck. Then discard all of your opponent's resource cards with resource value less than the discarded card.",
			"Your opponent must discard 2 influence tokens.",
			"Search either resource deck for 2 cards. Then discard 1 and place the other on top of that deck after shuffling it.",
			"Look at the top card of your resource deck. You may discard 1 of your resource cards and/or play the top resource card of your deck.",
			)

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

class Resource():
	# 16 regular resource cards per side split into 4 groups
	RESOURCE = {
		"Diplomacy": "Discard this card or 1 of your other resource cards of your choice.",
		"The Force": "Exaust 1 ready resource card of your choice of either faction.",
		"Military": "Discard 1 of your opponet's resource cards of your choice.",
		"Recon": "Look at the top 2 cards of either resource deck. Discard 1 of them and place the other on the top of that deck."
		}
	def __str__(self):
		rep = "Cards for {self.faction}\n"
		for card in self.deck:
			rep += card.__str__()
	def __init__(self,faction):
		self.deck = []
		self.faction = faction
		for name in self.RESOURCE:
			for value in range(2,6):
				add(name, value, value, self.RESOURCE[name])
	
	def add(self, stuff):
		self.deck.append(Card(stuff))

	def remove(self, card):
		self.deck.remove(card)



x = Resource("Empire")
print(x)
