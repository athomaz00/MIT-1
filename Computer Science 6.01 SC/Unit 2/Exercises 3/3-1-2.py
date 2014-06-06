from lib601 import sm

class Cascade(sm.SM):
    def __init__(self, sm1, sm2):
        self.sm1 = sm1
        self.sm2 = sm2

    def getNextValues(self, state, inp):
        state1, state2 = state if state else (self.sm1.startState, self.sm2.startState)
        next1, output1 = self.sm1.getNextValues(state1, inp)
        next2, output2 = self.sm1.getNextValues(state2, output1)
        return ((next1, next2), output2)
