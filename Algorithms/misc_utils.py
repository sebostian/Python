def is_simple(number):
	assert number > 1;

	divisor = 2;
	while divisor < number:
		if number % divisor == 0:
			return False
		divisor += 1
	return True

def is_odd(number):
	return number & 0b1 == True

def factorial(number):
	if number == 1:
		return 1
	return number * factorial(number - 1)

def inverse_array(a):
	lenght = len(a)
	for i in range(lenght//2):
		a[i], a[lenght-i-1] = a[lenght-i-1], a[i]

def power(x, y):
	if y == 0:
		return 1
	elif y % 2 == 1 :
		return x * power(x, y - 1)
	else:
		return power(x * x, y//2)