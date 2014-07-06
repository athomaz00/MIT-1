import lib601.sm as sm

def accumulator(init):
    """
    Returns a state machine such that y[n] = y[n-1] + x[n] with a starting state of init.
    """
    return sm.FeedbackAdd(sm.Gain(1), sm.R(init))

def accumulatorDelay(init):
    """
    Returns a state machine such that y[n] = y[n-1] + x[n-1] witgh a starting state of init.
    """
    return sm.Cascade(accumulator(init), sm.R(init))

def accumulatorDelayScaled(s, init):
    """
    Returns a state machine such that y[n] = y[n-1] + sx[n-1].
    """
    return sm.Cascade(accumulatorDelay(init), sm.Gain(s))
