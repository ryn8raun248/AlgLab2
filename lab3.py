import pdb

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
		print('pos', pos)

		# If position == k_value
		if (pos - l == k_value - 1):
			print('herebefore')
			return arr[pos]

		elif (pos - l > k_value - 1): # If position > k_value, recur for left subarray
			print('here')
			return kthSmallest(arr, l, pos - 1, k_value)

		# Else recur for right subarray
		else:
			print('hereELse')
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

if __name__ == "__main__":
	
	arr = [1,2,3,4,5,6]
	len_array = len(arr) - 1
	k_value = 3
	print("K'th smallest element is " + str(kthSmallest(arr, 0, len_array, k_value)) + " with k value of " + str(k_value))
