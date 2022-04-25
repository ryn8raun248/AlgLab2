import pdb
import random
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
"""
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/ was used to assist
with code in this lab
"""

def kthSmallest(arr, l, len_array, k_value):
	"""
	arr: array that is initialized in main method
	l: original position. For our case, this is defaulted to 0 in main method
	len_array: length of array - 1
	k_value: k value selected in main method
	"""

	# If k < # elements in array
	if (k_value > 0 and k_value <= len_array - l + 1):
	
		# Partition the array around last element and get position of pivot element in sorted array
		pos = partition(arr, len_array) 
		# print('pos', pos)

		# If position == k_value
		if (pos - l == k_value - 1):
			# print('herebefore')
			return arr[pos]

		elif (pos - l > k_value - 1): # If position > k_value, recur for left subarray
			# print('here')
			return kthSmallest(arr, l, pos - 1, k_value)

		# Else recur for right subarray
		else:
			# print('hereELse')
			return kthSmallest(arr, pos + 1, len_array, k_value - pos + l - 1)

	# If k is more than number of elements in array
	raise Exception('k larger than # elements in array')

def partition(arr, len_array):
	"""
	This helper method considers the last element as pivot and moves all smaller element to left of it and greater elements to right
	arr: User-inputted array
	len_array: Length of arr - 1
	"""

	x = arr[len_array]
	i = 0
	for j in range(i, len_array):
		if (arr[j] <= x):
			arr[i], arr[j] = arr[j], arr[i] # swap
			i += 1
	arr[i], arr[len_array] = arr[len_array], arr[i] # swap
	return i



# Python program for implementation of MergeSort used for benchmarking in this lab - https://www.geeksforgeeks.org/python-program-for-merge-sort/

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


def generate_list_sorted(size):
	"""
	Generate list of SORTED numbers
	"""
	list_new = list(range(1,size))
	# k_value = random.randint(1,size - 1)
	k_value = size - 1
	return list_new, k_value


def generate_list_reverse(size):
	"""
	Generate list of REVERSE SORTED numbers
	"""
	list_new = list(range(1,size))
	# k_value = random.randint(1,size - 1)
	k_value = size - 1
	list_new_reverse = list_new[::-1]
	return list_new_reverse, k_value


if __name__ == "__main__":

	
	sizes = [10, 100,1000, 10000, 100000, 1000000]

	runtimes = {}
	runtimes_merge_sort = {}
	print('Quick Select Results: \n')
	for size in sizes:
		# sys.setrecursionlimit(1000000) # this does not help with sizes > 1000 when k value is randomized - it just prevents from crashing
		arr, k_value = generate_list_reverse(size)
		len_array = len(arr) - 1
		start = time.perf_counter()
		print("K'th smallest element is " + str(kthSmallest(arr, 0, len_array, k_value)) + " with k value of " + str(k_value))
		end = time.perf_counter()
		runtimes[size] = end - start

	print('Runtimes for quick select: ', runtimes)


	# names = list(runtimes.keys())
	# values = list(runtimes.values())
	
	# xpoints = np.array(names)
	# ypoints = np.array(values)

	# plt.plot(xpoints, ypoints)
	# plt.ylabel('Time in Seconds')
	# plt.xlabel('List Size')
	# plt.title('Our Implementation')
	# plt.show()

	print('\nRunning merge sort..')
	for size in sizes:
		arr, k_value = generate_list_reverse(size)
		len_array = len(arr)
		start = time.perf_counter()
		mergeSort(arr, 0, len_array-1)
		end = time.perf_counter()
		runtimes_merge_sort[size] = end - start

	print('Runtimes for merge sort: ', runtimes_merge_sort)



# 	names = list(runtimes_merge_sort.keys())
# 	values = list(runtimes_merge_sort.values())
	
# 	xpoints = np.array(names)
# 	ypoints = np.array(values)

# 	plt.plot(xpoints, ypoints)
# 	plt.ylabel('Time in Seconds')
# 	plt.xlabel('List Size')
# 	plt.title('Merge Sort')
# 	plt.show()
