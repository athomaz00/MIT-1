class FruitSalad(object):
	servings = 4
	fruits = ["melons", "pineapples"]

	def __init__(self, fruits, servings):
		self.servings = servings
		self.fruits = fruits

	def __str__(self):
		return str(self.servings) + " of fruit salad with ", str(self.fruits)

	def add(self, fruit):
		self.fruits.append(fruit)

	def serve(self):
		if self.servings > 0:
			self.servings -= 1
			return "Enjoy"
		else:
			return "Sorry"

salad = FruitSalad(['bananas', 'apples'], 2 )
salad.add('cherries')
salad.fruits
# ['bananas', 'apples', 'cherries']
FruitSalad.fruits
# ['melons', 'pineapples']
salad.serve()
# Enjoy
salad.serve()
# Enjoy
salad.serve()
# Sorry
salad.servings
# 0
FruitSalad.servings	
# 4