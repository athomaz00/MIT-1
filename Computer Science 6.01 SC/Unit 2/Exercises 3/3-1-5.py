from lib601 import sm

class SumTSM(sm.SM):
    """
    Returns the sum of the inputs so far until the sum is greater than
    one-hundred.
    """
    startState = 0
    
    def getNextValues(self, state, inp):
        return (state + inp, state + inp)

    def done(self, state):
        return state > 100
        
class Repeat(sm.SM):
    def __init__(self, smachine, n):
        """
        Args:
            smachine: a state machine to be repeated
            n: the number of times to repeat the machine
        """
        self.n = n
        self.smachine = smachine
        self.startState = (0, smachine.startState)

    def advanceIfDone(self, counter, smState): 
        while self.smachine.done(smState) and not self.done((counter, smState)): 
            counter = counter + 1 
            smState = self.smachine.startState 
        return (counter, smState)

    def getNextValues(self, state, inp):
        (counter, smState) = state
        (smState, o) = self.smachine.getNextValues(smState, inp)
        (counter, smState) = self.advanceIfDone(counter, smState)
        return ((counter, smState), o)

    def done(self, state):
        counter, smState = state
        return counter == self.n

class CountUpTo(sm.SM):
    def __init__(self, n):
        """
        Args:
            n: The number to count to.
        """
        self.n = n
        self.startState = 0

    def getNextValues(self, state, inp):
        return (state + 1, state + 1)

    def done(self, state):
        return state == self.n

class Sequence(sm.SM): 
    def __init__(self, smList):
        self.smList = smList
        self.startState = (0, self.smList[0].startState)
        self.n = len(smList)

    def advanceIfDone(self, counter, smState): 
        while self.smList[counter].done(smState) and counter + 1 < self.n: 
            counter = counter + 1 
            smState = self.smList[counter].startState 
        return (counter, smState)

    def getNextValues(self, state, inp): 
        (counter, smState) = state 
        (smState, o) = self.smList[counter].getNextValues(smState, inp) 
        (counter, smState) = self.advanceIfDone(counter, smState) 
        return ((counter, smState), o)

    def done(self, state):
        (counter, smState) = state
        return self.smList[counter].done(smState)

def makeCountSequence(counts):
    count_sms = [CountUpTo(c) for c in counts]
    return Sequence(count_sms)




        
