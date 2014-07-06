import lib601.poly as poly
import lib601.sig
from lib601.sig import *

## You can evaluate expressions that use any of the classes or
## functions from the sig module (Signals class, etc.).  You do not
## need to prefix them with "sig."

s = UnitSampleSignal()
#s.plot(-5, 5)

import math
cs = CosineSignal(math.pi / 8)
# cs.plot(-10, 10)

step_signal = MyStepSignal()
sum_signal = MySummedSignal(step_signal, step_signal)

# sum_signal.plot(-5, 5)

p = poly.Polynomial([1, 2, 3])
a = myPolyR(s, p)

a.plot(-5, 5)


