def insert_sort(a):
	"""
	Sorts an array by insertion
Sorted array returns in a param
	"""
	length = len(a)
	for i in range(1, length):
		j = i
		while j > 0 and a[j] < a[j-1]:
			a[j], a[j-1] = a[j-1], a[j] 
			j -= 1
	return

def choice_sort(a):
	""" Sorts an array by choice method
Sorted array returns in A param
	"""
	length = len(a)
	for i in range (length - 1):
		for j in range(i+1, length):
			if (a[j] < a[i]):
				a[i], a[j] = a[j], a[i]

def bubble_sort(a):
	""" Sorts an array by bubble method
Sorted array returns in a param
	"""
	length = len(a)
	for k in range(1, length): 
		for i in range(length - k):
			if a[i+1] < a[i]:
				a[i+1], a[i] = a[i], a[i+1]

