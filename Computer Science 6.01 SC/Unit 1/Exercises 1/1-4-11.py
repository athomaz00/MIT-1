class Warehouse(object):
	def __init__(self):
		self.items = {}

	def process(self, instructions):
		command, item, number = instructions
		if command == "receive":
			try:
				self.items[item] += number
			except KeyError:
				self.items[item] = number
		elif command == "ship":
			self.items[item] -= number

	def lookup(self, item):
		try:
			return self.items[item]
		except KeyError:
			return 0

w = Warehouse()
w.process(('receive', 'a', 10))
w.process(('ship', 'a', 7))
w.lookup('a')
# 3
w.lookup('b')
# 0


