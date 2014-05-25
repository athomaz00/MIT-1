# This is a bunch of ways to randomly permute arrays.

from random import randint
from operator import itemgetter
from quick_sort import swap

def permute_by_sorting(arr):
    n = len(arr)
    priorities = [(i, randint(1, n)) for i in arr]
    sorted_priorities = sorted(priorities, key=itemgetter(1))
    return [x[0] for x in sorted_priorities]

def randomize_in_place(arr):
    for i in range(len(arr)):
        swap(arr, i, randint(i, len(arr) - 1))
