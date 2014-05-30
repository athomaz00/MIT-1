def slow_mod(a, b):
	if a == b:
		return 0
	elif a < b:
		return a
	else: 
		return slow_mod(a - b, b)