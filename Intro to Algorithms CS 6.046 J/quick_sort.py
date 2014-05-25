"""
Quicksort - Howe 1962
---------------------

- Divide and Conquer Algorithm
- Sorts "in place" (doesn't require extra storage)
- Very practical (with tuning)

1. Divide into two paritions around a pivot such that element in lower array
   are less than x which is itself less then the greater array.
2. Recursively sort the two arrays.

The key is the linear-time paritioning subroutine.
"""
from random import randint

def swap(arr, first, second):
	arr[first], arr[second] = arr[second], arr[first]

def partition(arr, start, end, random=False):
    if random:
        random_pivot = randint(start, end - 1)
        swap(arr, start, random_pivot)
    pivot = start
    lower_end = start + 1
    for i in range(start+1, end):
        if arr[i] < arr[pivot]:
            swap(arr, lower_end, i)
            lower_end += 1
    new_pivot = lower_end - 1
    swap(arr, pivot, new_pivot)
    return new_pivot

def quick_sort(arr, start, end):
    if end - start > 0:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot)
        quick_sort(arr, pivot+1, end)

arr = [ 3,7,2,8,1,6,8,9,6,9]

def random_quick_sort(arr, start, end):
    if end - start > 0:
        pivot = partition(arr, start, end, random=True)
        random_quick_sort(arr, start, pivot)
        random_quick_sort(arr, pivot+1, end)

def qsort(arr):
    if arr:
        lower = [x for x in arr[1:] if x < arr[0]]
        equal = [x for x in arr if x == arr[0]]
        upper = [x for x in arr[1:] if x > arr[0]]
        return qsort(lower) + equal + qsort(upper)
    else:
        return arr
