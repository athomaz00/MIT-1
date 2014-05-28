class Animal:
	isDog = False
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def birthday(self):
		self.age = self.age + 1
	def inDogYears(self):
		if not self.isDog:
			return self.age * 7
		else:
			return self.age

Animal
# class, Animal

snuffy = Animal('Aloysius Snuffleupagus', 25)
garfield = Animal('Garfield', 32)
george = Animal('Curious George', 70)
snoopy = Animal('Snoopy', 60)
garfield.birthday
# method, birthday
snoopy.inDogYears()
# int, 420
snoopy.birthday()
snoopy.inDogYears()
# int, 427
snoopy.isDog = True
snoopy.inDogYears()
# int,  61
snuffy.isDog = False
Animal.isDog = True
snuffy.inDogYears()
# int, 175
george.inDogYears()
# int, 70