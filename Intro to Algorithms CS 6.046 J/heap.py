import array

def swap(arr, first, second):
    """
    Swaps the first index with the second.

    arr: an input array
    first: an index in the array
    second: an index in the array

    This function has the side effect mentioned above.
    """
    arr[first], arr[second] = arr[second], arr[first]

def parent(i):
    """
    i: an integer index in a heap.

    Returns the index of the parent of the given index.
    """
    return (i + 1) / 2 - 1

def left(i):
    """
    i: an integer index in a heap.

    Returns the index of the left-child of the given index.
    """
    return 2 * (i + 1) - 1

def right(i):
    """
    i: an integer index in a heap

    Returns the index of the right-child of the given index.
    """
    return 2 * (i + 1)

def max_heapify(heap, i):
    """
    Assumes that the binary tree rooted at Left(i) and Right(i) are max-heaps
    but that A[i] may be smaller than its children. Max-heapify lets A[i] float
    down in order to satisfy the max-heap property.

    heap: an array that is being treated as a heap
    i: an index in the heap

    This method causes side effects in the heap given to it that bring the heap
    closer to a max-heap.
    """
    left_child = left(i)
    right_child = right(i)
    if left_child < len(heap) and heap[left_child] > heap[i]:
        largest = left_child
    else:
        largest = i
    if right_child < len(heap) and heap[right_child] > heap[largest]:
        largest = right_child
    if largest != i:
        swap(heap, i, largest)
        max_heapify(heap, largest)

example_heap = array.array('i', [16, 4, 10, 14, 7, 9, 3, 2, 8, 1])

def build_max_heap(arr):
    for i in range(len(arr) / 2, 0, -1):
        max_heapify(arr, i-1)

def max_heapify_unrecursive(heap, i):
    """
    Assumes that the binary tree rooted at Left(i) and Right(i) are max-heaps
    but that A[i] may be smaller than its children. Max-heapify lets A[i] float
    down in order to satisfy the max-heap property.

    heap: an array that is being treated as a heap
    i: an index in the heap

    This method causes side effects in the heap given to it that bring the heap
    closer to a max-heap.
    """
    while True:
        left_child = left(i)
        right_child = right(i)
        largest = i
        if left_child < len(heap) and heap[left_child] > heap[i]:
            largest = left_child
        if right_child < len(heap) and heap[right_child] > heap[largest]:
            largest = right_child
        if largest == i:
            return
        swap(heap, i, largest)
        i = largest

def heap_sort(arr):
    build_max_heap(arr)
    sorted_list = []
    while arr:
        sorted_list.append(arr.pop(0))
        max_heapify(arr, 0)
    sorted_list.reverse()
    return sorted_list

