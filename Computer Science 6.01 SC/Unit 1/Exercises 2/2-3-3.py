from lib601 import sm

class CountingStateMachine(sm.SM):
	startState = 0

	def getNextValues(self, state, inp):
		return (state + 1, state)

class AlternateZero(CountingStateMachine):
	def getNextValues(self, state, inp):
		state, output = CountingStateMachine.getNextValues(self, state, inp)
		return (state, 0 if output % 2 == 1 else inp)