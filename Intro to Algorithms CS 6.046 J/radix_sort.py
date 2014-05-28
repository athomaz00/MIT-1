def get_digit(number, i):
	"""
	Returns the digit in column i.

	Args:
		number: An integer.
		i: An integer column in number. In the number 10, the first column would be 0 and
			the second column would be 1.

	Returns:
		Returns the digit in column i.
	"""
	modulus = 10 ** (i + 1)
	diviser = 10 ** i
	return (number % modulus) / diviser

def radix_sort(arr):
	"""
	Radix sort works by first doing a counting sort by the least significant digit. Then
	by the next least and so on and so forth.

	Args:
		arr: An array of integers to be sorted.

	Returns:
		An array of intgers in sorted order.
	"""
	k = 10
	for i in range(k):
		buckets = [[], [], [], [], [], [], [], [], [], []]
		for number in arr:
			buckets[get_digit(number, i)].append(number)
		arr = reduce(lambda x, y: x + y, buckets)
	return arr



