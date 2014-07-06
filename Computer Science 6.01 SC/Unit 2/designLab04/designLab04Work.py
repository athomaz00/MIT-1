import lib601.sig  as sig # Signal
import lib601.ts as ts  # TransducedSignal
import lib601.sm as sm  # SM

######################################################################
##  Make a state machine model using primitives and combinators
######################################################################

def controller(k):
    """
    Returns a state machine whose output is k times its input.
    """
    return sm.Gain(k)

def plant(t, initD):
    """
    Returns a state machine whose input is the commanded velocity
    and whose output is the distance to the wall.
    
    Args:
        t - the duration of a time step
        initD - the starting distance from the wall
    """
    movement = sm.Gain(t)
    position = sm.R(initD)
    return sm.FeedbackAdd(movement, position)

def sensor(initD):
    """
    Returns a state machine whose input should be the distance to the wall
    and whose output should be the delayed distance to the wall.
    """
    return sm.R(initD)

def wallFinderSystem(t, initD, k):
    """
    Returns a state machine whose input is the desired distance from the wall
    and whose output is the actual distance from the wall.

    Args:
        t - the duration of a time step
        initD - the starting distance from the wall
        k - Scalar for velocity of movement
    """
    return sm.FeedbackAdd(sm.Cascade(controller(k), plant(t, initD)), sensor(initD))

# Plots the sequence of distances when the robot starts at distance
# initD from the wall, and desires to be at distance 0.7 m.  Time step
# is 0.1 s.  Parameter k is the gain;  end specifies how many steps to
# plot. 

initD = 1.5

def plotD(k, end = 50):
  d = ts.TransducedSignal(sig.ConstantSignal(1.5),
                          wallFinderSystem(0.1, initD, k))
  d.plot(0, end, newWindow = 'Gain '+str(k))

