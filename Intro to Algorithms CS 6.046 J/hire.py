"""
Joshua Cole
Notes on the hiring assistant problem.
"""

from random import randint, choice, shuffle



def hire(canidates):
    """
    Suppose you need to hire a new assistant and you go to a hiring agency.
    This agency promises to send you one canidate per day. You decide you 
    always want to have the best canidate so you will always hire the canidate
    if the interview suggests they are better then the current hire.

    canidates: a list of integers that represent current hires

    Returns: an interger representing the best hire
    """
    current_hire  = 0
    for canidate in canidates:
        if canidate > current_hire:  # interview operation
            current_hire = canidate # hiring operation
    return current_hire



"""
Lets analyze the cost of running the above algorithm. However we are not 
concerned with the running time. After all according to the problem
statment it is obviously going to be finished in n days where n is the
number of canidates. Instead we are interested in the buisness cost of
running the algorith: the cost of giving the interview and hiring the
assistant.

There are two operations that have a cost. The interview operation which
has a small cost and the hiring operation which has a large cost, because
we need to pay the hiring agency and fire an employee. I'll call the
interview cost i. The hiring cost will be called j.

Note that the interview always happens. So one term is going to n*i. However
the hiring doesn't always happen. Lets say it happens m times. That means in
full we have: O(mj + ni).

In the worst case analysis the candiates would come in increasing order of
quality. Each candiate would be better then the candiate before it. Then we
would end up hiring. That is unlikely to happen though. What we are really
interested in is the average case in this scenario.

Thus, we introudce probalistic analysis.

When doing this anaylsis we need to make assumptions about the input. We're
going to assume that the canidates come in a random order.
"""
canidates = [randint(1, 100) for x in range(1000)]
"""
However, what we really want is our algorithm to enforce a random order. For 
all we know the hiring agency could send candiates in the worst case way.
"""
candiates = [x for x in range(1000)]


def randomized_hire(canidates):
    """
    A randomzied version of the hiring algorithm seen above.

    canidates: a list of integers that represent current hires

    Returns: an interger representing the best hire
    """
    current_hire  = 0
    while canidates:
        # Get the canidate randomly
        canidate = choice(canidates)
        canidates.remove(canidate)

        if canidate > current_hire:  # interview operation
            current_hire = canidate # hiring operation
    return current_hire

def another_random_hire(canidates):
    """
    A shorter version of the above that is more effecient.
    """
    shuffle(canidates)
    current_hire  = 0
    for canidate in canidates:
        if canidate > current_hire:  # interview operation
            current_hire = canidate # hiring operation
    return current_hire