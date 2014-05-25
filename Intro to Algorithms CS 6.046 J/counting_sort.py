"""
This an implementation of the sorting algorithm counting sort. It is an in-place sorting
algorithm that runs in O(n+k) time. That is linear time, which is pretty impressive 
considering that comparison sorts like quick sort, heap sort, and merge sort have an
optimal sorting time of O(nlgn). However, in tthis case k is the range of the input.
Sometimes when sorting you might be sorting only ten elements but have them potentially
lying in a range between one and ten billion. In this case the algorithm wouldn't be the
best to use.
"""

def counting_sort(arr, k):
	"""
	An implementation of the counting sort. This is a stable sorting algorithm.

	Args:
		arr: The array of integers to be sorted. The integers must be between zero and k.
		k: The integer boundary that the array is constrained by.

	Returns:
		A stable sorting of the input arr.
	"""
	counts = [0] * k
	for item in arr:
		counts[item-1] += 1

	count_so_far = 0
	for i in range(k):
		count_so_far += counts[i]
		counts[i] = count_so_far

	output = [None] * len(arr)
	for i in range(len(arr)-1, -1, -1):
		output[counts[arr[i]-1]-1] = arr[i]
		counts[arr[i]-1] -= 1
	return output