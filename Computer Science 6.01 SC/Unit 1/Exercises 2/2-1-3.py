from lib601 import sm
class Delay2Machine(sm.SM):
	def __init__(self, val0, val1):
		self.startState = (val0, val1)

	def getNextValues(self, state, input):
		previous_state, state = state
		return ((state, input), previous_state)