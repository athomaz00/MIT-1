1: (x[n] + x[n-1]) / 2, none
2: 
3: 1.05y[n-1] + x[n]
4: Write a python program for the difference equation given above.

balance = [100]
for i in range(1, 26):
	new_balance = balance[i-1] * 1.05
	balance.append(new_balance)
	print i, balance[i]

4a. 121.550625
4b. 322.509994371
