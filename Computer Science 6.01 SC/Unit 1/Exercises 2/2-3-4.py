def add(a, b):
	if b == 0:
		return a
	else:
		return add(a, b - 1) + 1

# a can be any number and b must be a positive integer
# add(5, 2)
# add(5, 1)
# add(5, 0)

def sub(a, b):
	if b == 0:
		return a
	else:
		return sub(a, b-1) - 1