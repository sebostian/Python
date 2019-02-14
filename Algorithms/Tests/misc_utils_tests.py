import misc_utils

def test_inverse_array():
	normal_array = [1,2,3,4,5]
	inversed_array = [5,4,3,2,1]
	misc_utils.inverse_array(normal_array)
	return normal_array == inversed_array

def test_factorial():
	actual = misc_utils.factorial(5);
	expected = 120;
	return actual == expected

def test_power():
	actual = misc_utils.power(5, 5);
	expected = 3125
	return actual == expected


#print("test_factorial - ", test_factorial())
#print("test_inverse_array - ", test_inverse_array())
print("test_power - ", test_power())

