import sorting

def test_case_1(sorting_function):
	unsorted = [2,3,1,7,4,9,4,0]
	sorted = [0,1,2,3,4,4,7,9]
	sorting_function(unsorted)
	return sorted == unsorted

def test_case_2(sorting_function):
	unsorted = [2,2,2,2,2,2,0]
	sorted = [0,2,2,2,2,2,2]
	sorting_function(unsorted)
	return sorted == unsorted

def test_case_3(sorting_function):
	unsorted = [2,2,2,2,2,2]
	sorted = [2,2,2,2,2,2]
	sorting_function(unsorted)
	return sorted == unsorted


def run_tests():
	tests = [test_case_1, test_case_2, test_case_3];
	fuctions = [sorting.insert_sort, sorting.choice_sort, sorting.bubble_sort]
	for function in fuctions:
		for test in tests:
			result = "Passed" if test(function) else "Failed" 
			print(test.__name__, function.__name__, result, sep="-")

run_tests()

