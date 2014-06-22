from lib601 import sm

negate = sm.PureFunction(lambda x: not x)
feedback = sm.Feedback(negate)
