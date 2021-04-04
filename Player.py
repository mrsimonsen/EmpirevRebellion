class Player():
	def __init__(self, name = "Computer", faction = "Imperial Faction"):
		self.name = name
		self.faction = faction
		self.reserve = []
		self.resource = ResourseCards.Resource()
		self.strategy = StratageyCards.Stratagey()
		self.influence = 2

