from lib601 import sm

class PureFunction(sm.SM):
    startState = None
    def __init__(self, f):
        self.f = f

    def getNextValues(self, state, inp):
        return (state, self.f(inp))
