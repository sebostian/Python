import generate_numbers

def generate_numbers_test():
	#generate_numbers.generate_numbers(2, 5, None)
	return False

def generate_permutations_test():
	generate_numbers.generate_permutations(5, 5, None)
	return False


def run_tests():
	tests = [generate_numbers_test, generate_permutations_test]
	for test in tests:
		result = "Passed" if test() else "Failed" 
		print(test.__name__, result, sep="-")
run_tests()