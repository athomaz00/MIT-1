from lib601 import sm

class Delay(sm.SM):
    def __init__(self, v0):
        self.startState = v0

    def getNextValues(self, state, inp):
        # Output is old state
        return (inp, state)

class Increment(sm.SM):
    startState = 0
    def __init__(self, incr):
        self.incr = incr

    def getNextValues(self, state, inp):
        return (state, inp + self.incr)

sm1 = Delay(1)
sm2 = Delay(2)
c = sm.Cascade(sm1, sm2)
c.transduce([3,5,7,9])

# What are the inputs, states, and outputs of the two sms for the first 4 steps?
# sm1 input: 3, 5, 7, 9
# sm1 states: 1, 3, 5, 7, 9
# sm1 output: 1, 3, 5, 7
# sm2 input: 1, 3, 5, 7, 9
# sm2 states: 2, 1, 3, 5, 7
# sm2 output: 2, 1, 3, 5


sm1 = Delay(1)
sm2 = Increment(3)
c = sm.Cascade(sm1, sm2)
c.transduce([3,5,7,9])

# What are the inputs, states, and outputs of the two sms for the first 4 steps?
# sm1 input: 3, 5, 7, 9
# sm1 state: 1, 3, 5, 7, 9
# sm1 output: 1, 3, 5, 7
# sm2 input: 1, 3, 5, 7
# sm2 state: 0, 0, 0, 0
# sm2 output: 4, 6, 8, 10
