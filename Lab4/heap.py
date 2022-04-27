import math

def _parent(i):
    """
    Return the index of the parent of the element at index i.
    Converted from 1-based indexing.
    """
    return int((i - 1) // 2)

def _left(i):
    """
    Returns the index of the left child of the element at index i.
    Converted from 1-based indexing.
    """
    return 2 * i + 1

def _right(i):
    """
    Returns the index of the right child of the element at index i.
    Converted from 1-based indexing.
    """
    return 2 * i + 2

def _heap_increase_key(A, i, key):
    """
    "Bubble" a key up the heap.
    """
    assert key > A[i]

    A[i] = key

    while i > 0 and A[_parent(i)] < A[i]:
        parent = _parent(i)
        A[i], A[parent] = A[parent], A[i]
        i = parent

def _max_heapify(A, i, n):
    """
    Element is in the list but not yet part of the heap. This
    adds i into the heap.
    """

    left = _left(i)
    right = _right(i)
    largest = i

    if left < n and A[left] > A[i]:
        largest = left

    if right < n and A[right] > A[largest]:
        largest = right
        
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        _max_heapify(A, largest, n)

def max_heap_insert(A, key):
    """
    Inserts an element into the heap. This method
    should append a None value to the list to make
    room for the new key and call _heap_increase_key.
    """
    i = len(A)
    A.append(-float('inf'))
    _heap_increase_key(A, i, key)

def heap_extract_max(A):
    """
    Removes the maximum value from the heap and returns it.
    The list size should be reduced by 1.
    """
    n = len(A)
    max, last = A[0], A[n-1]
    A[0] = last
    A.pop()
    _max_heapify(A, 0, n - 1)

    return max

def build_max_heap(A):
    """
    Takes a list A of unordered elements and reorders the elements
    to construct a max binary heap.
    """
    n = len(A)

    for i in range(math.floor(n/2), -1, -1):
        _max_heapify(A, i, n)

def heapsort(A):
    """
    Sorts a list of elements by converting the list into a heap
    and then extracting each element from biggest to smallest.
    Note that this is done in place.
    """
    build_max_heap(A)

    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        _max_heapify(A, 0, i)