from lib601 import sm

class CommentSM(sm.SM):
	startState = "not capturing"

	def getNextValues(self, state, inp):
		if state == "not capturing":
			if inp == "#":
				return ("capturing", inp)
			else:
				return ("not capturing", None)
		else:
			if inp == "\n":
				return ("not capturing", None)
			else:
				return ("capturing", inp)

