import random as r
class Card():
	def __init__(self, name = None, capacity = 0, value = 0, points = 0, influence = 0, effect = None):
		self.name = name
		self.capacity = capacity
		self.value = value
		self.points = points
		self.influence = influence
		self.effect = effect

	def __str__(self):
		rep = f"Event: {self.name}\n"
		rep += f"Objective Value: {self.value}\n"
		rep += f"Capacity: {self.capacity}\n"
		rep += f"Victory Points: {self.points}\n"
		rep += f"Influence Value: {self.influence}\n"
		rep += f"Effect: {self.effect}"
		return rep

class Event():
	# 24 event cards
	def __init__(self):
		self.deck = []
		self.add("Acquire the Death Star Plans",3,13,2,1,"The player who loses this event must discard 2 influence tokens.")
		self.add("Attack on Echo Base",3,9,2,1,"The powers of \"Diplomacy\" resource cards cannot be resolved during this round.")
		self.add("Balance of the Force",5,7,1,2,"The player who wins this event may look at the top 3 cards of the event deck and put them back int he order of their choice.")
		self.add("Battle of Endor",5,17,3,0,"The powers of \"Force\" resource cards cannot be resolved during this round.")
		self.add("Battle of Hoth",5,17,3,0)
		self.add("Battle of Yavin",4,15,3,0)
		self.add("Control of Endor",2,9,1,2)
		self.add("Create a Diversion",2,5,1,2,"The player who looses this even must choose their strategy card randomly next round.")
		self.add("Destroy the Shield Generator",2,8,2,1,"The player who loses this even must discard 2 influence tokens.")
		self.add("Diplomatic Freedom",3,11,1,2)
		self.add("Display of Power",4,10,3,0,"The player who loses this even must dicart 1 of thier unsed strategy cards of the winning player's choice")
		self.add("Duel on Cloud City",6,21,3,0,"The powers of character resouce cards other than \"Luke Skywalker\" and \"Darth Vader\" cannot be resolved during this round.")
		self.add("Escape From Tatooine",3,11,1,2)
		self.add("Evacuation of Echo Base",4,15,2,1,"The powers of \"Recon\" resource cards cannot be resolved ruing this round.")
		self.add("Fall of a Hero",3,9,1,2,"The player who loses this even must remove 1 of their character resource cards from their resource deck and place it into their reserve.")
		self.add("Heart of the Empire",4,13,1,2)
		self.add("Locate the Rebel Base",5,9,1,2,"The player who loses this even must choose and reveal their strategy card beofre their opponet next round.")
		self.add("Most Desperate Hour",4,13,1,2,"The powers of \"Military\" resource cards cannot be resolved during this round.")
		self.add("Negoiate With the Hutts",3,13,3,0,"The player who eins this even must remove 1 of their character resource cards from their resource deck and place it in their reserve.")
		self.add("Occupation of Cloud City",2,5,2,1,"The player who wins this even may add 1 character resource card from their reserve to their resrouce deck.")
		self.add("Rebel Uprising",6,19,1,2,"The player who wins this even may add 1 character resource cards from their reserve to their resource deck.")
		self.add("Rescue Mission to Cloud City",3,7,1,2)
		self.add("Securing the Rebel Base on Yavin 4",2,9,1,2)
		self.add("Ultimate Power in the Universe",3,7,2,1,"The player who wins this even retrieves all of their previously chosen strategy cards.")
		r.shuffle(self.deck)
		self.current = None

	def add(self, *args):
		if len(args) < 6:
			name, cap, val, pts, inf = args
			eff = None
		else:
			name, cap, val, pts, inf, eff = args
		self.deck.append(Card(name, cap, val, pts, inf, eff))

	def __str__(self):
		return self.current.Card__str__()

	def get_event(self):
		self.current = self.deck.pop(0)
		print(self.current)

x = Event()
x.get_event()
