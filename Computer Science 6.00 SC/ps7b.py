# P(three heads) = (1/2)^3
# P({HTH}) = (1/2)^3
# P(two heads and one tail) = 3/8
# P(number of head greater then number of tails) = 1/2
# P(yahtzee) = P(all ones) + P(all twos) + P(all threes)...
# P(all ones) = 1/7776
# P(yahtzee = 6(1/6)^5 = 1/1296

import random

def roll_die():
    return random.randint(1, 6)

def simulate_yahtzee():
    number_of_attempts = 1000
    number_of_dice = 5

    yahtzees = 0.0
    for attempt in range(number_of_attempts):
        rolls = [roll_die() for i in range(number_of_dice)]
        if rolls[0] == rolls[1] == rolls[2] == rolls[3] == rolls[4]:
            yahtzees += 1
    return yahtzees / number_of_attempts
        

    
