from lib601 import sm
from threeonethree import PureFunction

class BA1(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        newState = state * 1.02
        if inp != 0:
            newState += inp - 100
        return (newState, newState)

class BA2(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        newState = state * 1.01 + inp
        return (newState, newState)

bank_one = BA1()
bank_two = BA2()
combined_bank = sm.Cascade(sm.Parallel(bank_one, bank_two), PureFunction(max))

def is_large_transaction(amount):
    return abs(amount) > 3000

def add(args):
    return args[0] + args[1]

class SwitchMachine(sm.SM):
    startState = None

    def getNextValues(self, state, inp):
        if is_large_transaction(inp):
            return (state, (inp, 0))
        else:
            return (state, (0, inp))


switchAccount = sm.Cascade(SwitchMachine(),
                    sm.Cascade(sm.Parallel2(bank_one, bank_two),
                               PureFunction(add)))
