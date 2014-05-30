class Hammok(object):
	sitting = False
	def sitDown(self, name):
		if not self.sitting:
			self.sitting = True
			return "welcome"
		else:
			return "sorry, hammok full"

	def leave(self):
		if self.sitting:
			self.sitting = False
			return 1
		return 0

