from lib601 import sm

class FirstWordSM(sm.SM):
	startState = "capturing"

	def getNextValues(self, state, inp):
		if state == "capturing":
			if inp == ' ':
				return ("not capturing", None)
			else:
				return ("capturing", inp)
		else:
			if inp == "\n":
				return ("capturing", None)
			else:
				return ("not capturing", None)