#
# File:   designLab01Work.py
# Author: Joshua Cole
# Date:   27-May-2014

#-----------------------------------------------------------------------------

def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	a = 0 
	b = 1 
	while n > 2:
		a, b = b, a + b
		n -= 1
	return b



#-----------------------------------------------------------------------------

class V2(object):
    def __init__(self, x, y):
    	self.vector = [x, y]

    def __str__(self):
    	return "V2" + str(self.vector)

    def getX(self):
    	return self.vector[0]

    def getY(self):
    	return self.vector[1]

    def add(self, rhs):
    	if type(rhs) is V2:
    		return V2(self.getX() + rhs.getX(), self.getY() + rhs.getY())
    	else:
    		return V2(self.getX() + rhs, self.getY() + rhs)

    def mul(self, rhs):
    	if type(rhs) is V2:
    		return V2(self.getX() * rhs.getX(), self.getY() * rhs.getY())
    	else:
    		return V2(self.getX() * rhs, self.getY() * rhs)

    def __add__(self, rhs):
    	return self.add(rhs)

    def __mul__(self, rhs):
    	return self.mul(rhs)

#-----------------------------------------------------------------------------

class Polynomial:
    # Delete the pass statement below and insert your own code
    def __init__(self, args):
    	self.coexs = map(float, args)
    
    def __call__(self, x):
    	s = 0
    	power = len(self.coexs) - 1
    	for coex in self.coexs:
    		s += coex * x ** power
    		power -= 1
    	return s

    def __str__(self):
        s = ""
        if self.coexs:
            power = len(self.coexs) - 1
            s += ("-" if self.coexs[0] < 0 else "") + str(self.coexs[0] ) + "z^" + str(power)
            power -= 1
            for coex in self.coexs[1:]:
                s_part = " - " if coex < 0 else " + "
                if power == 1:
                    z_to_power = str(coex) + "z"
                elif power == 0:
                    z_to_power = str(coex)
                else:
                    z_to_power = str(coex) + "z" + str(power)
                s_part += z_to_power
                s += s_part
                power -= 1
        return s

    def __repr__(self):
        return self.__str__()


    def __add__(self, rhs):
        reversed_coexs = []
        for cs in map(None, self.coexs[::-1], rhs.coexs[::-1]):
            if cs[0] is None:
                reversed_coexs.append(cs[1])
            elif cs[1] is None:
                reversed_coexs.append(cs[0])
            else:
                reversed_coexs.append(cs[0] + cs[1])
        return Polynomial(reversed_coexs[::-1])

    def __mul__(self, rhs):
        res = [0] * (len(self.coexs) + len(rhs.coexs) - 1)
        for pi1, c1 in enumerate(self.coexs[::-1]):
            for pi2, c2 in enumerate(rhs.coexs[::-1]):
                res[pi1 + pi2] += c1 * c2
        return Polynomial(res[::-1])


    def coef(self, i):
        return self.coexs[-i-1]

    def roots(self):
        if len(self.coexs) == 2:
            try:
                return self.coexs[1] / self.coexs[0]
            except ZeroDivisionError:
                return 0 
        if len(self.coexs) == 3:
            a, b, c = self.coexs
            root = b ** 2 - 4 * a * c
            return [(-b + complex(root) ** 0.5)/ 2, (-b - complex(root) ** 0.5)/ 2 ]
        else:
            print "Order wrong. Can't solve for roots."